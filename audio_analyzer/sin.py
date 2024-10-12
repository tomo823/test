import matplotlib.pyplot as plt
import numpy as np

# データ生成
x = np.linspace(0, 2 * np.pi, 100)  # 0から2πまでの範囲を100ステップで
y_sin = np.sin(x)  # 正弦波
y_cos = np.cos(x)  # 余弦波

# グラフの描画
plt.figure(figsize=(8, 6))  # グラフサイズを指定

# 正弦波の描画
plt.plot(x, y_sin, label="Sine", color="blue", linestyle='-', linewidth=2)

# 余弦波の描画
plt.plot(x, y_cos, label="Cosine", color="red", linestyle='--', linewidth=2)

# グラフのタイトルとラベル
plt.title("Sine and Cosine Waves")
plt.xlabel("x")
plt.ylabel("y")

# 凡例を表示
plt.legend()

# グリッドを表示
plt.grid(True)

# グラフを表示
plt.show()
