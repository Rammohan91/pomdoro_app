from tkinter import *
import time

global minutes_label
global seconds_label

def start_timer():
    pd_time = 1500
    try:
        while pd_time > -1:
            mins, secs = divmod(pd_time, 60)
            minute_value.set("{0:2d}".format(mins))
            second_value.set("{0:2d}".format(secs))
            time.sleep(1)
            pd_time -= 1
            window.update()
    except:
       window.destroy()

def stop_timer():
    minute_value.set("00")
    second_value.set("00")
    window.update()

window = Tk()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

wid = screen_width/1.13
hei = screen_height/1.20

window.title("Pomodoro")
window.geometry("200x100+{}+{}".format(int(wid),int(hei)))
window.attributes('-toolwindow', True)
window.attributes('-topmost',True)

minute_value = StringVar()
minute_value.set("00")
e1 = Entry(window, width=3, font=("Arial",18,""),textvariable=minute_value)
#e1.grid(row=0, column=1)
e1.place(x=55,y=20)

second_value = StringVar()
second_value.set("00")
e2 = Entry(window, width=3, font=("Arial",18,""),textvariable=second_value)
#e2.grid(row=0, column=2)
e2.place(x=105,y=20)

b1 = Button(window,bg="Green", activebackground="Dark Green", font=("Arial",12,""),text="Start", command=start_timer)
#b1.grid(row=1, column=0)
b1.place(x=50,y=60)

b2 = Button(window, bg="Red", activebackground="Dark Red", font=("Arial",12,""),text="Stop", command=stop_timer)
#b1.grid(row=1, column=0)
b2.place(x=105,y=60)

window.mainloop()