import customtkinter as ctk
import tkinter as tk

#Creating window and setting it up
root = ctk.CTk()
root.title("Expense Tracker")
root.geometry("1920x1080")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root.pack_propagate(False)

def home_page():
    #creating a frame for home page
    home_frame = ctk.CTkFrame(root,width = 1920, height = 1080)
    home_frame.pack()

    #Creating Labels for different section
    #Current in hand
    cih_label = ctk.CTkLabel(
        home_frame,width=300,height=142,fg_color="#ABABAB",text = "In Hand:\n {}",font= ('Khula Light',36),corner_radius=50)
    cih_label.pack_propagate(False)
    cih_label.place(x = 42, y = 55)
    
    #Profit
    profit_label = ctk.CTkLabel(
        home_frame,width=300,height=142,fg_color="#ABABAB",text = "Profit:\n {}",font= ('Khula Light',36),corner_radius=50)
    profit_label.place(x = 426, y = 55)
    
    #Inflow
    Inflow_label = ctk.CTkLabel(
        home_frame,width=300,height=142,fg_color="#00A241",text = "Inflow:\n {}",font= ('Khula Light',36),corner_radius=50)
    Inflow_label.place(x = 810, y = 55)
    
    #Outflow
    outflow_label = ctk.CTkLabel(
        home_frame,width=300,height=142,fg_color="#B00000",text = "Outflow:\n {}",font= ('Khula Light',36),corner_radius=50)
    outflow_label.place(x = 1194, y = 55)    
    
home_page()
root.mainloop()
