i = 0
listamedia = []
media = 0
total = 0
while True:
    while i < 20:
        try:
            media = float(input("Digite a média: "))
            if media >= 0 and media <= 10: 
                listamedia.append(media)
                total += media
                i+=1
            else:
                print("Valor inválido")
        except ValueError:
            print("Valor inválido")
    else:
        print(listamedia)
        break

