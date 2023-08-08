num1=int(input("digite o valor do número 01: \n "))
num2=int(input("digite o valor do número 02: \n "))

while num2<num1:
	print("O valor do número 01 não pode ser maior do que o valor do número 02")
	num1=int(input("digite o valor do número 01: \n"))
	num2=int(input("digite o valor do número 02: \n  "))
else:
	for i in range(num1,num2,1):
		print(i)