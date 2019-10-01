contreprovadofalta = 0
mediaturma = 0
for x in range(1, 11, 1) :
    matricula = int(input("Insira a matricula do aluno {}: ".format(x)))
    nota1 = float(input("Insira a Nota1 do aluno {}: ".format(x)))
    nota2 = float(input("Insira a Nota2 do aluno {}: ".format(x)))
    nota3 = float(input("Insira a Nota3 do aluno {}: ".format(x)))
    totalfaltas = int(input("Insira o total de faltas do aluno {}: ".format(x)))

    media = (nota1 + nota2 + nota3) / 3
    porcentagemfalta = (totalfaltas * 100) / 60
    if media >= 7 :
        print("O Aluno {} ".format(x) + "foi aprovado na media com {} ".format(media))
    elif media < 7 :
        print("O Aluno {} ".format(x) + "foi reprovado na media com {} ".format(media))

    if porcentagemfalta > 25 :
        contreprovadofalta += 1
    mediaturma +=  media
mediafinalturma = mediaturma / 10
print("Media final da turma: {}".format(mediafinalturma))
print("{}".format(contreprovadofalta) + " alunos foram reprovados por falta")
