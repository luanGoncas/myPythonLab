# 🐍 Capítulo 02 - Controle de Fluxo e Lógica Booleana

## 1. O Tipo de Dado Booleano

Diferente de números ou textos, o tipo booleano só aceita **dois valores possíveis**: `True` (Verdadeiro) ou `False` (Falso).

* **Case-Sensitivity:** Devem sempre começar com letra maiúscula (`True` e `False`). Escrever `true`, `false` ou `'True'` (com aspas, que vira string) causará erro ou comportamento incorreto.
* **Uso:** Podem ser atribuídos diretamente a variáveis (ex: `is_raining = True`).

Pense em um interruptor de luz no seu quarto. Ele só tem duas posições: ou está ligado (`True`), ou está desligado (`False`). Não existe meia-luz!

---

## 2. Operadores de Comparação (Relacionais)

Usados para comparar dois valores. Toda comparação resulta em um valor booleano (`True` ou `False`).

| Operador | Significado | Exemplo | Resultado |
| :---: | :--- | :---: | :---: |
| `==` | Igual a | `42 == 42.0` | `True` *(mesmo valor)* |
| `!=` | Diferente de | `42 != '42'` | `True` *(tipos diferentes)* |
| `>` | Maior que | `5 > 4` | `True` |
| `<` | Menor que | `3 < 2` | `False` |
| `>=` | Maior ou igual a | `5 >= 5` | `True` |
| `<=` | Menor ou igual a | `4 <= 2` | `False` |

### ⚠️ Cuidados e Pegadinhas de Comparação:
1. **Atribuição vs. Igualdade:** 
   * `=` serve para **guardar** um valor em uma variável (`spam = 10`).
   * `==` serve para **comparar** dois valores (`spam == 10`).
2. **Comparação de Tipos Diferentes:**
   * Um inteiro e um float com mesmo valor numérico são iguais (`42 == 42.0` é `True`).
   * Um inteiro e uma string nunca são iguais (`42 == '42'` é `False`).
   * Tentar usar os operadores `<` ou `>` entre um número e uma string lança um erro (`TypeError`).

Os operadores de comparação são como juízes de uma corrida. O juiz `<` pergunta: "O carrinho da esquerda está atrás do carrinho da direita?". Se estiver, ele grita "Verdadeiro!" (`True`).

---

## 3. Operadores Booleanos (Lógicos) e Tabelas Verdade

Servem para conectar várias comparações e avaliar uma expressão lógica mais complexa.

### 1. Operador `and` (E)
Retorna `True` **apenas se AMBAS** as condições forem verdadeiras.

| Operador 1 | Operador 2 | Resultado |
| :---: | :---: | :---: |
| `False` | `False` | `False` |
| `True` | `False` | `False` |
| `False` | `True` | `False` |
| `True` | `True` | `True` |

### 2. Operador `or` (OU)
Retorna `True` se **PELO MENOS UMA** das condições for verdadeira.

| Operador 1 | Operador 2 | Resultado |
| :---: | :---: | :---: |
| `False` | `False` | `False` |
| `True` | `False` | `True` |
| `False` | `True` | `True` |
| `True` | `True` | `True` |

### 3. Operador `not` (NÃO)
Inverte o valor booleano atual.

| Operador | Resultado |
| :---: | :---: |
| `False` | `True` |
| `True` | `False` |

* **E (`and`):** É como sua mãe dizendo: "Você só vai passear se arrumar a cama **E** escovar os dentes". Se fizer só um, você não vai!
* **OU (`or`):** É como ela dizendo: "Você pode comer uma maçã **OU** uma banana". Se comer qualquer uma das duas (ou as duas), ela fica feliz!
* **NÃO (`not`):** É o operador do "do contra". Se você diz "Sim" (`True`), ele transforma em "Não" (`False`).

---

## 4. Estrutura de Código: Condições, Indentação e Blocos

Para fazer o programa tomar decisões, agrupamos linhas de código em **blocos**.

* **Condição:** É uma expressão lógica que avalia em `True` ou `False`.
* **Identação (Recuo):** No Python, os blocos de código são definidos pelo nível de espaçamento (geralmente 4 espaços).
* **Dois Pontos (`:`):** Um novo bloco **sempre** começa após uma instrução terminada em `:`.
* **Início e Fim:** O bloco começa quando o recuo aumenta e termina quando a indentação volta ao nível anterior.

```python
# Exemplo de blocos aninhados
spam = 0
if spam == 10:          # <-- Bloco 1 começa
    print('eggs')
    if spam > 5:        # <-- Bloco 2 começa (dentro do Bloco 1)
        print('bacon')
    else:               # <-- Bloco 3 começa
        print('ham')
    print('spam')
print('spam')           # Fora de todos os blocos internos
```

Pense na indentação (espaço) como caixas dentro de caixas. Se uma linha de código está "empurrada para a direita", significa que ela mora dentro da caixinha da instrução de cima e só vai ser executada se aquela instrução mandar!

## 5. Instruções de Controle de Fluxo (if, elif, else)

Servem para guiar o caminho que o programa deve seguir com base em condições.

* **if:** Executa o bloco se a condição for True.
* **elif:** Abreviação de "else if". Testado apenas se todos os if/elif anteriores forem False. Pode haver múltiplos elif.
* **else:** Opcional. Executado como "plano de emergência" se todas as condições anteriores forem False.

🚨 Regra de Ouro da Ordem:
O else deve ser sempre o último. Tentar colocar um elif depois de um else causará erro de sintaxe.

```python
# Estrutura Correta e Válida
spam = 1

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
```

É como um mapa de escolhas em um jogo:
* **if (SE):** "SE o semáforo estiver verde, atravesse a rua."
* **elif (SENÃO, SE):** "SENÃO, SE estiver amarelo, preste atenção."
* **else (SENÃO):** "SENÃO (se estiver vermelho), pare!"
