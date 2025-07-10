from tkinter import*
window=Tk()
window.title("Age Calculator app")
window.geometry("400x400")

fr=Frame(master=window , height=200 , width=360 , bg="#a422cc")
lbl1=Label(text="Enter your name and birth year in the specific areas" , fg="pink" , bg="#3895D3")
name_lbl=Label(text="Name" , bg="#ccc922" , fg="white" , width=12)
year_lbl=Label(text="Birth Year" , bg="#ccc922" , fg="white" , width=12)
current_year_lbl=Label(text="Current year" , bg="#ccc922" , fg="white" , width=12)
name_entry=Entry(fr)
year_entry=Entry(fr)
curryear_entry=Entry(fr)

def display():
    name=name_entry.get()
    year=year_entry.get()
    curryear=curryear_entry.get()
    age=curryear-year
    greet="Hi" + name
    age_display="Your age is" + age
    text_box1.insert(END , greet)
    text_box2.insert(END,age_display)
text_box1=Text(width=12 , bg="white" , fg="black")
text_box2=Text(width=12 , bg="white" , fg="black")
btn=Button(text="COMPLETE" , fg="red" , bg="white" , command=display)

fr.place(x=20 , y=0)
lbl1.pack()
name_lbl.place(x=20 , y=20)
name_entry.place(x=150 , y=20)
year_lbl.place(x=20 , y=80)
year_entry.place(x=150 , y=80)
current_year_lbl.place(x=20 , y=140)
curryear_entry.place(x=150 , y=130)
btn.place(x=130 , y=210)
text_box1.place(x=100 , y=250)
text_box2.place(y=250)
window.mainloop()



