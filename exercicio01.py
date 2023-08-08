#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

numero = int(input("Digite um número:\n"))
numero_invalido = numero < 0 or numero > 10
while numero_invalido:
    print("O número deve ser entre 0 e 10")
    numero = int(input("Digite um número:\n"))
    numero_invalido = numero < 0 or numero > 10

else:
    print("numero está correto!")
