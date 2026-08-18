# 🐍 Depuração e Tratamento de Erros em Python

## 1. Disparo de Exceções (`raise`)

Enquanto o `try/except` serve para capturar erros, a instrução `raise` serve para **provocar/forçar um erro intencionalmente**. Isso sinaliza que algo que não deveria acontecer ocorreu no programa.

### 🛠️ Como Funciona
* **Declaração:** Usa-se `raise Exception('Mensagem de erro')`.
* **Efeito:** Interrompe a execução normal do código e transfere o fluxo para a cláusula `except` mais próxima. Se não houver `try/except`, o programa exibe o erro e para.

```python
name = input('Digite seu nome: ')
if name == '':
    # Força uma exceção se a string estiver vazia
    raise Exception('Você não digitou um nome.')
```

Pense no `raise` como o apito de um juiz de futebol ⚽. Se um jogador faz uma falta (ou entra com dados errados no programa), o juiz apita na hora e paralisa a jogada para corrigir o problema!

## 2. Asserções (`assert`)

Uma asserção é uma verificação de segurança interna feita pelo programador. Ela garante que o estado do programa esteja correto durante o desenvolvimento.

### 🎯 Características Principais
* **Erros de Programador:** Enquanto exceções tratam erros do usuário, asserções tratam erros do próprio código.
* **Falha Rápida (Fail Fast):** Descobre bugs imediatamente, reduzindo o tempo necessário para encontrar a causa de um erro.
* **Sintaxe:** `assert` [condição], 'Mensagem se for Falso'
* **Desativação:** Podem ser desativadas ao executar o Python com a flag -O na linha de comando.

```python
spam = 15
# Garante que spam é maior ou igual a 10; se for menor, lança AssertionError
assert spam >= 10, 'spam precisa ser pelo menos 10'

# Comparação ignorando maiúsculas/minúsculas
assert eggs.lower() != bacon.lower(), 'As strings não podem ser iguais!'
```

É como colocar uma fita métrica na porta de uma montanha-russa 🎢. Se você tiver menos de 1,20m, o brinquedo nem liga! O `assert` é essa trava de segurança que garante que só coisas certas entrem no brinquedo.

## 3. Registros de Log (`logging`)

O módulo `logging` registra o que está acontecendo no programa enquanto ele roda. É a forma profissional de monitorar a execução sem usar a função `print()`.

### ❌ Por que NÃO usar print() para depurar?
1. Apagar vários `print()` manualmente toma muito tempo.
2. Corre-se o risco de apagar um `print()` importante que fazia parte da interface do programa.
3. Logs podem ser desativados com uma única linha de código (`logging.disable()`) sem apagar nada do código.

### 📶 Os 5 Níveis de Log (do menor para o maior)
1. `DEBUG` (`logging.debug()`): Detalhes minuciosos (ex: valor de uma variável em um loop).
2. `INFO` (`logging.info()`): Confirmação de que as coisas estão funcionando (ex: programa iniciou).
3. `WARNING` (`logging.warning()`): Indicação de que algo inesperado aconteceu, mas o programa continua.
4. `ERROR` (`logging.error()`): Ocorreu um erro mais grave (ex: arquivo não encontrado).
5. `CRITICAL` (`logging.critical()`): Erro fatal que faz o programa travar sem recuperação.

### ⚙️ Configuração Básica e Salvar em Arquivo

```python
import logging

# Configura para exibir no terminal
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Para salvar os logs em um arquivo externo em vez da tela:
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Desativar todos os logs de nível CRITICAL e abaixo
logging.disable(logging.CRITICAL)
```

O `logging` é como a caixa-preta de um avião ✈️ ou um diário de bordo. Ele vai anotando tudo o que acontece na viagem. Se o avião passar por uma turbulência ou tiver algum problema, o piloto consegue ler o diário para entender exatamente o que aconteceu!

## 4. Depuração Passo a Passo (Debugger)

O depurador (debugger) permite pausar o programa e executá-lo linha por linha para inspecionar o valor das variáveis em tempo real.

### 📍 Ponto de Parada (Breakpoint)
É uma marcação feita em uma linha de código indicando onde o depurador deve pausar a execução automática. Quando você clica em Continue, o programa roda em velocidade normal até encontrar o próximo breakpoint.

### 🎮 Botões de Controle do Depurador

* **Step In:** Entra na função que está prestes a ser chamada para inspecionar linha por linha dentro dela.
* **Step Over:** Executa a linha atual direto. Se for uma função, ele executa a função inteira sem entrar nela.
* **Step Out:** Executa rapidamente o restante da função atual para sair dela e voltar ao nível superior de onde ela foi chamada.

É como assistir a um filme no controle remoto 🎬:

* **Breakpoint:** Colocar um alarme para o filme pausar na cena da explosão.
* **Step In:** Dar um zoom para ver detalhe por detalhe dentro da casa do filme.
* **Step Over:** Apertar o botão de passar 1 segundo para frente.
* **Continue:** Apertar o Play normal até a próxima cena importante.