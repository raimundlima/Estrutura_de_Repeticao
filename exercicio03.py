# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = str(input("Informe o seu nome: \n"))
while (len(nome)<= 3):
    print ("Informe o seu nome correto!")
    nome = str(input("Informe o seu nome: \n"))



idade = int(input("Informe sua Idade: \n"))
while (idade > 150 or idade < 0):
    print ("Informe sua idade correta!")
    idade = int(input("Informe sua Idade: \n"))
    

salario = float(input("Informe seu salário: \n"))
while (salario <= 0):
    print ("Informe seu salário correto!")
    salario = float(input("Informe seu salário: \n"))


genero = str(input("Informe o seu Gênero M para masculino, F para Feminino O para Outro \n "))
while genero !="M" and genero !="F" and genero !="O":
    print ("Informe o seu Gênero! ")
    genero = str(input("Informe o seu Gênero M para masculino, F para Feminino O para Outro \n "))

estado_civil = str(input("informe o seu estado Civil: S para solteiro, C para casado , V para viúvo ou D para divorciado \n "))
while estado_civil !="S" and estado_civil !="C" and estado_civil !="V" and estado_civil !="D":
    print ("Informe o seu Estado Civil")
    estado_civil = str(input("informe o seu estado Civil: S para solteiro, C para casado , V para viúvo ou D para divorciado \n "))




