frase = 'O python é uma linguagem multitarefas, ' \
    'muito bem elaborada no seu desenvolvimento ' \
    'e muito intuitiva.'
i = 0
apareceu_mais = 0
letra_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i +=1
        continue
    letra_x = frase.count(letra_atual)
    
    if apareceu_mais < letra_x:
        apareceu_mais = letra_x
        letra_apareceu_mais = letra_atual
    i +=1
print(f'A letra que apareceu mais vezes foi "{letra_apareceu_mais}". '
      f'Apareceu {apareceu_mais} vezes!')