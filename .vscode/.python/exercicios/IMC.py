import os

class IMC:
    def __init__(self):
        self.peso = 0
        self.altura = 0
    
    def __str__(self):
        return f'Peso: {self.peso} kg, Altura: {self.altura} m'

    def obter_peso(self, x):
        while True:
            p = input(x)
            try:
                p_float = float(p)
                if p_float > 0:
                    return float(p)
                else:
                    print("Não existem pessoas com peso menor ou igual a 0! ")
            except ValueError:
                print("Caracteres inválidos foram digitados!\n")

    def obter_altura(self, h):
        while True:
            a = input(h)
            try:
                a_float = float(a)
                if a_float != 0:
                    return float(a)
                else:
                    print("Não existe altura = 0")
            except ValueError:
                print("\nCaracteres inválidos foram digitados!\n")

    def calculadora(self):
        massa = self.obter_peso("Digite seu peso:\n")
        medida = self.obter_altura("Digite sua altura:\n")
        
        return (massa / (medida * medida))
    
    def encerra(self, mensagem):
        while True:
            sair = input(mensagem).strip().lower()                
            while sair not in ("s", "c"):
                sair = input('\nInválido! Aperte [S]air ou [C]ontinuar!\n').strip().lower()                
            return sair == "s"
        
    def apresentar_IMC(self):
        n = self.calculadora()
        os.system('cls')
        print(f'Seu IMC é {n:.2f}')
        if n < 18.5:
            print("Você está abaixo do peso!")
        elif n >= 18.5 and n <= 24.9:
            print("Você está dentro da faixa de peso!")
        elif n > 24.9 and n < 30:
            print("Você está obeso em grau I!")
        elif n >= 30 and n < 40:
            print("Você está obeso grau II (severa)!")
        else:
            print("Você está obeso grau III (mórbido)!")
    
    def main(self):
        while True:
            self.apresentar_IMC()
            sair = self.encerra('Aperte [S]air ou [C]ontinuar!\n')
            if sair:
                break
            else:
                os.system('cls')
    
if __name__ == '__main__': 
    IMC().main()