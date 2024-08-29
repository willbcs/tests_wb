tentativa = input('Digite sua senha de 6 números! Tentativa número, 1 de 3:\n')
repeticoes = 1
senha_salva = '160489'

while not tentativa.isdigit() and repeticoes < 3:
    repeticoes += 1
    print("Isso não é um número")
    tentativa = input(f'Digite sua senha de 6 números! Tentativa número, {repeticoes} de 3:\n')
    
while senha_salva != tentativa and repeticoes < 3:
    repeticoes += 1
    tentativa = input(f'Senha incorreta! \nDigite sua senha de 6 números! Tentativa número, {repeticoes} de 3:\n')
        
if senha_salva == tentativa:
    print('Bem-vindo')

if repeticoes == 3:
    print("Sua conta foi bloqueada!")
