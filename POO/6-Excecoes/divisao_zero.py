a = 5
b = 0
try:
    result = a/b
except ZeroDivisionError:
    result = "You can't divide with 0"

print(result)

