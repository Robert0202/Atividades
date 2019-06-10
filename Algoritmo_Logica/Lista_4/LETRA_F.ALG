Algoritmo "Letra_F"
// Disciplina  :  [Linguagem e Lógica de Programação] 
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/06/2019
Var
// Seção de Declarações das variáveis 
salarioinicial, salarioaumento, salariofinal: real;

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Insira o salario:")
leia(salarioinicial)

salarioaumento:= salarioinicial + (salarioinicial * (15/100))
salariofinal:= salarioaumento - (salarioaumento * (8/100))

escreval("Salario Inicial R$", salarioinicial)
escreval("Salario Com Aumento R$", salarioaumento)
escreval("Salario Final R$", salariofinal)

Fimalgoritmo