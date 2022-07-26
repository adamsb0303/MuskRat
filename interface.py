import back as bck
import hashTest as ht
from tkinter import *
import matplotlib.pyplot as plt
import cv2

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
from matplotlib.ft2font import HORIZONTAL 

class predictionList:
    def __init__(self, model1='', model2='', model3='', model4='', model5='', most_common=''):
        self._model1 = model1
        self._model2 = model2
        self._model3 = model3
        self._model4 = model4
        self._model5 = model5
        self._most_common = most_common

    #setter has list in parameters
    def set_model_pred(self, prediction_list):
        self._model1 = prediction_list[0]
        self._model2 = prediction_list[1]
        self._model3 = prediction_list[2]
        self._model4 = prediction_list[3]
        self._model5 = prediction_list[4]
        self._most_common = prediction_list[5]

predObj = predictionList()

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
        
        #filepath label
        filepath_label = ttk.Label(self, text="")
        #filepath_label.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
            
        #open file prompt and take selected file
        def upload_action(event=None):
            filename = filedialog.askopenfilename()
            filepath_label.config(text = filename)
            #tells the backend the path to the input file 
            #returns a list of predictions (real/fake) in the following order 
            #[model1, model2, model3, model4, model5, most_frequent_prediction_out_of_all_5_models]
            pred_list = bck.get_list_of_predictions(filename)
            predObj.set_model_pred(pred_list)

            #Hash the file 
            #hash_val = ht.hashFunc(filename)
            #ht.writeHashToCsv(hash_val)
            ht.hashAndWriteToCSV(filename, pred_list)
        
        #file upload
        upload_file = ttk.Button(self, text='File Upload', command=upload_action)
        upload_file.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
        
        #model output
        model1_label = ttk.Label(self, text = "Model Result: "+ str(predObj._model1))
        model1_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

if __name__ == "__main__":
    app = App()
    app.mainloop()


