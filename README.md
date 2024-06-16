# Implementação do Jogo Polícia e Ladrão em Grafos
## Feito por: Kaio Rodrigo, João Lucas, Thiago Andrade.

Esse trabalho foi realizado como atividade proposta da matéria Teoria dos Grafos em 2022.2 para aprofudar o conhecimento sobre Grafos. Como nossa atividade, escolhemos estudar sobre o jogo "Cops and Robbers" jogado num grafo finito, reflexivo e sem direção. 
Usamos o teorema 2.1 presente no arquivo "cops-and-robbers.pdf" desse repositório para categorizar um grafo como Cop-Win ou Robbers-Win utilizando propriedades como vizinhança. Utilizamos python para implementar a checagem desse teorema.

Informações detalhadas do trabalho está disponível no [artigo desenvolvido do projeto](artigos/artigo_final_trabalho_grafos.pdf).

## Introdução

 Cops and Robbers é um jogo modelado sobre um grafo conexo reflexivo
 e finito. Dois jogadores, um policial e um ladr˜ao, se movimentam de um
 vértice a vértices vizinhos em turnos alternados. O objetivo do jogo é
 alcançar um estado onde o policial ocupe o mesmo vértice do ladrão. Se isso
 acontecer, o ladrão é capturado e o grafo é dito cop−win, que condiciona a
 vitória ao jogador policial.

  Em 2007, Gena Hahn, pesquisador e professor titular da Universidade de
 Montreal, publicou o artigo Cops, Robbers and Graphs, dedicado a estudar matematicamente uma caracterização para um grafo cop−win. O objetivo desse trabalho é estudar o teorema proposto por Hahn e desenvolver um algoritmo que implemente a ideia do artigo e a tese do teorema, traduzindo o mesmo em termos computacionais. Através da implementação desse algoritmo, dada qualquer entrada de um grafo G de acordo com as especificações requisitadas, será possívl definir se G é ou não cop−win.

## Desenvolvimento e execução

 Aimplementação consiste em um código em python, cuja entrada é dada
 em um conjunto de inteiros representando os vértices e uma lista de duplas
 de inteiros representando as arestas. O algoritmo retorna o inteiro 1 caso o
 grafo G dado como entrada seja cop−win e retorna 0 caso contrário.
 
 A fim decomparação, foi ainda desenvolvido um algoritmo de simulação
 dos movimentos em um grafo G. Por forçaa bruta, o algoritmo busca movimentar o policial e o ladrão pelo grafo a fim de buscar uma posiçãoo de captura. Se isso ocorrer, o grafo é dito cop−win e o algoritmo retorna o inteiro 1. Caso contráario, como o programa sé termina com a captura do ladrão. Enquanto este fugir do policial, o programa roda indefinidamente.

## Como usar

- Formate uma entrada da seguinte forma: uma linha com os vértices representados em números separados por espaços, e outra linha com as arestas representados em dois vértices entre uma vírgula separados por espaços.
- Use um interpretador python (testado na ver. 3.10.6) para interpretar o arquivo "copWin.py" e passe a entrada.

### Exemplo:

entrada (K3):
```
0 1 2
0,0 0,1 0,2 1,1 1,2 2,2
```
Num terminal Unix
```sh
python3 copWin.py < entrada
```

## Considerações

Este repositório ainda mantém uma alternativa de força bruta (bruteForce.py) para fins de teste e comparações.
