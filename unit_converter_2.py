from tkinter import *

# DEFINING_FUNCTIONS
# ================================================================================================================================================================================
def exit():
    Sparsh_Root.destroy()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
def ctof():

    def the_result():
        fetch_number = float(entry_1.get())
        result = (fetch_number * 1.8) + 32
        print_the_result = Label(root, text = f"Your answer is {result}°F", font = ('Bahnschrift 15'))
        print_the_result.pack()
    root = Tk()
    root.geometry("853x480")
    Title_Label = Label(root, text = "Convert °C to °F", font = ('Bahnschrift 20 bold underline'))
    Title_Label.pack()

    entry_1 = Entry(root)
    entry_1.pack()
    enter_button = Button(root, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result)
    enter_button.pack()
    root.mainloop()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ftoc():
    def the_result_2():
        fetch_number_2 = float(entry_2.get())
        result_2 = (fetch_number_2 - 32) * (5/9)
        print_the_result_2 = Label(root_2, text = f"Your answer is {result_2}°C", font = ('Bahnschrift 15'))
        print_the_result_2.pack()
    root_2 = Tk()
    root_2.geometry("853x480")
    Title_Label_2 = Label(root_2, text = "Convert °F to °C", font = ('Bahnschrift 20 bold underline'))
    Title_Label_2.pack()

    entry_2 = Entry(root_2)
    entry_2.pack()
    enter_button_2 = Button(root_2, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_2)
    enter_button_2.pack()
    root_2.mainloop()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ctok():
    def the_result_3():
        fetch_number_3 = float(entry_3.get())
        result_3 = (fetch_number_3 + 273.15)
        print_the_result_3 = Label(root_3, text = f"Your answer is {result_3}K", font = ('Bahnschrift 15'))
        print_the_result_3.pack()
    root_3 = Tk()
    root_3.geometry("853x480")
    Title_Label_3 = Label(root_3, text = "Convert °C to K", font = ('Bahnschrift 20 bold underline'))
    Title_Label_3.pack()

    entry_3 = Entry(root_3)
    entry_3.pack()
    enter_button_3 = Button(root_3, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_3)
    enter_button_3.pack()
    root_3.mainloop()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def rtod():
    def the_result_4():
        fetch_number_4 = float(entry_4.get())
        result_4 = (fetch_number_4 / 74.58)
        print_the_result_4 = Label(root_4, text = f"Your answer is {result_4}$", font = ('Bahnschrift 15'))
        print_the_result_4.pack()
    root_4 = Tk()
    root_4.geometry("853x480")
    Title_Label_4 = Label(root_4, text = "Convert ₹ to $", font = ('Bahnschrift 20 bold underline'))
    Title_Label_4.pack()

    entry_4 = Entry(root_4)
    entry_4.pack()
    enter_button_4 = Button(root_4, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_4)
    enter_button_4.pack()
    root_4.mainloop()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def dtor():
    def the_result_5():
        fetch_number_5 = float(entry_5.get())
        result_5 = (fetch_number_5 * 74.58)
        print_the_result_5 = Label(root_5, text = f"Your answer is {result_5}₹", font = ('Bahnschrift 15'))
        print_the_result_5.pack()
    root_5 = Tk()
    root_5.geometry("853x480")
    Title_Label_5 = Label(root_5, text = "Convert $ to ₹", font = ('Bahnschrift 20 bold underline'))
    Title_Label_5.pack()

    entry_5 = Entry(root_5)
    entry_5.pack()
    enter_button_5 = Button(root_5, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_5)
    enter_button_5.pack()
    root_5.mainloop()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def rtop():
    def the_result_6():
        fetch_number_6 = float(entry_6.get())
        result_6 = (fetch_number_6 / 103.44)
        print_the_result_6 = Label(root_6, text = f"Your answer is {result_6}£", font = ('Bahnschrift 15'))
        print_the_result_6.pack()
    root_6 = Tk()
    root_6.geometry("853x480")
    Title_Label_6 = Label(root_6, text = "Convert ₹ to £", font = ('Bahnschrift 20 bold underline'))
    Title_Label_6.pack()

    entry_6 = Entry(root_6)
    entry_6.pack()
    enter_button_6 = Button(root_6, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_6)
    enter_button_6.pack()
    root_6.mainloop()
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ptor():
    def the_result_7():
        fetch_number_7 = float(entry_7.get())
        result_7 = (fetch_number_7 * 103.44)
        print_the_result_7 = Label(root_7, text = f"Your answer is {result_7}£", font = ('Bahnschrift 15'))
        print_the_result_7.pack()
    root_7 = Tk()
    root_7.geometry("853x480")
    Title_Label_7 = Label(root_7, text = "Convert £ to ₹", font = ('Bahnschrift 20 bold underline'))
    Title_Label_7.pack()

    entry_7 = Entry(root_7)
    entry_7.pack()
    enter_button_7 = Button(root_7, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_7)
    enter_button_7.pack()
    root_7.mainloop()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def gtokg():
    def the_result_8():
        fetch_number_8 = float(entry_8.get())
        result_8 = (fetch_number_8 / 1000)
        print_the_result_8 = Label(root_8, text = f"Your answer is {result_8}kg", font = ('Bahnschrift 15'))
        print_the_result_8.pack()
    root_8 = Tk()
    root_8.geometry("853x480")
    Title_Label_8 = Label(root_8, text = "Convert grams to kilograms", font = ('Bahnschrift 20 bold underline'))
    Title_Label_8.pack()

    entry_8 = Entry(root_8)
    entry_8.pack()
    enter_button_8 = Button(root_8, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_8)
    enter_button_8.pack()
    root_8.mainloop()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def kgtog():
    def the_result_9():
        fetch_number_9 = float(entry_9.get())
        result_9 = (fetch_number_9 * 1000)
        print_the_result_9 = Label(root_9, text = f"Your answer is {result_9}g", font = ('Bahnschrift 15'))
        print_the_result_9.pack()
    root_9 = Tk()
    root_9.geometry("853x480")
    Title_Label_9 = Label(root_9, text = "Convert kilograms to grams", font = ('Bahnschrift 20 bold underline'))
    Title_Label_9.pack()

    entry_9 = Entry(root_9)
    entry_9.pack()
    enter_button_9 = Button(root_9, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_9)
    enter_button_9.pack()
    root_9.mainloop()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ptokg():
    def the_result_11():
        fetch_number_11 = float(entry_11.get())
        result_11 = (fetch_number_11 / 2.2)
        print_the_result_11 = Label(root_11, text = f"Your answer is {result_11}KG", font = ('Bahnschrift 15'))
        print_the_result_11.pack()
    root_11 = Tk()
    root_11.geometry("853x480")
    Title_Label_11 = Label(root_11, text = "Convert Pounds to Kilograms", font = ('Bahnschrift 20 bold underline'))
    Title_Label_11.pack()

    entry_11 = Entry(root_11)
    entry_11.pack()
    enter_button_11 = Button(root_11, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_11)
    enter_button_11.pack()
    root_11.mainloop()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def cmtom():
    def the_result_12():
        fetch_number_12 = float(entry_12.get())
        result_12 = (fetch_number_12 / 100)
        print_the_result_12 = Label(root_12, text = f"Your answer is {result_12}m", font = ('Bahnschrift 15'))
        print_the_result_12.pack()
    root_12 = Tk()
    root_12.geometry("853x480")
    Title_Label_12 = Label(root_12, text = "Convert Centimetres to Metres", font = ('Bahnschrift 20 bold underline'))
    Title_Label_12.pack()

    entry_12 = Entry(root_12)
    entry_12.pack()
    enter_button_12 = Button(root_12, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_12)
    enter_button_12.pack()
    root_12.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def mtocm():
    def the_result_13():
        fetch_number_13 = float(entry_13.get())
        result_13 = (fetch_number_13 * 100)
        print_the_result_13 = Label(root_13, text = f"Your answer is {result_13}cm", font = ('Bahnschrift 15'))
        print_the_result_13.pack()
    root_13 = Tk()
    root_13.geometry("853x480")
    Title_Label_13 = Label(root_13, text = "Convert Metres to Centimetres", font = ('Bahnschrift 20 bold underline'))
    Title_Label_13.pack()

    entry_13 = Entry(root_13)
    entry_13.pack()
    enter_button_13 = Button(root_13, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_13)
    enter_button_13.pack()
    root_13.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def mtof():
    def the_result_14():
        fetch_number_14 = float(entry_14.get())
        result_14 = (fetch_number_14 * 3.28084)
        print_the_result_14 = Label(root_14, text = f"Your answer is {result_14}ft", font = ('Bahnschrift 15'))
        print_the_result_14.pack()
    root_14 = Tk()
    root_14.geometry("853x480")
    Title_Label_14 = Label(root_14, text = "Convert Metres to Foot (Feet)", font = ('Bahnschrift 20 bold underline'))
    Title_Label_14.pack()

    entry_14 = Entry(root_14)
    entry_14.pack()
    enter_button_14 = Button(root_14, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_14)
    enter_button_14.pack()
    root_14.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ftom():
    def the_result_15():
        fetch_number_15 = float(entry_15.get())
        result_15 = (fetch_number_15 / 3.28084)
        print_the_result_15 = Label(root_15, text = f"Your answer is {result_15}m", font = ('Bahnschrift 15'))
        print_the_result_15.pack()
    root_15 = Tk()
    root_15.geometry("853x480")
    Title_Label_15 = Label(root_15, text = "Convert Feet to Metre", font = ('Bahnschrift 20 bold underline'))
    Title_Label_15.pack()

    entry_15 = Entry(root_15)
    entry_15.pack()
    enter_button_15 = Button(root_15, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_15)
    enter_button_15.pack()
    root_15.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def mtoy():
    def the_result_16():
        fetch_number_16 = float(entry_16.get())
        result_16 = (fetch_number_16 * 1.09361)
        print_the_result_16 = Label(root_16, text = f"Your answer is {result_16}yd", font = ('Bahnschrift 15'))
        print_the_result_16.pack()
    root_16 = Tk()
    root_16.geometry("853x480")
    Title_Label_16 = Label(root_16, text = "Convert Metre to Yards", font = ('Bahnschrift 20 bold underline'))
    Title_Label_16.pack()

    entry_16 = Entry(root_16)
    entry_16.pack()
    enter_button_16 = Button(root_16, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_16)
    enter_button_16.pack()
    root_16.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ytom():
    def the_result_17():
        fetch_number_17 = float(entry_17.get())
        result_17 = (fetch_number_17 / 1.09361)
        print_the_result_17 = Label(root_17, text = f"Your answer is {result_17}m", font = ('Bahnschrift 15'))
        print_the_result_17.pack()
    root_17 = Tk()
    root_17.geometry("853x480")
    Title_Label_17 = Label(root_17, text = "Convert Yards to Metres", font = ('Bahnschrift 20 bold underline'))
    Title_Label_17.pack()

    entry_17 = Entry(root_17)
    entry_17.pack()
    enter_button_17 = Button(root_17, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_17)
    enter_button_17.pack()
    root_17.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def kmphtomph():
    def the_result_18():
        fetch_number_18 = float(entry_18.get())
        result_18 = (fetch_number_18 / 1.6)
        print_the_result_18 = Label(root_18, text = f"Your answer is {result_18} Miles/Hr", font = ('Bahnschrift 15'))
        print_the_result_18.pack()
    root_18 = Tk()
    root_18.geometry("853x480")
    Title_Label_18 = Label(root_18, text = "Convert Kilometre/Hr to Miles/Hr", font = ('Bahnschrift 20 bold underline'))
    Title_Label_18.pack()

    entry_18 = Entry(root_18)
    entry_18.pack()
    enter_button_18 = Button(root_18, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_18)
    enter_button_18.pack()
    root_18.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def mphtokmph():
    def the_result_19():
        fetch_number_19 = float(entry_19.get())
        result_19 = (fetch_number_19 * 1.60934)
        print_the_result_19 = Label(root_19, text = f"Your answer is {result_19} Kilometre/Hr", font = ('Bahnschrift 15'))
        print_the_result_19.pack()
    root_19 = Tk()
    root_19.geometry("853x480")
    Title_Label_19 = Label(root_19, text = "Convert Miles/Hr to Kilometre/Hr", font = ('Bahnschrift 20 bold underline'))
    Title_Label_19.pack()

    entry_19 = Entry(root_19)
    entry_19.pack()
    enter_button_19 = Button(root_19, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_19)
    enter_button_19.pack()
    root_19.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def kmphtoms():
    def the_result_20():
        fetch_number_20 = float(entry_20.get())
        result_20 = (fetch_number_20 * (5/18))
        print_the_result_20 = Label(root_20, text = f"Your answer is {result_20} m/s", font = ('Bahnschrift 15'))
        print_the_result_20.pack()
    root_20 = Tk()
    root_20.geometry("853x480")
    Title_Label_20 = Label(root_20, text = "Convert Kilometre/Hr to M/s", font = ('Bahnschrift 20 bold underline'))
    Title_Label_20.pack()

    entry_20 = Entry(root_20)
    entry_20.pack()
    enter_button_20 = Button(root_20, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_20)
    enter_button_20.pack()
    root_20.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def mstokmph():
    def the_result_21():
        fetch_number_21 = float(entry_21.get())
        result_21 = (fetch_number_21 * (18/5))
        print_the_result_21 = Label(root_21, text = f"Your answer is {result_21} Kilometre/Hr", font = ('Bahnschrift 15'))
        print_the_result_21.pack()
    root_21 = Tk()
    root_21.geometry("853x480")
    Title_Label_21 = Label(root_21, text = "Convert M/s to Kilometre/Hr", font = ('Bahnschrift 20 bold underline'))
    Title_Label_21.pack()

    entry_21 = Entry(root_21)
    entry_21.pack()
    enter_button_21 = Button(root_21, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_21)
    enter_button_21.pack()
    root_21.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def stom():
    def the_result_22():
        fetch_number_22 = float(entry_22.get())
        result_22 = (fetch_number_22 / 60)
        print_the_result_22 = Label(root_22, text = f"Your answer is {result_22} minutes", font = ('Bahnschrift 15'))
        print_the_result_22.pack()
    root_22 = Tk()
    root_22.geometry("853x480")
    Title_Label_22 = Label(root_22, text = "Convert Seconds to Minutes", font = ('Bahnschrift 20 bold underline'))
    Title_Label_22.pack()

    entry_22 = Entry(root_22)
    entry_22.pack()
    enter_button_22 = Button(root_22, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_22)
    enter_button_22.pack()
    root_22.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def mtos():
    def the_result_23():
        fetch_number_23 = float(entry_23.get())
        result_23 = (fetch_number_23 * 60)
        print_the_result_23 = Label(root_23, text = f"Your answer is {result_23} seconds", font = ('Bahnschrift 15'))
        print_the_result_23.pack()
    root_23 = Tk()
    root_23.geometry("853x480")
    Title_Label_23 = Label(root_23, text = "Convert Minutes to Seconds", font = ('Bahnschrift 20 bold underline'))
    Title_Label_23.pack()

    entry_23 = Entry(root_23)
    entry_23.pack()
    enter_button_23 = Button(root_23, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_23)
    enter_button_23.pack()
    root_23.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def stohr():
    def the_result_24():
        fetch_number_24 = float(entry_24.get())
        result_24 = (fetch_number_24 / 3600)
        print_the_result_24 = Label(root_24, text = f"Your answer is {result_24} Hr(s)", font = ('Bahnschrift 15'))
        print_the_result_24.pack()
    root_24 = Tk()
    root_24.geometry("853x480")
    Title_Label_24 = Label(root_24, text = "Convert Seconds to Hours", font = ('Bahnschrift 20 bold underline'))
    Title_Label_24.pack()

    entry_24 = Entry(root_24)
    entry_24.pack()
    enter_button_24 = Button(root_24, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_24)
    enter_button_24.pack()
    root_24.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def hrtos():
    def the_result_25():
        fetch_number_25 = float(entry_25.get())
        result_25 = (fetch_number_25 * 3600)
        print_the_result_25 = Label(root_25, text = f"Your answer is {result_25} second(s)", font = ('Bahnschrift 15'))
        print_the_result_25.pack()
    root_25 = Tk()
    root_25.geometry("853x480")
    Title_Label_25 = Label(root_25, text = "Convert Hours to Seconds", font = ('Bahnschrift 20 bold underline'))
    Title_Label_25.pack()

    entry_25 = Entry(root_25)
    entry_25.pack()
    enter_button_25 = Button(root_25, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_25)
    enter_button_25.pack()
    root_25.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def dtohr():
    def the_result_26():
        fetch_number_26 = float(entry_26.get())
        result_26 = (fetch_number_26 * 24)
        print_the_result_26 = Label(root_26, text = f"Your answer is {result_26} Hr(s)", font = ('Bahnschrift 15'))
        print_the_result_26.pack()
    root_26 = Tk()
    root_26.geometry("853x480")
    Title_Label_26 = Label(root_26, text = "Convert Days to Hours", font = ('Bahnschrift 20 bold underline'))
    Title_Label_26.pack()

    entry_26 = Entry(root_26)
    entry_26.pack()
    enter_button_26 = Button(root_26, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_26)
    enter_button_26.pack()
    root_26.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def hrtod():
    def the_result_27():
        fetch_number_27 = float(entry_27.get())
        result_27 = (fetch_number_27 / 24)
        print_the_result_27 = Label(root_27, text = f"Your answer is {result_27} day(s)", font = ('Bahnschrift 15'))
        print_the_result_27.pack()
    root_27 = Tk()
    root_27.geometry("853x480")
    Title_Label_27 = Label(root_27, text = "Convert Hours to Days", font = ('Bahnschrift 20 bold underline'))
    Title_Label_27.pack()

    entry_27 = Entry(root_27)
    entry_27.pack()
    enter_button_27 = Button(root_27, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_27)
    enter_button_27.pack()
    root_27.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def stod():
    def the_result_28():
        fetch_number_28 = float(entry_28.get())
        result_28 = (fetch_number_28 / 86400)
        print_the_result_28 = Label(root_28, text = f"Your answer is {result_28} day(s)", font = ('Bahnschrift 15'))
        print_the_result_28.pack()
    root_28 = Tk()
    root_28.geometry("853x480")
    Title_Label_28 = Label(root_28, text = "Convert Seconds to Days", font = ('Bahnschrift 20 bold underline'))
    Title_Label_28.pack()

    entry_28 = Entry(root_28)
    entry_28.pack()
    enter_button_28 = Button(root_28, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_28)
    enter_button_28.pack()
    root_28.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def dtos():
    def the_result_29():
        fetch_number_29 = float(entry_29.get())
        result_29 = (fetch_number_29 * 86400)
        print_the_result_29 = Label(root_29, text = f"Your answer is {result_29} second(s)", font = ('Bahnschrift 15'))
        print_the_result_29.pack()
    root_29 = Tk()
    root_29.geometry("853x480")
    Title_Label_29 = Label(root_29, text = "Convert Days to Seconds", font = ('Bahnschrift 20 bold underline'))
    Title_Label_29.pack()

    entry_29 = Entry(root_29)
    entry_29.pack()
    enter_button_29 = Button(root_29, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_29)
    enter_button_29.pack()
    root_29.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def wtod():
    def the_result_30():
        fetch_number_30 = float(entry_30.get())
        result_29 = (fetch_number_30 * 7)
        print_the_result_30 = Label(root_30, text = f"Your answer is {result_29} day(s)", font = ('Bahnschrift 15'))
        print_the_result_30.pack()
    root_30 = Tk()
    root_30.geometry("853x480")
    Title_Label_30 = Label(root_30, text = "Convert Weeks to Days", font = ('Bahnschrift 20 bold underline'))
    Title_Label_30.pack()

    entry_30 = Entry(root_30)
    entry_30.pack()
    enter_button_30 = Button(root_30, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_30)
    enter_button_30.pack()
    root_30.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def dtow():
    def the_result_31():
        fetch_number_31 = float(entry_31.get())
        result_31 = (fetch_number_31 / 7)
        print_the_result_31 = Label(root_31, text = f"Your answer is {result_31} week(s)", font = ('Bahnschrift 15'))
        print_the_result_31.pack()
    root_31 = Tk()
    root_31.geometry("853x480")
    Title_Label_31 = Label(root_31, text = "Convert Days to Weeks", font = ('Bahnschrift 20 bold underline'))
    Title_Label_31.pack()

    entry_31 = Entry(root_31)
    entry_31.pack()
    enter_button_31 = Button(root_31, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_31)
    enter_button_31.pack()
    root_31.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def cm2tom2():
    def the_result_32():
        fetch_number_32 = float(entry_32.get())
        result_32 = (fetch_number_32 / 10000)
        print_the_result_32 = Label(root_32, text = f"Your answer is {result_32} squred metre", font = ('Bahnschrift 15'))
        print_the_result_32.pack()
    root_32 = Tk()
    root_32.geometry("853x480")
    Title_Label_32 = Label(root_32, text = "Convert squared centimetre to square metre", font = ('Bahnschrift 20 bold underline'))
    Title_Label_32.pack()

    entry_32 = Entry(root_32)
    entry_32.pack()
    enter_button_32 = Button(root_32, text = "ENTER", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = the_result_32)
    enter_button_32.pack()
    root_32.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Sparsh_Root = Tk()
Sparsh_Root.geometry("1920x1080")
TITLE_LABEL = Label(Sparsh_Root, text = "PLEASE THE SELECT THE OPERATION", font = ('Bahnschrift 20 bold underline'))
TITLE_LABEL.pack()

# TEMPERATURE SECTION

TEMPERATURE_LABEL = Label(Sparsh_Root, text = "Temperature", font = ('Bahnschrift 15 bold'))
TEMPERATURE_LABEL.place(x = 25, y = 100)

C_TO_F_BUTTON = Button(Sparsh_Root, text = "°C to °F", font = ('Bahnschrift 10'), fg = "yellow", bg = "red", activebackground = "blue", command = ctof)
C_TO_F_BUTTON.place(x = 55, y = 135)

F_TO_C_BUTTON = Button(Sparsh_Root, text = "°F to °C", font = ('Bahnschrift 10'), fg = "yellow", bg = "red", activebackground = "blue", command = ftoc)
F_TO_C_BUTTON.place(x = 55, y = 165)

C_TO_K_BUTTON = Button(Sparsh_Root, text = "°C to K", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = ctok)  
C_TO_K_BUTTON.place(x = 55, y = 195)

# CURRENCY SECTION

CURRENCY_LABEL = Label(Sparsh_Root, text = "Currency", font = ('Bahnschrift 15 bold'))
CURRENCY_LABEL.place(x = 185, y = 100)

R_TO_D_BUTTON = Button(Sparsh_Root, text = "Rupees to Dollars", font = ('Bahnschrift 10'), fg = 'yellow', bg = "red", activebackground = "blue", command = rtod)
R_TO_D_BUTTON.place(x = 175, y = 135)

D_TO_R_BUTTON = Button(Sparsh_Root, text = "Dollars to Rupees", font = ('Bahnschrift 10'), fg = 'yellow', bg = "red", activebackground = "blue", command = dtor)
D_TO_R_BUTTON.place(x = 175, y = 165)

R_TO_P_BUTTON = Button(Sparsh_Root, text = "Rupees to Pounds", font = ('Bahnschrift 10'), fg = "yellow", bg = "red", activebackground = 'blue', command = rtop)
R_TO_P_BUTTON.place(x = 175, y = 195)

P_TO_R_BUTTON = Button(Sparsh_Root, text = "Pounds to Rupees", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = ptor)
P_TO_R_BUTTON.place(x = 175, y = 225)

# MASS SECTION

MASS_LABEL = Label(Sparsh_Root, text = "Mass", font = ('Bahnschrift 15 bold'))
MASS_LABEL.place(x = 365, y = 100)

G_TO_KG_BUTTON = Button(Sparsh_Root, text = "Grams to Kilograms", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = gtokg)
G_TO_KG_BUTTON.place(x = 330, y = 135)

KG_TO_G_BUTTON = Button(Sparsh_Root, text = "Kilograms to Grams", font = ('Bahnschrift 10'), fg = 'yellow', bg ='red', activebackground= 'blue', command = kgtog)
KG_TO_G_BUTTON.place(x = 330, y = 165)

KG_TO_P_BUTTON = Button(Sparsh_Root, text = "Kilograms to Pounds", font = ('Bahnschrift 10'), fg = 'yellow', bg ='red', activebackground= 'blue', command = None)
KG_TO_P_BUTTON.place(x = 330, y = 195)

P_TO_KG_BUTTON = Button(Sparsh_Root, text = "Pound to Kilogram", font = ('Bahnschrift 10'), fg = 'yellow', bg ='red', activebackground= 'blue', command = ptokg)
P_TO_KG_BUTTON.place(x = 330, y = 225)

# LENGTH SECTION

LENGTH_LABEL = Label(Sparsh_Root, text = "Length", font = ('Bahnschrift 15 bold'))
LENGTH_LABEL.place(x = 555, y = 100)

CM_TO_M_BUTTON = Button(Sparsh_Root, text = "Centimetre to Metre", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = cmtom)
CM_TO_M_BUTTON.place(x = 525, y = 135)

M_TO_CM_BUTTON = Button(Sparsh_Root, text = "Metre to Centimetre", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = mtocm)
M_TO_CM_BUTTON.place(x = 525, y = 165)

M_TO_FEET_BUTTON = Button(Sparsh_Root, text = "Metre to Feet", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = mtof)
M_TO_FEET_BUTTON.place(x = 525, y = 195)

FEET_TO_M_BUTTON = Button(Sparsh_Root, text = "Feet to Metre", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = ftom)
FEET_TO_M_BUTTON.place(x = 525, y = 225)

M_TO_Y_BUTTON = Button(Sparsh_Root, text = "Metre to Yard", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = mtoy)
M_TO_Y_BUTTON.place(x = 525, y = 255)

Y_TO_M_BUTTON = Button(Sparsh_Root, text = "Yard to Metre", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = ytom)
Y_TO_M_BUTTON.place(x = 525, y = 285)

# SPEED SECTION

SPEED_LABEL = Label(Sparsh_Root, text = "Speed", font = ('Bahnschrift 15 bold'))
SPEED_LABEL.place(x = 745, y = 100)

KMPH_TO_MPH = Button(Sparsh_Root, text = "Kilometre/Hr to Miles/Hr", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = kmphtomph)
KMPH_TO_MPH.place(x = 715, y = 135)

MPH_TO_KMPH = Button(Sparsh_Root, text = "Miles/Hr to Kilometre/Hr", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = mphtokmph)
MPH_TO_KMPH.place(x = 715, y = 165)

KMPH_TO_MS = Button(Sparsh_Root, text = "Kilometre/Hr to Metre/S", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = kmphtoms)
KMPH_TO_MS.place(x = 715, y = 195)

MS_TO_KMPH = Button(Sparsh_Root, text = "Metre/S to Kilometre/Hr", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = mstokmph)
MS_TO_KMPH.place(x = 715, y = 225)

# TIME SECTION

TIME_LABEL = Label(Sparsh_Root, text = "Time", font = ('Bahnschrift 15 bold'))
TIME_LABEL.place(x = 935, y = 100)

S_TO_M_BUTTON = Button(Sparsh_Root, text = "Seconds to Minutes", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = stom)
S_TO_M_BUTTON.place(x = 905, y = 135)

M_TO_S_BUTTON = Button(Sparsh_Root, text = "Minutes to Seconds", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = mtos)
M_TO_S_BUTTON.place(x = 905, y = 165)

S_TO_HR_BUTTON = Button(Sparsh_Root, text = "Seconds to Hours", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = stohr)
S_TO_HR_BUTTON.place(x = 905, y = 195)

HR_TO_S_BUTTON = Button(Sparsh_Root, text = "Hours to Seconds", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = hrtos)
HR_TO_S_BUTTON.place(x = 905, y = 225)

HR_TO_D_BUTTON = Button(Sparsh_Root, text = "Hours to Days", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = hrtod)
HR_TO_D_BUTTON.place(x = 905, y = 255)

D_TO_HR_BUTTON = Button(Sparsh_Root, text = "Days to Hours", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = dtohr)
D_TO_HR_BUTTON.place(x = 905, y = 285)

S_TO_D_BUTTON = Button(Sparsh_Root, text = "Seconds to Days", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = stod)
S_TO_D_BUTTON.place(x = 905, y = 315)

D_TO_S_BUTTON = Button(Sparsh_Root, text = "Days to Seconds", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = dtos)
D_TO_S_BUTTON.place(x = 905, y = 345)

W_TO_D_BUTTON = Button(Sparsh_Root, text = "Weeks to Days", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = wtod)
W_TO_D_BUTTON.place(x = 905, y = 375)

D_TO_W_BUTTON = Button(Sparsh_Root, text = "Days to Week(s)", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = dtow)
D_TO_W_BUTTON.place(x = 905, y = 405)

# AREA SECTION

AREA_LABEL = Label(Sparsh_Root, text = "Area", font = ('Bahnschrift 15 bold'))
AREA_LABEL.place(x = 1115, y = 100)

# ORIGINALLY, X was 1125

CM2_TO_M2 = Button(Sparsh_Root, text = "Cm^2 to M^2", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = cm2tom2)
CM2_TO_M2.place(x = 1095, y = 135)

M2_TO_CM2 = Button(Sparsh_Root, text = "M^2 to CM^2", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = None)
M2_TO_CM2.place(x = 1095, y = 165)

KM2_TO_M2 = Button(Sparsh_Root, text = "KM^2 to M^2", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = None)
KM2_TO_M2.place(x = 1095, y = 195)

M2_TO_KM2 = Button(Sparsh_Root, text = "M^2 to KM^2", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = None)
M2_TO_KM2.place(x = 1095, y = 225)

M2_TO_F2 = Button(Sparsh_Root, text = "M^2 to F^2", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = None)
M2_TO_F2.place(x = 1095, y = 255)

F2_TO_M2 = Button(Sparsh_Root, text = "F^2 to M^2", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = None)
F2_TO_M2.place(x = 1095, y = 285)

ACRE_TO_KM2 = Button(Sparsh_Root, text = "Acre to KM^2", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = None)
ACRE_TO_KM2.place(x = 1095, y = 315)

KM2_TO_ACRE = Button(Sparsh_Root, text = "KM^2 to Acre", font = ('Bahnschrift 10'), fg = 'yellow', bg = 'red', activebackground = 'blue', command = None)
KM2_TO_ACRE.place(x = 1095, y = 345)

# EXIT BUTTON

EXIT_BUTTON = Button(Sparsh_Root, text = "EXIT", font = ('Bahnschrift 17'), fg = 'black', bg = 'red', activebackground = 'blue', command = exit)
EXIT_BUTTON.pack()
    
Sparsh_Root.mainloop()
