# 5 - Estruturas de repetição

## Estruturas de repetição

As estruturas de repetição (ou loops) em Python permitem executar um bloco de código várias vezes, o que é fundamental para automatizar tarefas repetitivas e controlar o fluxo do programa.

#### Tipos de Estruturas de Repetição

Em Python, existem dois tipos principais de loops:

* `for`: Itera sobre uma sequência (como uma lista, tuplo, string, ou intervalo).
* `while`: Continua a executar o bloco de código enquanto a condição for verdadeira.

**1. O Loop `for`**

O loop `for` é utilizado para percorrer uma sequência, como listas, tuplos, strings, dicionários, ou até intervalos de números.

**Sintaxe:**

```python
for variavel in sequencia:
    # código a ser repetido
```

**Exemplo:**

```python
nomes = ["Ana", "Bruno", "Carlos"]
for nome in nomes:
    print(f"Olá, {nome}")
```

**Usando a Função `range()`**

A função `range()` é frequentemente usada com `for` para gerar uma sequência de números.

**Exemplo:**

```python
for i in range(5):
    print(i)
# Saída: 0, 1, 2, 3, 4
```

* `range(5)` gera uma sequência de números de 0 a 4 (não inclui o valor final).
* Também podes definir o início, fim, e o passo:

**Exemplo:**

```python
for i in range(2, 10, 2):
    print(i)
# Saída: 2, 4, 6, 8
```

**2. O Loop `while`**

O loop `while` repete o bloco de código enquanto a condição for verdadeira.

**Sintaxe:**

```python
while condicao:
    # código a ser repetido
```

**Exemplo:**

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

* Este loop continua até que a variável `contador` chegue a 5, momento em que a condição `contador < 5` passa a ser falsa e o loop termina.

**3. Controlar Loops com `break`, `continue` e `else`**

**`break`**

A instrução `break` é usada para sair imediatamente do loop, independentemente da condição.

**Exemplo:**

```python
for i in range(10):
    if i == 5:
        break
    print(i)
# Saída: 0, 1, 2, 3, 4
```

**`continue`**

A instrução `continue` pula a iteração atual e passa para a próxima.

**Exemplo:**

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
# Saída: 0, 1, 2, 4
```

**`else` em Loops**

O bloco `else` em loops é executado quando o loop termina sem que o `break` seja chamado.

**Exemplo:**

```python
for i in range(5):
    print(i)
else:
    print("Loop terminou sem interrupções")
```

**Exemplo com `break`:**

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Este bloco não será executado")
# Saída: 0, 1, 2
```

#### Loops Aninhados

Em Python, também podes usar loops dentro de loops, ou seja, loops aninhados.

**Exemplo:**

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

Este loop aninhado vai imprimir todas as combinações de `i` e `j`.

#### Loops com Estruturas de Dados

**Iterar sobre Listas:**

```python
lista = [10, 20, 30]
for elemento in lista:
    print(elemento)
```

**Iterar sobre Dicionários:**

```python
dicionario = {"nome": "Ana", "idade": 25}
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")
```

**Iterar sobre Strings:**

```python
texto = "Python"
for letra in texto:
    print(letra)
```

#### Conclusão

As estruturas de repetição (`for` e `while`) são componentes essenciais para o controle de fluxo em Python, permitindo iterar sobre sequências, controlar a execução com `break` e `continue`, e até adicionar blocos `else` para uma execução mais sofisticada. Usar estas estruturas de maneira eficiente pode melhorar bastante a clareza e a performance do teu código.
