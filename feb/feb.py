

def feb(num):
    if num <= 0:
        print('feb() Error : num <= 0 : num = ' + str(num))
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return feb(num - 2) + feb(num - 1)


if __name__ == '__main__':
    n = feb(100)
    print('feb(10) = ' + str(n))
