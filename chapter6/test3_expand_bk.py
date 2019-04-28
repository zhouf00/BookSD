import pandas as pd
from random import shuffle
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

def test():
    """
    偷漏税
    :return:
    """
    datafile = "./expand/Expand_Data.xls"

    # 读取数据
    data = pd.read_excel(datafile)
    data = data.drop([u"销售类型"], axis=1)
    data = data.drop([u"销售模式"], axis=1)
    data = data.values
    shuffle(data)  # 打乱数据

    p = 0.8  # 设置训练数据比例
    train = data[:int(len(data)*p), :]  # 前80%为训练集
    test = data[int(len(data)*p):, :]  # 后20%为测试集

    x_train = train[:, :13]
    y_train = train[:, 13]

    x_test = test[:, :13]
    y_test = test[:, 13]

    # 构建CART决策树模型
    treefile = "./tmp/treecar.pkl"
    tree = DecisionTreeClassifier()
    tree.fit(x_train, y_train)

    joblib.dump(tree, treefile)

    print("预测准确率：", tree.score(x_test, y_test))


if __name__ == '__main__':
        test()