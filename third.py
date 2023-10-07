def positive_sum(arr):
    sum=0
    for i in arr:
        if i < 0:
            continue
        else:
            sum += i
    print(sum)
positive_sum([7,4,-9,2,0,-5,-1])
