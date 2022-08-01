import sqlite3 as sq3
import tkinter as tk
from datetime import date

import tkmacosx as tkm

class OutputFrame:    
    def __init__(self) -> None:
        # connecting to db en creating a cursor
        self.connect = sq3.connect("./Data/acounting.db")
        self.cursor = self.connect.cursor()

        ## GUI
        # variabels
        self.curr_date = date.today().strftime("%d-%m-%Y")
        # self.curr_total_spending = self.total_spending_all_shops()

        # frames
        self.output_fr = tk.LabelFrame(text="Overzicht uitgaven")
        self.output_fr.grid(row=1, column=0, padx=20, pady=10, sticky="news")

        # labels
        self.current_date_lbl = tk.Label(
            self.output_fr, text=f"Huidige datum: {self.curr_date}"
        )
        self.total_per_shops_spending_lbl = tk.Label(
            self.output_fr, text=f""
        )

        self.total_spend_all_shops_lbl = tk.Label(
            self.output_fr, text=f"Totaal maand uitgave: €{self.total_spending_all_shops()}"
        )

        # buttons
        self.update_btn = tkm.Button(
            self.output_fr,
            text="Update",
            bg="#4F4FFF",
            fg="white",
            width=265,
            overbackground="green",
            command=self.total_spending_per_shop,
        )

        # grid position for labels and buttons
        self.current_date_lbl.grid(row=0, column=0, columnspan=5)
        self.total_per_shops_spending_lbl.grid(row=1, column=0, columnspan=5)
        self.total_spend_all_shops_lbl.grid(row=3, column=0, columnspan=5)
        self.update_btn.grid(
            row=4, column=0, columnspan=5, sticky="nsew", padx=20, pady=10
        )

        # set padding for all widgets in frame
        for widget in self.output_fr.winfo_children():
            widget.grid_configure(padx=10, pady=5, sticky="nsew")

    ## FUNCTIONS
    def total_spending_per_shop(self):
        # fetching shops out of db
        shops_list = self.cursor.execute("SELECT Winkel FROM uitgaven;")
                
        # filter out duplicate shops
        filterd_shop = []
        result_string = ""
        
        for shop in shops_list:
            for i in shop:
                if i not in filterd_shop:
                    filterd_shop.append(i)

        # finding amount for each shop
        for shop in sorted(filterd_shop):
            self.cursor.execute("SELECT sum (Bedrag) FROM uitgaven WHERE (winkel) = ?", (shop,))
            self.amounts = self.cursor.fetchall()
            
            # total amount for each shop
            for amount in self.amounts[0]:
                result_string += f"{shop}: {amount}€\n"
                
        # updating shops spending label
        self.total_per_shops_spending_lbl.config(text=f"{result_string}"
            )
        # updating total all shops speding label
        self.total_spend_all_shops_lbl.config(
                text=f"Totaal maand uitgave: €{self.total_spending_all_shops()}"
                )

    def total_spending_all_shops(self):
        self.cursor.execute("SELECT sum (Bedrag) FROM uitgaven")
        self.amount = self.cursor.fetchall()

        for amount in self.amount[0]:
            amount = round(amount, 2)
            return round(amount, 2)

if __name__ == "__main__":
    OutputFrame()
