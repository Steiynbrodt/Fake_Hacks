import random
import tkinter as tk


class MuffinCartelDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("MUFFINCARTEL")
        self.root.configure(bg="black")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        self.canvas = tk.Canvas(
            root,
            bg="black",
            highlightthickness=0,
            bd=0
        )
        self.canvas.pack(fill="both", expand=True)

        self.banner = r"""
███╗   ███╗██╗   ██╗███████╗███████╗██╗███╗   ██╗ ██████╗ █████╗ ██████╗ ████████╗███████╗██╗     
████╗ ████║██║   ██║██╔════╝██╔════╝██║████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║     
██╔████╔██║██║   ██║█████╗  █████╗  ██║██╔██╗ ██║██║     ███████║██████╔╝   ██║   █████╗  ██║     
██║╚██╔╝██║██║   ██║██╔══╝  ██╔══╝  ██║██║╚██╗██║██║     ██╔══██║██╔══██╗   ██║   ██╔══╝  ██║     
██║ ╚═╝ ██║╚██████╔╝██║     ██║     ██║██║ ╚████║╚██████╗██║  ██║██║  ██║   ██║   ███████╗███████╗
╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝
"""

        self.progress_steps = [
            "[+] preheating tray...",
            "[+] mixing ingredients...",
            "[+] frosting session...",
            "[+] scattering crumbs...",
            "[+] baking system..."
        ]

        self.final_lines = [
            "",
            "Your system is fully baked.",
            "Fresh out of the oven.",
            "",
            "Think before you click.",
            "",
            "[ ESC to close ]"
        ]

        self.current_step = 0
        self.progress_value = 0
        self.show_final = False

        self.target_text = ""
        self.visible_text = ""
        self.type_index = 0
        self.cursor_on = True

        self.start_typing(self.progress_steps[0])

        self.root.after(30, self.render_loop)
        self.root.after(15, self.type_loop)
        self.root.after(500, self.cursor_loop)

    def start_typing(self, text: str) -> None:
        self.target_text = text
        self.visible_text = ""
        self.type_index = 0

    def type_loop(self) -> None:
        if self.type_index < len(self.target_text):
            self.visible_text += self.target_text[self.type_index]
            self.type_index += 1
        self.root.after(15, self.type_loop)

    def cursor_loop(self) -> None:
        self.cursor_on = not self.cursor_on
        self.root.after(500, self.cursor_loop)

    def render_loop(self) -> None:
        width = self.root.winfo_width()
        height = self.root.winfo_height()

        self.canvas.delete("all")

        self.draw_noise(width, height)
        self.draw_scanlines(width, height)
        self.draw_banner(width)

        if not self.show_final:
            self.update_progress()
            self.draw_progress_scene(width, height)
        else:
            self.draw_final_scene(width, height)

        self.root.after(33, self.render_loop)

    def update_progress(self) -> None:
        self.progress_value += 2
        if self.progress_value >= 100:
            self.progress_value = 0
            self.current_step += 1
            if self.current_step >= len(self.progress_steps):
                if not self.show_final:
                    self.show_final = True
                    self.start_typing("\n".join(self.final_lines))
            else:
                self.start_typing(self.progress_steps[self.current_step])

    def draw_noise(self, width: int, height: int) -> None:
        for _ in range(100):
            x1 = random.randint(0, max(1, width))
            y1 = random.randint(0, max(1, height))
            x2 = x1 + random.randint(2, 10)
            y2 = y1 + random.randint(1, 3)
            color = random.choice(["#003300", "#004d00", "#006600", "#00aa33"])
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

    def draw_scanlines(self, width: int, height: int) -> None:
        for y in range(0, height, 4):
            self.canvas.create_line(0, y, width, y, fill="#031a03")

    def draw_banner(self, width: int) -> None:
        self.canvas.create_text(
            width // 2,
            40,
            text=self.banner.strip(),
            fill="#00ff66",
            font=("Consolas", 10, "bold"),
            justify="center",
            anchor="n"
        )

    def draw_progress_scene(self, width: int, height: int) -> None:
        line = self.visible_text + ("_" if self.cursor_on else "")

        self.canvas.create_text(
            width // 2,
            height // 2 - 40,
            text=line,
            fill="#00ff66",
            font=("Consolas", 24, "bold"),
            justify="center"
        )

        bar_width = min(700, width - 200)
        bar_height = 28
        x1 = (width - bar_width) // 2
        y1 = height // 2 + 40
        x2 = x1 + bar_width
        y2 = y1 + bar_height

        self.canvas.create_rectangle(x1, y1, x2, y2, outline="#00ff66", width=2)

        fill_width = int((self.progress_value / 100) * (bar_width - 4))
        if fill_width > 0:
            self.canvas.create_rectangle(
                x1 + 2, y1 + 2, x1 + 2 + fill_width, y2 - 2,
                fill="#00aa33", outline=""
            )

        self.canvas.create_text(
            width // 2,
            y2 + 25,
            text=f"{self.progress_value}%",
            fill="#00ff66",
            font=("Consolas", 16)
        )

    def draw_final_scene(self, width: int, height: int) -> None:
        text = self.visible_text + ("_" if self.cursor_on else "")

        box_w = min(900, width - 200)
        box_h = 240
        x1 = (width - box_w) // 2
        y1 = height // 2 - box_h // 2
        x2 = x1 + box_w
        y2 = y1 + box_h

        self.canvas.create_rectangle(x1, y1, x2, y2, outline="#00ff66", width=2)
        self.canvas.create_text(
            width // 2,
            height // 2,
            text=text,
            fill="#00ff66",
            font=("Consolas", 24, "bold"),
            justify="center"
        )


def main() -> None:
    root = tk.Tk()
    MuffinCartelDemo(root)
    root.mainloop()


if __name__ == "__main__":
    main()
