contreprovadofalta = 0
mediaturma = 0
for x in range(1, 11, 1) :
    matricula = int(input("Insira a matricula do aluno {}: ".format(x))) #Recebe Matricula
    nota1 = float(input("Insira a Nota1 do aluno {}: ".format(x))) #Recebe Nota1
    nota2 = float(input("Insira a Nota2 do aluno {}: ".format(x))) #Recebe Nota2
    nota3 = float(input("Insira a Nota3 do aluno {}: ".format(x))) #Recebe Nota3
    totalfaltas = int(input("Insira o total de faltas do aluno {}: ".format(x))) #Recebe o total de faltas

    media = (nota1 + nota2 + nota3) / 3 #media aritmetica das 3 notas
    porcentagemfalta = (totalfaltas * 100) / 60 #A porcentagem de faltas do aluno (0 faltas = 0% de faltas, 60 faltas = 100% de faltas)
    if media >= 7 :
        print("O Aluno {} ".format(x) + "foi aprovado na media com {} ".format(media))
    elif media < 7 :
        print("O Aluno {} ".format(x) + "foi reprovado na media com {} ".format(media))

    if porcentagemfalta > 25 : #Se a porcentagem de falta for maior que 25% (ou seja presenca menor que 75%) entra no IF
        contreprovadofalta += 1 #Conta +1 aluno reprovado
    mediaturma +=  media #conta media de cada aluno e adiciona a media da turma
mediafinalturma = mediaturma / 10 #Media aritmetica da turma
print("Media final da turma: {}".format(mediafinalturma))
print("{}".format(contreprovadofalta) + " alunos foram reprovados por falta")
