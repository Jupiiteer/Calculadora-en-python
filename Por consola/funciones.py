def suma(*args):
    total = 0
    for num in args:
        total += num
    print("Resultado: " + str(total))
def resta(*args):
    total = 0
    for num in args:
        total -= num
    print("Resultado: " + str(total))
def division(*args):
    total = 0
    for num in args:
        total /= num
    print("Resultado: " + str(total))
def multipliacion(*args):
    total = 0
    for num in args:
        total *= num
    print("Resultado: " + str(total))