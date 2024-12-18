data = [
    [[5, 6, 7], '寅将军', '太白', 'white'],
    [[8], '', '', 'white'],
    [[9], '小白龙', '观音', 'pink'],
    [[10, 11], '黑大王', '观音', 'white'],
    [[12], '猪八戒', '', 'pink'],
    [[13, 14], '黄风大王', '灵吉菩萨', 'white'],
    [[15, 16], '沙和尚', '木吒（观音）', 'pink'],
    [[17], '', '', 'white'],
    [[18, 19], '镇元子', '观音', 'lightblue'],
    [[20], '白骨夫人', '山神土地', 'lightblue'],
    [[21, 22, 23], '黄袍怪', '玉帝', 'lightblue'],
    [[24, 25], '金角银角', '', 'lightblue'],
    [[26, 27], '乌鸡国狮子精', '', 'orange'],
    [[28, 29, 30, 31], '', '', 'white'],
    [[32], '', '', 'lightblue'],
    [[33, 34, 35], '虎力鹿力羊力', '', 'white'],
    [[36, 37, 38], '灵感大王', '观音', 'white'],
    [[39, 40, 41], '青牛精', '太上老君', 'lightblue'],
    [[42], '如意真仙', '', 'white'],
    [[43, 44], '蝎子精', '星官', 'white'],
    [[45, 46], '六耳猕猴', '如来', 'white'],
    [[47, 48, 49], '牛魔王铁扇公主', '众天神', 'white'],
    [[50, 51], '九头虫', '二郎神', 'white'],
    [[52], '', '', 'white'],
    [[53, 54], '黄眉', '天神、弥勒佛', 'orange'],
    [[55], '', '', 'white'],
    [[56, 57, 58], '', '', 'orange'],
    [[59], '', '', 'white'],
    [[60], '', '', 'white'],
    [[61, 62, 63, 64], '狮驼国', '如来、文殊、普贤', 'orange'],
    [[65, 66], '比丘国', '', 'lightblue'],
    [[67, 68, 69], '', '', 'white'],
    [[70], '', '', 'white'],
    [[71], '', '', 'white'],
    [[72], '', '', 'white'],
    [[73, 74], '黄狮精', '', 'white'],
    [[75, 76], '九灵元圣', '太乙救苦天尊', 'lightblue'],
    [[77], '', '', 'white'],
    [[78], '玉兔', '', 'lightblue'],
    [[79], '', '', 'white'],
    [[81], '老鼋', '', 'white']
]

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
font_properties = FontProperties(fname='SimHei', weight='bold')

fig, ax = plt.subplots(figsize=(12, 5))
plt.subplots_adjust(left=0, right=1, top=.9, bottom=0)  # Adjust the margins
x = np.arange(len(data))
bar_width = 0.8  # Width of the bars
for i, d in enumerate(data):
    ax.bar(i, len(d[0]) * 2, color=d[3], width=bar_width, align='center', bottom=-len(d[0])-3, edgecolor='black', linewidth=1+bool(d[2]))
    ax.text(i, -3, '\n'.join(d[1]), ha='center', va='center', rotation=0, fontsize=8, fontproperties='SimHei')  # Use SimHei font for Chinese characters

# Calculate the envelope line
envelope_x = np.arange(len(data))
envelope_y_upper = [len(d[0]) * 2 -3 for d in data]
envelope_y_lower = [-len(d[0]) * 2 -3 for d in data]

# Plot the upper and lower envelope lines
segments = [(0, 8, "red"), (8, 20, "purple"), (20, 30, "blue"), (30, len(data), "green")]
stories = [(0, 8, "师徒相聚"), (8, 20, "师徒磨合"), (20, 30, "硬核考验"), (30, len(data), "完美蜕变")]
for start, end, color in segments:
    ax.plot(envelope_x[start:end+1], envelope_y_upper[start:end+1], color=color, linestyle='--', linewidth=1)
    ax.plot(envelope_x[start:end+1], envelope_y_lower[start:end+1], color=color, linestyle='--', linewidth=1)
    
for i, (start, end, story) in enumerate(stories):
    ax.text((start+end)/2, -9, story, ha='center', va='bottom', fontsize=10, fontproperties='SimHei', color=segments[i][2])  # Use SimHei font for Chinese characters
    if i > 0:
        ax.axvline(x=start, color='gray', linestyle='--', linewidth=1)
        

names = [d[2] for d in data if d[2] != '']
# 去重但保持顺序
names = list(dict.fromkeys(names))
# Display names at the top
for i, name in enumerate(names):
    ax.text(5+2*i, max(envelope_y_upper)+(i%2), name, ha='center', va='bottom', fontsize=10, fontproperties='SimHei', color='orange', weight='bold')  # Use SimHei font for Chinese characters

# Draw arrows from names to corresponding bars
for i, d in enumerate(data):
    if d[2]:
        name_index = list(names).index(d[2])
        ax.annotate('', xy=(i, 0), xytext=(5 + name_index * 2, max(envelope_y_upper)+name_index%2),
                arrowprops=dict(arrowstyle='->', color=(1, .8, .6, .8), lw=1))

ax.set_xticks(x)
ax.set_xticklabels([d[1] for d in data], rotation=90, fontproperties='SimHei')  # Use SimHei font for Chinese characters
ax.axis('off')  # Turn off the axis
plt.show()
