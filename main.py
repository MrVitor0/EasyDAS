import TaxCalculator as tc
from CompoundInterestCalculator import CompoundInterestCalculator
from multiprocessing import Process

def main_menu():
    print("Menu Principal:")
    print("1. Calculadora de Impostos")
    print("2. Calculadora de Juros Compostos")
    choice = input("Escolha a funcionalidade (1 ou 2): ")

    if choice == "1":
        tax_calculator = tc.TaxCalculator()
        tax_calculator.menu()
    elif choice == "2":
        compound_interest_menu()
    else:
        print("Escolha inválida. Por favor, escolha 1 ou 2.")

def compound_interest_menu():
    initial_amount = float(input("Informe o valor inicial: "))
    monthly_investment = float(input("Informe o valor de aporte mensal: "))
    annual_interest_rate = float(input("Informe a taxa de juros anual: "))
    investment_period = int(input("Qual o período? (em anos): "))

    interest_calculator = CompoundInterestCalculator(initial_amount, monthly_investment, annual_interest_rate, investment_period)
    future_value = interest_calculator.calculate_compound_interest()

    print(f"\nApós investir por {investment_period} ano(s): ${future_value:.2f}")

    # Utiliza multiprocessing para exibir o gráfico e a tabela simultaneamente
    graph_process = Process(target=interest_calculator.plot_history)
    table_process = Process(target=interest_calculator.display_table)

    graph_process.start()
    table_process.start()

    graph_process.join()
    table_process.join()

if __name__ == "__main__":
    main_menu()
