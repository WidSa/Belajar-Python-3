# GUI(Graphical User Interface)

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
app = tk.Tk()
app.configure(bg="white")
app.geometry("300x200")
app.resizable(False,False)
app.title("Program Test")

# Veriabel
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

# Function tombol 
def tombol_clik():
    pesan = f"Hallo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
    showinfo(title="Sapa",message=pesan)

# Frame Input
input_frame = ttk.Frame(app)
# Penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# Komponen-komponen
# 1. Label Nama Depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan")
nama_depan_label.pack(padx=5,fill="x",expand=True)

# 2. Entry Nama Depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=5,fill="x",expand=True)

# 3. Label Nama Belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama belakang")
nama_belakang_label.pack(padx=5,fill="x",expand=True)

# 4. Entry Nama Belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=5,fill="x",expand=True)

# 5.Tombol
Submit_button = ttk.Button(input_frame,text="Submit",command=tombol_clik)
Submit_button.pack(fill='x',expand=True,padx=5,pady=5)


app.mainloop()
