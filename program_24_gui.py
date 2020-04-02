import Tkinter as tk

window = tk.Tk()

textBox = tk.Entry(window)
textBox.pack()

def saveText():
    getText = textBox.get()
    file_object = open("user-text.txt","w")
    file_object.write(getText)
    file_object.close()

button = tk.Button(window, text = "Save", command = saveText)
button.pack()

window.mainloop()
