import jieba
import codecs
import sys
import time
from progressbar import ProgressBar


class CharacterGraph:
    # properties
    name_list = {}  # 存储人物名字
    division_num = 0  # 按此数值将文本分段
    name_in_section = []  # 存储段落中人物的出现情况
    relations = {}

    #读取名字列表和文本文件并分段
    def __init__(self, nameFile, novleFile, division_num=3000, scope=sys.maxsize):

        # 设置分割段落长度
        self.division_num = division_num

        # 读取人物名称
        with codecs.open(nameFile, encoding='utf-8', mode='r') as f:
            for name in f.readlines():
                self.name_list.setdefault(name.strip(), 0)

        # 将文本分段存储
        count = 0
        nameInSection = {}
        with codecs.open(novleFile, encoding='utf-8', mode='r') as f:
            print("Start reading the file:")
            lines = f.readlines()
            bar = ProgressBar()
            for i, line in enumerate(bar(lines[:scope])):
                # 统计人物出现次数
                for name in self.name_list:
                    if (name in line):
                        self.name_list[name] += 1
                        # 统计每段中人物的出现次数
                        if (name not in nameInSection):
                            nameInSection[name] = 1
                        else:
                            nameInSection[name] += 1

                count += len(line.strip())
                if (count > self.division_num):
                    count = 0
                    self.name_in_section.append(nameInSection)
                    nameInSection = {}
        time.sleep(0.01)

    #获取对应的人物关系
    def getRelationship(self):
        for section in self.name_in_section:
            if (len(section) <= 1):
                continue
            items = [x for x in section]
            sorted(items)
            s = 0

            #TODO:improve the algorithm
            for i1, v1 in enumerate(items[:-2]):
                for i2, v2 in enumerate(items[i1 + 1:]):
                    if ((v1, v2) not in self.relations):
                        self.relations.setdefault((v1, v2), section[v1]+section[v2])
                    else:
                        self.relations[(v1, v2)] += section[v1]+section[v2]



    #保存节点文件和边文件,用于gephi绘图
    def saveGephiData(self,threshold=0):
        dirName = "Gephi"
        import os
        if(not os.path.exists(dirName)):
            os.mkdir(dirName)
        with codecs.open("%s/Nodes.txt" % dirName,encoding='utf-8',mode='w') as f:
            f.write("Id Label Weight\n")
            f.writelines(
                ["%s %s %d\n" % (name,name,self.name_list[name]) for name in self.name_list if self.name_list[name]!=0]
            )
        with codecs.open("%s/Edges.txt" % dirName,encoding='utf-8',mode='w') as f:
            f.write("Source Target Weight Type\n")
            f.writelines(
                ["%s %s %d undirected\n" % (tup[0],tup[1],self.relations[tup]) for tup in self.relations if self.relations[tup]>threshold]
            )

        print("Save finished.")

if (__name__ == "__main__"):
    cg = CharacterGraph(nameFile='example_2/name_list.txt', novleFile="example_2/zx.txt",division_num=5000)
    cg.getRelationship()
    # print('\n'.join([str(x) + "=%d" % cg.relations[x] for x in cg.relations if (cg.relations[x] != 0)]))
    # print([(x,cg.name_list[x]) for x in cg.name_list if cg.name_list[x]!=0])
    cg.saveGephiData(threshold=0)
