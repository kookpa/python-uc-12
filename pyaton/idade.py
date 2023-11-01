idade = int(input("digite a idade:"))

if idade < 8:
    print("bebê")
elif idade >= 8 and idade <= 13:
    print("criança")
elif idade >= 14 and idade <= 20:
    print("adolecente")
elif idade >= 21 and idade <= 64:
    print("idoso")
