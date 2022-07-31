import sqlite3 as sq3
import tkinter as tk
from datetime import date

import tkmacosx as tkm


class OutputFrame:    
    def __init__(self) -> None:
        # connecting to db en creating a cursor
        self.connect = sq3.connect("./Data/acounting.db")
        self.cursor = self.connect.cursor()

        ## GUI SECTION
        # output variabels
        self.curr_date = date.today().strftime("%d-%m-%Y")
        self.curr_delhaize_spending = self.total_delhaize()
        self.curr_match_spending = self.total_match()
        self.curr_total_spending = self.total_spending()

        # frames
        self.output_fr = tk.LabelFrame(text="Overzicht uitgaven")
        self.output_fr.grid(row=1, column=0, padx=20, pady=10, sticky="news")

        # labels
        self.current_date_lbl = tk.Label(
            self.output_fr, text=f"Huidige datum: {self.curr_date}"
        )
        self.total_shops_spending_lbl = tk.Label(
            self.output_fr, text="Testing kurt"
        )
        # self.total_delhaize_lbl = tk.Label(
        #     self.output_fr,
        #     text=f"Maand uitgave Delhaize: €{self.curr_delhaize_spending}",
        # )
        # self.total_match_lbl = tk.Label(
        #     self.output_fr, text=f"Maand uitgave Match: €{self.curr_match_spending}"
        # )
        self.total_spend_lbl = tk.Label(
            self.output_fr, text=f"Totaal maand uitgave: €{self. curr_total_spending}"
        )

        # buttons
        self.update_btn = tkm.Button(
            self.output_fr,
            text="Update",
            bg="#4F4FFF",
            fg="white",
            width=265,
            overbackground="green",
            # command=self.update_labels,
            command=self.total_per_shop,
        )

        # grid position for labels and buttons
        self.current_date_lbl.grid(row=0, column=0)
        self.total_shops_spending_lbl.grid(row=1, column=0)
        # self.total_delhaize_lbl.grid(row=1, column=0)
        # self.total_match_lbl.grid(row=2, column=0)
        self.total_spend_lbl.grid(row=3, column=0)
        self.update_btn.grid(
            row=4, column=0, columnspan=5, sticky="nsew", padx=20, pady=10
        )

        # set padding for all widgets in frame
        for widget in self.output_fr.winfo_children():
            widget.grid_configure(padx=10, pady=5, sticky="nsew")

    ## FUNCTIONS SECTION
    def total_delhaize(self):
        self.cursor.execute(
            "SELECT sum (Bedrag) FROM uitgaven WHERE (Winkel) IS 'Delhaize';"
        )
        self.connect.commit()
        self.rows = self.cursor.fetchall()
        self.row = self.rows[0]
        for self.num in self.row:
            round(self.num, 2)
        return self.num

    def total_match(self):
        self.cursor.execute(
            "SELECT sum (Bedrag) FROM uitgaven WHERE (Winkel) IS 'Match';"
        )
        self.connect.commit()
        self.rows = self.cursor.fetchall()
        self.row = self.rows[0]
        for self.num in self.row:
            round(self.num, 2)
        return self.num

    def total_per_shop(self):
        # fetching shops out of db
        shops_list = self.cursor.execute("SELECT Winkel FROM uitgaven;")

        # filter out duplicate shops
        f_shop = []
        for shop in shops_list:
            for i in shop:
                if i not in f_shop:
                    f_shop.append(i)
        for s in f_shop:
            # print(s[::1])
            print(s)

            # self.total_shops_spending_lbl.config(text=f"{f_shop.sort()}"
            # )
            self.total_shops_spending_lbl.config(text=f"{s}"
            )

        # adding filterd shops and amounts in to ther list
        for i in f_shop:
            self.cursor.execute("SELECT sum (Bedrag) FROM uitgaven WHERE (winkel) = ?", (i,))
            self.rows = self.cursor.fetchall()
            self.row = self.rows[0]
            for r in self.row:
                print(r)
            
            self.total_shops_spending_lbl.config(text=f"{f_shop}"
            )

        self.connect.commit()


    def total_spending(self):
        self.spend_1 = float(self.total_delhaize())
        self.spend_2 = float(self.total_match())
        total = self.spend_1 + self.spend_2
        return round(total, 2)

    def update_labels(self):
        self.total_delhaize_lbl.config(
            text=f"Maand uitgave Delhaize: €{self.total_delhaize()}"
        )
        self.total_match_lbl.config(text=f"Maand uitgave Match: €{self.total_match()}")
        self.total_spend_lbl.config(
            text=f"Totaal maand uitgave: €{self.total_spending()}"
        )


if __name__ == "__main__":
    OutputFrame()
