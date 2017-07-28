import jieba
import codecs
import sys


class CharacterGraph:
    # properties
    name_list = {}  # 存储人物名字
    division_num = 0  # 按此数值将文本分段
    section_list = []  # 存储文章段落

    def __init__(self, nameFile, novleFile, division_num=3000, scope=sys.maxsize):

        # 设置分割段落长度
        self.division_num = division_num

        # 读取人物名称
        with codecs.open(nameFile, encoding='utf-8', mode='r') as f:
            for name in f.readlines():
                self.name_list.setdefault(name.strip(), 0)

        # 将文本分段存储
        count = 0
        section = []
        with codecs.open(novleFile, encoding='utf-8', mode='r') as f:
            for line in f.readlines()[:scope]:
                # 统计人物出现次数
                for name in self.name_list:
                    if (name in line):
                        self.name_list[name] += 1

                section.append(line.strip())
                count += len(line.strip())
                if (count > self.division_num):
                    count = 0
                    self.section_list.append(section)
                    section = []



if (__name__ == "__main__"):
    cg = CharacterGraph(nameFile='example/name_list.txt', novleFile="example/pfdsj.txt", scope=10000)
    print([(x,cg.name_list[x]) for x in cg.name_list if cg.name_list[x]!=0])
