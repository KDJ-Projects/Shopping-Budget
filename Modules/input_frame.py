import sqlite3 as sq3
import tkinter as tk
from tkinter import messagebox

import tkmacosx as tkm


class InputFrame:
    def __init__(self) -> None:
        # frames
        self.input_fr = tk.LabelFrame(text="Ingave")  # type: ignore
        self.input_fr.grid(row=0, column=0, padx=20, pady=10)

        # labels
        self.date_lbl = tk.Label(self.input_fr, text="Datum")
        self.expenses_lbl = tk.Label(self.input_fr, text="Uitgave")
        self.store_lbl = tk.Label(self.input_fr, text="Winkel")

        # labels grid position
        self.date_lbl.grid(row=0, column=0)
        self.expenses_lbl.grid(row=1, column=0)
        self.store_lbl.grid(row=2, column=0)

        # entrys
        self.date_entry = tk.Entry(self.input_fr)
        self.expenses_entry = tk.Entry(self.input_fr)
        self.store_entry = tk.Entry(self.input_fr)

        # button
        self.add_btn = tkm.Button(
            self.input_fr,
            text="Toevoegen",
            bg="#4F4FFF",
            fg="white",
            overbackground="green",
            command=self.sql_input,
        )

        # grid position entrys
        self.date_entry.grid(row=0, column=1)
        self.expenses_entry.grid(row=1, column=1)
        self.store_entry.grid(row=2, column=1)

        # grid position button
        self.add_btn.grid(
            row=3, column=0, columnspan=3, sticky="news", padx=20, pady=10
        )

        # padding widgets
        for widget in self.input_fr.winfo_children():
            widget.grid_configure(padx=10, pady=5)

    # functions
    def sql_input(self):
        input_store = self.store_entry.get()
        try:
            if (
                self.date_entry.get() == ""
                or self.expenses_entry.get() == ""
                or self.store_entry.get() == ""
            ):
                messagebox.showinfo(
                    title="Error", message="Vul ontbrekende gegevens in!"
                )
            else:
                conn = sq3.connect("./Data/acounting.db")
                curr = conn.cursor()
                curr.execute(
                    "INSERT INTO uitgaven(Datum, Bedrag, Winkel) VALUES (?,?,?);",
                    (
                        self.date_entry.get(),
                        self.expenses_entry.get(),
                        self.store_entry.get(),
                    ),
                )
                conn.commit()
                conn.close()
                self.date_entry.delete(0, tk.END)
                self.expenses_entry.delete(0, tk.END)
                self.store_entry.delete(0, tk.END)
                messagebox.showinfo(  # type: ignore
                    title="Information",
                    message=f"Added data to database {input_store}",
                )
        except ValueError as err:
            messagebox.showinfo(title="Error", message=err)  # type: ignore


if __name__ == "__main__":
    InputFrame()
