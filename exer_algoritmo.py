
# 01 Faça um algoritmo que apareça "Boa tarde pessoal";
print("Boa tarde pessoal!")
print("-------------------------------------------------")

# 02 Faça um algoritmo que solicite o nome do usuário;
nome_usuario = input("Qual é o seu nome? ")
print("Meu nome é {}".format(nome_usuario))
print("-------------------------------------------------")

#03 Faça um algoritmo que solicite o nome, idade do usuário e exiba-os com uma saudação calorosa;
nome_usuario02 = input("Digite seu nome completo: ")
idade_usuario = int(input("Digite sua idade: "))
print(f"Seja bem-vindo(a) {nome_usuario02}! Muito bom ter alguém com {idade_usuario} anos estudando programação.")
print("-------------------------------------------------")

#04 Faça um algoritmo que solicite o nome, 4 notas e exiba se ele está aprovado ou reprovado e a média;
notas = []

for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media_nota = sum(notas) / len(notas)

if media_nota >= 8.0:
    print(f"{nome_usuario02} sua média é {media_nota}. Parabéns, você está aprovado(a)!")
else:
    print(f"{nome_usuario02} sua média é {media_nota}. Infelizmente você está reprovado(a), continue estudando.")
print("-------------------------------------------------")

#05 Faça um algoritmo que exiba um menu simples com 3 opções de programa de TV/Internet e exiba um comentário sobre cada um;
def exibir_menu():
    #Exibe um menu com 3 opções de programa de TV/Internet e comentários.
    print("------------------------------------")
    print("Menu de Programas:")
    print("------------------------------------")
    print("1. The Mandalorian (Disney+)")
    print("2. Cobra Kai (Netflix)")
    print("3. Rick and Morty  (HBO+)")
    print("4. Sair")
    print("------------------------------------")
    print("Digite o número da sua escolha:")

def obter_escolha():
  """Obtém a escolha do usuário no menu."""
  while True:
    try:
      escolha = int(input())
      if 1 <= escolha <= 4:
        return escolha
      else:
        print("Escolha inválida. Digite um número entre 1 e 3.")
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")

def exibir_comentario(escolha):
    #Exibe um comentário sobre o programa escolhido.
    if escolha == 1:
        print("The Mandalorian é uma série de ficção científica espacial emocionante e visualmente impressionante, ambientada cinco anos após os eventos de O Retorno de Jedi.")
    elif escolha == 2:
        print("Cobra Kai é uma sequência hilária e nostálgica de Karate Kid, que segue a rivalidade contínua entre Johnny Lawrence e Daniel LaRusso enquanto eles reabrem seus dojos de caratê.")
    elif escolha == 3:
        print("Rick and Morty é uma série que desafia as convenções tradicionais da animação adulta, oferecendo uma experiência divertida e provocativa que vai além do simples entretenimento.")
    elif escolha == 4:
        print(f"Obrigado, {nome_usuario02}. Volte sempre!")
        exit() #Sai do programa

# Execução do programa
exibir_menu()
escolha = obter_escolha()
exibir_comentario(escolha)

#06 Aproveite o algoritmo anterior e coloque uma quarta opção para que o usuário saia do programa
#elif escolha == 4:
#print(f"Volte sempre {nome_usuario02}")
#exit()  # Sai do programa

print("-------------------------------------------------")