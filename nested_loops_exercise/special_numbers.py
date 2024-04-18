num = int(input())

special_num = ''

for n in range(1111, 10000):

    flag = False
    n_as_str = str(n)

    for i in range(0, len(n_as_str)):

        if int(n_as_str[i]) == 0:
            flag = False
            break
        else:
            if num % int(n_as_str[i]) == 0:
                flag = True
            else:
                flag = False
                break

    if flag:
        special_num += f'{n_as_str} '
        flag = False

print(special_num)
