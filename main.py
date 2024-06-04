import customtkinter as ctk
import tkinter as tk

#Creating window and setting it up
root = ctk.CTk()
root.title("Expense Tracker")
root.geometry("1920x1080")
root._set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root.pack_propagate("False")

def home_page():
    #creating a frame for home page
    home_frame = ctk.CTkFrame(root,width = 1920, height = 1080)
    home_frame.pack()

    #Creating Labels for different section
    #Current in hand
    cih_label = ctk.CTkLabel(
        home_frame,width=390,height=142,bg_color="#ABABAB",text = "Currently In Hand:\n {}",font= ('Khula Light',44),corner_radius=5)
    cih_label.place(x = 20, y = 23)
home_page()
root.mainloop()