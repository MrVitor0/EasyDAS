from CompoundInterestCalculator import CompoundInterestCalculator
from multiprocessing import Process

def display_table_and_plot(interest_calculator):
    interest_calculator.plot_history()
    interest_calculator.display_table()

def main():
    initial_amount = float(input("Enter the initial amount: "))
    monthly_investment = float(input("Enter the monthly investment: "))
    annual_interest_rate = float(input("Enter the annual interest rate: "))
    investment_period = int(input("Enter the investment period (in years): "))

    interest_calculator = CompoundInterestCalculator(initial_amount, monthly_investment, annual_interest_rate, investment_period)
    future_value = interest_calculator.calculate_compound_interest()

    print(f"\nFuture Value after {investment_period} years: ${future_value:.2f}")

    # Utiliza multiprocessing para exibir o gráfico e a tabela simultaneamente
    graph_process = Process(target=interest_calculator.plot_history)
    table_process = Process(target=interest_calculator.display_table)

    graph_process.start()
    table_process.start()

    graph_process.join()
    table_process.join()

if __name__ == "__main__":
    main()
