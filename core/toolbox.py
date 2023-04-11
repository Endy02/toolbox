import json

import customtkinter
from PIL import Image, ImageTk

from tools.logger import Logger


class Toolbox(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.logger = Logger()
        customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
        self.configuration()

    def launch(self):
        try:
            self.mainloop()
        except Exception as e:
            self.logger.error(f"An error occured with the launch function : {e}")

    def configuration(self):
        try:
            #getting screen width and height of display
            width= self.winfo_screenwidth()
            height= self.winfo_screenheight()

            #setting tkinter window size
            self.geometry("%dx%d" % (width, height))
            self.title("Fu-Labelizer")

            # configure grid layout (0x2)
            self.grid_columnconfigure(1, weight=1)
            self.grid_columnconfigure(1, weight=0)
            self.grid_rowconfigure(0, weight=1)

            self.create_frame()

        except Exception as e:
            self.logger.error(f"An error occured with the toolbox configuration : {e}")
    
    def create_frame(self):
        try:
            # create sidebar
            self.sidebar_frame = customtkinter.CTkFrame(self, corner_radius=0)
            self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
            self.sidebar_frame.grid_columnconfigure(0, weight=1)
            self.sidebar_frame.grid_rowconfigure(10, weight=1)

            
        except Exception as e:
            self.logger.error(f"An error occured with the frame creation : {e}")

    