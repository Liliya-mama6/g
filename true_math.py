def apply_all_func(spisok, *func):
    a={}
    for i in range(len(func)):
        a[func[i].__name__]=func[i](spisok)
    return a
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
