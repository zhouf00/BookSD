# 提取信息

import pandas as pd


datafile = "./data/air_data.csv"
cleanedfile = "./tmp/data_new.xls"  # 数据清洗后保存的文件

data = pd.read_csv(datafile, encoding="utf-8")
data = data[["LOAD_TIME", "FFP_DATE", "LAST_TO_END", "FLIGHT_COUNT", "SEG_KM_SUM", "AVG_DISCOUNT"]]

data["L"] = pd.to_datetime(data["LOAD_TIME"]) - pd.to_datetime(data["FFP_DATE"])
#data["L"] = pd.to_numeric(data["L"])  # 转换成数字
data["L"] = data["L"].map(lambda x:x.days)  # 把时间转化成天的整数
data = data.drop(["LOAD_TIME"],axis=1)
data = data.drop(["FFP_DATE"],axis=1)
data["R"] = data["LAST_TO_END"]
data["F"] = data["FLIGHT_COUNT"]
data["M"] = data["SEG_KM_SUM"]
data["C"] = data["AVG_DISCOUNT"]
data = data.drop(
    ["LAST_TO_END", "FLIGHT_COUNT","SEG_KM_SUM", "AVG_DISCOUNT"],axis=1)
# 单位转换
data.eval("""
    L = L / 30
    R = R / 30""", inplace=True)  # 列进行计算

data.to_excel(cleanedfile, index=False)

data.to_excel(cleanedfile)