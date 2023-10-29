from tkinter import Checkbutton, IntVar, Tk, Label, Entry, Button, Frame
from datetime import datetime, timedelta
import os
import subprocess

def create_first_window():
    first_window = Tk()
    first_window.title("Choose your desired time:")
    first_window.geometry("400x230")

    separator = Frame(first_window, height=20, bg="")
    separator.pack()

    label = Label(first_window, text="At what time do you want?:")
    label.pack()

    separator = Frame(first_window, height=5, bg="")
    separator.pack()

    label = Label(first_window, text="Hours (24):")
    label.pack()

    entryH = Entry(first_window)
    entryH.pack()

    separator = Frame(first_window, height=10, bg="")
    separator.pack()

    label = Label(first_window, text="Minutes:")
    label.pack()

    entryM = Entry(first_window)
    entryM.pack()

    separator = Frame(first_window, height=5, bg="")
    separator.pack()

    def run_sleeper(hours,mins):
        current_time = datetime.now().time()
        input_time = datetime.strptime("{}:{}:00".format(hours,mins), "%H:%M:%S").time()
        difference_time = timedelta(hours=input_time.hour - current_time.hour,
                            minutes=input_time.minute - current_time.minute,
                            seconds=input_time.second - current_time.second)
        totalSeconds = int(difference_time.total_seconds())

        command = "shutdown -s -t {}".format(totalSeconds)
        subprocess.run(["shutdown", "/a"], stdout=subprocess.PIPE)
        subprocess.run(command, shell=True)

        first_window.destroy()

        if(let1.get() == 1):
            path = os.path.join(os.getcwd(),"random_cursor.exe")
            subprocess.run(path,shell=True)
            subprocess.run(path,shell=True)


    def check_time(hours,mins):
        current_hour = datetime.now().hour
        current_mins = datetime.now().minute
        if(current_hour == hours):
            if(current_mins <= mins):
                return True
        elif(current_hour < hours):
            return True
        return False

    def second_window(mssg):
        second_window = Tk()
        second_window.geometry("300x60")

        separator = Frame(second_window, height=20, bg="")
        separator.pack()

        label = Label(second_window, text=mssg)
        label.pack()

        separator = Frame(second_window, height=20, bg="")
        separator.pack()

    def submit_function():
        hours = -1 if entryH.get() == '' else int(entryH.get()) if entryH.get().isdigit() else -1
        minutes = -1 if entryM.get() == '' else int(entryM.get()) if entryM.get().isdigit() else -1
        
        if( (hours>=0 and hours<24) and (minutes>=0 and minutes<60) ):
            if(check_time(hours,minutes) == False):
                second_window("Input time should be minor than current Time")
            else:
                run_sleeper(hours,minutes)
        else:
            second_window("Wrong Time")

    separator = Frame(first_window, height=10, bg="")
    separator.pack()
    
    let1 = IntVar()
    let1.set(1)
    c1 = Checkbutton(first_window, text='Run Random Cursor', variable=let1, onvalue=1, offvalue=0)
    c1.pack()

    separator = Frame(first_window, height=10, bg="")
    separator.pack()

    submit_button = Button(first_window, text="Submit", command=submit_function)
    submit_button.pack()

    first_window.bind('<Return>',lambda event=None: submit_button.invoke())

    first_window.mainloop()

create_first_window()