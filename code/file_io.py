import pandas as pd
import json
### 1. csv
# file_path = './Data/read_csv_sample.csv'
# df = pd.read_csv(file_path, header=0)
# print(df)
# df = pd.read_csv(file_path, index_col='c1')
# print(df)

### 2. Excel
df = pd.read_excel('./Data/남북한발전전력량.xlsx') # header = 0
print(df)

### 3. json
df = pd.read_json('./Data/read_json_sample.json')
print(df)
print(df.index)

# file = open('./Data/000000.json')
# return json file
# with open('./Data/000000.json') as f:
#     data = json.load(f)
#     # print(data)
#     img = data['Image']
#     objects = data['Object']
#
#     # python: filter
#     # filter(function, arg)
#     # mask = list(filter(lambda objects: objects['level']==0
#     #                                    and objects['class'] != 'Dontcare', objects))
#     mask = [obj for obj in objects if obj['level']==0 and obj['class'] != 'Dontcare']
#
#     for idx, val in enumerate(mask):
#         w = val['box2d']['x2'] - val['box2d']['x1']
#         h = val['box2d']['y2'] - val['box2d']['y1']
#         size = w * h
#         if ((val['class'] == 'Truck' or val['class'] == 'Car') and size >= 10000):
#             mask[idx]['class'] = 'Bus'
#
#     rtn_data = {
#         'Image': img,
#         'Object': mask[:]
#     }
#     print(rtn_data)

with open('./Data/000000.json') as f:
    data = json.load(f)
    objects = data['Object']
    df = pd.DataFrame(objects)
    print(df)
    # print(df[(df['level'] != 0) | (df['class'] == 'Dontcare')].index)
    df.drop(df[(df['level'] != 0) | (df['class'] == 'Dontcare')].index, inplace=True)
    df.loc[df[(df['class'] == 'Truck') | (df['class'] == 'Car')].index, 'class'] = 'Bus'
    print(df)
    # orient: records ==> list of dictionary
    dict_data = df.to_dict(orient='records')
    data['Object'] = dict_data

file_path = './Data/000000_modify.json'
with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)



