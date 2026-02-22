import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("320x450")
root.configure(bg="#1e1e1e")

current_player = "X"
buttons = []

def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        buttons[row][col].config(
            fg="#00e676" if current_player == "X" else "#ff5252"
        )
        if check_winner():
            label.config(text=f"Ganó {current_player}", fg="#ffd600")
            disable_buttons()
        else:
            current_player = "O" if current_player == "X" else "X"
            label.config(text=f"Turno: {current_player}")

def disable_buttons():
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")

def reset_game():
    global current_player
    current_player = "X"
    label.config(text="Turno: X", fg="white")
    for row in buttons:
        for btn in row:
            btn.config(text="", state="normal", fg="white")

label = tk.Label(
    root,
    text="Turno: X",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="white"
)
label.pack(pady=15)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

for r in range(3):
    row = []
    for c in range(3):
        btn = tk.Button(
            frame,
            text="",
            width=6,
            height=3,
            font=("Arial", 20, "bold"),
            bg="#2d2d2d",
            fg="white",
            command=lambda r=r, c=c: on_click(r, c)
        )
        btn.grid(row=r, column=c, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

reset_button = tk.Button(
    root,
    text="Reiniciar Juego",
    font=("Arial", 14, "bold"),
    bg="#1976d2",
    fg="white",
    command=reset_game
)
reset_button.pack(pady=20)

root.mainloop()