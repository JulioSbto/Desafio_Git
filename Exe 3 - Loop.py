import random

# Variáveis #
nome: str
idade: int
sexo: str
horas: float
horario: str
contador: int
nota: float
media: float
loop: int = 1

'''
Início do código
'''
#Definindo o horário

horas = random.uniform(0.00, 23.59)

if horas < 12:
    horario = "Bom dia"
elif 12 <= horas < 18:
    horario = "Boa tarde"
else:
    horario = "Boa noite"

#Primeiro Loop
while (loop == 1):

    print(f"{horas:.2f}: {horario} Senaizeiro!")
    
    print(f"Bem-vindo ao portal do aluno.")

    nome = input("Informe o seu nome: ")
    idade = int(input("Informe a sua idade: "))

#Sexo#
    while True:
        sexo = input("Informe seu sexo (masculino ou feminino): ").lower()
    
        if sexo in ['masculino', 'feminino']:
            break
        else:
            print("Entrada inválida. Por favor, digite 'masculino' ou 'feminino'.")


    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Sexo: {sexo.capitalize()}")

#Notas e cálculo da média

    print("Informe as suas últimas 3 notas.")

    soma_notas = 0

    for contador in range(1, 4):
        nota = float(input(f"Digite a nota {contador}: "))  
        soma_notas += nota  


    media = soma_notas / 3
    print(f"A média suas 3 notas é: {media:.2f}")

#Segundo Loop #
    while True:
        print("Deseja responder o formulário novamente?")
        print("1 - Sim")
        print("2 - Não")
        loop = int(input(""))

        if loop == 1 or loop == 2:
            break
        else:
            print("Entrada inválida. Por favor, digite '1' para sim ou '2' para não.")

#Atualizando as horas#
        if loop == 1:
            horas = random.uniform(0.00, 23.59)  
            if horas < 12:
                horario = "Bom dia"
            elif 12 <= horas < 18:
                horario = "Boa tarde"
            else:
                horario = "Boa noite"

print("Obrigado por usar a nossa plataforma! tenha um(a) {horario} ")