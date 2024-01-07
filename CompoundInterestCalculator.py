import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

class CompoundInterestCalculator:
    def __init__(self, initial_amount, monthly_investment, annual_interest_rate, investment_period):
        self.initial_amount = initial_amount
        self.monthly_investment = monthly_investment
        self.annual_interest_rate = annual_interest_rate
        self.investment_period = investment_period
        self.history = []

    def calculate_compound_interest(self):
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        total_months = self.investment_period * 12

        total_invested = 0
        total_interest = 0
        future_value = self.initial_amount

        for month in range(1, total_months + 2):
            monthly_interest = (total_invested + total_interest) * monthly_interest_rate
            total_invested += self.monthly_investment
            total_interest += monthly_interest
            future_value = total_invested + total_interest
            self.history.append(future_value)

        return future_value

    def plot_history(self):
        plt.style.use('_mpl-gallery')
        fig, ax = plt.subplots(figsize=(10, 6))  # Definindo um tamanho inicial

        # Adiciona labels aos pontos do gráfico
        for i, value in enumerate(self.history, start=0):
            ax.text(i, value + 0.1, f'R${value:.2f}', ha='center', va='bottom', fontsize=8)

        ax.bar(range(len(self.history)), self.history, width=1, edgecolor="white", linewidth=0.7)

        ax.set(xlim=(-0.5, len(self.history) - 0.5), ylim=(0, max(self.history) + 1),
            xticks=np.arange(0, len(self.history)), yticks=[])

        # Adiciona padding ao redor do gráfico
        plt.margins(x=0.1)
        plt.xlabel('Meses')
        plt.ylabel('')  # Label vazia para o eixo Y
        plt.title('Juros Compostos ao Longo do Tempo')

        # Define o tamanho para a janela (modo janela)
        mng = plt.get_current_fig_manager()
        mng.window.state('normal')  # Modo janela

        # Ajusta os parâmetros bottom e top
        plt.subplots_adjust(bottom=0.06, top=0.943)
        ax.xaxis.grid(False)
        plt.show()


    def display_table(self):
        total_invested = 0
        total_interest = 0

        table_window = tk.Toplevel()
        table_window.title("Informativo de Juros Compostos")

        tree = ttk.Treeview(table_window)
        tree["columns"] = ("Meses", "Juros", "Total Investido", "Total Juros", "Total Acumulado")

        for i, value in enumerate(self.history, start=0):
            monthly_interest = (total_invested + total_interest) * (self.annual_interest_rate / 100 / 12)
            total_invested += self.monthly_investment
            total_interest += monthly_interest
            total_acumulado = total_invested + total_interest

            tree.insert("", tk.END, values=(i, f'R${monthly_interest:.2f}', f'R${total_invested:.2f}', f'R${total_interest:.2f}', f'R${total_acumulado:.2f}'))

        tree.column("#0", anchor=tk.W, width=50)
        tree.column("Meses", anchor=tk.W, width=50)
        tree.column("Juros", anchor=tk.W, width=120)
        tree.column("Total Investido", anchor=tk.W, width=120)
        tree.column("Total Juros", anchor=tk.W, width=120)
        tree.column("Total Acumulado", anchor=tk.W, width=120)

        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("Meses", text="Meses", anchor=tk.W)
        tree.heading("Juros", text="Juros", anchor=tk.W)
        tree.heading("Total Investido", text="Total Investido", anchor=tk.W)
        tree.heading("Total Juros", text="Total Juros", anchor=tk.W)
        tree.heading("Total Acumulado", text="Total Acumulado", anchor=tk.W)

        tree.pack(expand=tk.YES, fill=tk.BOTH)
        table_window.resizable(False, False)
        table_window.mainloop()
