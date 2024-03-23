import tkinter as tk
import time


class PomodoroApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")

        self.focus_time = 25
        self.short_break_time = 5
        self.long_break_time = 15
        self.pomodoro_count = 0

        self.timer_running = False
        self.timer_paused = False
        self.current_time = self.focus_time * 60

        self.label = tk.Label(self.master, text="", font=("Helvetica", 48))
        self.label.pack()

        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.pack()

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack()

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.timer_paused = False
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)

            while self.current_time > 0:
                mins, secs = divmod(self.current_time, 60)
                time_str = "{:02d}:{:02d}".format(mins, secs)
                self.label.config(text=time_str)
                self.master.update()
                time.sleep(1)
                self.current_time -= 1

            self.pomodoro_count += 1
            self.label.config(text="Time's up!")

            if self.pomodoro_count % 4 == 0:
                self.current_time = self.long_break_time * 60
            else:
                self.current_time = self.short_break_time * 60

        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)

    def pause_timer(self):
        self.timer_running = False
        self.timer_paused = True
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)

    def reset_timer(self):
        self.timer_running = False
        self.timer_paused = False
        self.current_time = self.focus_time * 60
        self.label.config(text="")
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        self.pomodoro_count = 0


if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.geometry("400x200")  # Ширина и высота окна
    root.mainloop()