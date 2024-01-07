import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR')

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

        total_invested = self.initial_amount
        total_interest = 0
        future_value = self.initial_amount

        for month in range(1, total_months + 2):
            monthly_interest = (total_invested + total_interest) * monthly_interest_rate
            total_invested += self.monthly_investment
            total_interest += monthly_interest
            future_value = total_invested + total_interest
            self.history.append(future_value)

        return locale.currency(future_value, grouping=True) 

    def plot_history(self):
        plt.style.use('_mpl-gallery')
        fig, ax = plt.subplots(figsize=(10, 6))

        total_invested = self.initial_amount
        total_interest = 0

        for i, value in enumerate(self.history, start=0):
            monthly_interest = (total_invested + total_interest) * (self.annual_interest_rate / 100 / 12)
            total_interest += monthly_interest

            if i >= 1:
                total_invested += self.monthly_investment

            total_acumulado = total_invested + total_interest
            formatted_total_acumulado = locale.currency(total_acumulado, grouping=True)

            ax.text(i, total_acumulado + 0.1, f'{formatted_total_acumulado}', ha='center', va='bottom', fontsize=8, color="white")


        ax.bar(range(len(self.history)), self.history, width=1, edgecolor="white", linewidth=0.7)

        ax.set(xlim=(-0.5, len(self.history) - 0.5), ylim=(0, max(self.history) + 1),
            xticks=np.arange(0, len(self.history)), yticks=[])

        plt.margins(x=0.1)
        plt.xlabel('Meses')
        plt.ylabel('')
        plt.title('Juros Compostos ao Longo do Tempo')

        mng = plt.get_current_fig_manager()
        mng.window.state('normal')
        plt.subplots_adjust(bottom=0.06, top=0.943)
        ax.xaxis.grid(False)
        plt.show()



    def display_table(self):
        total_invested = self.initial_amount
        total_interest = 0

        table_window = tk.Toplevel()
        table_window.title("Informativo de Juros Compostos")

        tree = ttk.Treeview(table_window)
        tree["columns"] = ("Meses", "Juros", "Total Investido", "Total Juros", "Total Acumulado")

        for i, value in enumerate(self.history, start=0):
            monthly_interest = (total_invested + total_interest) * (self.annual_interest_rate / 100 / 12)
            total_interest += monthly_interest
            if i >= 1:
              total_invested += self.monthly_investment

            total_acumulado = total_invested + total_interest
           

            formatted_monthly_interest = locale.currency(monthly_interest, grouping=True)
            formatted_total_invested = locale.currency(total_invested, grouping=True)
            formatted_total_interest = locale.currency(total_interest, grouping=True)
            formatted_total_acumulado = locale.currency(total_acumulado, grouping=True)

            tree.insert("", tk.END, values=(i, formatted_monthly_interest, formatted_total_invested, formatted_total_interest, formatted_total_acumulado))

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
