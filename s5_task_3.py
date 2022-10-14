'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
'''
from itertools import groupby , starmap

def rle_encode(origin, encd):
    with open(origin, "r", encoding = "utf-8") as file, \
        open(encd, "w", encoding = "utf-8") as file_encode:
        for i in file:
            file_encode.write("".join([f"{len(list(v))}{ch}" for ch,v in groupby(i)]))

def rle_decode(file_name):
    with open(file_name, "r", encoding = "utf-8") as file:
        n = ""
        for i in file:
            word_list = []
            for k in i.strip():
                if k.isdigit():
                    n+=k
                else:
                    word_list.append([int(n),k])
                    n = ""
            print("".join(starmap(lambda x,y: x*y, word_list)))


rle_encode("task_3_text.txt", "task_3_encode.txt")
rle_decode("task_3_encode.txt")