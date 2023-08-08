print ("Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000")
print ("habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A") 
print (" ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. \n\n")

popA = 80000
popB = 200000

ano=0

while popA < popB:
    popA+=round((popA*3.0)/100)
    popB+=round((popB*1.5)/100)
    ano=ano+1

print ("levará", ano, "anos para a População do País A ser maior do que o País B ")
print ("população País A: \n " , popA, "habitantes")
print ("população País B: \n " , popB, "habitantes")
