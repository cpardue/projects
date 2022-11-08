import tkinter as tk
from tkinter import Text
from tkinter.filedialog import askopenfile, asksaveasfile
import os.path


# start tkinter window loop
root = tk.Tk()
root.resizable(True, True)
root.title("Log Search")
root.configure(bg="#181818")

# actual tkinter gui canvas
canvas = tk.Canvas(root, width=600, height=300)
canvas.configure(bg="#181818", highlightbackground="#181818")
canvas.grid(columnspan=3, rowspan=6)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(5, weight=1)

# header
top_header = tk.Label(root, text="Log Search", font=("Roboto", 25), bg="#181818", fg="#AAAAAA")
top_header.grid(columnspan=2, rowspan=2, column=0, row=0, sticky="nw")
bottom_header = tk.Label(root, text="github.com/cpardue", font=("Roboto", 8), bg="#181818", fg="#AAAAAA")
bottom_header.grid(column=0, row=2, sticky="nw")


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
    filename_text = tk.Label(root, text="    " + filename + "    ", font=("Roboto", 9), bg="#181818", fg="#AAAAAA")
    filename_text.grid(column=2, row=1, sticky="n")
    print("open_file() was closed")


def search_file(search_term):
    try:
        search_text.set("Search")
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
        scrollbar = tk.Scrollbar(root, orient="vertical")
        scrollbar.grid(column=3, row=5, sticky="nsw")
        results = Text(root, height=20, yscrollcommand=scrollbar.set)
        results.grid(columnspan=3, row=5, padx=15, pady=15, sticky="nsew")
        results.columnconfigure(0, weight=2)
        results.columnconfigure(1, weight=2)
        results.columnconfigure(3, weight=2)
        results.rowconfigure(5, weight=2)
        search_results = open("search_results.txt", "r")
        results_text = search_results.read()
        results.insert("1.0", results_text)
        # save as button
        save_text = tk.StringVar()
        save_btn = tk.Button(root, textvariable=save_text, command=lambda: save_as(),
                             font="Roboto", bg="#212121", fg="#FFFFFF")
        save_text.set("Save As...")
        save_btn.grid(column=2, row=6, sticky="nw")
        # end save as button stuff
        search_results.close()
        line_count = tk.Label(root, text=str(count) + " lines matched.    ", bg="#181818", fg="#AAAAAA")
        line_count.grid(column=0, row=6, sticky="sw")
        print("search_file() was closed")
    except NameError:
        print("!!! NameError !!!")
        pass
    except UnicodeDecodeError:
        print("!!! UnicodeDecodeError !!!")
        pass


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


def exit_app():
    root.destroy()


# upload log_file button
upload_text = tk.StringVar()
upload_btn = tk.Button(root, textvariable=upload_text, command=lambda: open_file(),
                       font="Roboto", bg="#212121", fg="#FFFFFF")
upload_text.set("Upload Logfile")
upload_btn.grid(column=2, row=0, sticky="s")

# instructions
instructions = tk.Label(root, text="Enter a Keyword to search for", font="Roboto", bg="#181818", fg="#AAAAAA")
instructions.grid(columnspan=3, column=0, row=2, sticky="s")

# search term box
search_term = tk.StringVar(root)
search_term.set("")
textbox_entry = tk.Entry(root, textvariable=search_term, width=55, font="Roboto", bg="#3D3D3D", fg="#FFFFFF")
textbox_entry.grid(columnspan=3, column=0, row=3, padx=5, pady=5)
textbox_entry.focus()

# search button
search_text = tk.StringVar()
search_btn = tk.Button(root, textvariable=search_text, command=lambda: search_file(search_term),
                       font="Roboto", bg="#212121", fg="#FFFFFF")
search_text.set("Search")
search_btn.grid(columnspan=3, column=0, row=4, sticky="n")

# exit button
exit_btn = tk.Button(root, text="Exit", command=lambda: exit_app(), font="Roboto", bg="#212121", fg="#AAAAAA")
exit_btn.grid(column=1, row=6, sticky="ne")

# end of tkinter window loop
root.mainloop()
