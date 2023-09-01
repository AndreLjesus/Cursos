lista_nome = []
lista_media = []
valor = 0
lista_notas = []

while True:

    nome = input("Digite um nome: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = float((nota1 + nota2) / 2)

    lista_nome.append(nome)
    lista_media.append(media)
    lista_notas.append(nota1)
    lista_notas.append(nota2)

    input_loop = str(input("Deseja parar o loop? [S/N]: "))
    if input_loop == "s" or input_loop == "S":
        break
    else:
        continue

print("\nN°   Nome      Media\n-=-=-=-=-=-=-=-=-=-=-=-=")
for c in lista_media:
    print("{}   {}      {}".format(valor, lista_nome[valor], lista_media[valor]))
    valor+=1

while True:
    aluno = int(input("Mostrar a nota de qual aluno? (999 interrompe)"))
    
    if aluno == 999:
        break
    else:
        print(lista_nome[aluno])
        print("{}   {}".format( lista_notas[aluno*2], lista_notas[(aluno*2+1)]))

    
