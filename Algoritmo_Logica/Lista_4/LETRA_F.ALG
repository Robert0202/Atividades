Algoritmo "Letra_F"
// Disciplina  :  [Linguagem e L�gica de Programa��o] 
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/06/2019
Var
// Se��o de Declara��es das vari�veis 
salarioinicial, salarioaumento, salariofinal: real;

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Insira o salario:")
leia(salarioinicial)

salarioaumento:= salarioinicial + (salarioinicial * (15/100))
salariofinal:= salarioaumento - (salarioaumento * (8/100))

escreval("Salario Inicial R$", salarioinicial)
escreval("Salario Com Aumento R$", salarioaumento)
escreval("Salario Final R$", salariofinal)

Fimalgoritmo