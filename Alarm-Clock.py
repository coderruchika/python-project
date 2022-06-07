#                                        *Alarm Clock*


#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
import winsound



def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarm Clock")
clock.iconbitmap(r"logo.ico")
clock.geometry("400x200")
clock.configure(bg='light blue')
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="white",bg="grey",relief = "solid",width = 30,font=("Arial",12,"bold")).place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min  Sec",fg="white",font=("Arial",12,"bold"),relief = "solid",bg="grey",width = 12).place(x = 250)
setYourAlarm = Label(clock,text = "When to wake you up",fg="white",bg="grey",width = 20,relief = "solid",font=("Helevetica",12,"bold")).place(x=5, y=32)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "grey",fg="white",justify="center",relief = "solid",font=("Arial",12,"bold"),width = 5).place(x=250,y=35)
minTime= Entry(clock,textvariable = min,bg = "grey",font=("Arial",12,"bold"),justify="center",relief = "solid",fg="white",width = 5).place(x=290,y=35)
secTime = Entry(clock,textvariable = sec,bg = "grey",font=("Arial",12,"bold"),justify="center",relief = "solid",fg="white",width=5).place(x=330,y=35)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="white",bg = "grey",relief = "solid",font=("Arial",12,"bold"),width = 10,command = actual_time).place(x =140,y=70)

clock.mainloop()
#Execution of the window.

