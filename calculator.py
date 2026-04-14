expressao = []  # Lista que armazena sequencialmente números e operadores formando a expressão matemática.

print("-=-" * 12)
print("CALCULADORA EM PYTHON!!")
print("-=-" * 12)

print("\nDigite '=' para finalizar o calculo.")

# Função responsável por converter uma entrada textual para número (int ou float).
# Estratégia:
# 1. Tenta converter para float (abrange inteiros e decimais).
# 2. Se o valor for inteiro (ex: 5.0), converte para int para evitar representação desnecessária.
# 3. Retorna None caso a conversão falhe (entrada inválida).
def number(value): 
    try:
        num = float(value)
        if num.is_integer():
            return int(num)
        return num
    except ValueError:
        return None

# Loop de validação da primeira entrada numérica da expressão.
# Garante que a expressão sempre comece com um número válido.
while True:
    entrada1 = input("Digite um numero: ")

    # Caso o usuário finalize sem inserir dados válidos.
    if entrada1 == "=":
        print("Nada para calcular.")
        exit()

    primeiro_numero = number(entrada1)

    # Validação de entrada: rejeita qualquer valor não numérico.
    if primeiro_numero is None:
        print("\nSyntaxe ERROR")
        continue

    expressao.append(primeiro_numero)  # Armazena o primeiro número validado.
    break


# Loop principal de construção da expressão matemática.
# Alterna entre operador e número até o usuário encerrar com '='.
while True:
    operador = input("Escolha um operador (+, -, *, /) ou '=' para sair: ")

    # Condição de parada: encerra a construção da expressão.
    if operador == '=':
        break

    # Validação restrita aos operadores básicos suportados.
    if operador not in ["+", "-", "*", "/"]:
        print("\nOperador inválido")
        continue

    expressao.append(operador)  # Adiciona o operador à expressão.

    entrada = input("Digite um numero: ")
    proximo_numero = number(entrada)

    # Caso o número seja inválido:
    # Remove o operador previamente inserido para manter consistência da expressão.
    if proximo_numero is None:
        print("\nSyntaxe ERROR")
        expressao.pop()
        continue

    expressao.append(proximo_numero)  # Adiciona o número validado.


# Validação estrutural:
# Garante que a expressão não termine com operador (o que geraria erro no eval).
if isinstance(expressao[-1], str):
    print("\nExpressão inválida (terminou com operador).")
    exit()

# Converte a lista de tokens (números e operadores) em uma string executável.
# Exemplo: [2, '+', 3] -> "2 + 3"
conta_texto = " ".join(map(str, expressao))

# Execução da expressão matemática.
# Uso de eval: interpreta a string como código Python.
# Observação crítica: embora funcional, eval é perigoso em contextos não controlados.
try:
    resultado = eval(conta_texto)

    print("\n-=-=-=-=-=-= Resultado =-=-=-=-=-=-")
    print(f"Sua conta foi: {conta_texto}")
    print(f"O resultado foi: {resultado}")

# Captura genérica de erros durante a avaliação da expressão.
except Exception:
    print("\nErro ao calcular expressão.")


print("Beba água!")  # Mensagem final sem impacto funcional.