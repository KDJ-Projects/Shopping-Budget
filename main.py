import tkinter as tk

from Modules.input_frame import InputFrame
from Modules.output_frame import OutputFrame


class MainWindow:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Huishoud boekje")
        # self.root.geometry("300x150+1615+400")
        self.root.eval("tk::PlaceWindow . center")

        # Frames
        InputFrame()
        OutputFrame()

        self.root.mainloop()


if __name__ == "__main__":
    MainWindow()
