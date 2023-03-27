lst=[5, 10, 20]
msg = ""
try:
    lst[5]
except IndexError:
    msg = "you're out of list range"

print(msg)

