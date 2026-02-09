import tkinter as tk

w = tk.Tk()
w.title("Simple GUI")

tk.Label(w, text="Username").grid(row=0, column=0)
tk.Label(w, text="Password").grid(row=1, column=0)

e1 = tk.Entry(w)
e2 = tk.Entry(w)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(w, text="Submit").grid(row=2, column=0)
tk.Button(w, text="Reset").grid(row=2, column=1)

w.mainloop()
