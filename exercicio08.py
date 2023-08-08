numeros=5

primeiro=int(input("Numero 1: "))

count=1
maior=primeiro
soma=primeiro

while count< numeros:
    count += 1
    temp=int(input("Numero %d: " % count))
    soma += temp
    if temp>maior:
        maior = temp


media = soma / numeros
print("A Soma dos números é: \n:",soma)
print("O maior numero é \n:", maior)
print("A Media dos números é \n: %.2f" % (soma/numeros))

