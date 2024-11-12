import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib import patches
import files_management

img_left = files_management.read_left_image()
img_right = files_management.read_right_image()
p_left, p_right = files_management.get_projection_matrices()
np.set_printoptions(suppress=True)

def compute_left_disparity_map(num_disparities, block_size, window_size, img_left, img_right):
    min_disparity = 0
    img_left = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
    img_right = cv2.cvtColor(img_right, cv2.COLOR_BGR2GRAY)

    left_matcher_SGBM = cv2.StereoSGBM_create(
        minDisparity=min_disparity,
        numDisparities=num_disparities,
        blockSize=block_size,
        P1=8 * 3 * window_size ** 2,
        P2=32 * 3 * window_size ** 2,
        mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY
    )

    return left_matcher_SGBM.compute(img_left, img_right).astype(np.float32) / 16

disparity_maps = [
    compute_left_disparity_map(int(6 * 16 * 1), 15, 6, img_left, img_right),
    compute_left_disparity_map(int(8 * 16 * 1), 15, 6, img_left, img_right),
    compute_left_disparity_map(int(6 * 16 * 1), 21, 6, img_left, img_right),
    compute_left_disparity_map(int(6 * 16 * 1), 5, 6, img_left, img_right),
    compute_left_disparity_map(int(6 * 16 * 1), 15, 12, img_left, img_right),
    compute_left_disparity_map(int(6 * 16 * 1), 15, 2, img_left, img_right)
]

for disp in disparity_maps:
    plt.figure(figsize=(10, 10))
    plt.imshow(disp)
    plt.show()

def decompose_projection_matrix_QR(p):
    partial_matrix = p[:, :3]
    Q, R = np.linalg.qr(partial_matrix)
    r = np.linalg.inv(Q)
    k = R
    if np.linalg.det(k) < 0: k = -k
    if np.linalg.det(r) < 0: r = -r
    t = -np.linalg.inv(k) @ p[:, 3].reshape(3, 1)
    return k, r, np.append(t, 1).reshape(4, 1)

def decompose_projection_matrix(p):
    k, r, t, rx, ry, rz, ea = cv2.decomposeProjectionMatrix(p)
    t = t /t[3, 0]
    return k, r, t

k_left, r_left, t_left = decompose_projection_matrix(p_left)
k_right, r_right, t_right = decompose_projection_matrix(p_right)

print("k_left \n", k_left)
print("\nr_left \n", r_left)
print("\nt_left \n", t_left)
print("\nk_right \n", k_right)
print("\nr_right \n", r_right)
print("\nt_right \n", t_right)

def calc_depth_map(disp_left, k_left, t_left, t_right):
    f = (k_left[0, 0] + k_left[1, 0]) / 2
    b = abs(t_left[1] - t_right[1])
    disp_left[disp_left == 0] = 0.1
    disp_left[disp_left == -1] = 0.1
    return (f * b) / disp_left

depth_maps = [calc_depth_map(disp, k_left, t_left, t_right) for disp in disparity_maps]

for depth_map in depth_maps:
    plt.figure(figsize=(8, 8), dpi=100)
    plt.imshow(depth_map, cmap='flag')
    plt.show()
