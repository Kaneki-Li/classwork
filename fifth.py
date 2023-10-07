def solution(string):
    result=""
    for i in range(len(string)-1, -1, -1):
        result += string[i]
    print(result)
user_string = str(input("Введите строку которую необходимо инвертировать: "))
solution(user_string)
