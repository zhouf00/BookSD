from keras.models import load_model

my_model = load_model("./tmp/net.model2")

import pandas as pd
from random import shuffle  # 导入随机函数shuffle，用来打乱数据


datafile = "./data/model.xls"
data = pd.read_excel(datafile)  # 读取数据，数据前三列是特征，第四列是标签
data = data.values  # 将表格转换为矩阵
shuffle(data)

p = 0.8  # 设置训练数据比例
train = data[:int(len(data)*p), :]  # 前80%为训练集
test = data[int(len(data)*p):, :]  # 后20%为测试集

print(my_model.predict(test[:])[0])