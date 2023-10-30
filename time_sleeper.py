from tkinter import Checkbutton, IntVar, Tk, Label, Entry, Button, Frame
from datetime import datetime, timedelta
import os
import subprocess

# Function to create the first window for user input
def create_first_window():
    # Create a Tkinter window
    first_window = Tk()
    first_window.title("Choose your desired time:")
    first_window.geometry("400x180")

    # GUI elements for user input
    # Labels and entry fields for hours and minutes
    label = Label(first_window, text="At what time do you want?:")
    label.pack()
    label = Label(first_window, text="Hours (24):")
    label.pack()
    entryH = Entry(first_window)
    entryH.pack()
    label = Label(first_window, text="Minutes:")
    label.pack()
    entryM = Entry(first_window)
    entryM.pack()

    # Function to set up the shutdown command and execute it
    def run_sleeper(hours, mins):
        # Get current time
        current_time = datetime.now().time()
        # Create target time based on user input
        input_time = datetime.strptime("{}:{}:00".format(hours, mins), "%H:%M:%S").time()
        # Calculate time difference between target and current time
        difference_time = timedelta(hours=input_time.hour - current_time.hour,
                                    minutes=input_time.minute - current_time.minute,
                                    seconds=input_time.second - current_time.second)
        totalSeconds = int(difference_time.total_seconds())
        # Construct and execute shutdown command
        command = "shutdown -s -t {}".format(totalSeconds)
        subprocess.run(["shutdown", "/a"], stdout=subprocess.PIPE)
        subprocess.run(command, shell=True)
        first_window.destroy()
        # If checkbox is checked, run random_cursor.exe
        if(let1.get() == 1):
            path = os.path.join(os.getcwd(), "random_cursor.exe")
            subprocess.run(path, shell=True)

    # Function to validate user input time
    def check_time(hours, mins):
        current_hour = datetime.now().hour
        current_mins = datetime.now().minute
        if(current_hour == hours):
            if(current_mins <= mins):
                return True
        elif(current_hour < hours):
            return True
        return False

    # Function to display a second window with a message
    def second_window(mssg):
        second_window = Tk()
        second_window.geometry("300x60")
        label = Label(second_window, text=mssg)
        label.pack()

    # Function to handle the submission of user input
    def submit_function():
        # Get user input for hours and minutes, validate it, and take appropriate action
        hours = -1 if entryH.get() == '' else int(entryH.get()) if entryH.get().isdigit() else -1
        minutes = -1 if entryM.get() == '' else int(entryM.get()) if entryM.get().isdigit() else -1
        
        if( (hours >= 0 and hours < 24) and (minutes >= 0 and minutes < 60) ):
            if(check_time(hours, minutes) == False):
                second_window("Input time should be earlier than current time")
            else:
                run_sleeper(hours, minutes)
        else:
            second_window("Invalid time input")

    # GUI elements for checkbox and submit button
    let1 = IntVar()
    let1.set(1)
    c1 = Checkbutton(first_window, text='Run Random Cursor', variable=let1, onvalue=1, offvalue=0)
    c1.pack()
    submit_button = Button(first_window, text="Submit", command=submit_function)
    submit_button.pack()

    # Bind Enter key to invoke the submit button
    first_window.bind('<Return>', lambda event=None: submit_button.invoke())

    # Start the main loop for the Tkinter window
    first_window.mainloop()

# Call the function to create the first window
create_first_window()
