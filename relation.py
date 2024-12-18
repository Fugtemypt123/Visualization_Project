import pandas as pd
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.lines import Line2D

import json

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 假设你的CSV文件为 relations.csv，并且有列：head, tail, relation, label
# CSV编码如果为UTF-8则无需额外指定，否则需要指定encoding
df = pd.read_csv('./original_data/triples.csv')

# 创建有向图（如需要无向图，可使用Graph()）
G = nx.DiGraph()

with open('./relation_data/relation.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

identity_color_map = {
    "佛家": "gold",
    "天庭": "lightblue",
    "其它": "lightgreen"
}

name_role_map = {}
for role_type, name_list in data.items():
    for name in name_list:
        name_role_map[name] = role_type

# 将数据加入图中
# 节点为人物（head和tail），边为关系。你可以决定是从head指向tail还是tail指向head。
# 这里假设从head指向tail表示某种关系。
for _, row in df.iterrows():
    head = row['head']
    tail = row['tail']
    relation = row['relation']  # 英文关系标签
    label = row['label']        # 中文关系标签
    
    # 将边加入图中，并将关系作为边的属性
    G.add_node(head)
    G.add_node(tail)
    G.add_edge(head, tail, relation=relation, label=label)

# 选择一个布局
pos = nx.spring_layout(G, k=1.5, seed=42)  
# 你也可以尝试其他布局，如 nx.circular_layout(G)

# 定义关系类型与颜色映射，可以自行挑选颜色
unique_relations = df['relation'].unique()
colors = plt.cm.get_cmap('tab10', len(unique_relations))  # 使用tab10调色板
relation_color_map = {rel: colors(i) for i, rel in enumerate(unique_relations)}

node_colors = []
for node in G.nodes():
    identity = name_role_map.get(node, "其它")
    node_colors.append(identity_color_map.get(identity, "lightblue"))

plt.figure(figsize=(12, 8))
# 绘制节点：减小节点大小
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=800, alpha=0.65)
nx.draw_networkx_labels(G, pos, font_size=6, font_family='sans-serif')

# 分关系类型绘制边，不显示标签
for rel in unique_relations:
    # 找出该关系类型对应的边
    edges_rel = [(u, v) for u, v, d in G.edges(data=True) if d.get('relation') == rel]
    nx.draw_networkx_edges(G, pos, edgelist=edges_rel, width=2, alpha=0.7, arrows=True, arrowstyle='-|>', arrowsize=15, edge_color=relation_color_map[rel])

# 创建图例
legend_elements = []
for identity, color in identity_color_map.items():
    legend_elements.append(Line2D([0], [0], marker='o', color='w', label=identity,
                                  markerfacecolor=color, markersize=10))
    
# plt.legend(handles=legend_elements, title='d', loc='upper left', bbox_to_anchor=(1.05, -1))
    
# legend_elements = []
for rel in unique_relations:
    legend_elements.append(Line2D([0], [0], color=relation_color_map[rel], lw=2, label=rel))

plt.legend(handles=legend_elements, title='人物身份&关系类型', loc='upper left', bbox_to_anchor=(1.05, 1))
plt.title("人物关系图", fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()