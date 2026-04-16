from src.services.calculation import calculation
from src.services.info import info

expressao = []  # Lista que armazena sequencialmente números e operadores formando a expressão matemática.

def menu():
    print("-=-" * 12)
    print("CALCULADORA EM PYTHON v0.1.0")
    print("-=-" * 12)

    print("\n[CALC] CALCULAR")
    print("[INF] INFO")
    print("[OFF] SAIR")

    while True:
        choice = input(">> ").upper().strip()

        if choice == "CALC":
            calculation(expressao)
        elif choice == "INF":
            info()
        elif choice == "OFF":
            break
        else:
            print("opção invalida!!")
menu()
