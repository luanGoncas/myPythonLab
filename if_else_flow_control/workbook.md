# Valores Booleanos
## O tipo de dados booleano possui apenas dois valores: True ou False. Eles podem ser armazenados em variáveis ​​e usados ​​em expressões, assim como os valores de outros tipos de dados. Para cada um dos itens a seguir, responda “sim” se for um valor booleano em Python e “não” caso contrário.

1. False
- Sim
2. 'True'
- Não
3. false
- Não
4. True
- Sim
5. 'false'
- Não
6. true
- Não

# Operadores de Comparação
## Os operadores de comparação, também chamados de operadores relacionais, comparam dois valores e resultam em um valor booleano Verdadeiro ou Falso. Para cada um dos seguintes, responda "sim" se for um operador de comparação em Python e "não" caso contrário.

7. =
 - Não
8. <
- Sim
9. =>
- Sim
10. =!
- Sim
11. !=
- Sim
12. ==
- Sim
13. >
- Sim
14. <=
- Sim

## Para testar sua compreensão dos operadores de comparação em Python, responda às seguintes perguntas.
15. Qual a diferença entre os operadores < e <=?
- O primeiro significa "Menor", enquanto que o segundo significa "Menor ou Igual"
16. Qual a diferença entre os operadores = e ==?
- O primeiro é um operador de atribuição, enquanto que o segundo é um operador de comparação
17. Por que 42 == 42.0 resulta em Verdadeiro?
- Porque apesar de tipos de dados diferentes, ambos representam o mesmo valor numérico
18. Por que 42 == '42' resulta em Falso?
- Porque enquanto que o valor da esquerda é um tipo inteiro, o valor da direita é uma string
19. O que acontece se você digitar 42 < 'hello' no shell interativo?
- Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    42 < 'hello'
TypeError: '<' not supported between instances of 'int' and 'str'

# Operadores Booleanos
## Os três operadores booleanos (and, or e not) são usados ​​para comparar valores booleanos. Assim como os operadores de comparação, eles avaliam expressões para um valor booleano True ou False.

## Desenhe as tabelas verdade para os operadores booleanos nas questões 20 a 22.

20. and

21. or

22. not

## Qual é o valor das seguintes expressões?

23. 2 + 2 > 4 or True
- True
24. True and 2 + 2 ≥ 4
- True
25. True and (True or False)
- True
26. (False or True) and True
- True
27. True and not False
- True
28. not (False and True)
- True
29. not False and True
- True
30. True and True and True and True and False
- False
31. False or False or False or True or False
- True

Você pode usar operadores booleanos em uma expressão juntamente com os operadores de comparação para avaliar o valor de uma variável. Responda às seguintes perguntas.

32. Suponha que a variável `is_raining` seja definida como True ou False. Descreva o que a instrução de atribuição `is_raining = not is_raining` faz.
- Ela está invertendo o valor booleano dentro da variável is_raining, ou seja, se ela tiver o valor False, seu valor será substituído pro True, e vice versa.
33. Se a variável `name` tiver o valor 'Alice', qual expressão está correta: `name == 'Alice' or name == 'Bob'` ou `name == 'Alice' or 'Bob'`?
- As duas estão corretas.

# Componentes de Controle de Fluxo
## As instruções de controle de fluxo geralmente começam com uma parte chamada condição e são sempre seguidas por um bloco de código chamado cláusula. Uma instrução de controle de fluxo decide o que fazer com base no valor da sua condição (True ou False), e quase todas as instruções de controle de fluxo usam uma condição. O código Python pode ser agrupado em blocos, que podem ser identificados pelo seu nível de indentação.

34. Quando começa um novo bloco?
- Quando o nível de indentação aumenta
35. Um bloco pode estar dentro de outro bloco?
- Sim
36. Um novo bloco é esperado após instruções que terminam com qual caractere?
- Dois pontos
37. Quando termina um bloco?
- Quando o nível de indentação chega a zero ou quando termina a indentação do bloco pai
38. O que é a execução do programa?
- É um termo utilizado para a instrução atual sendo executada pelo programa

As questões 39 a 41 referem-se ao seguinte programa (que está identificado com números de linha):

name = 'Dolly'
if name == 'Dolly':
    print('Hello, Dolly!')
print('Done')

39. Quantos blocos há neste programa?
- Apenas um
40. Em que linha começa o primeiro bloco?
- Na linha 3
41. Em que linha termina o primeiro bloco?
- Na linha 3

# Declarações de Controle de Fluxo
## O tipo mais comum de declaração de controle de fluxo é a declaração if. A cláusula de uma instrução if (ou seja, o bloco que segue a instrução if) será executada se a condição da declaração for True e será ignorada se a condição for False. As instruções else e elif podem seguir declarações if com outras declarações.

Responda "sim" se as seguintes declarações "if" forem válidas, considerando uma variável chamada "eggs" que tem o valor 12. Responda "não" se elas não forem válidas.

42. if eggs = 12:
- Não
43. if eggs > 12
- Não
44. if:
- Não
45. if eggs == 12:
- Sim
46. if eggs != 'hello':
- Sim
47. if eggs < 12:
- Sim

Responda "sim" se as seguintes declarações else forem válidas, considerando que seguem uma declaração if eggs == 12: e seu bloco if. Responda "não" se não forem válidas.

48. else:
- Sim
49. else if eggs != 12:
- Não
50. else
- Não
51. else if not:
- Não
52. else not:
- Não

Responda "sim" se as seguintes declarações `elif` forem válidas, considerando que seguem uma declaração `if eggs == 12:` e seu bloco `if`. Responda "não" se não forem válidas.

53. elif:
- Não
54. elif eggs != 12:
- Sim
55. else if eggs != 12:
- Não
56. elif eggs == 12:
- Sim

Examine o seguinte programa com falhas:

password = 'swordfish'
if password == 'rosebud':
    print('Access granted.')
else:
    print('Access denied.')
elif password == 'swordfish':
    print('That is the old password.')

57. Por que este programa causa um erro?
- Porque uma declaração else foi utilizada antes de uma declaração elif.
58. Quantas declarações `elif` (cada uma seguida de um bloco de código `elif`) podem seguir uma declaração `if` e um bloco de código `if`?
- Não há um limite, desde que não haja uma declaração else nas declarações.

