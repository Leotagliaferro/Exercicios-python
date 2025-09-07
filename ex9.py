nome = input("Nome: ")
disciplina = input("Digite o nome da disciplina: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

print("Sua media foi de ", media)

if media >= 6:
    print("Aprovado")
else: 
    print("reprovado")    