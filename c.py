import tkinter as tk
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch Simulator")
        self.root.geometry("300x150")

        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Label to display time
        self.time_label = tk.Label(self.root, text="00:00:00", font=("Helvetica", 30))
        self.time_label.pack()

        # Start/Stop button
        self.start_stop_button = tk.Button(self.root, text="Start", width=10, command=self.toggle)
        self.start_stop_button.pack(pady=5)

        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset", width=10, command=self.reset)
        self.reset_button.pack(pady=5)

    def toggle(self):
        """Start or stop the stopwatch based on its current state."""
        if self.running:
            self.running = False
            self.start_stop_button.config(text="Start")
        else:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.start_stop_button.config(text="Stop")
            self.update_time()

    def update_time(self):
        """Update the time display on the label."""
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(self.elapsed_time, 60)
            seconds, milliseconds = divmod(seconds, 1)
            time_str = f"{int(minutes):02}:{int(seconds):02}:{int(milliseconds*100):02}"
            self.time_label.config(text=time_str)
            self.root.after(10, self.update_time)  # Update every 10ms

    def reset(self):
        """Reset the stopwatch."""
        self.running = False
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")
        self.start_stop_button.config(text="Start")

# Create the main window
root = tk.Tk()
app = StopwatchApp(root)

# Start the Tkinter event loop
root.mainloop()
