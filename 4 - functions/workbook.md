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