import os

print("=+"*20)
print('          JOGO DA ADIVINHAÇÃO')
print("=+"*20)
print('Adivinhe a palavra secreta!! Você tem 8 chutes!\n')

palavra_secreta = "paralelo"
tentativa = 0
letras_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra: ').lower()
    tentativa += 1
    
    if not letra_digitada.isalpha() or len(letra_digitada) > 1 and tentativa < 8:
        print('\nVale somente uma letra!\n')
        continue
    
    if tentativa == 8:
        print('\nGAME OVER!! Você usou suas 8 tentativas e'
              'não acertou a palavra secreta!')
        break

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
        
    palavraFormada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavraFormada += letra_secreta

        else:
            palavraFormada += '*'
    print('Palavra Secreta:', palavraFormada, '\n')

    if palavraFormada == palavra_secreta:
        os.system('cls')
        print('Você ganhou!! Parabéns!\n')
        print(f'A Palavra Secreta era {palavra_secreta}!\n')
        print(f'Você resolveu em {tentativa} tentativas!')
        tentativa = 0
        letras_acertadas = ''
        







