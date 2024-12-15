import matplotlib.pyplot as plt
import numpy as np
import re
import json

# 您提供的归一化数据字典
with open('occur_times_data/occur_times_norm.json', 'r', encoding='utf-8') as file:
    chapter_data = json.load(file)

# 定义中文数字到阿拉伯数字的映射
num_map = {
    '零': 0, '一': 1, '二': 2, '三': 3, '四':4, '五':5, '六':6, '七':7, '八':8, '九':9,
    '十':10, '百':100
}

def chapter_number(chapter):
    """
    将章节名称转换为数字，以便正确排序。
    例如：“第一回” -> 1，“第二十回” -> 20
    """
    match = re.match(r'第([一二三四五六七八九十百]+)回', chapter)
    if not match:
        return 0
    num_str = match.group(1)
    total = 0
    unit = 1
    for char in reversed(num_str):
        if char == '十':
            if total == 0:
                total += 10
            else:
                total += 10 * unit
            unit = 1
        elif char == '百':
            total += 100 * unit
            unit =1
        else:
            total += num_map.get(char,0) * unit
            unit *=10
    return total

# 获取并排序回合名称
# sorted_chapters = sorted(chapter_data.keys(), key=lambda x: chapter_number(x))
sorted_chapters = list(chapter_data.keys())

del_keys = []
# 删除没有任何出现的章节
for chapter in sorted_chapters:
    if chapter_data[chapter]['佛家'] == 0 and chapter_data[chapter]['天庭'] == 0 and chapter_data[chapter]['其他妖怪'] == 0:
        del_keys.append(chapter)

for key in del_keys:
    del chapter_data[key]
    sorted_chapters.remove(key)

print(len(sorted_chapters))

# 提取每个类别的数据
buddhism = [chapter_data[chapter]['佛家'] for chapter in sorted_chapters]
heavenly_court = [chapter_data[chapter]['天庭'] for chapter in sorted_chapters]
other_monsters = [chapter_data[chapter]['其他妖怪'] for chapter in sorted_chapters]

# 设置柱状图的位置
x = np.arange(len(sorted_chapters))  # 回合数量
width = 0.8  # 柱子的宽度

plt.rcParams['font.family'] = ['SimHei']
# 创建图形和轴
fig, ax = plt.subplots(figsize=(30, 15))  # 调整图表尺寸以适应100回

# 绘制堆叠柱状图
ax.bar(x, buddhism, width, label='佛家', color='gold')
ax.bar(x, heavenly_court, width, bottom=buddhism, label='天庭', color='skyblue')
bottom_total = np.array(buddhism) + np.array(heavenly_court)
ax.bar(x, other_monsters, width, bottom=bottom_total, label='其他妖怪', color='lightgreen')

# 设置标签和标题
ax.set_xlabel('回合', fontsize=20)
ax.set_ylabel('比例', fontsize=20)
ax.set_title('100回中各类别妖怪比例堆叠柱状图', fontsize=24)

# 设置x轴刻度
ax.set_xticks(x)
# 由于回合较多，建议只显示每隔10回的标签
tick_interval = 10
ax.set_xticklabels([chapter if (i % tick_interval == 0) else '' for i, chapter in enumerate(sorted_chapters)],
                   rotation=90, fontsize=10)

# 添加图例
ax.legend(fontsize=16)

# 优化布局
plt.tight_layout()

# 存储图形（名称为柱状图的英文.png）
plt.savefig('visualize_images/stacked_bar_chart_ch.png')