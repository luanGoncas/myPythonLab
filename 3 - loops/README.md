# 🐍 Capítulo 03 - Laços de Repetição, Controle e Módulos

## 1. O Laço `while` e Avaliação Booleana (Truthy/Falsy)

O laço `while` executa um bloco de código repetidamente **enquanto** uma condição for verdadeira (`True`).

### 🔄 Estrutura do `while`
* **Validação:** A condição é checada antes de cada iteração. Se for `False` de início, o bloco é ignorado.
* **Loop Infinito:** Se a condição nunca se tornar `False`, o programa trava em loop. Para interrompê-lo via terminal, pressione **`Ctrl + C`**.

```python
# Executa 6 vezes (de 0 a 5)
i = 0
while i < 6:
    print('Hello')
    i = i + 1
```

### ☯️ Valores Verdadeiros e Falsos (Truthy e Falsy)
Em condições de controle de fluxo, outros tipos de dados são convertidos automaticamente para booleanos:  ￼

* **Valores "Falsos" (Falsy):** O número 0, o float 0.0 e a string vazia ''.
* **Valores "Verdadeiros" (Truthy):** Qualquer número diferente de zero (42, -1.0) e qualquer string não vazia ('False', 'true', 'T').

O `while` é como um guarda na porta do parque de diversões. Enquanto você disser "Sim, eu quero brincar de novo!", ele te deixa andar no carrossel. Se a sua resposta virar "Não", ele fecha o portão. Se você se esquecer de parar de gritar "Sim", o brinquedo roda para sempre até alguém puxar a tomada!

## 2. Ferramentas de Interrupção de Fluxo: break e continue

São instruções usadas exclusivamente dentro de laços para alterar a execução normal. Usá-las fora de um loop gera erro de sintaxe.

* **break:** Interrompe e sai do laço imediatamente, indo direto para o código após o loop.
* **continue:** Interrompe a iteração atual e salta imediatamente de volta para o início do laço para testar a condição novamente.

```python
# O 'break' cancela o loop na primeira iteração
i = 0
while i < 6:
    print(i) # Imprime 0
    break
    i = i + 1
```

Imagine que você está fazendo uma fila de tarefas:  ￼

* O `break` é como o alarme de incêndio: você para tudo o que está fazendo, sai da fila e vai embora.  ￼
* O `continue` é como se você percebesse que esqueceu a carteira: você abandona a tarefa atual e corre de volta para o começo da fila para recomeçar.

## 3. O Laço for e a Função range()

Enquanto o while roda com base em uma condição, o for é ideal para executar um bloco de código um número determinado de vezes.  ￼

### 🎯 A Função range()

Gera uma sequência de números para o for iterar. Aceita até 3 argumentos: range(início, fim, passo).  ￼

* **1 Argumento (range(10)):** Vai de 0 até 9 (o valor final é exclusivo).
* **2 Argumentos (range(1, 11)):** Define o início e o fim. Vai de 1 até 10.
* **3 Argumentos (range(0, 10, 2)):** Define início, fim e o passo (incremento). Gera: 0, 2, 4, 6, 8.

```python
# Somando números de 1 a 100
total = 0
for i in range(1, 101):
    total += i
print(total) # 5050
```

O `for` junto com o `range()` é como um contador de polichinelos. Se a professora diz `range(1, 11)`, você conta do 1 até o 10 e para. Se ela diz `range(0, 10, 2)`, você pula de 2 em 2 (0, 2, 4, 6, 8)! 


## 4. Módulos e a Biblioteca Padrão

O Python possui funções nativas (como `print()`, `input()`, `len()`) que não exigem nenhuma preparação. Para recursos avançados, importamos módulos da biblioteca padrão usando a instrução `import`.

### 📦 Importando e Chamando Módulos

* **Sintaxe de Importação:** Pode-se importar múltiplos módulos separados por vírgula (`import random, sys`). Não se usam aspas ao importar módulos.  ￼
* **Chamada de Função:** Após importar um módulo, suas funções devem ser chamadas com a notação `nome_do_modulo.nome_da_funcao()` (ex: `spam.bacon()`).

```python
import sys, random

# Chamando função do módulo
numero = random.randint(1, 10)

# Encerrando o programa antes do fim
sys.exit()
```

### 🛑 Encerrando com sys.exit()

Normalmente, o programa termina quando chega ao fim das linhas de código. A função `sys.exit()` faz uma chamada ao sistema operacional para encerrar o programa imediatamente em qualquer ponto. Exige a instrução `import sys` antes de ser chamada.

Os módulos são como "caixas de ferramentas extras" que você guarda no armário. A caixa do Python já vem com algumas ferramentas na mão (como a caneta `print`). Se você precisa de uma ferramenta especial, você diz `import sys` para pegar a caixa do armário e depois usa a ferramenta chamando `sys.exit()`!