# K-Means聚类算法

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib as plt

def func():
    inputfile = "./tmp/data_new.xls"
    k = 5

    # 读取数据并进行聚类分析
    data = pd.read_excel(inputfile)

    # 调用k-means算法，进行聚类分析
    kmodel = KMeans(n_clusters=k, n_jobs=4)  # n_jobs是并行数，一般等于CPU数
    kmodel.fit(data)  # 训练模型

    # kmodel.cluster_centers_  # 查看聚类中心
    # kmodel.labels_  # 查看各样本对应的类别
    r1 = pd.DataFrame(kmodel.cluster_centers_)

def func1():
    inputfile = "./tmp/zscoredata.xls"
    outfile = "./tmp/data_new1.xls"
    k = 5
    mylist = ["ZL","ZR", "ZF", "ZM","ZC"]

    # 读取数据并进行聚类分析
    data = pd.read_excel(inputfile)
    result = pd.DataFrame()
    # kmodel.cluster_centers_  # 查看聚类中心
    # kmodel.labels_  # 查看各样本对应的类别
    for i in range(len(mylist)):
        # 调用k-means算法，进行聚类分析
        kmodel = KMeans(n_clusters=k, n_jobs=4)  # n_jobs是并行数，一般等于CPU数
        kmodel.fit(data[[mylist[i]]].values)  # 训练模型
        r1 = pd.DataFrame(kmodel.cluster_centers_, columns=[mylist[i]])
        result = result.append(r1.T)
        #r2 = pd.Series(kmodel.labels_).value_counts()  # 分类统计
        #r2 = pd.DataFrame(r2,)
    result.to_excel(outfile)



if __name__ == '__main__':
    #func()
    func1()