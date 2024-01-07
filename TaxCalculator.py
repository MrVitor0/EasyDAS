import os

class TaxCalculator:
    DECIMAL_PLACES = 2
    MONTHLY_SUBSCRIPTION = 178.00
    MONTHLY_DAS_RATE = 0.0305

    def __init__(self):
        pass

    @staticmethod
    def calculate_pro_labor(amount):
        pro_labor = round((amount * 0.28), TaxCalculator.DECIMAL_PLACES)
        pro_labor_tax = round((pro_labor * 0.11), TaxCalculator.DECIMAL_PLACES)

        return {
            'pro_labor': pro_labor,
            'pro_labor_tax': pro_labor_tax,
        }

    @staticmethod
    def calculate_monthly_das(amount):
        return round(amount * TaxCalculator.MONTHLY_DAS_RATE, TaxCalculator.DECIMAL_PLACES)

    @staticmethod
    def calculate_monthly_tax(amount):
        monthly_subscription = TaxCalculator.MONTHLY_SUBSCRIPTION

        pro_labor_tax = TaxCalculator.calculate_pro_labor(amount)['pro_labor_tax']
        monthly_das = TaxCalculator.calculate_monthly_das(amount)
        total_tax = round((monthly_das + pro_labor_tax), TaxCalculator.DECIMAL_PLACES)

        return total_tax + monthly_subscription

    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def get_float_input(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Entrada inválida. Por favor, insira um valor numérico.")

    def menu(self):
        while True:
            TaxCalculator.clear_console()
            print("\nMenu:")
            print("1. Calcular Imposto Mensal")
            print("2. Obter Pro Labore")
            print("3. Sair")
            option = input("Escolha uma opção: ")

            if option == '1':
                amount = TaxCalculator.get_float_input("Digite o valor: ")
                total_tax = TaxCalculator.calculate_monthly_tax(amount)
                print("\nTotal de impostos: ", total_tax)
            elif option == '2':
                amount = TaxCalculator.get_float_input("Digite o valor: ")
                pro_labor_result = TaxCalculator.calculate_pro_labor(amount)
                print("\nPro Labore Bruto: ", pro_labor_result['pro_labor'])
                print("O Pro Labore Líquido é:", pro_labor_result['pro_labor'] - pro_labor_result['pro_labor_tax'])
            elif option == '3':
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
            input("\nPressione Enter para continuar...")

