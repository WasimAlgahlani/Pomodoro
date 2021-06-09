from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MINUTES = 25
SHORT_BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 20
reps = 0
timer = None


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MINUTES * 60
    short_break = SHORT_BREAK_MINUTES * 60
    long_break = LONG_BREAK_MINUTES * 60
    if reps % 8 == 0:
        count_down(long_break)
        timer_title.config(text="Long Break", fg=RED)
    elif reps % 2 != 0:
        count_down(work_sec)
        timer_title.config(text="Work", fg=GREEN)
    else:
        count_down(short_break)
        timer_title.config(text="Short Break", fg=PINK)


def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_can, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "@"
        check_label.config(text=marks)
        start_timer()


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_can, text="25:00")
    timer_title.config(text="Timer")
    check_label.config(text="")


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_can = canvas.create_text(100, 112, text="25:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

timer_title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), highlightthickness=0, bg=YELLOW)
timer_title.grid(row=0, column=1)

check_label = Label(fg=GREEN, font=(FONT_NAME, 12, "bold"), highlightthickness=0, bg=YELLOW)
check_label.grid(row=2, column=1)
check_label.config(pady=20)

start_button = Button(text="Start", fg=RED, font=(FONT_NAME, 10, "bold"), highlightthickness=0,
                      bg=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", fg=RED, font=(FONT_NAME, 10, "bold"), highlightthickness=0,
                      bg=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
