import tkinter as tk

window = tk.Tk()
window.geometry("500x600")
window.title("How Tall Are You?")

object_heights = {'hot cheetos': 1.68,
                  'fruit by foots': 36,
                  'solo cups': 4.25,
                  'eggs': 2.2,
                  'Oreos': .35,
                  'Cheezits': 1,
                  'Sunchips': 2,
                  'M&Ms': 0.4094488,
                  'iPhone 11s': 5.94,
                  '32 oz Hydroflasks': 8.7,
                  'golf balls': 1.69,
                  'basketballs': 9.4,
                  'hockey pucks': 1,
                  'baseballs': 2.875,
                  'ping pong balls': 1.6,
                  'soda cans': 4.80315,
                  'TI 84 graphing calculators': 7.9,
                  'javalinas': 24,
                  'Jack Black': 66}


def calculate():
    global object_heights
    l1 =  tk.Label(window, text='You are...', font=('Helvetica', 14, 'bold'))
    l1.grid(row=3, column=0)
    if not entryIn.get().isnumeric() and not entryFt.get().isnumeric():
        l2 = tk.Label(window, text='Dumb >:( enter numbers', font=('Helvetica', 10, 'bold'))
        l2.grid(row=4, column=0)
        return
    height = float(entryIn.get()) + float(entryFt.get())*12
    i = 4
    for thing in object_heights:
        convert_and_display(thing, object_heights, height, i)
        i += 1
    l2 =  tk.Label(window, text='tall.', font=('Helvetica', 14, 'bold'))
    l2.grid(row=i, column=0)


def convert_and_display(thing, object_heights, height, current_row):
    height_in_object = round(height/object_heights[thing], 3)
    label = tk.Label(window, text=str(height_in_object) + ' ' + thing)
    label.grid(row=current_row, column=0)


prompt = tk.Label(window, text="Please enter your height", font=('Helvetica', 14, 'bold'))
prompt.grid(row=0, column=0)
entryFt = tk.Entry(window)
entryFt.grid(row=1, column=0)
labelFt = tk.Label(window, text='ft')
labelFt.grid(row=1, column=1)
entryIn = tk.Entry(window)
entryIn.grid(row=1, column=2)
labelIn = tk.Label(window, text='in')
labelIn.grid(row=1, column=3)

buttonCalc = tk.Button(window, text='calculate', command=calculate)
buttonCalc.grid(row=2, column=1)



window.mainloop()
