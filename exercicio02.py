# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

print("Informe um usuário e uma senha para cadastro no sistema")
usuario=str(input("Usuário: \n "))
senha=(input("Senha: \n"))
while usuario==senha:
	print("ERRO: o usuário não pode ser igual a senha, tente novamente")
	usuario=str(input("Usuário: \n "))
	senha=(input("Senha: \n"))
else:
	print("cadastrado efetuado com sucesso")