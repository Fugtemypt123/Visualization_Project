import pandas as pd
import json

def extract_people():
    # 读取CSV文件
    df = pd.read_csv('./original_data/triples.csv')

    # 提取head和tail列的所有人物
    all_people = pd.concat([df['head'], df['tail']])

    # 去重并转为列表
    unique_people = all_people.unique().tolist()

    # 保存为JSON文件
    with open('./relation_data/people.json', 'w', encoding='utf-8') as f:
        json.dump(unique_people, f, ensure_ascii=False, indent=4)


def reverse():
    # 假设你将上一步的.json文件命名为 roles.json
    with open('roles.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # data的结构为：
    # {
    #   "佛家": [...],
    #   "天庭": [...],
    #   "其它": [...]
    # }

    name_role_map = {}
    for role_type, name_list in data.items():
        for name in name_list:
            name_role_map[name] = role_type

    # 测试打印结果
    print(name_role_map)


