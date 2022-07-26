import back as bck
from tkinter import *
import matplotlib.pyplot as plt
import cv2

import tkinter as tk
from tkinter import LEFT, ttk
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

        self.geometry("960x540")
        self.title('MUSKRAT')
        self.resizable(0, 0)
        self.configure(background='white')

        # configure grid
        self.rowconfigure(0)
        self.rowconfigure(1)
        self.rowconfigure(2)
        self.rowconfigure(3)
        self.rowconfigure(4)

        self.create_widgets()

    def create_widgets(self):
        #logo image
        logo_image = Image.open("img\muskrat_logo_transparent.png")
        logo_resize = logo_image.resize((240,150))
        logo_final = ImageTk.PhotoImage(logo_resize)
        logo_label = tk.Label(image=logo_final)
        logo_label.Image = logo_final
        logo_label.config(background='white')
        
        logo_label.grid(column=0, row=0, columnspan=2, sticky= tk.E, padx=(240,0), pady=40)
        
        #app title
        title_label = tk.Label(self, text = "MUSKRAT\nDeepfake Detection")
        title_label.configure(background='white')
        title_label.grid(column=2, row=0, columnspan=3, sticky=tk.W, pady = 40)
        
        #file upload section
        file_upload_master = tk.Frame(self, width=420, height=40, borderwidth=1, relief="solid", bg='white')
        file_upload_master.pack_propagate(False)
        file_upload_master.grid(column=0, row=1, columnspan=5,padx=(260,0), pady=(0,20))
            
        #open file prompt and take selected file
        def uploadAction(event=None):
            filename = filedialog.askopenfilename()
            if(filename == ''):
                return
            filepath_label.config(text = filename)
            #tells the backend the path to the input file 
            #returns a list of predictions (real/fake) in the following order 
            #[model1, model2, model3, model4, model5, most_frequent_prediction_out_of_all_5_models]
            pred_list = bck.get_list_of_predictions(filename)
            predObj.set_model_pred(pred_list)
            #print(predObj._model1)
            submit_file.grid(row=2, column=1, columnspan=2, padx=(150,0))
        
        #file upload
        upload_file = tk.Button(file_upload_master, text='Select File', command=uploadAction, borderwidth=1, relief="solid", bg='white')
        upload_file.pack(side = LEFT, padx=5)
        
        #filepath label
        filepath_label = tk.Label(file_upload_master, text="No file selected")
        filepath_label.configure(background='white')
        filepath_label.pack(side = LEFT)
        
        def submitFile(event=None):
            file_upload_master.grid_remove()
            submit_file.grid_remove()        
            
        #model outputs
        model1_label = tk.Label(self, text = "Model Result: ")
        
        #submit button
        submit_file = tk.Button(self, text="Submit", command=submitFile, borderwidth=1, relief="solid", bg='white')

        #title font
        title_font = ("Oswald", 20)
        title_label.configure(font = title_font)

if __name__ == "__main__":
    app = App()
    app.mainloop()


