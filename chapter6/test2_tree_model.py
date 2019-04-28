import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
#from cm_plot import *

def tree():
    """
    决策树对窃漏电用户自动识别
    :return: None
    """

    # 获取数据
    treefile = "./data/model.xls"
    data = pd.read_excel(treefile)

    # 取出数据当中的特征值和目标值
    y = data[u"是否窃漏电"]
    x = data.drop([u"是否窃漏电"], axis=1)

    # 进行数据的分割训练集合测试集
    x_train, x_test,  y_train, y_test = train_test_split(x, y, test_size=0.2)

    # 特征工程（标准化）
    std = StandardScaler()

    # 对测试集和训练集的特征值进行标准化
    x_train = std.fit_transform(x_train)

    x_test = std.transform(x_test)

    # 进行算法流程
    dec = DecisionTreeClassifier()
    dec.fit(x_train, y_train)

    # 预测准确率
    print("预测准确率：", dec.score(x_test, y_test))

    #cm_plot(x_test, dec.predict(x_train)).show()


if __name__ == '__main__':
    tree()