for i in range(10):
    if i == 2:
        print('Seu i vale 2...continua')
        continue
    elif i == 8:
        print('Seu i vale 8...Comente esse função' 
              'para ver o "Else" funcionar')
        break
    for j in range(1,4):
        print(i, j)
else:
    print('For foi completado')