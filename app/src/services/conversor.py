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