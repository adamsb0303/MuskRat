import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image 


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1280x720")
        self.title('MUSKRAT')
        self.resizable(0, 0)

        # configure grid
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.create_widgets()

    def create_widgets(self):
        #logo image
        logo_file = ImageTk.PhotoImage(Image.open("img\muskrat_logo_transparent.png"))
        logo_image = ttk.Label(image=logo_file)
        logo_image.Image = logo_file
        logo_image.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        
        #app title
        title_label = ttk.Label(self, text = "MUSKRAT\nDeepfake Detection")
        title_label.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        
        #title font
        title_font = ("Oswald", 20, "bold")
        title_label.configure(font = title_font)
        
        #model output
        model1_label = ttk.Label(self, text = "Model Result: ")
        model1_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        


if __name__ == "__main__":
    app = App()
    app.mainloop()
