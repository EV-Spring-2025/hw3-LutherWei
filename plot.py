import matplotlib.pyplot as plt

file = "wolf/grid_v_damp2"
# 讀取檔案
with open(file+"/psnr_values.txt", "r") as f:
    lines = f.readlines()

# 解析數據
frames = []
psnr_values = []

for line in lines:
    if ":" in line:
        frame_str, value_str = line.strip().split(":")
        frames.append(int(frame_str))
        psnr_values.append(float(value_str))

# 繪製圖形
plt.figure(figsize=(12, 6))
plt.plot(frames, psnr_values, marker='o', linewidth=1.5)
plt.title("PSNR per Frame", fontsize=16)
plt.xlabel("Frame Index", fontsize=14)
plt.ylabel("PSNR (dB)", fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.savefig(file + "/psnr_per_frame.png")

