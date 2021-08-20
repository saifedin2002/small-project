"""
learn tkinter
create gui app
"""

from  tkinter import *
import tkinter
from tkinter import messagebox
#create main window
age_app = tkinter.Tk()

# change app text
age_app.title("saif calcuate")

# change dimensions
age_app.geometry("400x200")

#write the text label
text_label = Label(age_app,text= "write your age :",height=2,font=("Arial",20)) 
text_label.pack()  # PLACE THE TEXT IN TO THE MAIN WINDOW
# age variable
age = StringVar( )
age.set("00")
#create the input for age
age_input = Entry(age_app, width=2,font=("Arial",30),textvariable=age)
age_input.pack()  # PLACE THE input IN TO THE MAIN WINDOW
#create the calculate button

def calc() :
    #get age in year
    age_value = age.get()
    # get time unite
    months = int(age_value) * 12
    weeks = int(months) * 4
    days = int(age_value) * 365
    line_one = f"your age in months is :  {months} "
    line_two = f"your age in weeks is  : {weeks} "
    line_three = f"your age in days is :  {days} "
    lines = [line_one,line_two,line_three]
    messagebox.showinfo("your age in all time unite", "\n".join(lines))

btn = Button(age_app, text= "result",width=20,height=2,bg="#333",fg="#fff",borderwidth=0,command=calc)
btn.pack()
#run app
age_app.mainloop()
