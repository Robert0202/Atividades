Algoritmo "Q2"
// Disciplina  :  [Linguagem e Lógica de Programação] 
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/06/2019
Var
// Seção de Declarações das variáveis 
chocolate, valorpago, troco, nota50, nota10, nota5, nota1, resto: inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Insira o valor pago")
leia(valorpago)
chocolate:= 1
troco:= valorpago - 1

nota50:= troco \ 50
resto:= troco - (nota50 * 50)

nota10:= resto \ 10
resto:= resto - (nota10 * 10)

nota5:= resto \ 5
resto:= resto - (nota5 * 5)

nota1:= resto \ 1
resto:= resto - (nota1 * 1)

escreval("Notas de 50: ", nota50)
escreval("Notas de 10: ", nota10)
escreval("Notas de 5: ", nota5)
escreval("Notas de 1: ", nota1)


Fimalgoritmo