dicio = {
  "nome": str(input("Digite seu nome: ")),
  "idade": int(input("Digite seu ano de nascimento: ")),
  "carteira_de_trabalho": int(input("Digite o numero da sua carteira de trabalho: "))
}

dicio["idade"] = 2023 - dicio["idade"]

if dicio["carteira_de_trabalho"] != 0:
  dicio2 = {
    "ano_contratação": int(input("Digite o ano de contratação: ")),
    "Salario": int(input("Digite o salario: "))
  }

  dicio3 = {
    "aposentadoria": dicio2["ano_contratação"] + 35
  }
  dicio.update(dicio2)
  dicio.update(dicio3)
  
print()
print(dicio)
print()
for k,v in dicio.items():
  print("{}: {}".format(k,v))
