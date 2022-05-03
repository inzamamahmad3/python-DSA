def add(i):
    if i > 10:
        return
    print(i)
    i = i+ 1
    add(i)




add(1)