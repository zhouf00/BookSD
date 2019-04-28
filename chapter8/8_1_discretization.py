"""
聚类离散化，最后的result的格式为：
"""

import pandas as pd
from sklearn.cluster import KMeans  # 导入K均值聚类算法

datafile = "./data/data.xls"
processedfile = "./tmp/data_processed.xls"  # 处理后的文件
typelabel = {u"肝气郁结证型系数":"A", u"热毒蕴结证型系数":"B",u"冲任失调证型系数":"C",
             u"气血两虚结证型系数":"D",u"脾胃虚弱证型系数":"E",u"肝肾阴虚证型系数":"F"}

keys = list(typelabel.keys())
print(keys[0])
print(typelabel[keys[0]]+"n")