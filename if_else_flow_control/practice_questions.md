1. Quais são os dois valores do tipo de dados booleano? Como você os escreve?
R: Verdadeiro ou Falso. True para verdadeiro, e False para falso.

2. Quais são os três operadores booleanos?
R: and, or e not.

3. Elabore as tabelas verdade de cada operador booleano (ou seja, todas as combinações possíveis de valores booleanos para o operador e seus respectivos valores).
R:
- AND

| OP 1 | OP 2 | RESULTADO |
--------------------------
| False| False|  False    |
---------------------------
| True | False|  False    |
---------------------------
| True | True |   True    |
---------------------------

- OR

| OP 1 | OP 2 | RESULTADO |
--------------------------
| False| False|  False    |
---------------------------
| True | False|   True    |
---------------------------
| True | True |   True    |
---------------------------

- NOT
| OP 1 | RESULTADO |
--------------------
| False|   True    |
--------------------
| True |    False  | 
--------------------

4. Qual é o resultado das seguintes expressões?
- (5 > 4) and (3 == 5)
False
- not (5 > 4)
False
- (5 > 4) or (3 == 5)
True
- not ((5 > 4) or (3 == 5))
False
- (True and True) and (True == False)
False
- (not False) or (not True)
True

5. Quais são os seis operadores de comparação?
R:
- > (Maior)
- < (Menor)
- == (Igual)
- <= (Menor ou igual)
- >= (Maior ou igual)
- != (Diferente)

6. Qual é a diferença entre o operador de igualdade e o operador de atribuição?
R: A quantidade de vezes que o símbolo de igual é utilizada. O operador de igualdade usa ele duas vezes, enquanto que o de atribuição apenas uma.

7. Explique o que é uma condição e onde você a utilizaria.
R: Uma expressão que sempre retorna um valor booleano. Utilizamos ela quando queremos controlar o fluxo de execução do código de forma mais específica

8. Identifique os três blocos neste código:

spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')

R:
spam = 0
if spam == 10: (BLOCO 1)
    print('eggs')
    if spam > 5: (BLOCO 2)
        print('bacon')
    else: (BLOCO 3)
        print('ham')
    print('spam')
print('spam')

9. Escreva um código que imprima "Hello" se o número 1 estiver armazenado na variável spam, imprima "Howdy" se o número 2 estiver armazenado em variável spam e imprima "Greetings!" se qualquer outro número estiver armazenado na variável spam.

R:
spam = 1
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')