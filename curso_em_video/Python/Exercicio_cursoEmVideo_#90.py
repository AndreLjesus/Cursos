nome = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))
media = (nota1+nota2) / 2

sit = "aprovado" if media < 6 else "aprovado"

dicio = {
  "nome": nome, "media": media,
  "situação": sit,
}

for k,v in dicio.items():
  print("{}: {}".format(k, v))
  
