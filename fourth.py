def make_negative(num):
    if num == 0:
        print(0)
    elif num < 0:
        print(num)
    else:
        print(num-(num*2))
user_num = int(input("Введите число которое необходимо сделать отрицательным: "))
make_negative(user_num)
