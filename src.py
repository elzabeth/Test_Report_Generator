from tkinter import *
from tkinter import filedialog

window = Tk()


def upload_action_document_a(event=None):
    filename = filedialog.askopenfilename(parent=window, title='Choose a file')
    document_a_file_name.set(filename)


def upload_action_document_b(event=None):
    filename = filedialog.askopenfilename(parent=window, title='Choose a file')
    document_b_file_name.set(filename)


system_type_label = Label(window,
                          text="SYSTEM TYPE : ",
                          foreground="white",  # Set the text color to white,
                          background="black",  # Set the bg color to black,
                          # width=10,
                          # height=10,
                          font=("Arial Bold", 10))
system_type_label.place(x=90, y=40)

# datatype of menu text
system_clicked = StringVar()
# initial menu text
system_clicked.set("HMI")
# Dropdown menu options
options = [
    "HMI",
    "ACU"
]
# Create Dropdown menu
system_type_drop = OptionMenu(window, system_clicked, *options)
system_type_drop.place(x=210, y=40)

############################################################################################

document_type_label = Label(window,
                            text="DOCUMENT TYPE : ",
                            foreground="white",  # Set the text color to white,
                            background="black",  # Set the bg color to black,
                            # width=10,
                            # height=10,
                            font=("Arial Bold", 10))
document_type_label.place(x=310, y=40)

# datatype of menu text
document_clicked = StringVar()
# initial menu text
document_clicked.set("Testcase")
# Dropdown menu options
options = [
    "Testcase",
    "Testreport"
]
# Create Dropdown menu
document_type_drop = OptionMenu(window, document_clicked, *options)
document_type_drop.place(x=460, y=40)

############################################################################################

document_a_label = Label(window,
                         text="DOCUMENT A : ",
                         foreground="white",  # Set the text color to white,
                         background="black",  # Set the bg color to black,
                         # width=10,
                         # height=10,
                         font=("Arial Bold", 10))
document_a_label.place(x=90, y=80)

document_a_file_name = StringVar(None)
document_a_text = Entry(window, textvariable=document_a_file_name)
document_a_text.grid(column=0, row=0, sticky='EW')
document_a_text.update()
document_a_text.focus_set()
# yourName.pack(padx=20, pady=20, anchor='n')
document_a_text.place(x=200, y=80, width=320, height=25)

document_a_browse = Button(window,
                           text="Browse",
                           foreground="black",  # Set the text color to white,
                           background="white",  # Set the bg color to black,
                           width=6,
                           height=1,
                           font=("Arial Bold", 10),
                           command=upload_action_document_a)
document_a_browse.place(x=530, y=80)

############################################################################################


document_b_label = Label(window,
                         text="DOCUMENT B : ",
                         foreground="white",  # Set the text color to white,
                         background="black",  # Set the bg color to black,
                         # width=10,
                         # height=10,
                         font=("Arial Bold", 10))
document_b_label.place(x=90, y=120)

document_b_file_name = StringVar(None)
document_b_text = Entry(window, textvariable=document_b_file_name)
document_b_text.grid(column=0, row=0, sticky='EW')
document_b_text.update()
document_b_text.focus_set()
# yourName.pack(padx=20, pady=20, anchor='n')
document_b_text.place(x=200, y=120, width=320, height=25)


document_b_browse = Button(window,
                           text="Browse",
                           foreground="black",  # Set the text color to white,
                           background="white",  # Set the bg color to black,
                           width=6,
                           height=1,
                           font=("Arial Bold", 10),
                           command=upload_action_document_b)
document_b_browse.place(x=530, y=120)

############################################################################################

btn = Button(window,
             text="UPLOAD",
             foreground="black",  # Set the text color to white,
             background="white",  # Set the bg color to black,
             width=15,
             height=1,
             font=("Arial Bold", 10))
btn.place(x=270, y=170)

############################################################################################

log_window_label = Label(window,
                         text="EXECUTION LOG : ",
                         foreground="white",  # Set the text color to white,
                         background="black",  # Set the bg color to black,
                         # width=10,
                         # height=10,
                         font=("Arial Bold", 10))
log_window_label.place(x=90, y=210)

# Create text widget and specify size.
log_window = Text(window, height=10, width=62)
log_window.place(x=90, y=250)
# # Insert The text
# log_window.insert(tk.END, Fact)

############################################################################################

window.title("TESTCASE/TESTREPORT DOCUMENT GENERATOR")
window.geometry('700x500')
window.configure(bg='black')
window.mainloop()
