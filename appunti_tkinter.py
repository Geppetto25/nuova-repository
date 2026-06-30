    ### APPUNTI TKINTER ###

from tkinter import*
from tkinter import ttk
root.mainloop()

    ###    ROOT    ###

root = Tk()

root.title("il nostro programma")

root.geometry("600x400+50+50")

root.iconbitmap("icon.ico") #flaticon.com convertio.com thenounproject.com

root.resizable(False, False)
root.minsize(300, 200)
root.maxsize(800, 600)

root.attributes("-alpha", 0.5) #trasparenza

root.attributes("-topmost", 1) #sempre in primo piano

root.lift() #porta la finestra in primo piano

root.lower() #porta la finestra in secondo piano

    ###    LABEL    ###

photo = PhotoImage(file="python.png")
photo = photo.subsample(10, 10) # Riduci la dimensione dell'immagine


label  = Label(text="ciao", background="#305554", padx=50, pady=50, foreground="white", font="Arial 20 bold", cursor="pirate", justify="right", immage=None, compound="bottom")

label.pack()

    ###    BUTTON    ###

def saluta():
    print("Ciao, benvenuto nel mio programma!")

photo = PhotoImage(file="python.png")

button = ttk.Button(text="cliccami", background="red", foreground="blue", width=20, borderwidth=3, command=lambda: root.quuit(), image=photo)
button.state(["disabled"]) #disabilita il pulsante

button = Button(text="cliccami", background="red", foreground="blue", width=20, borderwidth=3, command=lambda: root.quit())
button["state"] = "disabled" #disabilita il pulsante

button.pack()

    ###    CHECKBOX    ###

def premo_check():
    print(valoreCheck.get())


valoreCheck = BooleanVar()
check = Checkbutton(text="ciao", font="Helvetica 15", command=premo_check, variable=valoreCheck, onvalue=True, offvalue=False)
check.pack()

    ###    RADIOBUTTON    ###

genere = StringVar()
r1 = ttk.Radiobutton(text="Maschio", variable=genere, value="m")
r2 = ttk.Radiobutton(text="Femmina", variable=genere, value="f")
r1.pack()
r2.pack()

    ###    ENTRY    ###

label_email = ttk.Label(text="Email")
label_email.pack()


email = StringVar()
entry_email = ttk.Entry(root, textvariable=email, show="*")
entry_email.pack()
#email.set("Inserisci la tua email")
entry_email.focus()

    ###    FRAME    ###

frame1 = Frame(root, width=200, height=100, background="red", padx=10, pady=50)
frame1.pack()#fill=BOTH, expand=True)# X Y BOTH

button1 = ttk.Button(frame1, text="Ciao")
button1.pack()

    ###   COMBOBOX    ###

mese_selezionato = StringVar()
combobox = ttk.Combobox(root, textvariable=mese_selezionato)
combobox['values'] = ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]
combobox.pack(fill=X, padx=10, pady=10)
combobox['state'] = "readonly"
combobox.bind("<<ComboboxSelected>>", lambda e: print("Hai selezionato:", mese_selezionato.get()))


    ###    SCROLLBAR    ###

from tkinter import scrolledtext

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


linguaggi = ('javascript', 'python', 'java', 'c++', 'c#', 'ruby', 'go', 'swift', 'kotlin', 'php')

linguaggio_selezionato = StringVar(value=linguaggi)
listbox = Listbox(root, listvariable=linguaggio_selezionato, height=6, selectmode="extended")
listbox.grid(row=0, column=0, sticky="nwes")

scrollbar = ttk.Scrollbar(root, orient="vertical", command=listbox.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

listbox.config(yscrollcommand=scrollbar.set)

scrolledtext = scrolledtext.ScrolledText(root, width=40, height=10)
scrolledtext.pack(fill=BOTH, side=LEFT, expand=True)
























import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser

def on_button_click():
    messagebox.showinfo("Info", "Hai cliccato il pulsante!")

def on_check():
    print("Checkbutton:", check_var.get())

def on_radio():
    print("Radiobutton:", radio_var.get())

def on_scale(val):
    print("Scale:", val)

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        color_label.config(text=f"Colore scelto: {color}", bg=color)

def open_file():
    file = filedialog.askopenfilename()
    if file:
        file_label.config(text=f"Hai scelto: {file}")

def add_to_list():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)

# Finestra principale
root = tk.Tk()
root.title("Tkinter Playground")
root.geometry("600x600")

# Label
label = tk.Label(root, text="Benvenuto nel Tkinter Playground!", font=("Arial", 16))
label.pack(pady=10)

# Button
button = tk.Button(root, text="Cliccami", command=on_button_click)
button.pack(pady=5)

# Entry
entry = tk.Entry(root)
entry.pack(pady=5)

# Listbox
listbox = tk.Listbox(root, height=5)
listbox.pack(pady=5)

add_button = tk.Button(root, text="Aggiungi alla lista", command=add_to_list)
add_button.pack(pady=5)

# Checkbutton
check_var = tk.BooleanVar()
check = tk.Checkbutton(root, text="Opzione", variable=check_var, command=on_check)
check.pack(pady=5)

# Radiobutton
radio_var = tk.StringVar(value="A")
radio_frame = tk.Frame(root)
radio_frame.pack(pady=5)

tk.Radiobutton(radio_frame, text="Opzione A", variable=radio_var, value="A", command=on_radio).pack(side="left")
tk.Radiobutton(radio_frame, text="Opzione B", variable=radio_var, value="B", command=on_radio).pack(side="left")

# Scale
scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=on_scale)
scale.pack(pady=5)

# Combobox (ttk)
combo = ttk.Combobox(root, values=["Python", "Java", "C++", "JavaScript"])
combo.set("Scegli un linguaggio")
combo.pack(pady=5)

# Color chooser
color_button = tk.Button(root, text="Scegli un colore", command=choose_color)
color_button.pack(pady=5)

color_label = tk.Label(root, text="Nessun colore scelto")
color_label.pack(pady=5)

# File dialog
file_button = tk.Button(root, text="Apri file", command=open_file)
file_button.pack(pady=5)

file_label = tk.Label(root, text="Nessun file selezionato")
file_label.pack(pady=5)

# Text widget
text = tk.Text(root, height=5)
text.pack(pady=5)
text.insert(tk.END, "Scrivi qualcosa qui...")

# Canvas
canvas = tk.Canvas(root, width=200, height=100, bg="lightgray")
canvas.pack(pady=10)
canvas.create_rectangle(20, 20, 180, 80, fill="blue")

# Start
root.mainloop()



#Widget	Funzione
#Label	Testo statico
#Button	Pulsante cliccabile
#Entry	Input a riga singola
#Listbox	Lista di elementi
#Checkbutton	Checkbox
#Radiobutton	Scelta singola
#Scale	Slider
#Combobox	Menu a tendina
#Text	Area di testo
#Canvas	Disegni e grafica
#filedialog	Aprire file
#colorchooser	Scegliere colori
#messagebox	Popup informativi
