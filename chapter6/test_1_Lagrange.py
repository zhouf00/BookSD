# 拉格朗插值代码
import pandas as pd
from scipy.interpolate import lagrange  # 导入拉格朗日插值函数


inputfile = "./data/missing_data.xls"
outputfile = "./tmp/missing_data_processed.xls"

data = pd.read_excel(inputfile, header=None)

# 自定义列向量插值函数
# s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
def ployinterp_column(s, n, k=5):
    y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))]  # 取数
    y = y[y.notnull()]  # 剔除空值
    print("%s,%s"%(y.index, n))
    print("list y:",list(y))
    return lagrange(y.index, list(y))(n)  # 插值并返回插值结果
    # y.index索引， list(y)值
print("%s"%"*"*50)
print(data)
print("%s"%"*"*50)
print("data:%d"%len(data))
print((data[1].isnull())[3])
print("%s"%"*"*50)

for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j] = ployinterp_column(data[i], j)
print("%s"%"*"*50)
print(data.columns)
data.to_excel(outputfile, header=None, index=False)