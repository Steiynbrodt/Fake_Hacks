import tkinter as tk
from tkinter import messagebox
import random
import getpass
from datetime import datetime, timedelta


class LockerSim:
    def __init__(self, root):
        self.root = root
        self.root.title("Training Simulation")
        self.root.configure(bg="black")
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root.overrideredirect(True)
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        self.username = getpass.getuser()

        self.start_time = datetime.now()
        self.deadline = self.start_time + timedelta(hours=23, minutes=59, seconds=59)

        self.flash = False
        self.current_tab = "HOME"
        self.boot_mode = True

        self.fake_files = 1247
        self.fake_price = "0.0085 BTC"
        self.fake_wallet = "bc1q-muffin-cartel-demo-wallet-7x9p2fake"
        self.notice_var = tk.StringVar(value="")
        self.key_var = tk.StringVar()

        self.boot_lines = [
            "[+] Initializing operator session...",
            "[+] Loading locker interface modules...",
            "[+] Enumerating local file metadata...",
            "[+] Building payment portal...",
            "[+] Starting recovery services...",
            "[+] Finalizing UI state..."
        ]
        self.boot_progress = 0

        self.fake_file_names = [
            fr"C:\Users\{self.username}\Documents\payroll_2026.xlsx",
            fr"C:\Users\{self.username}\Pictures\family_trip.zip",
            fr"C:\Users\{self.username}\Desktop\passport_scan.pdf",
            fr"C:\Users\{self.username}\Work\contracts_final.docx",
            fr"C:\Users\{self.username}\Desktop\server_notes.txt",
            fr"C:\Users\{self.username}\Downloads\crypto_notes.txt",
            fr"C:\Users\{self.username}\Documents\budget_q4.xlsx",
            fr"C:\Users\{self.username}\Desktop\customer_export.db",
            fr"C:\Users\{self.username}\Pictures\wedding_video.mp4",
            fr"C:\Users\{self.username}\Desktop\private_keys_DO_NOT_DELETE.txt",
            fr"C:\Users\{self.username}\Documents\tax_return_2025.pdf",
            fr"C:\Users\{self.username}\Downloads\backup_important_2.zip",
        ]

        self.build_ui()
        self.show_boot()

        self.root.after(120, self.update_boot)
        self.root.after(500, self.blink)
        self.root.after(100, self.update_clock)
        self.root.after(1500, self.tick_files)
        self.root.after(60, self.animate_background)

    def build_ui(self):
        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0, bd=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        self.outer = tk.Frame(self.root, bg="black", highlightbackground="#cc0000", highlightthickness=3)
        self.outer.place(relx=0.03, rely=0.04, relwidth=0.94, relheight=0.92)

        self.header = tk.Frame(self.outer, bg="#050505", highlightbackground="#ff3333", highlightthickness=2)
        self.header.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.22)

        self.logo_shadow = tk.Label(
            self.header,
            text="MUFFIN\nCARTEL",
            bg="#050505",
            fg="#660000",
            font=("Consolas", 42, "bold"),
            justify="center"
        )
        self.logo_shadow.place(relx=0.503, rely=0.03, anchor="n")

        self.logo_label = tk.Label(
            self.header,
            text="MUFFIN\nCARTEL",
            bg="#050505",
            fg="#ff3333",
            font=("Consolas", 42, "bold"),
            justify="center"
        )
        self.logo_label.place(relx=0.5, rely=0.02, anchor="n")

        self.title_label = tk.Label(
            self.header,
            text="FILES LOCKED - TRAINING SIMULATION",
            bg="#050505",
            fg="white",
            font=("Arial", 20, "bold")
        )
        self.title_label.place(relx=0.5, rely=0.80, anchor="center")

        self.tabs_bar = tk.Frame(self.outer, bg="black")
        self.tabs_bar.place(relx=0.02, rely=0.27, relwidth=0.96, relheight=0.07)

        self.tab_buttons = {}
        for name in ["HOME", "INFO", "RECOVERY", "SUPPORT"]:
            btn = tk.Button(
                self.tabs_bar,
                text=name,
                command=lambda n=name: self.show_tab(n),
                bg="#990000",
                fg="white",
                activebackground="#bb1111",
                activeforeground="white",
                relief="flat",
                bd=0,
                font=("Arial", 13, "bold"),
                cursor="hand2",
                padx=18,
                pady=8
            )
            btn.pack(side="left", padx=(0, 12))
            self.tab_buttons[name] = btn

        self.body = tk.Frame(self.outer, bg="black")
        self.body.place(relx=0.02, rely=0.36, relwidth=0.96, relheight=0.52)

        self.left_panel = tk.Frame(self.body, bg="#111111", highlightbackground="#cc0000", highlightthickness=2)
        self.left_panel.place(relx=0.00, rely=0.00, relwidth=0.62, relheight=1.0)

        self.right_panel = tk.Frame(self.body, bg="#111111", highlightbackground="#cc0000", highlightthickness=2)
        self.right_panel.place(relx=0.66, rely=0.00, relwidth=0.34, relheight=1.0)

        self.footer = tk.Label(
            self.outer,
            text="MUFFINCARTEL training screen • educational simulation only • press ESC to close",
            bg="black",
            fg="#bbbbbb",
            font=("Consolas", 12)
        )
        self.footer.place(relx=0.5, rely=0.965, anchor="center")

        self.notice = tk.Label(
            self.outer,
            textvariable=self.notice_var,
            bg="#111111",
            fg="#ffddcc",
            font=("Consolas", 12, "bold"),
            highlightbackground="#ff4444",
            highlightthickness=2
        )

        self.build_right_panel()

    def build_right_panel(self):
        for child in self.right_panel.winfo_children():
            child.destroy()

        self.timer_title = tk.Label(
            self.right_panel,
            text="TIME REMAINING",
            bg="#111111",
            fg="#ff5555",
            font=("Arial", 20, "bold")
        )
        self.timer_title.pack(pady=(24, 6))

        self.timer_value = tk.Label(
            self.right_panel,
            text="00:00:00",
            bg="#111111",
            fg="#ff4444",
            font=("Consolas", 28, "bold")
        )
        self.timer_value.pack(pady=(0, 20))

        self.price_title = tk.Label(
            self.right_panel,
            text="RECOVERY AMOUNT",
            bg="#111111",
            fg="#ff5555",
            font=("Arial", 16, "bold")
        )
        self.price_title.pack()

        self.price_value = tk.Label(
            self.right_panel,
            text=self.fake_price,
            bg="#111111",
            fg="white",
            font=("Consolas", 22, "bold")
        )
        self.price_value.pack(pady=(4, 16))

        wallet_frame = tk.Frame(self.right_panel, bg="#111111")
        wallet_frame.pack(fill="x", padx=24, pady=(0, 14))

        tk.Label(
            wallet_frame,
            text="WALLET",
            bg="#111111",
            fg="#ff5555",
            font=("Arial", 14, "bold")
        ).pack(anchor="w")

        self.wallet_box = tk.Text(
            wallet_frame,
            height=3,
            bg="#1b1b1b",
            fg="white",
            relief="flat",
            bd=0,
            wrap="word",
            font=("Consolas", 11)
        )
        self.wallet_box.pack(fill="x", pady=(6, 8))
        self.wallet_box.insert("1.0", self.fake_wallet)
        self.wallet_box.config(state="disabled")

        self.copy_wallet_btn = self.make_button(wallet_frame, "COPY WALLET", self.copy_wallet, small=True)
        self.copy_wallet_btn.pack(anchor="w")

        self.decrypt_btn = self.make_button(self.right_panel, "DECRYPT SAMPLE FILE", self.decrypt_sample)
        self.decrypt_btn.pack(fill="x", padx=24, pady=(18, 10))

        self.status_btn = self.make_button(self.right_panel, "CHECK PAYMENT STATUS", self.check_payment_status)
        self.status_btn.pack(fill="x", padx=24, pady=10)

    def make_button(self, parent, text, command, small=False):
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
            font=("Arial", 11 if small else 13, "bold"),
            cursor="hand2",
            pady=6 if small else 9
        )
        btn.bind("<Enter>", lambda e: btn.configure(bg="#bb1111"))
        btn.bind("<Leave>", lambda e: btn.configure(bg="#990000"))
        return btn

    def copy_wallet(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.fake_wallet)
        self.show_notice("Wallet copied to clipboard.")

    def decrypt_sample(self):
        messagebox.showinfo(
            "Sample Decrypt",
            "sample_restored.txt\n\n"
            "This is a training simulation.\n"
            "Nothing was encrypted.\n"
            "This dialog exists to make the UI feel more believable."
        )

    def check_payment_status(self):
        self.show_notice("Payment gateway unavailable.")

    def clear_left_panel(self):
        for child in self.left_panel.winfo_children():
            child.destroy()

    def set_active_tab_style(self):
        for name, btn in self.tab_buttons.items():
            btn.config(bg="#cc1111" if name == self.current_tab else "#990000")

    def show_boot(self):
        self.clear_left_panel()
        self.current_tab = "HOME"
        self.set_active_tab_style()

        frame = tk.Frame(self.left_panel, bg="#111111")
        frame.pack(fill="both", expand=True, padx=26, pady=24)

        self.boot_title = tk.Label(
            frame,
            text="INITIALIZING SESSION",
            bg="#111111",
            fg="#ff6666",
            font=("Arial", 24, "bold"),
            anchor="w"
        )
        self.boot_title.pack(anchor="nw", pady=(0, 18))

        self.boot_text = tk.Label(
            frame,
            text="",
            bg="#111111",
            fg="white",
            justify="left",
            anchor="nw",
            font=("Consolas", 15),
            width=60,
            height=10
        )
        self.boot_text.pack(anchor="nw")

        self.boot_bar_outer = tk.Frame(frame, bg="#111111", highlightbackground="#ff4444", highlightthickness=2)
        self.boot_bar_outer.pack(anchor="nw", fill="x", pady=(16, 6))

        self.boot_bar_fill = tk.Frame(self.boot_bar_outer, bg="#aa0000")
        self.boot_bar_fill.place(x=0, y=0, relheight=1.0, relwidth=0.01)

        self.boot_pct = tk.Label(
            frame,
            text="0%",
            bg="#111111",
            fg="#ffaaaa",
            font=("Consolas", 13, "bold")
        )
        self.boot_pct.pack(anchor="nw")

    def update_boot(self):
        if not self.boot_mode:
            return

        self.boot_progress = min(100, self.boot_progress + random.randint(4, 9))
        lines = min(len(self.boot_lines), max(1, self.boot_progress // 18))
        self.boot_text.config(text="\n".join(self.boot_lines[:lines]))
        self.boot_pct.config(text=f"{self.boot_progress}%")
        self.boot_bar_fill.place(relwidth=max(0.01, self.boot_progress / 100.0))

        if self.boot_progress >= 100:
            self.boot_mode = False
            self.show_tab("HOME")
            return

        self.root.after(140, self.update_boot)

    def show_tab(self, tab):
        self.current_tab = tab
        self.set_active_tab_style()
        self.clear_left_panel()

        if tab == "HOME":
            self.build_home_tab()
        elif tab == "INFO":
            self.build_info_tab()
        elif tab == "RECOVERY":
            self.build_recovery_tab()
        elif tab == "SUPPORT":
            self.build_support_tab()

    def build_home_tab(self):
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

        lbl = tk.Label(
            self.left_panel,
            text=body,
            bg="#111111",
            fg="white",
            justify="left",
            anchor="nw",
            font=("Consolas", 15),
            wraplength=760
        )
        lbl.pack(anchor="nw", padx=26, pady=(24, 18))

        info = tk.Label(
            self.left_panel,
            text="Use the tabs above to view file information, test recovery actions, and open the support panel.",
            bg="#111111",
            fg="#ffb3b3",
            justify="left",
            anchor="nw",
            font=("Consolas", 13),
            wraplength=760
        )
        info.pack(anchor="nw", padx=26)

    def build_info_tab(self):
        container = tk.Frame(self.left_panel, bg="#111111")
        container.pack(fill="both", expand=True, padx=24, pady=20)

        top = tk.Frame(container, bg="#111111")
        top.pack(fill="x", pady=(0, 14))

        self.info_files_value = self.metric(top, "AFFECTED FILES", str(self.fake_files), 0)
        self.info_price_value = self.metric(top, "RECOVERY AMOUNT", self.fake_price, 1)
        self.info_state_value = self.metric(top, "STATE", "DEMO MODE", 2)

        bottom = tk.Frame(container, bg="#111111")
        bottom.pack(fill="both", expand=True)

        box = tk.Frame(bottom, bg="#0d0d0d", highlightbackground="#ff3333", highlightthickness=1)
        box.pack(fill="both", expand=True)

        tk.Label(
            box,
            text="FILE INDEX",
            bg="#0d0d0d",
            fg="#ff6666",
            font=("Arial", 16, "bold")
        ).pack(anchor="w", padx=12, pady=(10, 6))

        self.file_listbox = tk.Listbox(
            box,
            bg="#0d0d0d",
            fg="white",
            selectbackground="#550000",
            selectforeground="white",
            relief="flat",
            bd=0,
            highlightthickness=0,
            font=("Consolas", 12)
        )
        self.file_listbox.pack(side="left", fill="both", expand=True, padx=(12, 0), pady=(0, 12))

        scroll = tk.Scrollbar(box, command=self.file_listbox.yview)
        scroll.pack(side="right", fill="y", padx=(0, 12), pady=(0, 12))
        self.file_listbox.config(yscrollcommand=scroll.set)

        self.refresh_file_list()

    def metric(self, parent, title, value, col):
        frame = tk.Frame(parent, bg="#111111", highlightbackground="#ff3333", highlightthickness=1)
        frame.grid(row=0, column=col, sticky="nsew", padx=(0 if col == 0 else 12, 0))
        parent.grid_columnconfigure(col, weight=1)

        tk.Label(
            frame,
            text=title,
            bg="#111111",
            fg="#ff5555",
            font=("Arial", 12, "bold")
        ).pack(anchor="w", padx=12, pady=(10, 4))

        val = tk.Label(
            frame,
            text=value,
            bg="#111111",
            fg="white",
            font=("Consolas", 18, "bold")
        )
        val.pack(anchor="w", padx=12, pady=(0, 10))
        return val

    def refresh_file_list(self):
        if hasattr(self, "file_listbox") and self.file_listbox.winfo_exists():
            self.file_listbox.delete(0, tk.END)
            items = random.sample(self.fake_file_names, k=min(len(self.fake_file_names), 10))
            for name in items:
                self.file_listbox.insert(tk.END, f"[LOCKED] {name}")

    def build_recovery_tab(self):
        title = tk.Label(
            self.left_panel,
            text="RECOVERY PANEL",
            bg="#111111",
            fg="#ff6666",
            font=("Arial", 22, "bold")
        )
        title.pack(anchor="nw", padx=26, pady=(24, 12))

        body = tk.Label(
            self.left_panel,
            text=(
                "Enter your recovery key below.\n\n"
                "This is fake.\n"
                "No recovery is needed because nothing was encrypted.\n"
                "This tab exists to make the interface feel complete."
            ),
            bg="#111111",
            fg="white",
            justify="left",
            anchor="nw",
            font=("Consolas", 15),
            wraplength=760
        )
        body.pack(anchor="nw", padx=26, pady=(0, 18))

        entry = tk.Entry(
            self.left_panel,
            textvariable=self.key_var,
            bg="#1b1b1b",
            fg="white",
            insertbackground="white",
            relief="flat",
            font=("Consolas", 15)
        )
        entry.pack(anchor="nw", padx=26, pady=8, ipadx=220, ipady=8)

        row = tk.Frame(self.left_panel, bg="#111111")
        row.pack(anchor="nw", padx=26, pady=18)

        self.make_button(row, "SUBMIT KEY", self.submit_fake_key).pack(side="left", padx=(0, 12))
        self.make_button(row, "DECRYPT SAMPLE", self.decrypt_sample).pack(side="left")

    def build_support_tab(self):
        title = tk.Label(
            self.left_panel,
            text="SUPPORT",
            bg="#111111",
            fg="#ff6666",
            font=("Arial", 22, "bold")
        )
        title.pack(anchor="nw", padx=26, pady=(24, 12))

        transcript = (
            "[12:41] session opened\n"
            "[12:41] operator unavailable\n"
            "[12:42] payment verification delayed\n"
            "[12:42] retry later\n\n"
            "This panel is decorative.\n"
            "It exists because fake support channels make scare UIs feel more real."
        )

        tk.Label(
            self.left_panel,
            text=transcript,
            bg="#111111",
            fg="white",
            justify="left",
            anchor="nw",
            font=("Consolas", 14),
            wraplength=760
        ).pack(anchor="nw", padx=26, pady=(0, 18))

        row = tk.Frame(self.left_panel, bg="#111111")
        row.pack(anchor="nw", padx=26)

        self.make_button(row, "OPEN CHAT", lambda: self.show_notice("No agents available.")).pack(side="left", padx=(0, 12))
        self.make_button(row, "REFRESH", lambda: self.show_notice("Support status unchanged.")).pack(side="left")

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
        self.notice.place(relx=0.5, rely=0.91, anchor="center")
        self.root.after(ms, lambda: self.notice.place_forget())

    def update_clock(self):
        remaining = self.deadline - datetime.now()
        if remaining.total_seconds() < 0:
            remaining = timedelta(0)

        total_seconds = int(remaining.total_seconds())
        hrs = total_seconds // 3600
        mins = (total_seconds % 3600) // 60
        secs = total_seconds % 60
        self.timer_value.config(text=f"{hrs:02}:{mins:02}:{secs:02}")

        if hasattr(self, "info_files_value") and self.info_files_value.winfo_exists():
            self.info_files_value.config(text=str(self.fake_files))

        if hasattr(self, "info_state_value") and self.info_state_value.winfo_exists():
            self.info_state_value.config(
                text="FRESH OUT OF THE OVEN" if self.flash else "DEMO MODE",
                fg="#00ff66" if self.flash else "white"
            )

        self.root.after(100, self.update_clock)

    def tick_files(self):
        self.fake_files += random.randint(0, 3)
        if random.random() < 0.35:
            self.refresh_file_list()
        self.root.after(1500, self.tick_files)

    def blink(self):
        self.flash = not self.flash
        self.logo_label.config(fg="#ff2222" if self.flash else "#ff5555")
        self.logo_shadow.config(fg="#440000" if self.flash else "#660000")
        self.timer_value.config(fg="white" if self.flash else "#ff4444")
        self.root.after(500, self.blink)

    def animate_background(self):
        self.canvas.delete("fx")
        w = self.root.winfo_width()
        h = self.root.winfo_height()

        for y in range(0, h, 4):
            self.canvas.create_line(0, y, w, y, fill="#120000", tags="fx")

        for _ in range(28):
            x1 = random.randint(0, max(1, w))
            y1 = random.randint(0, max(1, h))
            x2 = x1 + random.randint(2, 12)
            y2 = y1 + random.randint(1, 3)
            color = random.choice(["#180000", "#220000", "#2a0000"])
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color, tags="fx")

        self.root.after(60, self.animate_background)


def main():
    root = tk.Tk()
    LockerSim(root)
    root.mainloop()


if __name__ == "__main__":
    main()
