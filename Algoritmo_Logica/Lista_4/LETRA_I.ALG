Algoritmo "Letra_I"
// Disciplina  :  [Linguagem e Lógica de Programação] 
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/06/2019
Var
// Seção de Declarações das variáveis 
qntrefresco, qntagua, qntsuco: real;

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Quantos litros de refresco gostaria de fazer ?")
leia(qntrefresco)

qntagua:= qntrefresco * 0.8
qntsuco:= qntrefresco * 0.2

escreval("Você vai precisar de", qntagua, "Litros de agua")
escreval( "Você vai precisar de", qntsuco, " Litros de suco")

Fimalgoritmo