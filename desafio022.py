nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print("Seu nome em letras maiúsculas fica, {} ".format(nome.upper()))
print ("Seu nome em letras minúsculas fica, {} ".format(nome.lower()))
print("Seu nome tem o total de {} letras. ".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome tem {} letras. ".format(nome.find(" ")))