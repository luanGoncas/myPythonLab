# Declarações de Loop While
## Você pode executar um bloco de código repetidamente usando uma instrução `while`. O código dentro da cláusula `while` será executado enquanto a condição da instrução for verdadeira. Para as perguntas a seguir, responda "sim" se o código Python for uma instrução `while` válida; responda "não" se for uma instrução `while` inválida. (Considere que as variáveis ​​receberam valores corretamente.)

1. while True:
- Sim
2. while name != 'Alice':
- Sim
3. while:
- Não
4. while counter < 10
- Não
5. while counter < 10 and counter > 5:
- Sim
6. while if counter < 10:
- Não
7. while name != 'your name':
- Sim
8. while False:
- Sim

## As instruções `break` e `continue` inseridas em um loop podem alterar o comportamento normal da repetição. Elas são frequentemente utilizadas em conjunto com instruções `if` dentro do loop. Teste sua capacidade de utilizá-las respondendo às perguntas a seguir.

9. Qual instrução faz com que a execução passe imediatamente para o final de um laço?
- break
10. Qual instrução faz com que a execução passe imediatamente para o início de um laço?
- continue
11. As instruções `break` e `continue` terminam com dois pontos?
- Não

## Para cada um dos exemplos a seguir, descreva o que o código imprime.
12.

i = 0
while i < 6:
    print('Hello')
    i = i + 1

- Imprime a string 'Hello' 6 vezes

13.

i = 9999
while i < 6:
    print('Hello')
    i = i + 1

- Nada é impresso na tela

14.

i = 0
while i < 6:
    print(i)
    i = i + 1

- Imprime os valores de 0 a 5

15.

i = 0
while i < 6:
    break
    print(i)
    i = i + 1

- Nada é impresso na tela

16.

i = 0
while i < 6:
    print(i)
    break
    i = i + 1

- Apenas o valor 0 é impresso na tela

17.

i = 0
while False:
    print(i)
    i = i + 1

- Nada é impresso na tela