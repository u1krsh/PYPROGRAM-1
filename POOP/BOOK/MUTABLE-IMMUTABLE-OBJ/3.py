def cnt(strr):  
    dic = {}
    for i in strr:
        dic[i] = dic.get(i, 0) + 1
    return dic
    

print(cnt('Hello World'))