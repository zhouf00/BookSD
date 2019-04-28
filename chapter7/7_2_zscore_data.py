import pandas as pd


datafile = "./tmp/data_new1.xls"
zscorefile = "./tmp/zscoredata.xls"  # 标准差化后的数据存储路径

data = pd.read_excel(datafile)
data = (data - data.mean(axis=0))/(data.std(axis=0))
# 简洁的语句实现标准化变换，类似的可以实现任何想要的变换

data.columns = ["Z" + i for i in data.columns]  # 表头重命名

data.to_excel(zscorefile, index=False)