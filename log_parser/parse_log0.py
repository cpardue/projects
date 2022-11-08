import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Entry
from tkinter import Tk, Text
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.constants import *
import os.path

'''
dark mode colors
background     = #181818
button color   = #212121
hover color    = #3D3D3D
primary text   = #FFFFFF
secondary text = #AAAAAA
'''

# start tkinter window loop
root = tk.Tk()
root.resizable(True, True)
root.title("Log Search")

# actual tkinter gui canvas
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=6)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(5, weight=1) # see https://tkdocs.com/tutorial/grid.html for more info on Grid

# header
header = tk.Label(root, text="Log Search", font=("Roboto", 25))
header.grid(columnspan=2, rowspan=2, column=0, row=0)


def open_file():
    print("open_file() was opened")
    global file
    global filepath
    upload_text.set("Uploading...")
    file = askopenfile(parent=root, mode='r', title="Choose a logfile")
    if file:
        upload_text.set("Upload Logfile")
        filepath = os.path.abspath(file.name)
        filename = os.path.basename(file.name)
        print("Selected " + filename)
    file.close()
    filename_text = tk.Label(root, text="    " + filename + "    ", font=("Roboto", 9))
    filename_text.grid(column=2, row=1, sticky="n")
    print("open_file() was closed")

def search_file(search_term):
    search_text.set("Searching...")
    print("search_file() was opened")
    print("search term was: " + search_term.get())
    with open(str(filepath), "r") as f:
        with open("search_results.txt", "w") as results:
            count = 1
            for line in f:
                if search_term.get() in line:
                    count += 1
                    results.write(line)
        results.close()
    f.close()
    search_text.set("Search")
    scrollbar = tk.Scrollbar(root, orient="vertical")
    scrollbar.grid(column=3, row=5, sticky="ns")
    results = Text(root, height=20, yscrollcommand=scrollbar.set)
    results.grid(columnspan=3, row=5, padx=15, pady=15, sticky="sew")
    results.columnconfigure(0, weight=2)
    results.columnconfigure(1, weight=2)
    results.columnconfigure(3, weight=2)
    results.rowconfigure(5, weight=2)
    search_results = open("search_results.txt", "r")
    results_text = search_results.read()
    results.insert("1.0", results_text)
    # save as button
    save_text = tk.StringVar()
    save_btn = tk.Button(root, textvariable=save_text, command=lambda:save_as(), font="Roboto")
    save_text.set("Save As...")
    save_btn.grid(column=2, row=6, sticky="nw")
    # end save as button stuff
    search_results.close()
    line_count = tk.Label(root, text=str(count) + " lines matched.")
    line_count.grid(column=0, row=6, sticky="sw")
    print("search_file() was closed")

def save_as():
    save_filetypes = [("All Files", "*.*"), ("Text Document", "*.txt")]
    output_file = asksaveasfile(filetypes=save_filetypes)
    if output_file:
        output_filepath = os.path.abspath(output_file.name)
        print(output_filepath + " is output_file_path")
        print(filepath + " is the old global filepath")
        with open(str(output_filepath), "w") as ofp:
            with open("search_results.txt", "r") as sr:
                for line in sr:
                    ofp.write(line)
                    print("wrote a line to sr")
                ofp.close()
            sr.close()

def exit():
    root.destroy()


# upload log_file button
upload_text = tk.StringVar()
upload_btn = tk.Button(root, textvariable=upload_text, command=lambda:open_file(), font="Roboto")
upload_text.set("Upload Logfile")
upload_btn.grid(column=2, row=0, sticky="s")

# instructions
instructions = tk.Label(root, text="Enter a Keyword to search for", font="Roboto")
instructions.grid(columnspan=3, column=0, row=2, sticky="s")

# search term box
search_term = tk.StringVar(root)
search_term.set("")
textbox_entry = tk.Entry(root, textvariable=search_term, width=55, font="Roboto")
textbox_entry.grid(columnspan=3, column=0, row=3, padx=15, pady=15)
textbox_entry.focus()

# search button
search_text = tk.StringVar()
search_btn = tk.Button(root, textvariable=search_text, command=lambda:search_file(search_term), font="Roboto")
search_text.set("Search")
search_btn.grid(columnspan=3, column=0, row=4, sticky="n")

# quit button
exit_btn = tk.Button(root, text="Exit", command=lambda:exit(), font="Roboto")
exit_btn.grid(column=1, row=6, sticky="ne")

# end of tkinter window loop
root.mainloop()