import matplotlib.pyplot as plt
import json

# 定义数据
with open('occur_times.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 处理数据
# 提取并排序章节
chapters = data.keys()

# 定义类别及其对应的Y轴位置
categories = ['佛家', '天庭', '其他妖怪']
y_positions = {category: i for i, category in enumerate(categories)}

# 准备绘图数据
x = []  # 章节编号
y = []  # 类别位置
sizes = []  # 气泡大小
colors = []  # 气泡颜色

# 定义颜色映射
color_map = {'佛家': 'blue', '天庭': 'green', '其他妖怪': 'red'}

for chapter_num, chapter in enumerate(chapters):
    # chapter_num = int(chapter.replace('第','').replace('回',''))
    print(chapter_num, chapter)
    for category in categories:
        value = data[chapter].get(category, 0)
        if value > 0:
            x.append(chapter_num)
            y.append(y_positions[category])
            sizes.append(value * 1000)  # 调整气泡大小的比例
            colors.append(color_map[category])

# 绘制气泡图
plt.figure(figsize=(20, 8))
scatter = plt.scatter(x, y, s=sizes, c=colors, alpha=0.6, edgecolors='w', linewidth=0.5)

# 设置Y轴标签
plt.yticks(list(y_positions.values()), list(y_positions.keys()))

# 设置X轴范围
plt.xlim(0, 101)
plt.xlabel('章节', fontsize=14)
plt.title('《西游记》一百回中佛家、天庭和妖怪出现次数气泡图', fontsize=16)

# 创建图例
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='佛家',
           markerfacecolor='blue', markersize=10),
    Line2D([0], [0], marker='o', color='w', label='天庭',
           markerfacecolor='green', markersize=10),
    Line2D([0], [0], marker='o', color='w', label='其他妖怪',
           markerfacecolor='red', markersize=10)
]
plt.legend(handles=legend_elements, title='类别', loc='upper right')

# 显示网格
plt.grid(True, linestyle='--', alpha=0.5)

# 保存图片
plt.savefig('bubble_chart.png')