# Criando Funções
## A primeira linha de qualquer definição de função é uma declaração `def`. Se uma função puder aceitar argumentos, essa instrução `def` conterá parâmetros, que são variáveis ​​que armazenam os argumentos. Para cada um dos itens a seguir, responda "sim" se for uma instrução `def` válida em Python; responda "não" se for uma instrução `def` inválida em Python.

1. def hello:
- Não
2. define hello(name):
- Não
3. def h(name):
- Sim
4. hello(name):
- Não
5. def:
- Não
6. def hello():
- Sim
7. def hello(name):
- Sim

# Argumentos e Parâmetros
## As perguntas a seguir testam ainda mais sua capacidade de reconhecer os elementos de definições de funções.

8. Como você pode afirmar que o código a seguir define uma função em vez de chamar uma função?

def say_hello():
- Por causa da declaração def, no início dela

9. Quais são os parâmetros na seguinte declaração def?
def add_club_member(first_name, last_name):
- first name e last name

10. No código a seguir, 'Albert' é um parâmetro ou um argumento?
say_hello('Albert')
- É um argumento, já que ele é um valor de string

## O código no bloco que segue a instrução `def` é o corpo da função. Para compreender corretamente um programa, você deve ser capaz de distinguir o corpo — que é executado apenas quando a função é chamada — do código que existe fora da função. Com esse objetivo, cada um dos exemplos a seguir é um programa completo; descreva o que ele imprime.

11.

def say_hello():
    print('Hello')

- Ele não imprime nada, já que ele apenas define a função say_hello()

12.

def say_hello():
    print('Hello')
for i in range(3):
    say_hello()

- Ele imprime 'Hello' na tela três vezes

13.

def say_hello():
    for i in range(3):
        print('Hello')
say_hello()
say_hello()

- Ele imprime 'Hello' na tela seis vezes

# Valores de Retorno e Declarações Return
## De modo geral, o valor resultante de uma chamada de função é chamado de valor de retorno da função, mas você também pode especificar o valor de retorno usando uma declaração `return`, que consiste no seguinte:

- A palavra-chave `return`
- O valor ou a expressão que a função deve retornar

## Para testar se você compreende os tipos de dados retornados por funções do Python, responda às perguntas a seguir sobre declarações `return`.

14. Qual é o tipo de dado do valor de retorno na seguinte função?

def enter_password(password):
    if password == 'swordfish':
        return True
    else:
        return False

- Tipo booleano

15. Na função enter_password() anterior, qual pode ser o tipo de dado do parâmetro password?
- String
16. Qual é o tipo de dado do valor de retorno na seguinte função?
def get_greeting():
    print('Qual é o seu nome?')
    name = input()
    return 'Hello, ' + name

- String

# O Valor None
## Em Python, um valor chamado `None` representa a ausência de um valor. Nos bastidores, o Python adiciona `return None` ao final de qualquer definição de função que não contenha uma instrução `return`.

## É importante entender como `None` funciona para que você saiba o que suas funções estão retornando. Determine se as seguintes expressões envolvendo `None` resultam em `True` ou `False`. (Você pode inserir a expressão no shell interativo para descobrir.)

17. None == True
- False
18. None == False
- False
19. None == 'None'
- False
20. None == None
- True
21. None == 'hello'
- False
22. None == 0
- False
23. None == -1.5
- False

# A Pilha de Chamada
## A piha de chamadas é a forma como o Python registra para onde retornar a execução após cada chamada de função. A pilha de chamadas não fica armazenada em uma variável do seu programa; em vez disso, ela é uma seção da memória do computador que o Python gerencia automaticamente nos bastidores. Quando o programa chama uma função, o Python cria um objeto de quadro (*frame object*) no topo da pilha de chamadas. Esses objetos de quadro armazenam o número da linha da chamada de função original, permitindo que o Python saiba para onde retornar. Responda às perguntas a seguir sobre os objetos de quadro, a pilha de chamadas e as chamadas de função.

24. O que representa um objeto de quadro de pilha?
- O número da linha onde houve a chamada de função para que o Python se lembre para onde voltar
25. Quando um objeto de quadro de pilha é adicionado ao topo da pilha de chamadas?
- Quando uma nova chamada de função é realizada
26. Quando um objeto de quadro de pilha é removido do topo da pilha de chamadas?
- Quando o corre o retorno da chamada de função
27. O que representa o objeto de quadro de pilha no topo da pilha de chamadas?
- A função atualmente sendo executada
28. Uma chamada para uma função chamada spam() é feita. Em seguida, uma chamada para a função eggs() é feita. Depois, eggs() retorna. Após isso, uma chamada para a função bacon() é feita. Como fica a pilha de chamadas neste ponto?
- spam() | eggs() | spam() | bacon() |
---------| spam() | ------ |  spam() |
------------------------------------ |
29. Um programa não possui absolutamente nenhuma chamada de função. Como fica a pilha de chamadas enquanto o programa está em execução?
- Vazia

# Escopos Locais e Globais
## Apenas o código dentro de uma função chamada pode acessar os parâmetros e as variáveis ​​atribuídos nessa função. Diz-se que essas variáveis ​​existem no escopo local daquela função. Em contrapartida, o código em qualquer parte de um programa pode acessar variáveis ​​atribuídas fora de todas as funções. Diz-se que essas variáveis ​​existem no escopo global. Responda às perguntas a seguir sobre variáveis ​​globais, variáveis ​​locais e escopos.

30. Os parâmetros de função são variáveis ​​globais ou locais?
- Variáveis locais
31. Uma variável em uma função é marcada com a instrução `global`. Ela é uma variável global ou local?
- Ela é uma variável global
32. Uma variável pode ser, ao mesmo tempo, global e local?
- Não
33. Se existir uma variável global `spam` e uma função contiver uma instrução de atribuição `spam = 42` (sem uma instrução `global spam`), a variável `spam` dentro da função será local ou global?
- Local
34. Se existir uma variável global `spam` e uma função contiver uma instrução de atribuição `spam = 42` e também uma instrução `global spam`, a variável `spam` dentro da função será local ou global?
- Global
35. Se existir uma variável global `spam` e uma função nunca atribuir um valor a `spam` nem contiver uma instrução `global spam`, mas utilizar a variável `spam` (por exemplo, em `print(spam)`), a variável `spam` dentro da função será local ou global?
- Global