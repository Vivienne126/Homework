from tkinter import*
window=Tk()
window.title("Getting started with widgets")
window.geometry("400x300")
lbl=Label(text="Lets find the product of numbers" , fg="white" , height=2, width=300)
num1=Label(text="Enter the first number" , height=2 , width=200)
num2=Label(text="Enter the second number" , height=1 , width=200)
name_entry1=Entry()
name_entry2=Entry()
def product():
    input1=name_entry1.get()
    input2=name_entry2.get()
    result=float(input1)*float(input2)
    global final_result
    final_result="The result is" +str(result)
    text_box.insert(END , final_result)
btn=Button(text="Product" , fg="blue" , height=1 , width=300 , command=product)
text_box=Text(height=3)
lbl.pack()
num1.pack()
name_entry1.pack()
num2.pack()
name_entry2.pack()
btn.pack()
text_box.pack()
window.mainloop()


