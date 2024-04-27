from tkinter import *
from tkcalendar import  *
from datetime import datetime
root = Tk()
root.title("Calender")
root.geometry("600x400")

current_day = datetime.now().day
current_month = datetime.now().month
current_year = datetime.now().year

cal = Calendar(root, year=current_year,month=current_month,day=current_day)
cal.pack(pady=60)

root.mainloop()