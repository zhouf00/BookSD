import pandas as pd  # 导入数据分析库
from random import shuffle  # 导入随机函数shuffle，用来打乱数据
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from cm_plot import *

def tree():
    """
    决策树对窃漏电用户自动识别
    :return: None
    """

    # 获取数据
    treefile = "./data/model.xls"
    data = pd.read_excel(treefile)
    data = data.values  # 将表格转换为矩阵
    shuffle(data)  # 随机打乱数据

    p = 0.8  # 设置训练数据比例
    train = data[:int(len(data)*p), :]  # 前80%为训练集
    test = data[int(len(data)*p):, :]  # 后20%为训练集


    x_train = train[:, :3]
    y_train = train[:, 3]

    x_test = test[:, :3]
    y_test = test[:, 3]

    treefile2 = "./tmp/tree.pkl"  # 模型输出名字
    dec = DecisionTreeClassifier()  # 建立决策树模型
    dec.fit(x_train, y_train)

    joblib.dump(tree, treefile2)
    print("预测准确率：", dec.score(x_test, y_test))
    #cm_plot(y_test, dec.predict(x_test)).show()
    #RF = joblib.load(treefile2)
    #result = RF.predict(x_test)
    #print(result)
    print(y_test)


if __name__ == '__main__':
    tree()