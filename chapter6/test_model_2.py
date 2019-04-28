import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
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
    data = data.drop([u"纳税人编号"], axis=1)

    # 取出数据当中的特征值和目标值
    y = data[u"输出"]
    x = data.drop([u"输出"], axis=1)

    # 进行处理（特征工程）
    dict = DictVectorizer(sparse=False)

    x = dict.fit_transform(x.to_dict(orient="recorrds"))


    treefile = "./tmp/treecar.pkl"  # 模型输出名字
    RF = joblib.load(treefile)  # 加载模型
    result = RF.predict(x)  # 预测结果
    print(result)
    print(mysorce(y, result))





if __name__ == '__main__':
    test()