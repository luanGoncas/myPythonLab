1. Por que é vantajoso ter funções em seus programas?
- Evitar duplicação de código
2. Quando o código de uma função é executado: quando a função é definida ou quando ela é chamada?
- Quando ela é chamada
3. Qual declaração cria uma função?
- A palavra reservada `def`
4. Qual é a diferença entre uma função e uma chamada de função?
- Uma função é a definição de um mini-programa dentro de um programa, enquanto que a chamada de função é a linha que vai executar aquele mini-programa previamente definido
5. Quantos escopos globais existem em um programa Python? Quantos escopos locais existem?
- Há somente um escopo global, e a quantidade de escopos locais vai depender da quantidade de funções que o código possuir
6. O que acontece com as variáveis ​​em um escopo local quando a chamada da função
retorna?
- Elas são apagadas
7. O que é um valor de retorno? Um valor de retorno pode fazer parte de uma expressão?
- É o valor retornado de uma função, especificamente pela palavra reservada `return`, e sim, ela pode fazer parte de uma expressão
8. Se uma função não possui uma instrução `return`, qual é o valor de retorno de uma chamada a essa função?
- None
9. Como você pode forçar uma variável dentro de uma função a referenciar a variável
global?
- Utilizando a palavra reservada `global`
10. Qual é o tipo de dado de `None`?
- `NoneType`
11. O que a instrução `import areallyourpetsnamederic` faz?
- Importa um módulo de nome `areallyourpetsnamederic` no seu código
12. Se você tivesse uma função chamada `bacon()` em um módulo chamado `spam`, como você a chamaria após importar o `spam`?
- spam.bacon()
13. Como você pode impedir que um programa trave (ou encerre abruptamente) ao ocorrer um erro?
- Através das cláusulas try except
14. O que vai na cláusula `try`? O que vai na cláusula `except`?
- A cláusula `try` recebe o código com o comportamento esperado, enquanto que a cláusula `except` recebe o código a ser executado em casos de erro na cláusula `try`
15. Escreva o seguinte programa em um arquivo chamado notrandomdice.py e execute-o. Por que cada chamada de função retorna o mesmo número?
import random

random_number = random.randint(1, 6)
def get_random_dice_roll():
    # Returns a random integer from 1 to 6.
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
- Retorna o mesmo número pois a variável random_number, no escopo local da função, nunca recebe nada, então ela utiliza a única variável com esse nome na pilha, que é a random_number do escopo global, que nesse código é fixa por ser executada apenas uma única vez