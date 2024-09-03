SOMA = 0; Qa = 0; Qb = 0
listaACC = [] 
listaMCC = []
for i in range (1, 16):
    SNum = input("Digite um número inteiro entre 1 e 200: ")
    
    while not SNum.isdigit() or int(SNum) < 1 or int(SNum) > 200:
        SNum = input("Inválido! Digite um número inteiro entre 1 e 200: ")
    
    Num = int(SNum)
    if Num > 100:
        listaACC.append(Num)
        Qa += 1
    else:
        listaMCC.append(Num) 
        Qb += 1

    SOMA += Num

MEDIA = SOMA/(Qa + Qb)
print(f"Seguem os valores maiores que 100:\n {listaACC}")
print(f"Seguem os valores menores que 100:\n {listaMCC}")
print(f"A Média dos valores digitados é {MEDIA}")
