from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
check = ""
clock = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps, check
    window.after_cancel(clock)
    reps = 0
    check = ""
    checkmark["text"] = check
    canvas.itemconfig(timer_text, text="00:00")
    timer["text"] = "Timer"
    timer["fg"] = GREEN

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 
    global check
    reps += 1
    work_s = WORK_MIN * 60
    short_s = SHORT_BREAK_MIN * 60
    long_s = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_s)
        check += "✔"
        checkmark["text"] = check
        timer["text"] = "Break"
        timer["fg"] = RED
        motive["text"] = "Esooo relaxing hours"
    elif reps % 2 == 0:
        check += "✔"
        count_down(short_s)
        checkmark["text"] = check
        timer["text"] = "Break"
        timer["fg"] = PINK
        motive["text"] = "Descanzaguer bien ganado B.....Beee"
    else:
        count_down(work_s)
        timer["text"] = "Work!"
        timer["fg"] = GREEN
        motive["text"] = "A darrrrle Chiquibaby!!!"

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global clock
        clock = window.after(1000, count_down, count - 1)
    else:
        start_timer()
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Mary Linda Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer.grid(column=1, row=0)

checkmark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "bold"))
checkmark.grid(column=1, row=3)

motive = Label(text="Arranca La carretera!", fg=PINK, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
motive.grid(column=1, row=4)


start_b = Button(text="Start", command=start_timer, highlightthickness=0)
start_b.grid(column=0, row=2)


reset_b = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_b.grid(column=2, row=2)

window.mainloop()