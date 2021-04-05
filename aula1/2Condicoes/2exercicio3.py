x = int(input("digite um valor para X: "))
y = int(input("digite um valor para Y: "))
z = int(input("digite um valor para Z: "))

if x%y == 0:
    if x%z == 0:
        print(True)
    else:
        print(False)
else:
    print(False)