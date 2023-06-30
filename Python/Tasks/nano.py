a = int(input('Please insert a value "a": '))
b = int(input('Please insert a value "b": '))
opr = input('What operation do you want perform (and, or, xor, nand, xnor, nor): ').lower()
# print(f"Your chosen values are: {a} and {b}. The operation you chose is {opr}.")
print(f"{a} {opr} {b}")

if opr == "and":
    print(bool(a and b))
elif opr == "or":
    print(bool(a or b))
elif opr == "xor":
    print(bool(a ^ b))
elif opr == "nand":
    print(bool(not(a and b)))
elif opr == "xnor":
    print(bool(not(a ^ b)))
elif opr == "nor":
    print(bool(not(a or b)))
else:
    print("Wrong option. ")