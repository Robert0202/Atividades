Algoritmo "Letra_E"
// Disciplina  :  [Linguagem e L�gica de Programa��o] 
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/06/2019
Var
// Se��o de Declara��es das vari�veis 
pequenas, medias, grandes: inteiro;
valorpequenas, valormedias, valorgrandes, valorfinal: real;

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Informe a quantidade de camisas pequenas")
leia(pequenas)
escreval("Informe a quantidade de camisas medias")
leia(medias)
escreval("Informe a quantidade de camisas grandes")
leia(grandes)

valorpequenas:= pequenas * 18
valormedias:= medias * 22
valorgrandes:= grandes * 25

valorfinal:= valorpequenas + valormedias + valorgrandes
escreval("Valor Final: R$", valorfinal, " Reais")
Fimalgoritmo