popA = float(input("Informe a população do País A: \n"))
popB = float (input("Informe a população do País B: \n"))

ano=0

tx_crescimentoA = float(input("Informe a taxa de crescimento do País A: \n"))
tx_crescimentoB = float(input("Informe a taxa de crescimento do País B: \n"))


while popA < popB:
    popA+=round((popA*tx_crescimentoA)/100)
    popB+=round((popB*tx_crescimentoB)/100)
    ano=ano+1

print ("levará", ano, "anos para a População do País A ser maior do que o País B ")
print ("população País A: \n " , popA, "habitantes")
print ("população País B: \n " , popB, "habitantes")
