import imageio
import numpy as np
import os
from skimage.metrics import peak_signal_noise_ratio as psnr

# 修改這兩個路徑
gt_folder = 'wolf/substep_4e5'
rendered_folder = 'default_output_sand'

frame_start = 0
frame_end =  49 # 根據 config 設定 frame_num

psnr_values = []

for i in range(frame_start, frame_end + 1):
    gt_path = os.path.join(gt_folder, f"{i:04d}.png")
    render_path = os.path.join(rendered_folder, f"{i:04d}.png")

    if not os.path.exists(gt_path) or not os.path.exists(render_path):
        print(f"Skipping frame {i:05d}, file not found.")
        continue

    gt_img = imageio.imread(gt_path)
    render_img = imageio.imread(render_path)

    # 確保 shape 一樣
    if gt_img.shape != render_img.shape:
        print(f"Skipping frame {i:05d}, shape mismatch.")
        continue

    value = psnr(gt_img, render_img, data_range=255)
    psnr_values.append(value)
    with open(os.path.join(gt_folder, "psnr_values.txt"), "a") as f:
        f.write(f"{i:04d}: {value:.6f}\n")
    print(f"Frame {i:04d}: PSNR = {value:.2f} dB")

if psnr_values:
    avg_psnr = sum(psnr_values) / len(psnr_values)
    print(f"\nAverage PSNR over {len(psnr_values)} frames: {avg_psnr:.2f} dB")
else:
    print("No PSNR values computed.")
