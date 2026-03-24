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

        self.start_time = datetime.now()
        self.deadline = self.start_time + timedelta(hours=23, minutes=59, seconds=59)

        self.fake_files = 1247
        self.fake_price = "300 USD"
        self.flash = False
        self.current_view = "main"

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

        self.notice_var = tk.StringVar(value="")
        self.key_var = tk.StringVar()

        self.build_ui()

        self.root.after(500, self.blink)
        self.root.after(1000, self.tick_files)
        self.root.after(100, self.update_timer)
        self.root.after(50, self.animate_background)

    def build_ui(self):
        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0, bd=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        self.outer = tk.Frame(self.root, bg="black", highlightbackground="#aa0000", highlightthickness=3)
        self.outer.place(relx=0.03, rely=0.04, relwidth=0.94, relheight=0.92)

        self.header = tk.Frame(self.outer, bg="#0a0a0a", highlightbackground="#ff3333", highlightthickness=2)
        self.header.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.25)

        self.logo_label = tk.Label(
            self.header,
            text=self.logo.strip("\n"),
            bg="#0a0a0a",
            fg="#ff6666",
            font=("Consolas", 11, "bold"),
            justify="center"
        )
        self.logo_label.pack(pady=(12, 0))

        self.title_label = tk.Label(
            self.header,
            text="FILES LOCKED - TRAINING SIMULATION",
            bg="#0a0a0a",
            fg="white",
            font=("Arial", 22, "bold")
        )
        self.title_label.pack(pady=(8, 8))

        self.body = tk.Frame(self.outer, bg="black")
        self.body.place(relx=0.02, rely=0.30, relwidth=0.96, relheight=0.62)

        self.left_panel = tk.Frame(self.body, bg="#111111", highlightbackground="#cc0000", highlightthickness=2)
        self.left_panel.place(relx=0.00, rely=0.00, relwidth=0.58, relheight=1.0)

        self.right_panel = tk.Frame(self.body, bg="#111111", highlightbackground="#cc0000", highlightthickness=2)
        self.right_panel.place(relx=0.62, rely=0.00, relwidth=0.38, relheight=1.0)

        self.footer = tk.Label(
            self.outer,
            text="MUFFINCARTEL training screen • educational simulation only • press ESC to close",
            bg="black",
            fg="#bbbbbb",
            font=("Consolas", 13)
        )
        self.footer.place(relx=0.5, rely=0.955, anchor="center")

        self.notice = tk.Label(
            self.outer,
            textvariable=self.notice_var,
            bg="#111111",
            fg="#ffccaa",
            font=("Consolas", 13, "bold"),
            highlightbackground="#ff4444",
            highlightthickness=2
        )
        self.notice.place(relx=0.5, rely=0.90, anchor="center")
        self.notice.place_forget()

        self.build_right_panel()
        self.show_view("main")

    def build_right_panel(self):
        self.timer_title = tk.Label(
            self.right_panel,
            text="TIME REMAINING",
            bg="#111111",
            fg="#ff5555",
            font=("Arial", 20, "bold")
        )
        self.timer_title.pack(pady=(28, 6))

        self.timer_value = tk.Label(
            self.right_panel,
            text="00:00:00",
            bg="#111111",
            fg="#ff4444",
            font=("Consolas", 30, "bold")
        )
        self.timer_value.pack(pady=(0, 22))

        self.btn_instructions = self.make_button(self.right_panel, "VIEW INSTRUCTIONS", lambda: self.show_view("instructions"))
        self.btn_status = self.make_button(self.right_panel, "CHECK STATUS", lambda: self.show_view("status"))
        self.btn_recovery = self.make_button(self.right_panel, "RECOVERY PANEL", lambda: self.show_view("recovery"))

        self.btn_instructions.pack(fill="x", padx=36, pady=10)
        self.btn_status.pack(fill="x", padx=36, pady=10)
        self.btn_recovery.pack(fill="x", padx=36, pady=10)

    def make_button(self, parent, text, command):
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            bg="#990000",
            fg="white",
            activebackground="#bb1111",
            activeforeground="white",
            relief="flat",
            bd=0,
            font=("Arial", 15, "bold"),
            cursor="hand2",
            pady=10
        )

        btn.bind("<Enter>", lambda e: btn.configure(bg="#bb1111"))
        btn.bind("<Leave>", lambda e: btn.configure(bg="#990000"))
        return btn

    def clear_left_panel(self):
        for child in self.left_panel.winfo_children():
            child.destroy()

    def show_view(self, view):
        self.current_view = view
        self.clear_left_panel()

        if view == "main":
            self.build_main_view()
        elif view == "instructions":
            self.build_instructions_view()
        elif view == "status":
            self.build_status_view()
        elif view == "recovery":
            self.build_recovery_view()

    def build_main_view(self):
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

        text = tk.Label(
            self.left_panel,
            text=body,
            bg="#111111",
            fg="white",
            justify="left",
            anchor="nw",
            font=("Consolas", 17),
            wraplength=720
        )
        text.pack(anchor="nw", padx=28, pady=(28, 20))

        stats = tk.Frame(self.left_panel, bg="#111111")
        stats.pack(anchor="nw", padx=28, pady=10)

        self.files_value = self.stat_row(stats, "Affected files:", str(self.fake_files), 0)
        self.price_value = self.stat_row(stats, "Recovery fee:", self.fake_price, 1)
        self.status_value = self.stat_row(stats, "Status:", "DEMO MODE", 2)

    def stat_row(self, parent, key, value, row):
        k = tk.Label(parent, text=key, bg="#111111", fg="#ff5555", font=("Consolas", 18, "bold"))
        k.grid(row=row, column=0, sticky="w", padx=(0, 24), pady=10)

        v = tk.Label(parent, text=value, bg="#111111", fg="white", font=("Consolas", 18))
        v.grid(row=row, column=1, sticky="w", pady=10)
        return v

    def build_instructions_view(self):
        text = (
            "INSTRUCTIONS\n\n"
            "1. Stay calm.\n"
            "2. This is a harmless simulation.\n"
            "3. No files have been encrypted.\n"
            "4. No files have been modified.\n"
            "5. This screen only demonstrates how convincing visual design can be.\n\n"
            "Why it works:\n"
            "- fullscreen UI creates pressure\n"
            "- timers create urgency\n"
            "- fake stats create credibility\n"
            "- buttons make it feel real\n\n"
            "Takeaway:\n"
            "Think before you click."
        )

        lbl = tk.Label(
            self.left_panel,
            text=text,
            bg="#111111",
            fg="white",
            justify="left",
            anchor="nw",
            font=("Consolas", 17),
            wraplength=760
        )
        lbl.pack(anchor="nw", padx=28, pady=(28, 20))

        bar = tk.Frame(self.left_panel, bg="#111111")
        bar.pack(anchor="nw", padx=28, pady=20)

        self.make_button(bar, "BACK", lambda: self.show_view("main")).pack(side="left", padx=(0, 14))
        self.make_button(bar, "SHOW WARNING", lambda: self.show_notice("User panic simulation successful.")).pack(side="left")

    def build_status_view(self):
        title = tk.Label(
            self.left_panel,
            text="SYSTEM STATUS",
            bg="#111111",
            fg="#ff6666",
            font=("Arial", 24, "bold")
        )
        title.pack(anchor="nw", padx=28, pady=(28, 18))

        rows = [
            ("Operator", "MUFFINCARTEL"),
            ("Mode", "Training Simulation"),
            ("File State", "Untouched"),
            ("Encryption", "Disabled"),
            ("Persistence", "Disabled"),
            ("Threat Level", "Visual Only"),
            ("User Confidence", "Declining"),
        ]

        table = tk.Frame(self.left_panel, bg="#111111")
        table.pack(anchor="nw", padx=28, pady=8)

        for i, (k, v) in enumerate(rows):
            tk.Label(table, text=f"{k}:", bg="#111111", fg="#ff5555", font=("Consolas", 17, "bold")).grid(row=i, column=0, sticky="w", padx=(0, 20), pady=8)
            tk.Label(table, text=v, bg="#111111", fg="white", font=("Consolas", 17)).grid(row=i, column=1, sticky="w", pady=8)

        bar = tk.Frame(self.left_panel, bg="#111111")
        bar.pack(anchor="nw", padx=28, pady=24)

        self.make_button(bar, "BACK", lambda: self.show_view("main")).pack(side="left", padx=(0, 14))
        self.make_button(bar, "REFRESH STATUS", lambda: self.show_notice("Status refreshed.")).pack(side="left")

    def build_recovery_view(self):
        title = tk.Label(
            self.left_panel,
            text="RECOVERY PANEL",
            bg="#111111",
            fg="#ff6666",
            font=("Arial", 24, "bold")
        )
        title.pack(anchor="nw", padx=28, pady=(28, 18))

        body = (
            "Enter your recovery key below.\n\n"
            "This is fake.\n"
            "No recovery is needed because nothing was encrypted.\n"
            "But an interactive form makes the screen feel much more believable."
        )

        lbl = tk.Label(
            self.left_panel,
            text=body,
            bg="#111111",
            fg="white",
            justify="left",
            anchor="nw",
            font=("Consolas", 17),
            wraplength=760
        )
        lbl.pack(anchor="nw", padx=28, pady=(0, 20))

        entry = tk.Entry(
            self.left_panel,
            textvariable=self.key_var,
            bg="#1b1b1b",
            fg="white",
            insertbackground="white",
            relief="flat",
            font=("Consolas", 16)
        )
        entry.pack(anchor="nw", padx=28, pady=10, ipadx=220, ipady=8)

        bar = tk.Frame(self.left_panel, bg="#111111")
        bar.pack(anchor="nw", padx=28, pady=20)

        self.make_button(bar, "SUBMIT KEY", self.submit_fake_key).pack(side="left", padx=(0, 14))
        self.make_button(bar, "BACK", lambda: self.show_view("main")).pack(side="left")

    def submit_fake_key(self):
        entered = self.key_var.get().strip()
        if not entered:
            self.show_notice("No recovery key provided.")
        elif len(entered) < 8:
            self.show_notice("Invalid recovery key format.")
        else:
            self.show_notice("Recovery server unavailable.")
        self.key_var.set("")

    def show_notice(self, text, ms=2200):
        self.notice_var.set(text)
        self.notice.place(relx=0.5, rely=0.90, anchor="center")
        self.root.after(ms, lambda: self.notice.place_forget())

    def update_timer(self):
        remaining = self.deadline - datetime.now()
        if remaining.total_seconds() < 0:
            remaining = timedelta(0)

        total_seconds = int(remaining.total_seconds())
        hrs = total_seconds // 3600
        mins = (total_seconds % 3600) // 60
        secs = total_seconds % 60
        countdown = f"{hrs:02}:{mins:02}:{secs:02}"

        self.timer_value.config(text=countdown)

        if self.current_view == "main":
            self.files_value.config(text=str(self.fake_files))
            self.status_value.config(
                text="FRESH OUT OF THE OVEN" if self.flash else "DEMO MODE",
                fg="#00ff66" if self.flash else "white"
            )

        self.root.after(100, self.update_timer)

    def tick_files(self):
        self.fake_files += random.randint(0, 3)
        self.root.after(1500, self.tick_files)

    def blink(self):
        self.flash = not self.flash
        self.logo_label.config(fg="#ff3333" if self.flash else "#ff6666")
        self.timer_value.config(fg="white" if self.flash else "#ff4444")
        self.root.after(500, self.blink)

    def animate_background(self):
        self.canvas.delete("fx")
        w = self.root.winfo_width()
        h = self.root.winfo_height()

        for y in range(0, h, 4):
            self.canvas.create_line(0, y, w, y, fill="#120000", tags="fx")

        for _ in range(30):
            x1 = random.randint(0, max(1, w))
            y1 = random.randint(0, max(1, h))
            x2 = x1 + random.randint(2, 12)
            y2 = y1 + random.randint(1, 3)
            color = random.choice(["#180000", "#220000", "#2a0000"])
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color, tags="fx")

        self.root.after(50, self.animate_background)


def main():
    root = tk.Tk()
    TrainingRansomwareWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
