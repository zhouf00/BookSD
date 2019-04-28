import pandas as pd
from random import shuffle  # 导入随机函数shuffle，用来打乱数据
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib


def mysorce(x, y):
    count = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            pass
        else:
            count += 1
    return (len(x)-count)/len(x)

def test():
    # 获取数据
    treefile = "./expand/Expand_Data.xls"
    data = pd.read_excel(treefile)
    data = data.drop([u"销售类型"], axis=1)
    data = data.drop([u"销售模式"], axis=1)
    data = data.values

    x_train = data[:, :13]
    y_train = data[:, 13]

    treefile2 = "./tmp/treecar.pki"  # 模型输出名字
    #tree = DecisionTreeClassifier()  # 建立决策树模型
    RF = joblib.load(treefile2)  # 加载模型
    result = RF.predict(x_train)  # 预测结果
    print(result)
    print(mysorce(y_train, result))





if __name__ == '__main__':
    test()