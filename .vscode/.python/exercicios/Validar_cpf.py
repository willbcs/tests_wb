import re 
import os

def cpf_verifica(mensagem):
    while True:
        formato_cpf = input(mensagem)
        formato_cpf = re.sub(r'[.-]', '', formato_cpf)
        if len(formato_cpf) == 11 and formato_cpf.isdigit():
            return formato_cpf
        else:
            os.system('cls')
            print("CPF em formato incorreto!\n")


def Validar_penultimo_digito(cpf):
    nove_digitos = cpf[:9]
    contadord1 = 10
    resultado = 0
    for numero in nove_digitos:
        resultado += int(numero) * contadord1
        contadord1 -= 1
    return 0 if (resultado * 10) % 11 > 9 else (resultado * 10) % 11
    
def Validar_ultimo_digito(cpf):
    nove_digitos = cpf[:10]
    contadord2 = 11
    resultado = 0
    for numero in nove_digitos:
        resultado += int(numero) * contadord2
        contadord2 -= 1
    return 0 if (resultado * 10) % 11 > 9 else (resultado * 10) % 11

def Validador():
    cpf = cpf_verifica("Digite um CPF:\n")
    penultimo_digito_calculado = Validar_penultimo_digito(cpf)
    penultimo_digito_original = int(cpf[9])
    ultimo_digito_calculado = Validar_ultimo_digito(cpf)
    ultimo_digito_original = int(cpf[10])
    
    mensagem = f'O CPF informado é VÁLIDO! ' if (penultimo_digito_calculado == penultimo_digito_original) and (ultimo_digito_calculado == ultimo_digito_original) else f'O CPF informado é INVÁLIDO! '
    os.system('cls')
    print(mensagem)
    
    
if __name__=='__main__':
    Validador()