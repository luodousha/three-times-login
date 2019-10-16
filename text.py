# _*_ encoding=utf-8 _*_
file_path= r'C:\Users\Administrator\Desktop\Python-100-Days-master\python_practice\day10\login\user'


def func():
    with open(file_path,'r')as f:
        # for line in f:
        #     pass
            # print(line.strip())
        # print(f.tell())
        f.read()#必须要读一遍
        f.seek((int(f.tell())-2),0)
        kk=f.read()
        id_=int(kk[0])
        return id_
id=func()
print(id)
