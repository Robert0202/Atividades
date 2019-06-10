Algoritmo "Letra_H"
// Disciplina  :  [Linguagem e Lógica de Programação] 
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/06/2019
Var
// Seção de Declarações das variáveis 
qntfrangos: inteiro;
anelchip, anelaliment, totalgasto: real;

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Quantos frangos há na granja ?")
leia(qntfrangos)

anelchip:= qntfrangos * 4
anelaliment:= (qntfrangos * 2) * 3.5
totalgasto:= anelchip + anelaliment
escreval("Irá gastar: R$", totalgasto, " Com aneis")

Fimalgoritmo