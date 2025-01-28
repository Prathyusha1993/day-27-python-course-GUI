import tkinter

window = tkinter.Tk()
window.title('Miles to Kilometer Converter')
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

def calculate_mile_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result.config(text=f'{km}')


miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

my_label = tkinter.Label(text='Miles', font=('Arial', 24))
my_label.grid(column=2, row=0)

my_label2 = tkinter.Label(text='is equal to', font=('Arial', 24))
my_label2.grid(column=0, row=1)

km_result = tkinter.Label(text='0')
km_result.grid(column=1, row=1)

my_label3 = tkinter.Label(text='Km', font=('Arial', 24))
my_label3.grid(column=2, row=1)

button = tkinter.Button(text='Calculate', command=calculate_mile_to_km)
button.grid(column=1, row=2)



window.mainloop()