def count_num(arr,to_cnt):
    count = 0
    for i in arr:
        if i == to_cnt:
            count += 1
    return count

x = [1,2,2,4,4,4,4,4,3,2,6]

print(count_num(x,4))
