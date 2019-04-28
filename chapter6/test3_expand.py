import pandas as pd
from random import shuffle  # 导入随机函数shuffle，用来打乱数据
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.externals import joblib

def func():
    datafile = "./expand/Expand_Data.xls"

    # 读取数据
    data = pd.read_excel(datafile)

    # 删除无用特征
    data = data.drop([u"纳税人编号"], axis=1)

    # 取出数据当中的特征值和目标值
    y = data[u"输出"]
    x = data.drop([u"输出"], axis=1)

    # 分割数据集到训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 进行处理（特征工程）
    dict = DictVectorizer(sparse=False)

    x_train = dict.fit_transform(x_train.to_dict(orient="recorrds"))
    x_test = dict.transform(x_test.to_dict(orient="recorrds"))

    # 用决策树进行预测
    treefile = "./tmp/treecar.pkl"
    dec = DecisionTreeClassifier()
    dec.fit(x_train, y_train)
    joblib.dump(dec, treefile)

    # 预测准确率
    print(dec.score(x_test, y_test))
    print(x_train)


if __name__ == '__main__':
    func()