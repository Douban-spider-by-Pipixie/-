import random
import math


# -*- coding:utf-8 -*-
class ItemBasedCF:
    def __init__(self, datafile=None, encoding='utf-8'):
        self.encoding = encoding
        self.datafile = datafile
        self.readData()
        self.splitData(3, 47)

    def readData(self, datafile=None):
        """
        read the data from the data file which is a data set
        """
        self.datafile = datafile or self.datafile
        self.data = []
        for line in open(self.datafile):
            userid, itemid, record, mtime = line.split("\t")  # 分割每行信息,导出属性
            self.data.append((userid, itemid, int(record)))  # 去掉时间导入到数据集data中

    def splitData(self, k, seed, data=None, M=8):
        """
        split the data set
        testdata is a test data set
        traindata is a train set
        """
        self.testdata = {}  # dict字典数据类型
        self.traindata = {}
        data = data or self.data  # readDate()里的数据
        random.seed(seed)
        for user, item, record in self.data:
            if random.randint(0, M) == k:
                self.testdata.setdefault(user, {})
                # testdata[user]={}
                self.testdata[user][item] = record  # 建立user,item二维组存储测试数据
            else:
                self.traindata.setdefault(user, {})
                self.traindata[user][item] = record  # 建立user,item二维组存储训练数据

    def ItemSimilarity(self, train=None):  #
        """
        calculate co-rated users between items
        """
        train = train or self.traindata
        C = dict()  # 创建空字典 https://blog.csdn.net/qq_42278791/article/details/90180538?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158798036719195239824207%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=158798036719195239824207&biz_id=0&utm_source=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-2
        N = dict()
        for u, items in train.items():  # 找出item
            for i in items.keys():
                N.setdefault(i, 0)
                N[i] += 1
                for j in items.keys():  # 找出不同item的
                    if i == j:
                        continue
                    C.setdefault(i, {})
                    C[i].setdefault(j, 0)
                    C[i][j] += 1
                    print("C[", i, "][", j, "]=", C[i][j], "   ", "N[", i, "]=", N[i])


if __name__ == "__main__":
    cf = ItemBasedCF('C:/Users/HP/Desktop/u.data')
    cf.ItemSimilarity()
