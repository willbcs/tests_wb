import os

def temp_Fahrenheit(mensagem):
    while True:
        far = input(mensagem)
        try:
            return float(far)
        except:
            os.system('cls')
            print("Caracteres inválidos foram digitados!\n")
            
def Converter():
    while True:
        temp_f = temp_Fahrenheit("Digite a temperatura em Fahrenheit:\n")
        temp_c = (5 * (temp_f - 32) /9)
        os.system('cls')
        print(f"A temperatura equivalente em Celsius é {temp_c:.2f}°\n ")

        print("Deseja continuar as conversões?")
        end = input("Digite 's' para sair ou aperte qualquer tecla para continuar!\n")
        os.system('cls')
        
        if end =='s':
            os.system('cls')
            print("Até logo!")
            break
           
if __name__== "__main__":
    Converter()