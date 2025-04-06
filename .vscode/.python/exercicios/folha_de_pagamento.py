import os

class FolhaPagamento:
    def __init__(self):
        self.valorHora = 0
        self.qtHora = 0
        self.totalSalario = 0
        self.descont = 0
        self.salarioBruto = 0
        self.d_inss = 0
        self.fgts = 0
        self.d_sindicato = 0
        self.t_desconto = 0

    def valor(self, mensagem):
        while True:
            dinheiro = input(mensagem)
            try:
                s_dinheiro = float(dinheiro)
                if s_dinheiro > 0:
                    return s_dinheiro
                else:
                    os.system('cls')
                    print("Valor inválido! Digite um valor maior que zero!")
            except ValueError:
                os.system('cls')
                print("Caracteres inválidos foram digitados!\n")

    def hora(self, mensagem):
        while True:
            hora = input(mensagem)
            try:
                h_hora = float(hora)
                if h_hora > 0:
                    return h_hora
                else:
                    os.system('cls')
                    print("Digite um valor maior que zero!")
            except ValueError:
                os.system('cls')
                print("Caracteres inválidos foram digitados!\n")

    def descontoIR_e_salario(self):
        self.valorHora = self.valor("Digite o valor da hora do trabalhador:\n")
        self.qtHora = self.hora("Digite quantas horas no mês foram trabalhadas:\n")
        self.salarioBruto = self.valorHora * self.qtHora

        if self.salarioBruto <= 900:
            self.descont = 0
        elif self.salarioBruto <= 1500:
            self.descont = self.salarioBruto * 0.05
        elif self.salarioBruto <= 2500:
            self.descont = self.salarioBruto * 0.1
        else:
            self.descont = self.salarioBruto * 0.2

    def descontoTotal(self):
        while True:
            self.descontoIR_e_salario()
            self.d_inss = self.salarioBruto * 0.1
            self.fgts = self.salarioBruto * 0.11
            self.d_sindicato = self.salarioBruto * 0.03
            self.t_desconto = self.descont + self.d_inss + self.d_sindicato
            sal_liquido = self.salarioBruto - self.t_desconto

            os.system('cls')
            print(f'#     Salário Bruto            : R${self.salarioBruto:.2f}')
            print(f'#     (-) IR                   : R${self.descont:.2f}')
            print(f'#     (-) INSS                 : R${self.d_inss:.2f}')
            print(f'#     FGTS                     : R${self.fgts:.2f}')
            print(f'#     (-) Sindicato (3%)       : R${self.d_sindicato:.2f}')
            print(f'#     (-) Total de descontos   : R${self.t_desconto:.2f}')
            print(f'#     Salário Líquido          : R${sal_liquido:.2f}')

            entrada = input("\nDeseja recomeçar a operação? Digite 's' para sair ou qualquer tecla para continuar.\n").lower()
            if entrada == 's':
                os.system('cls')
                print('Até logo!')
                break
            else:
                os.system('cls')

if __name__ == "__main__":
    folha = FolhaPagamento()
    folha.descontoTotal()