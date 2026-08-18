1. Escreva uma instrução `assert` que dispare um `AssertionError` se a variável `spam` for um número inteiro menor que 10.
- assert spam >= 10
2. Escreva uma instrução `assert` que dispare um `AssertionError` se as variáveis ​​`eggs` e `bacon` contiverem strings idênticas, mesmo que as letras maiúsculas e minúsculas sejam diferentes (ou seja, 'hello' e 'hello' são consideradas iguais, assim como 'goodbye' e 'GOODbye').
- assert eggs.lower() != bacon.lower()
3. Escreva uma instrução `assert` que sempre dispare um `AssertionError`.
- assert False
4. Quais duas linhas seu programa deve conter para poder chamar `logging.debug()`?
- import logging
- logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -%(levelname)s - %(message)s')
5. Quais duas linhas seu programa deve conter para fazer com que `logging.debug()` envie uma mensagem de log para um arquivo chamado `programLog.txt`?
- import logging
- logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
6. Quais são os cinco níveis de log?
- DEBUG, INFO, WARNING, ERROR e CRITICAL
7. Que linha de código você pode adicionar para desativar todas as mensagens de log no seu programa?
- logging.disable(logging.CRITICAL)
8. Por que usar mensagens de log é melhor do que usar `print()` para exibir a mesma mensagem?
- Pois evita o erro de remover chamadas de print() que não eram para mensagens de log, além do tempo levado para remover todas elas
9. Quais são as diferenças entre os botões Step Over, Step In e Step Out no depurador?
- Step Over executa a linha atual, mesmo que seja uma função, enquanto que o Step In entra na função que está prestes a ser chamada. O Step Out executa rapidamente o escopo da função para sair dela
10. Depois de clicar em Continue, quando o depurador irá parar?
- Até a última linha de código a ser executada quando se deparar com um breakpoint 
11. O que é um breakpoint?
- É um ponto de parada configurado previamente para que o debugger comece a executar passo a passo, para assim inspecionar o que está acontecendo no programa