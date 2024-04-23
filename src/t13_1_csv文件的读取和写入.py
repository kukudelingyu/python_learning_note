import csv

# 读取csv文件
with open("../data/score_data.csv") as f:
    # 用csv库处理数据 返回list[list[str]]
    cf = csv.reader(f)
    # 去除表头
    head = next(cf)
    scores = []
    for ele in cf:
        scores.append(float(ele[2]))
    # 统计总分
    all_socre = sum(scores)
    print(f"总分是：{all_socre}")
    # 统计平均分
    avg_score = all_socre/len(scores)
    print(f"平均分是：{avg_score}")

with open("../data/score_data.csv", mode="a", encoding="utf-8") as f:
    cf = csv.writer(f)
    cf.writerow(["tom","英语","75.5"])
