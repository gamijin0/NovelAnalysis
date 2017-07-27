import codecs
res = []

with codecs.open("name_pre.txt",encoding='utf-8') as f:
    for line in f.readlines():
        if(line[0] in [str(x) for x in range(0,10)]):
            res.append(line[line.find('、')+1:line.find('：')])


with codecs.open("name_list.txt",encoding='utf-8',mode='w') as f:
    for name in res:
        f.write(name+'\n')