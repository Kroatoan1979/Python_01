# 4 - Estruturas condicionais

## Estruturas condicionais

As estruturas condicionais em Python permitem que o código tome decisões baseadas em condições específicas. A estrutura condicional mais comum é o `if`, que pode ser complementada com `elif` (else if) e `else` para cobrir diferentes cenários.

#### 1. A Estrutura `if`

A estrutura `if` avalia uma condição e, se for verdadeira, executa o bloco de código correspondente.

**Sintaxe:**

```python
if condicao:
    # código executado se a condição for verdadeira
```

**Exemplo:**

```python
x = 10
if x > 5:
    print("x é maior que 5")
```

#### 2. A Estrutura `else`

A estrutura `else` define um bloco de código a ser executado caso a condição no `if` seja falsa.

**Sintaxe:**

```python
if condicao:
    # código executado se a condição for verdadeira
else:
    # código executado se a condição for falsa
```

**Exemplo:**

```python
x = 3
if x > 5:
    print("x é maior que 5")
else:
    print("x não é maior que 5")
```

#### 3. A Estrutura `elif` (else if)

A estrutura `elif` permite testar múltiplas condições. Assim que uma condição `elif` for verdadeira, o bloco de código correspondente é executado, e o restante das condições é ignorado.

**Sintaxe:**

```python
if condicao1:
    # código executado se condicao1 for verdadeira
elif condicao2:
    # código executado se condicao1 for falsa e condicao2 for verdadeira
else:
    # código executado se todas as condições anteriores forem falsas
```

**Exemplo:**

```python
x = 10
if x > 15:
    print("x é maior que 15")
elif x > 5:
    print("x é maior que 5, mas menor ou igual a 15")
else:
    print("x é menor ou igual a 5")
```

#### 4. Condicionais Aninhadas

As estruturas `if`, `elif` e `else` podem ser aninhadas para tratar cenários mais complexos.

**Exemplo:**

```python
x = 10
if x > 5:
    print("x é maior que 5")
    if x % 2 == 0:
        print("x é um número par")
else:
    print("x não é maior que 5")
```

#### 5. Operadores Condicionais e Comparação

Nas estruturas condicionais, utilizam-se frequentemente operadores de comparação e operadores lógicos para combinar condições.

**Operadores de Comparação:**

* `==`: Igual a
* `!=`: Diferente de
* `>`: Maior que
* `<`: Menor que
* `>=`: Maior ou igual a
* `<=`: Menor ou igual a

**Exemplo:**

```python
x = 10
if x == 10:
    print("x é igual a 10")
```

**Operadores Lógicos:**

* `and`: Retorna `True` se ambas as condições forem verdadeiras.
* `or`: Retorna `True` se pelo menos uma das condições for verdadeira.
* `not`: Inverte o valor lógico.

**Exemplo:**

```python
x = 10
y = 5
if x > 5 and y < 10:
    print("Ambas as condições são verdadeiras")
```

#### 6. Expressão Condicional (Operador Ternário)

Python suporta uma sintaxe compacta para expressões condicionais, também chamada de operador ternário.

**Sintaxe:**

```python
valor = resultado1 if condicao else resultado2
```

**Exemplo:**

```python
x = 10
resultado = "maior que 5" if x > 5 else "menor ou igual a 5"
print(resultado)
```

#### 7. Função `pass`

Em Python, a função `pass` é usada como um placeholder em um bloco de código condicional quando não se quer que ele faça nada.

**Exemplo:**

```python
x = 10
if x > 5:
    pass  # Não faz nada, mas evita erros de sintaxe
```

#### 8. Verificar Múltiplos Valores com `in`

A palavra-chave `in` é frequentemente usada em estruturas condicionais para verificar se um valor está presente numa sequência, como uma lista ou string.

**Exemplo:**

```python
nome = "Ana"
if nome in ["Ana", "Bruno", "Carlos"]:
    print("O nome está na lista")
```

#### Conclusão

As estruturas condicionais são uma parte essencial de qualquer linguagem de programação, e em Python não é diferente. Elas permitem que o programa tome decisões e execute diferentes blocos de código com base nas condições. Com operadores de comparação, operadores lógicos, condicionais aninhados e o operador ternário, é possível lidar com uma vasta gama de cenários lógicos.
