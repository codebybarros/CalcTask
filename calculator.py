expressao = []  # Armazenará a expressão

print("-=-" * 12)
print("CALCULADORA EM PYTHON!!")
print("-=-" * 12)

print("\nDigite '=' para finalizar o calculo.")

# Função que irá converter inteiro (int) para decimal (float) quando precisar.
def number(value): 
    try:
        num = float(value)
        if num.is_integer():
            return int(num)
        return num
    except ValueError:
        return None

# Looping para validar a primeira expressao.
while True:
    entrada1 = input("Digite um numero: ")

    if entrada1 == "=":
        print("Nada para calcular.")
        exit()

    primeiro_numero = number(entrada1)

    # Retornará erro de sintaxe para dados que não seja numero.
    if primeiro_numero is None:
        print("\nSyntaxe ERROR")
        continue

    expressao.append(primeiro_numero) # Armazena o primeiro numero na expressão.
    break


while True:
    operador = input("Escolha um operador (+, -, *, /) ou '=' para sair: ")

    if operador == '=': # Transforma o operador "=" em um break, assim encerrando o calculo.
        break

    # Valida apenas as operações basicas.
    if operador not in ["+", "-", "*", "/"]:
        print("\nOperador inválido")
        continue

    expressao.append(operador)

    entrada = input("Digite um numero: ")
    proximo_numero = number(entrada)

    if proximo_numero is None:
        print("\nSyntaxe ERROR")
        expressao.pop()
        continue

    expressao.append(proximo_numero)

# Retorna erro caso a expressão termine com um operador.
if isinstance(expressao[-1], str):
    print("\nExpressão inválida (terminou com operador).")
    exit()

# Impede que as expressões sejam printadas como lista.
conta_texto = " ".join(map(str, expressao))

# 
try:
    resultado = eval(conta_texto)

    print("\n-=-=-=-=-=-= Resultado =-=-=-=-=-=-")
    print(f"Sua conta foi: {conta_texto}")
    print(f"O resultado foi: {resultado}")

except Exception:
    print("\nErro ao calcular expressão.")


print("Beba água!") 