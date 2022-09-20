import tkinter as tk

from Frames.input_frame import InputFrame
from Frames.output_frame import OutputFrame


class MainWindow:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Huishoud boekje")
        # self.root.geometry("+2900+400")
        self.root.eval("tk::PlaceWindow . center")

        # Frames
        InputFrame()
        OutputFrame()

        self.root.mainloop()


if __name__ == "__main__":
    MainWindow()
