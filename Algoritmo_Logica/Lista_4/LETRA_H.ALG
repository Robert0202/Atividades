Algoritmo "Letra_H"
// Disciplina  :  [Linguagem e L�gica de Programa��o] 
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/06/2019
Var
// Se��o de Declara��es das vari�veis 
qntfrangos: inteiro;
anelchip, anelaliment, totalgasto: real;

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Quantos frangos h� na granja ?")
leia(qntfrangos)

anelchip:= qntfrangos * 4
anelaliment:= (qntfrangos * 2) * 3.5
totalgasto:= anelchip + anelaliment
escreval("Ir� gastar: R$", totalgasto, " Com aneis")

Fimalgoritmo