import os
def valor(mensagem):
    while True:
        dinheiro = input(mensagem)
        try:
            s_dinheiro = float(dinheiro)
            if s_dinheiro >= 0:
                return float(dinheiro)
            else:
                os.system('cls')                
                print("Valor de salário inválido! Digite uma valor maior que zero!")
        except ValueError:
            os.system('cls')                
            print("Caracteres inválidos foram digitados!\n")

def hora(mensagem):
    while True:
        hora = input(mensagem)
        try:
            h_hora = float(hora)
            if h_hora >= 0:
                return float(h_hora)
            else:
                os.system('cls')                
                print("Digite uma valor maior que zero! ")
        except ValueError:
            os.system('cls')                
            print("Caracteres inválidos foram digitados!\n")

def descontoIR_e_salario():
    valorHora = valor("Digite o valor da hora do trabalhador:\n")
    qtHora = hora("Digite quantas horas no mês foram trabalhadas:\n")

    totalSalario = valorHora * qtHora

    if totalSalario <= 900:
        return 0, totalSalario
    
    elif totalSalario > 900 and totalSalario <= 1500:
        descont = (totalSalario * 0.05)
        return descont, totalSalario
    
    elif totalSalario > 1500 and totalSalario <= 2500:
        descont = (totalSalario * 0.1)
        return descont, totalSalario

    else:
        descont = (totalSalario * 0.2)
        return descont, totalSalario

def descontoTotal():
    while True:      
        ir_valor, salarioBruto = descontoIR_e_salario()
        d_inss = (salarioBruto*0.1)
        fgts = (salarioBruto*0.11)
        d_sindicato = (salarioBruto*0.03)
        t_desconto = ir_valor + d_inss + d_sindicato
        sal_liquido = salarioBruto - t_desconto

        os.system('cls')
        
        print(f'#     Salário Bruto            : R${salarioBruto:.2f}')
        print(f'#     (-) IR                   : R${ir_valor:.2f}')
        print(f'#     (-) INSS                 : R${d_inss:.2f}')
        print(f'#     FGTS                     : R${fgts:.2f}')
        print(f'#     (-) Sindicato (3%)       : R${d_sindicato:.2f}')
        print(f'#     (-) Total de descontos   : R${t_desconto:.2f}')
        print(f'#     Salário Líquido          : R${sal_liquido:.2f}')

        print("\nDeseja recomeçar a operação?")
        entrada = input("Digite 's' para sair ou aperte qualquer tecla para continuar.\n").lower()
        if entrada == 's':
            os.system('cls')
            print('Até logo!')
            break
        else:
            os.system('cls')


if __name__=="__main__":
    descontoTotal()




        


# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00