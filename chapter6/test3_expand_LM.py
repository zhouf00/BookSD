import pandas as pd
from random import shuffle
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

def test():
    """
    偷漏税
    :return:
    """
    datafile = "./expand/Expand_Data.xls"

    # 读取数据
    data = pd.read_excel(datafile,encoding="utf-8")

    # pandas数值替换
    data.replace(["正常","异常"],["a","b"], inplace=True)

    # 取出数据当中的特征值和目标值
    y = data[u"输出"]
    x = data.drop([u"输出"], axis=1)

    # 进行数据的分割训练集合测试集
    x_train, x_test,  y_train, y_test = train_test_split(x, y, test_size=0.2)
    print(y_train)

    # 进行处理（特征工程）
    dict = DictVectorizer(sparse=False)

    x_train = dict.fit_transform(x_train.to_dict(orient="recorrds"))

    x_test = dict.transform(x_test.to_dict(orient="recorrds"))

    # 构建LM神经网络模型
    modelfile = "./tmp/LMcar.model"

    model = Sequential()
    model.add(Dense(units=10, input_dim=26))
    model.add(Activation("relu"))
    model.add(Dense(input_dim=10, units=1))
    model.add(Activation("sigmoid"))
    #model.compile(loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])
    model.compile(loss="binary_crossentropy", optimizer="adam")
    model.fit(x_train, y_train, epochs=5, batch_size=1)

    #classes = model.predict(x_test, batch_size=128)
    prdeict_result =model.predict_classes(x_train.reshape(len(data)))
    print()

if __name__ == '__main__':
    test()