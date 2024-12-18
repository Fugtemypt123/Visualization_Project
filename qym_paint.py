import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

# 设置中文显示（需要系统有SimHei字体）
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 人物数据：姓名, 加入回数, 颜色
# 原顺序为：唐僧(0), 孙悟空(14), 白龙马(15), 猪八戒(19), 沙悟净(22)
# 我们不改变数据顺序，但稍后会反转显示顺序
characters = [
    ("唐僧", 0, 'blue'),
    ("孙悟空", 14, 'red'),
    ("白龙马", 15, 'gray'),
    ("猪八戒", 19, 'green'),
    ("沙悟净", 22, 'purple')
]

total_chapters = 100

# 翻转顺序使最终显示为：沙悟净(紫,最上) - 猪八戒(绿) - 白龙马(灰) - 孙悟空(红) - 唐僧(蓝,最下)
characters_reversed = list(reversed(characters))

# 分配 y 位置，从上到下：4,3,2,1,0
y_positions = [0, 1, 2, 3, 4]

fig, ax = plt.subplots(figsize=(10, 5))

i = 0
j = 0
for (name, chapter, color), y in zip(characters, y_positions):
    
    if name == "唐僧":
        ax.hlines(y=0, xmin=0, xmax=total_chapters, color=color, linewidth=3, label=name)
        ax.vlines(x=chapter, ymin=-0.5, ymax=i, color=color, linestyles='dashed', linewidth=1)
        ax.text(chapter, -0.46, f"第{chapter}回", ha='left', va='bottom', color=color, fontsize=10)
    else:
        # x_pre = np.linspace(0, chapter, 50)
        # y_pre = np.linspace(y, i, 50)  # 从 y 逐渐下降到0

        x_pre = np.linspace(0, chapter, 200)

        mid = chapter / 2  # 中点位置，大约在章节中段时变化最为剧烈
        scale = chapter / 10  # 调整该值以控制下降的陡峭程度
        y_pre = i-0.012 + (y - i + 0.012) / (1 + np.exp((x_pre - mid) / scale))

        ax.plot(x_pre, y_pre, color=color, linewidth=3)

        # 绘制过渡曲线
        ax.plot(x_pre, y_pre, color=color, linewidth=3)

        # 从加入章节到总章节数，在坐标轴上继续水平线
        ax.hlines(y=i, xmin=chapter, xmax=total_chapters, color=color, linewidth=3, label=name)

        # 在加入章节处画一条垂直虚线
        ax.vlines(x=chapter, ymin=-0.5, ymax=i, color=color, linestyles='dashed', linewidth=1)

        # 文本标注
        ax.text(chapter-2, -0.58 - 0.12 * ((-1)**j), f"第{chapter}回", ha='left', va='bottom', color=color, fontsize=10)
    i += 0.12
    j += 1

# 金角、银角大王(31—33回)：唐僧(y=0)、猪八戒(y=-1)、沙僧(y=-2)
ax.hlines(y=0, xmin=31, xmax=33, color='black', linewidth=3, label="被抓走")   # 覆盖唐僧线段
ax.hlines(y=0.36, xmin=31, xmax=33, color='black', linewidth=3)  # 覆盖八戒线段
ax.hlines(y=0.48, xmin=31, xmax=33, color='black', linewidth=3)  # 覆盖沙僧线段

# 黄袍怪(36—39回)抓走唐僧(y=0)
ax.hlines(y=0, xmin=36, xmax=39, color='black', linewidth=3)

# 红孩儿(40—42回)抓走唐僧(y=0)
ax.hlines(y=0, xmin=40, xmax=42, color='black', linewidth=3)

# 蜘蛛精盘丝洞(72—73回)抓走唐僧(y=0)
ax.hlines(y=0, xmin=72, xmax=73, color='black', linewidth=3)

# 狮驼岭三魔(85—87回)抓走唐僧(y=0)、八戒(y=-1)、沙僧(y=-2)
ax.hlines(y=0, xmin=85, xmax=87, color='black', linewidth=3)
ax.hlines(y=0.36, xmin=85, xmax=87, color='black', linewidth=3)
ax.hlines(y=0.48, xmin=85, xmax=87, color='black', linewidth=3)


# 设置横轴范围
ax.set_xlim(0, total_chapters + 1)
ax.set_ylim(-0.5, 4.5)

# 在全部绘制完成后调用
ax.legend()

# 去掉y轴刻度与标签
ax.set_yticks([])
ax.set_yticklabels([])
ax.set_ylabel('')

# 设置x轴标签
ax.set_xlabel("加入西天取经队伍回数", fontsize=12)

# 去除图的上、右、左边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# 在特定回数(例如20,40,60,80)添加竖直参考虚线
for line_pos in [20, 40, 60, 80]:
    ax.axvline(x=line_pos, color='grey', linestyle=':', linewidth=1, alpha=0.7)

# 添加标题
ax.set_title("《西游记》师徒取经队伍形成示意图", fontsize=14)

plt.tight_layout()
plt.show()
