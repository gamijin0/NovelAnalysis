import jieba
import codecs
import sys
import time
from progressbar import  ProgressBar


class CharacterGraph:
    # properties
    name_list = {}  # 存储人物名字
    division_num = 0  # 按此数值将文本分段
    name_in_section = []  # 存储段落中人物的出现情况


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
            lines = f.readlines()
            bar = ProgressBar()
            for i,line in enumerate(bar(lines[:scope])):
                # 统计人物出现次数
                for name in self.name_list:
                    if (name in line):
                        self.name_list[name] += 1
                        #统计每段中人物的出现次数
                        if (name not in nameInSection):
                            nameInSection[name] = 1
                        else:
                            nameInSection[name]+=1

                count += len(line.strip())
                if (count > self.division_num):
                    count = 0
                    self.name_in_section.append(nameInSection)
                    nameInSection = {}
        time.sleep(0.01)

    def getRelationship(self):
        for section in self.name_in_section:
            pass


if (__name__ == "__main__"):
    cg = CharacterGraph(nameFile='example/name_list.txt', novleFile="example/pfdsj.txt")
    print(cg.name_in_section)
    # print([(x,cg.name_list[x]) for x in cg.name_list if cg.name_list[x]!=0])
