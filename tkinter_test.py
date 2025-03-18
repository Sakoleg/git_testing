import tkinter as tk

root = tk.Tk()
root.title("Tkinter Test by Sakoleg")
root.geometry("500x300")


def change_text():
    label.config(text="Больше не нажимай")


button = tk.Button(root, height=3, text="Кнопка", command=change_text, width=10, bg="cyan", fg="green",
                   font=("Arial", 24, "bold"))
button.pack(pady=10)

label = tk.Label(root, text="Нажми кнопку")
label.pack(pady=10)

close_button = tk.Button(root, text="EXIT", command=root.quit, fg="red")
close_button.pack(pady=10)

root.mainloop()
