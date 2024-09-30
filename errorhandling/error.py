try:
    a=10
    print(a/0)
except ZeroDivisionError as e:
    print("0 is not divide")