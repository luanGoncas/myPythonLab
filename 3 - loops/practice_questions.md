1. Quais teclas você pode pressionar se o seu programa Python ficar preso em um loop infinito?
R: Ctrl + C

2. Qual a diferença entre o `break` e  `continue`?
R: O `break`interrompe o laço de repetição, enquanto que o `continue` volta ao início do laço de repetição.

3. Qual é a diferença entre range(10), range(0, 10) e range(0, 10, 1) em um loop for?
R: O primeiro delimita números de 0 até 10 (com exceção de 10), o segundo delimita o início e o fim (com exceção de 10), e o terceiro delimita o início, o fim e a quantidade a se iterar

4. Escreva um programa simples que imprima os números de 1 a 10 usando um loop `for`. Em seguida, escreva um programa equivalente que imprima os números de 1 a 10 usando um loop `while`.

R:
for i in range(1, 11):
    print(i)

i = 0
while i != 10:
    print(i + 1)
    i = i + 1

5. Se você tivesse uma função chamada `bacon()` dentro de um módulo chamado `spam`, como você a chamaria após importar o `spam`?
R: spam.bacon()
