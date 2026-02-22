import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x350")

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
        if check_winner():
            label.config(text=f"Ganó {current_player}")
        else:
            current_player = "O" if current_player == "X" else "X"

label = tk.Label(root, text="Turno: X")
label.pack()

frame = tk.Frame(root)
frame.pack()

for r in range(3):
    row = []
    for c in range(3):
        btn = tk.Button(frame, text="", width=5, height=2,
                        command=lambda r=r, c=c: on_click(r, c))
        btn.grid(row=r, column=c)
        row.append(btn)
    buttons.append(row)

root.mainloop()