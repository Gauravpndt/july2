import streamlit as st
import tkinter as tk
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.time_elapsed = 0
        self.running = False

        self.label = tk.Label(root, text="0:00:00", font=("Helvetica", 48))
        self.label.pack(padx=20, pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side="left", padx=10)

        self.update_clock()

    def update_clock(self):
        if self.running:
            self.time_elapsed += 1
            self.update_label()
            self.root.after(1000, self.update_clock)

    def update_label(self):
        seconds = self.time_elapsed % 60
        minutes = (self.time_elapsed // 60) % 60
        hours = self.time_elapsed // 3600
        self.label.config(text=f"{hours}:{minutes:02}:{seconds:02}")

    def start(self):
        if not self.running:
            self.running = True
            self.update_clock()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.time_elapsed = 0
        self.update_label()

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
