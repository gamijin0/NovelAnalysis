import codecs
res = []

with codecs.open("name_pre.txt",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        if(line):
            name = line[:line.find('：')].strip()
            res.append(name)


with codecs.open("name_list.txt",encoding='utf-8',mode='w') as f:
    for name in res:
        f.write(name+'\n')