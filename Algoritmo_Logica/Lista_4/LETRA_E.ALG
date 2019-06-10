Algoritmo "Letra_E"
// Disciplina  :  [Linguagem e Lógica de Programação] 
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/06/2019
Var
// Seção de Declarações das variáveis 
pequenas, medias, grandes: inteiro;
valorpequenas, valormedias, valorgrandes, valorfinal: real;

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
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