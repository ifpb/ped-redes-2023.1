food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []

for x in food:
    try:
        fifth.append(x[4])
    except IndexError:
        print(x, "pulado porque não tem 5 letras")
        pass

print(fifth)
