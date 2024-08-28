entrada = input(f'Aperte "1" para prosseguir ou outra tecla para sair: ')
if entrada == '1':
    senha_permitida = '16041989'
    senha_digitada = input('Digite a senha de 8 números: ')
    while senha_digitada != senha_permitida:
        senha_digitada = input("Senha inválida!" 
            "Digite sua senha de 8 números: ")
    print ('Seu saldo é 0 reais. Você é pobre')
    quit()
else:
    print('Até breve!')
    quit()