# Inserir código no shell interativo permite que você experimente executar instruções uma de cada vez. No prompt >>>, você pode inserir expressões compostas por valores, operadores e outros códigos Python. Após a execução do código, o shell interativo imprime o resultado. Associe os nomes das questões de 1 a 7 a estes operadores matemáticos:

+ - * / ** // %

1. Division
- [/]
2. Multiplication
- [*]
3. Subtraction
- [-]
4. Modulo
- [%]
5. Addition
- [+]
6. Exponentiation
- [**]
7. Floor division
- [//]
8. Existe alguma diferença na forma como o Python interpreta estas duas expressões? 2 + 2 e 2     + 2
- Não, não há. Espaços não fazem diferença na hora de comprar uma expressão
9. Se a expressão 26 / 8 resulta em 3,25, qual é o resultado da expressão 26 // 8?
- 3
10. 26 dividido por 8 é igual a 3 com resto 2. Qual é o resultado da expressão 26 % 8?
- 2
11. Escreva a expressão que soma os números de 1 a 10. (Dica: Começa com 1 + 2 + 3 + ... e assim por diante.)
- 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10

# Qual dos dois operadores nas expressões a seguir é avaliado primeiro de acordo com as regras de ordem de operação do Python?

12. (4 + 5) * 6
- Adição, por causa do parênteses
13. 2 ** 3 + 1
- Exponenciação tem maior precedência
14. 1 + 2 ** 3
- Exponenciação tem maior precedência
15. (1 + 2) ** 3
- Adição, por causa do parênteses
16. 2 + 4 + 6
- A ordem não importa

# Quais das seguintes expressões geram erros? (Você pode digitá-las no shell interativo para verificar.)

17. 2 +
- Erro, pois a falta de um valor depois do + gera erro de sintaxe
18. 42
- Correto
19. ((3 + 1) * 2)
- Correto
20. ((3 + 1 * 2)
- Dá erro pois o primeiro parêntese não é fechado
21. (0)
- Correto
22. 1 + 2 3
- Dá erro por falha de sintaxe

# Classifique os tipos de dados dos valores nas questões 23 a 29 como int, float ou string. Dica: você pode passá-los para a função type() no shell interativo para encontrar as respostas, como type(2) ou type('hello').

23. 2
- int
24. -2
- int
25. 2.0
- float
26. 'hello'
- string
27. 2.2
- float
28. '2'
- string
29. '2.2'
- string
30. Qual a diferença entre os valores 10, 10.0 e '10'?
- O seu tipo de dados. O primeiro é um int, o segundo um float, e o terceiro uma string

# Quando o operador + combina dois valores de string, ele os une, funcionando como o operador de concatenação de strings. Quando o operador * é usado em um valor de string e um valor inteiro, ele se torna o operador de replicação de strings. Qual é o resultado das seguintes expressões?

31. 'Hello' + 'Hello' + 'Hello'
- 'HelloHelloHello'
32. 'Hello' * 3
- 'HelloHelloHello'
33. 3 * 'Hello'
- 'HelloHelloHello'
34. (2 * 2) * 'Hello'
- 'HelloHelloHelloHello'
35. '13' + '12'
- '1312'

# Qual das seguintes expressões produz erros?

36. 'Forgot the closing quote
- Erro de sintaxe por não fechar as aspas simples da string
37. 'Hello' * 3.0
- Correta
38. 'Hello' + 3
- Erro de sintaxe por não ser possível utilizar o operador + com um valor de string e outro valor inteiro
39. Hello + Hello + Hello
- Erro por não ter definido uma variável chamada 'Hello'
40. 'Alice' * 'Bob'
- Erro por não ser possível utilizar operador * com duas strings
41. 'Hello' / 5
- Erro por não ser possível fazer divisão de strings
42. 'Hello' / 'Hello'
- Erro por não ser possível fazer divisão de strings

# Uma variável é como uma caixa na memória do computador que pode armazenar um único valor. Se você quiser usar o resultado de uma expressão avaliada posteriormente em seu programa, poderá salvá-lo em uma variável. Existem algumas regras que os nomes de variáveis ​​devem seguir, e um bom nome de variável descreve os dados que ela contém.

# Os programas a seguir armazenam valores em variáveis. Determine o que cada programa produz como saída.

43.
nephew = 'Jack'
print(nephew)
- 'Jack'
44.
nephew = 'Jack'
print('nephew')
- 'nephew'
45.
nephew = 'Jack'
nephew = 'Albert'
print(nephew)
- 'Albert'
46.
nephew = 'Jack'
Nephew = 'Albert'
print(nephew)
- 'Jack'

# Quais dos seguintes são nomes de variáveis ​​válidos?

51. number_of_cats
- Válido
52. number-of-cats
- Inválido
53. numberofcats
- Válido
54. numberOfCats
- Válido
55. _42
- Válido
56. _
- Válido
57. 42
- Inválido

# Embora o shell interativo seja útil para executar instruções Python uma de cada vez, para escrever programas Python completos, você precisará inserir as instruções no editor de arquivos. O Capítulo 1 de Automatize as Tarefas Monótonas com Python inclui um programa "Olá, mundo!" que usa comentários, as funções `print()` e `input()`, e os conceitos de valor e operador da seção anterior. Para explorar ainda mais esses blocos de construção de programas, classifique o seguinte como uma variável, uma chamada de função ou uma string.

58. 'hello'
- String
59. hello
- Variável
60. print()
- Chamada de função
61. 'print()'
- String

# As expressões a seguir causam um erro ou não? Se não causarem erro, qual é o resultado da avaliação delas?

62. int('42')
- Não causa erro
63. int('forty two')
- Erro por literal inválida para base decimal
64. int('Hello')
- Erro por literal inválida para base decimal
65. int(-42)
- Não causa erro
66. int(3.1415)
- Não causa erro
67. float(-42)
- Não causa erro
68. str(-42)
- Não causa erro
69. str(3.1415)
- Não causa erro
70. str('Hello')
 - Não causa erro
71. str(float(int(3.14)))
- Não causa erro
72. str(3)
- Não causa erro
73. str(3.0)
- Não causa erro

# Responda às seguintes perguntas para aprofundar sua compreensão das técnicas utilizadas no programa "Olá, mundo!".

74. Por que esse programa de duas linhas causa um erro?
number_of_cats = 4
print('I have ' + number_of_cats)

- Porque a string passada como argumento para a função print está concatenando uma string e uma variável contendo um valor do tipo inteiro, o que Python não permite

75. O resultado de round(4.9) é o inteiro 5 ou o float 5.0?
- É o inteiro 5

76. Descreva o que a função abs() retorna.
- A função abs() precisa receber como argumento um valor do tipo float ou inteiro para retornar o seu valor absoluto. O valor absoluto de um número nada mais é que a distância dele de zero, em outras palavras, o valor positivo dele

77. O que abs(5) retorna?
- 5

78. O que abs(-5) retorna?
- 5

# O sistema binário, também chamado de sistema numérico de base 2, pode representar todos os mesmos números que o nosso sistema numérico decimal de base 10, mais familiar. O sistema decimal tem 10 dígitos, de 0 a 9, enquanto o binário tem apenas 0 e 1. Ao representar texto, imagem, áudio e outros tipos de dados como números binários, os computadores podem armazenar e processar esses dados. Responda às seguintes perguntas sobre representação de dados.

79. Por que os computadores usam o sistema numérico binário de base 2 em vez do sistema decimal de base 10, mais familiar aos humanos?
- É mais simples de se usar o sistema binário em computadores por haver apenas dois estados. Seria caro demais utilizar um equipamento que, assim como no sistema decimal, possuiria dez estados diferentes

80. Quantos bits há em 1 byte?
- 8 bits

# Determine quantos bytes as unidades de 81 a 84 representam, tanto como um expoente, como 2¹⁰, quanto como um número inteiro, como 1.024. Você pode inserir uma expressão como 2 ** 10 no shell interativo para calcular 2¹⁰.

81. Kilobyte
- 2¹⁰, 1024 bytes
82. Megabyte
- 2²⁰, 1048576 bytes
83. Gigabyte
- 2³⁰, 1073741824 bytes
84. Terabyte
- 2⁴⁰, 1099511627776 bytes

85. O número decimal 2 é 10 em binário. Qual é o número decimal 3 em binário?
- 11
86. O número decimal 7 é 111 em binário. Qual é o número decimal 8 em binário?
- 1000

