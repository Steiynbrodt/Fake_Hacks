import tkinter as tk
import random
from datetime import datetime, timedelta


class TrainingRansomwareWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Training Simulation")
        self.root.configure(bg="black")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        self.canvas = tk.Canvas(root, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.start_time = datetime.now()
        self.deadline = self.start_time + timedelta(hours=23, minutes=59, seconds=59)

        self.fake_files = 1247
        self.fake_price = "300 USD"
        self.flash = False

        self.logo = r"""
███╗   ███╗██╗   ██╗███████╗███████╗██╗███╗   ██╗
████╗ ████║██║   ██║██╔════╝██╔════╝██║████╗  ██║
██╔████╔██║██║   ██║█████╗  █████╗  ██║██╔██╗ ██║
██║╚██╔╝██║██║   ██║██╔══╝  ██╔══╝  ██║██║╚██╗██║
██║ ╚═╝ ██║╚██████╔╝██║     ██║     ██║██║ ╚████║
╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═══╝

 ██████╗ █████╗ ██████╗ ████████╗███████╗██╗     
██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║     
██║     ███████║██████╔╝   ██║   █████╗  ██║     
██║     ██╔══██║██╔══██╗   ██║   ██╔══╝  ██║     
╚██████╗██║  ██║██║  ██║   ██║   ███████╗███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝
"""

        self.root.after(50, self.render)
        self.root.after(500, self.blink)
        self.root.after(1000, self.tick_files)

    def blink(self):
        self.flash = not self.flash
        self.root.after(500, self.blink)

    def tick_files(self):
        self.fake_files += random.randint(0, 3)
        self.root.after(1500, self.tick_files)

    def render(self):
        w = self.root.winfo_width()
        h = self.root.winfo_height()

        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, w, h, fill="black", outline="")
        self.draw_scanlines(w, h)

        self.canvas.create_rectangle(40, 40, w - 40, h - 40, outline="#aa0000", width=4)
        self.canvas.create_rectangle(60, 60, w - 60, 250, fill="#0a0a0a", outline="#ff3333", width=2)

        self.canvas.create_text(
            w // 2,
            90,
            text=self.logo.strip("\n"),
            fill="#ff3333" if self.flash else "#ff6666",
            font=("Consolas", 12, "bold"),
            justify="center",
            anchor="n"
        )

        self.canvas.create_text(
            w // 2,
            220,
            text="FILES LOCKED - TRAINING SIMULATION",
            fill="white",
            font=("Arial", 24, "bold")
        )

        self.canvas.create_rectangle(70, 270, int(w * 0.58), h - 80, fill="#111111", outline="#cc0000", width=2)
        self.canvas.create_rectangle(int(w * 0.62), 270, w - 70, h - 80, fill="#111111", outline="#cc0000", width=2)

        body = (
            "This is a harmless awareness demo.\n\n"
            "Your documents, pictures, databases, and other important files\n"
            'have been marked as "unavailable" for simulation purposes only.\n\n'
            "Nothing has been encrypted.\n"
            "Nothing has been modified.\n"
            "This screen exists to demonstrate the visual style of extortion malware.\n\n"
            "Operator: MUFFINCARTEL\n"
            "Status: YOUR SYSTEM IS FULLY BAKED\n\n"
            "Think before you click."
        )

        self.canvas.create_text(
            100,
            320,
            text=body,
            fill="white",
            font=("Consolas", 18),
            anchor="nw",
            width=int(w * 0.48)
        )

        stats_y = 560
        self.canvas.create_text(100, stats_y, text="Affected files:", fill="#ff5555",
                                font=("Consolas", 20, "bold"), anchor="nw")
        self.canvas.create_text(360, stats_y, text=str(self.fake_files), fill="white",
                                font=("Consolas", 20), anchor="nw")

        self.canvas.create_text(100, stats_y + 50, text="Recovery fee:", fill="#ff5555",
                                font=("Consolas", 20, "bold"), anchor="nw")
        self.canvas.create_text(360, stats_y + 50, text=self.fake_price, fill="white",
                                font=("Consolas", 20), anchor="nw")

        self.canvas.create_text(100, stats_y + 100, text="Status:", fill="#ff5555",
                                font=("Consolas", 20, "bold"), anchor="nw")
        self.canvas.create_text(
            360,
            stats_y + 100,
            text="FRESH OUT OF THE OVEN" if self.flash else "DEMO MODE",
            fill="#00ff66" if self.flash else "white",
            font=("Consolas", 20, "bold"),
            anchor="nw"
        )

        remaining = self.deadline - datetime.now()
        if remaining.total_seconds() < 0:
            remaining = timedelta(0)

        total_seconds = int(remaining.total_seconds())
        hrs = total_seconds // 3600
        mins = (total_seconds % 3600) // 60
        secs = total_seconds % 60
        countdown = f"{hrs:02}:{mins:02}:{secs:02}"

        self.canvas.create_text(
            int(w * 0.81),
            330,
            text="TIME REMAINING",
            fill="#ff5555",
            font=("Arial", 22, "bold")
        )
        self.canvas.create_text(
            int(w * 0.81),
            390,
            text=countdown,
            fill="white" if self.flash else "#ff4444",
            font=("Consolas", 34, "bold")
        )

        self.draw_button(int(w * 0.70), 500, int(w * 0.22), 55, "VIEW INSTRUCTIONS")
        self.draw_button(int(w * 0.70), 575, int(w * 0.22), 55, "CHECK STATUS")
        self.draw_button(int(w * 0.70), 650, int(w * 0.22), 55, "DEMO INFO")

        footer = "MUFFINCARTEL training screen • educational simulation only • press ESC to close"
        self.canvas.create_text(
            w // 2,
            h - 45,
            text=footer,
            fill="#bbbbbb",
            font=("Consolas", 14)
        )

        self.root.after(50, self.render)

    def draw_button(self, x, y, bw, bh, text):
        self.canvas.create_rectangle(x, y, x + bw, y + bh, fill="#990000", outline="#ff3333", width=2)
        self.canvas.create_text(
            x + bw // 2,
            y + bh // 2,
            text=text,
            fill="white",
            font=("Arial", 16, "bold")
        )

    def draw_scanlines(self, w, h):
        for y in range(0, h, 4):
            self.canvas.create_line(0, y, w, y, fill="#120000")


def main():
    root = tk.Tk()
    TrainingRansomwareWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
