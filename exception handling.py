# exception handling using try except finally

a = 5
b = 0

try:
    print(a/b)

except ZeroDivisionError as ze:
    print("please check the input, the error message is - ", ze)

finally:
    print("hello from finally")