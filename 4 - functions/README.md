# 🐍 Capítulo 04 - Funções, Escopos, Pilha de Chamada e Exceções

## 1. O que são Funções e Como Criá-las

Funções são "mini-programas" dentro do programa principal. Sua grande vantagem é **evitar a duplicação de código**.

### 🛠️ Criação vs. Chamada
* **Definição (`def`):** A palavra reservada `def` cria a função. **O código interno da função NÃO é executado ao ser definido**.
* **Chamada de Função:** É a linha que realmente executa o bloco de código previamente criado.

```python
# Criação/Definição (Não imprime nada na tela ainda)
def say_hello():
    print('Hello')

# Chamada de Função (Agora sim é executado)
say_hello()
```

### 📥 Parâmetros e Argumentos
* **Parâmetro:** É a variável nomeada na instrução def para receber dados (ex: first_name em def add_member(first_name):).
* **Argumento:** É o valor real passado durante a chamada (ex: 'Albert' em say_hello('Albert')).  ￼

Criar uma função é como escrever uma receita de bolo em um caderno. Escrever a receita não faz o bolo aparecer na mesa. O bolo só existe quando você segue a receita e cozinha (faz a chamada da função)! Os parâmetros são os ingredientes genéricos que a receita pede (ex: "uma fruta"), e os argumentos são o que você realmente usa na hora de fazer (ex: "uma maçã").

## 2. Valores de Retorno e o Valor None

Uma função pode processar dados e "devolver" um resultado para o programa principal.

### 📤 A Instrução return
Sinaliza o fim da execução da função e envia um valor de volta. Esse valor retornado pode fazer parte de expressões matemáticas ou lógicas.

```python
def enter_password(password):
    if password == 'swordfish':
        return True # Retorna um booleano
    else:
        return False
```

### 🚫 O Valor None
Representa a ausência de um valor e pertence ao tipo `NoneType`.  ￼

* Se uma função não possui a instrução `return`, o Python adiciona automaticamente `return None` ao final.  ￼
* `None` é diferente de `False`, de 0 e de uma string vazia `''`. Comparar `None == None` resulta em `True`.

Imagine que você pede para um robô ir buscar uma maçã na cozinha. Se ele voltar e te entregar a maçã, essa maçã é o valor de retorno. Se você pedir para o robô apenas dar uma pirueta, ele faz o movimento e volta de mãos vazias. As mãos vazias dele são o valor `None`!

## 3. Escopos: Variáveis Globais vs. Locais

O local onde uma variável é criada determina onde ela pode ser lida ou alterada.

* **Escopo Global:** Existe apenas UM escopo global no programa. Variáveis criadas fora de qualquer função vivem aqui e podem ser lidas por qualquer parte do código.
* **Escopo Local:** Criado sempre que uma função é chamada. Variáveis e parâmetros criados dentro da função vivem aqui e são apagados assim que a função termina.

```python
# Regras de Escopo na Prática
spam = 'dog' # Variável Global

def func():
    global spam # Força o uso da variável global
    spam = 'cat' # Altera a variável global para 'cat'

func()
print(spam) # Imprime 'cat'
```

### 🎯 Regras Rápidas de Acesso:

1. Uma variável não pode ser global e local ao mesmo tempo.
2. Se uma função tenta ler uma variável que não foi criada localmente, o Python busca no escopo global.  ￼
3. Se você atribui um valor a uma variável dentro de uma função sem usar a palavra global, o Python cria uma variável local.

O escopo global é como a praça pública da cidade: todo mundo que está na cidade pode ver o que está lá. O escopo local é como um diário secreto dentro da mochila de alguém: só aquela pessoa (a função) consegue ler o diário, e quando a pessoa vai embora, o diário desaparece!

## 4. A Pilha de Chamadas (Call Stack)

A pilha de chamadas é a estrutura de memória interna que o Python usa para saber para onde voltar após executar cada função.  ￼

* **Objeto de Quadro (Frame Object):** Criado no topo da pilha sempre que uma função é chamada. Ele guarda o número da linha de onde a chamada veio.
* **Topo da Pilha:** Representa a função que está sendo executada no exato momento.
* **Retorno:** Quando a função termina, seu quadro é removido do topo da pilha.

Evolução da Pilha com chamadas aninhadas:
1. Chamou spam()   ➔ [ spam() ]
2. spam() chamou eggs() ➔ [ eggs() | spam() ]
3. eggs() retornou ➔ [ spam() ]
4. spam() chamou bacon() ➔ [ bacon() | spam() ]

Pense em uma pilha de pratos. Cada vez que você entra em uma função nova, você coloca um prato no topo da pilha com um lembrete de onde você estava. O computador sempre trabalha no prato que está lá no topo. Quando termina, ele tira o prato de cima e olha o prato de baixo para saber onde parou!

## 5. Tratamento de Exceções (`try` e `except`)

Por padrão, quando um erro ocorre, o Python paralisa a execução e trava o programa. O bloco try/except é usado para interceptar falhas suavemente.  ￼

* **`try`:** Recebe o código que pode gerar um erro (ex: converter texto digitado para número com int()).  ￼
* **`except`:** Recebe o código que será executado somente se o erro especificado ocorrer no bloco try.

```python
# Exemplo correto e seguro contra erros
print('Digite um número:')
try:
    number = int(input()) # Linha perigosa
    print('Você digitou um número!')
except ValueError: # Captura o erro específico de tipo
    print('Você NÃO digitou um número válido.')
```

⚠️ Atenção: O código que pode quebrar PRECISA estar dentro do bloco `try`. Se a linha perigosa estiver fora, o programa vai travar antes mesmo de chegar na cláusula `except`.

O `try` é como colocar rodinhas de treinamento na sua bicicleta. Você tenta andar pelo caminho difícil. Se você se desequilibrar (ocorrer um erro), em vez de ralar o joelho no chão e parar a brincadeira (travar o programa), as rodinhas do `except` te seguram e você continua pedalando em segurança!