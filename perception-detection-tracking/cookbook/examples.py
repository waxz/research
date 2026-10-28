#!/usr/bin/env python3
"""Worked examples for the Perception Cookbook (detection and tracking in images and point clouds).

Every number quoted under "Worked example" in COOKBOOK.md comes from a function
here. Requires only NumPy.

    python3 examples.py          # run all recipes
    python3 examples.py p05      # run recipes whose name contains "p05"
"""
import itertools
import sys

import numpy as np

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(3)


def iou(a, b):
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0.0, x2 - x1) * max(0.0, y2 - y1)
    area = lambda r: (r[2] - r[0]) * (r[3] - r[1])
    return inter / (area(a) + area(b) - inter)


def p01_conv_arithmetic():
    H, k, s, p = 224, 3, 1, 1
    print(f"3x3 conv, stride 1, pad 1 on 224x224 -> {(H + 2 * p - k) // s + 1}x{(H + 2 * p - k) // s + 1}; stride 2 -> {(H + 2 * p - k) // 2 + 1}")
    rf = 1
    for n in range(1, 6):
        rf += 2
        print(f"  {n} stacked 3x3 convs (stride 1): receptive field {rf}x{rf}") if n in (1, 2, 5) else None
    cin, cout = 256, 256
    params = k * k * cin * cout
    flops = params * 56 * 56
    print(f"one 3x3 conv, 256->256 channels on 56x56: {params / 1e6:.2f} M weights, {flops / 1e9:.2f} G multiply-adds")


def p02_residual_gradients():
    depth = 50
    plain = 0.9 ** depth  # each plain layer scales the gradient by ~0.9
    resid = (1 + 0.02) ** depth  # residual: identity + small branch
    print(f"{depth} layers: gradient scale through a plain stack {plain:.4f}, through residual blocks {resid:.2f}")
    print("residual blocks keep an identity path, so gradients neither vanish nor need careful init to flow")


def p03_iou_giou():
    a, b, c = [0, 0, 10, 10], [5, 5, 15, 15], [20, 20, 30, 30]
    for name, x, y in [("overlapping", a, b), ("disjoint", a, c)]:
        i = iou(x, y)
        cx1, cy1, cx2, cy2 = min(x[0], y[0]), min(x[1], y[1]), max(x[2], y[2]), max(x[3], y[3])
        Cs = (cx2 - cx1) * (cy2 - cy1)
        inter = max(0, min(x[2], y[2]) - max(x[0], y[0])) * max(0, min(x[3], y[3]) - max(x[1], y[1]))
        union = 200 - inter
        giou = i - (Cs - union) / Cs
        print(f"{name:11s}: IoU {i:.3f}, GIoU {giou:.3f}")


def p04_box_encoding():
    anchor = np.array([50.0, 50.0, 100.0, 60.0])  # cx, cy, w, h
    gt = np.array([60.0, 45.0, 120.0, 50.0])
    t = np.array([(gt[0] - anchor[0]) / anchor[2], (gt[1] - anchor[1]) / anchor[3], np.log(gt[2] / anchor[2]), np.log(gt[3] / anchor[3])])
    dec = np.array([anchor[0] + t[0] * anchor[2], anchor[1] + t[1] * anchor[3], anchor[2] * np.exp(t[2]), anchor[3] * np.exp(t[3])])
    print("regression targets (tx, ty, tw, th):", t.round(4), "| decoded box:", dec)


def p05_nms():
    boxes = np.array([[10, 10, 50, 50], [12, 12, 52, 52], [11, 9, 49, 51], [60, 60, 100, 100], [62, 58, 101, 99]], float)
    scores = np.array([0.9, 0.85, 0.7, 0.8, 0.6])
    order, keep = list(np.argsort(-scores)), []
    while order:
        i = order.pop(0); keep.append(i)
        order = [j for j in order if iou(boxes[i], boxes[j]) < 0.5]
    print(f"5 raw detections of 2 objects -> NMS (IoU 0.5) keeps indices {[int(i) for i in keep]} with scores {scores[keep]}")


def p06_focal_loss():
    def ce(p): return -np.log(p)
    def fl(p, g=2.0, a=0.25): return -a * (1 - p) ** g * np.log(p)
    easy_neg, n_easy, hard_pos, n_hard = 0.99, 100_000, 0.3, 10
    for name, f in [("cross-entropy", ce), ("focal (gamma=2)", fl)]:
        e, h = n_easy * f(easy_neg), n_hard * f(hard_pos)
        print(f"{name:16s}: 100k easy negatives contribute {e:9.2f}, 10 hard positives {h:7.3f} -> hard share {100 * h / (e + h):.1f}%")


def p07_average_precision():
    # 10 ranked detections, 6 ground-truth objects; True = matched (IoU >= 0.5)
    tp = np.array([1, 1, 0, 1, 0, 1, 0, 0, 1, 0], float)
    n_gt = 6
    ctp, cfp = np.cumsum(tp), np.cumsum(1 - tp)
    rec, prec = ctp / n_gt, ctp / (ctp + cfp)
    mprec = np.maximum.accumulate(prec[::-1])[::-1]
    r = np.r_[0, rec]
    ap_all = np.sum((r[1:] - r[:-1]) * mprec)
    ap101 = np.mean([mprec[rec >= t].max() if np.any(rec >= t) else 0 for t in np.linspace(0, 1, 101)])
    print(f"precision {prec.round(2)}\nrecall    {rec.round(2)}\nAP (all-point) {ap_all:.3f}, AP (101-point, COCO style) {ap101:.3f}; max recall {rec.max():.2f}")


def p08_dense_vs_sparse_predictions():
    yolo1 = 7 * 7 * 2
    H = W = 1024
    retina = sum((H // s) * (W // s) * 9 for s in [8, 16, 32, 64, 128])
    print(f"YOLOv1: 7x7 grid x 2 boxes = {yolo1} candidate boxes; RetinaNet on 1024x1024 (P3-P7, 9 anchors) = {retina:,} anchors; DETR: 100 object queries")


def p09_attention_cost():
    for side, patch in [(224, 16), (512, 16), (1024, 16)]:
        n = (side // patch) ** 2
        print(f"{side}x{side} image, {patch}px patches: {n:5d} tokens, attention matrix {n * n / 1e6:7.2f} M entries per head per layer")


def p10_hungarian_matching():
    preds = [[0, 0, 10, 10], [20, 20, 30, 30], [5, 5, 15, 15], [50, 50, 60, 60]]
    gts = [[21, 19, 31, 29], [1, 0, 11, 10], [4, 6, 14, 16]]
    C = np.array([[1 - iou(p, g) for g in gts] for p in preds])
    best = min(itertools.permutations(range(len(preds)), len(gts)), key=lambda perm: sum(C[perm[j], j] for j in range(len(gts))))
    print("cost (1-IoU) matrix:\n", C.round(2))
    print("optimal one-to-one match gt->pred:", {j: best[j] for j in range(len(gts))}, "| unmatched prediction 3 -> 'no object'")


def p11_clip_zero_shot():
    d = 8
    text = {name: rng.standard_normal(d) for name in ["a forklift", "a pallet", "a person", "a cardboard box"]}
    for k in text: text[k] /= np.linalg.norm(text[k])
    img = 0.6 * text["a pallet"] + 0.4 * text["a cardboard box"] + 0.3 * rng.standard_normal(d); img /= np.linalg.norm(img)
    logits = np.array([img @ t for t in text.values()]) / 0.1  # temperature 0.1
    p = np.exp(logits - logits.max()); p /= p.sum()
    for (name, _), pi in zip(text.items(), p):
        print(f"  P('{name}') = {pi:.3f}")
    # contrastive (InfoNCE) loss for a batch of 4 matched pairs
    S = rng.standard_normal((4, 4)) * 0.15 + 0.3 * np.eye(4)  # cosine similarities, matched pairs on the diagonal
    L = S / 0.07
    li = -np.mean(np.diag(L) - np.log(np.exp(L).sum(1)))
    lt = -np.mean(np.diag(L) - np.log(np.exp(L).sum(0)))
    print(f"symmetric InfoNCE loss on a 4-pair batch: {(li + lt) / 2:.3f}")


def p12_pointnet_invariance():
    W = rng.standard_normal((3, 16))
    pts = rng.standard_normal((500, 3))
    f = lambda P: np.max(np.maximum(P @ W, 0), axis=0)
    perm = rng.permutation(500)
    print("max-pooled feature unchanged under point permutation:", np.allclose(f(pts), f(pts[perm])))
    f_concat = lambda P: np.maximum(P @ W, 0).ravel()[:16]
    print("order-dependent (no symmetric pooling) feature unchanged:", np.allclose(f_concat(pts), f_concat(pts[perm])))


def p13_pillars():
    # synthetic scene: ground + a car-sized cluster, 0.16 m pillars over 70 x 80 m
    ground = np.c_[rng.uniform(0, 70, 30000), rng.uniform(-40, 40, 30000), rng.normal(-1.7, 0.03, 30000)]
    car = np.c_[rng.normal(20, 0.9, 2000), rng.normal(3, 0.4, 2000), rng.uniform(-1.7, -0.2, 2000)]
    P = np.r_[ground, car]
    ix, iy = (P[:, 0] / 0.16).astype(int), ((P[:, 1] + 40) / 0.16).astype(int)
    keys, counts = np.unique(ix * 1000 + iy, return_counts=True)
    print(f"grid {int(70 / 0.16)} x {int(80 / 0.16)} = {int(70 / 0.16) * int(80 / 0.16):,} pillars; occupied {len(keys):,} "
          f"({100 * len(keys) / (437 * 500):.1f}%); max points per pillar {counts.max()}, median {int(np.median(counts))}")


def p14_lidar_to_camera():
    K = np.array([[720, 0, 640], [0, 720, 360], [0, 0, 1.0]])
    R = np.array([[0, -1, 0], [0, 0, -1], [1, 0, 0.0]])  # lidar x-forward,y-left,z-up -> camera z-forward,x-right,y-down
    t = np.array([0.0, -0.3, 0.1])
    for X in [np.array([15.0, 2.0, 0.5]), np.array([-5.0, 0.0, 0.0])]:
        Xc = R @ X + t
        if Xc[2] <= 0:
            print(f"lidar point {X} is behind the camera (z={Xc[2]:.1f}) -> discard"); continue
        u = K @ Xc; u = u[:2] / u[2]
        print(f"lidar point {X} -> camera {Xc.round(2)} -> pixel {u.round(1)}")


def p15_lss_lift():
    H, W, D, C = 32, 88, 41, 64  # feature map, depth bins (4-45 m, 1 m), channels
    pts = H * W * D
    print(f"lifting a {H}x{W} feature map with {D} depth bins x {C} channels per camera: {pts:,} frustum points, "
          f"{pts * C * 4 / 1e6:.0f} MB in fp32; 6 cameras -> {6 * pts:,} points to splat into BEV")


def p16_sort_kalman():
    # state [u, v, s, r, du, dv, ds]: box centre, area, aspect; constant velocity in image space
    dt = 1.0
    F = np.eye(7); F[0, 4] = F[1, 5] = F[2, 6] = dt
    x = np.array([100.0, 200, 1500, 0.5, 4.0, -1.0, 0.0])
    for k in range(5):
        x = F @ x
    print(f"object occluded for 5 frames: predicted centre ({x[0]:.0f}, {x[1]:.0f}) from (100, 200) at (+4, -1) px/frame")


def p17_bytetrack():
    tracks = {1: [100, 100, 140, 180], 2: [300, 100, 340, 180]}
    dets = [([102, 101, 142, 182], 0.91), ([305, 105, 345, 185], 0.32), ([500, 50, 520, 90], 0.25)]  # track 2 occluded -> low score
    high = [d for d in dets if d[1] >= 0.6]; low = [d for d in dets if 0.1 <= d[1] < 0.6]
    matched = {}
    for tid, tb in tracks.items():
        best = max(high, key=lambda d: iou(tb, d[0]), default=None)
        if best and iou(tb, best[0]) > 0.3:
            matched[tid] = ("high", round(best[1], 2)); high.remove(best)
    for tid, tb in tracks.items():
        if tid in matched: continue
        best = max(low, key=lambda d: iou(tb, d[0]), default=None)
        if best and iou(tb, best[0]) > 0.5:
            matched[tid] = ("low", round(best[1], 2)); low.remove(best)
    print("matches:", matched, "| unmatched low-score boxes discarded as background:", [d[1] for d in low])
    print("a single high threshold would have lost track 2 while it was occluded")


def p18_mot_metrics():
    GT, FN, FP, IDSW = 1000, 120, 80, 15
    mota = 1 - (FN + FP + IDSW) / GT
    IDTP, IDFP, IDFN = 760, 160, 240
    idf1 = 2 * IDTP / (2 * IDTP + IDFP + IDFN)
    DetA, AssA = 0.62, 0.55
    print(f"MOTA = 1 - (FN+FP+IDSW)/GT = {mota:.3f}; IDF1 = {idf1:.3f}; HOTA (one threshold) = sqrt(DetA*AssA) = {np.sqrt(DetA * AssA):.3f}")
    print(f"15 identity switches cost MOTA only {15 / GT:.3f}; association quality shows up in IDF1 and AssA")


def p19_nds():
    mAP = 0.60
    mTP = {"ATE (m)": 0.25, "ASE": 0.24, "AOE (rad)": 0.30, "AVE (m/s)": 0.25, "AAE": 0.19}
    nds = (5 * mAP + sum(1 - min(1, v) for v in mTP.values())) / 10
    print(f"nuScenes NDS = [5 mAP + sum(1 - min(1, mTP))]/10 = {nds:.3f} for mAP {mAP} and errors {list(mTP.values())}")


def p20_latency_budget():
    for fps in [10, 30, 60]:
        print(f"{fps:>3} FPS -> {1000 / fps:.1f} ms per frame end-to-end (sensor + preprocess + network + NMS/tracking)")
    params = 25e6
    print(f"25 M parameters: {params * 4 / 1e6:.0f} MB fp32, {params * 2 / 1e6:.0f} MB fp16, {params / 1e6:.0f} MB int8")


RECIPES = {name: fn for name, fn in globals().items() if name.startswith("p") and name[1:3].isdigit()}

if __name__ == "__main__":
    pattern = sys.argv[1] if len(sys.argv) > 1 else ""
    for name, fn in RECIPES.items():
        if pattern in name:
            print(f"\n=== {name} ===")
            fn()
