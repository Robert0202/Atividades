Algoritmo "Letra_G"
// Disciplina  :  [Linguagem e L�gica de Programa��o] 
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : 2 fatias de queijo(30g), 1 de presunto(30g), 1 carne(100g)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/06/2019
Var
// Se��o de Declara��es das vari�veis 
qnthamburguer: inteiro;
qntqueijo, qntpresento, qntcarne: real;

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Quantos Hamburguers deseja fazer ?")
leia(qnthamburguer)

qntqueijo:= (qnthamburguer * 2) * (30/1000)
qntpresento:= qnthamburguer * (30/1000)
qntcarne:= qnthamburguer * (100/1000)

escreval(qntqueijo, " Quilos de queijo")
escreval(qntpresento, " Quilos de presunto")
escreval(qntcarne, " Quilos de carne")
Fimalgoritmo