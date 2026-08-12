# Disparo de Exceções
## Já praticamos o tratamento de exceções em Python usando as instruções `try` e `except`, permitindo que seu programa se recupere de exceções previstas. No entanto, você também pode disparar suas próprias exceções. Disparar uma exceção é uma forma de dizer: "Pare de executar este código e transfira a execução do programa para a instrução `except`". Disparamos exceções utilizando a instrução `raise`. Responda às perguntas a seguir sobre exceções, as instruções `try` e `except` e a instrução `raise`.

1. O que acontece se você executar o seguinte programa e pressionar ENTER em vez de digitar um nome?
print('Enter your name:')
name = input()
if name == '':
    raise Exception('You did not enter a name.')
else:
    print('Hello,', name)

- O código exibirá na tela um erro especificando a exceção disparada dentro do if

2. Escreva o código que gera uma exceção com a mensagem de erro 'An error happened. This error message is vague and unhelpful.'
def vague_function(x):
    if type(x) != type(5) and type(x) != type(5.0):
        raise Exception('An error happened. This error message is vague and unhelpful.')
    else:
        print(x / 2)

try:
    vague_function(1)
    vague_function(25)
    vague_function(3.175)
    vague_function('Luan')
except Exception as err:
    print(str(err))

3. Verdadeiro ou falso: Uma instrução `raise` deve estar dentro de um bloco `try`.
- Falso. Não necessariamente. Ela pode estar em um código para disparar uma exceção, mas será disparada quando houver um bloco try a ser executado, e isso se o fluxo principal gerar um erro

4. O que acontece se você executar o seguinte programa e pressionar ENTER em vez de digitar um nome?
def get_name():
    print('Enter your name:')
    name = input()
    if name == '':
        raise Exception('You did not enter a name.')

    return name

try:
    name = get_name()
except:
    name = 'Guido'

print('Hello,', name)

- O código ira imprimir na tela a string 'Hello, Guido'

# Asserções
## Uma asserção é uma verificação de consistência que garante que seu código não esteja realizando algo obviamente errado. Criamos asserções utilizando a instrução `assert`. Se a condição em uma instrução `assert` for falsa, o Python gera a exceção `AssertionError`. As perguntas a seguir testam seu conhecimento sobre instruções `assert` e como utilizar asserções para detectar problemas.

5. “Enquanto as exceções servem para erros do usuário, as asserções servem para erros de ____.”
- Programador

6. Por que falhar rápido é algo bom?
- Porque você encurta o tempo de causa de um bug, reduzindo a quantidade de código a ser verificado quando um bug acontecer

7. Qual argumento de linha de comando para o interpretador Python suprime as verificações de asserção ao executar um programa?
- A flag -0

8. O que o `assert False` faz?
- Dispara a exceção AssertionError na tela