from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import win32print
import win32api

root = Tk()
root.title('Word Processor Made by Dovg / tututuana')
root.geometry("1200x710")


global open_status_name
open_status_name = False

global selected
selected = False

def new_file():
	# Delete previous text
	my_text.delete("1.0", END)
	# Update status bars
	root.title('New File')
	status_bar.config(text="New File        ")

	global open_status_name
	open_status_name = False

def open_file():
	my_text.delete("1.0", END)

	text_file = filedialog.askopenfilename(initialdir="C:/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
	
	if text_file:
		global open_status_name
		open_status_name = text_file

	# Update Status bars
	name = text_file
	status_bar.config(text=f'{name}        ')
	name = name.replace("C:/", "")
	root.title(f'{name}')

	text_file = open(text_file, 'r')
	stuff = text_file.read()
	my_text.insert(END, stuff)
	text_file.close()

def save_as_file():
	text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
	if text_file:
		name = text_file
		status_bar.config(text=f'Saved: {name}        ')
		name = name.replace("C:/", "")
		root.title(f'{name} - TextPad!')

		text_file = open(text_file, 'w')
		text_file.write(my_text.get(1.0, END))
		text_file.close()

def save_file():
	global open_status_name
	if open_status_name:
		text_file = open(open_status_name, 'w')
		text_file.write(my_text.get(1.0, END))
		text_file.close()
		status_bar.config(text=f'Saved: {open_status_name}        ')
		name = open_status_name
		name = name.replace("C:/", "")
		root.title(f'{name}')
	else:
		save_as_file()

def cut_text(e):
	global selected
	if e:
		selected = root.clipboard_get()
	else:
		if my_text.selection_get():
			selected = my_text.selection_get()
			my_text.delete("sel.first", "sel.last")
			root.clipboard_clear()
			root.clipboard_append(selected)

def copy_text(e):
	global selected
	if e:
		selected = root.clipboard_get()

	if my_text.selection_get():
		selected = my_text.selection_get()
		root.clipboard_clear()
		root.clipboard_append(selected)

def paste_text(e):
	global selected
	if e:
		selected = root.clipboard_get()
	else:
		if selected:
			position = my_text.index(INSERT)
			my_text.insert(position, selected)

def bold_it():
	bold_font = font.Font(my_text, my_text.cget("font"))
	bold_font.configure(weight="bold")

	my_text.tag_configure("bold", font=bold_font)

	current_tags = my_text.tag_names("sel.first")

	if "bold" in current_tags:
		my_text.tag_remove("bold", "sel.first", "sel.last")
	else:
		my_text.tag_add("bold", "sel.first", "sel.last")

def italics_it():
	italics_font = font.Font(my_text, my_text.cget("font"))
	italics_font.configure(slant="italic")

	my_text.tag_configure("italic", font=italics_font)

	current_tags = my_text.tag_names("sel.first")

	if "italic" in current_tags:
		my_text.tag_remove("italic", "sel.first", "sel.last")
	else:
		my_text.tag_add("italic", "sel.first", "sel.last")

def text_color():
	my_color = colorchooser.askcolor()[1]
	if my_color:
		color_font = font.Font(my_text, my_text.cget("font"))

		my_text.tag_configure("colored", font=color_font, foreground=my_color)

		current_tags = my_text.tag_names("sel.first")

		if "colored" in current_tags:
			my_text.tag_remove("colored", "sel.first", "sel.last")
		else:
			my_text.tag_add("colored", "sel.first", "sel.last")

def bg_color():
	my_color = colorchooser.askcolor()[1]
	if my_color:
		my_text.config(bg=my_color)

def all_text_color():
	my_color = colorchooser.askcolor()[1]
	if my_color:
		my_text.config(fg=my_color)

def print_file():
	#printer_name = win32print.GetDefaultPrinter()
	#status_bar.config(text=printer_name)
	
	file_to_print = filedialog.askopenfilename(initialdir="C:/", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))

	if file_to_print:
		# Print the file
		win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)

def select_all(e):
	my_text.tag_add('sel', '1.0', 'end')

def clear_all():
	my_text.delete(1.0, END)

# Turn on Night Mode
def night_on():
	main_color = "#000000"
	second_color = "#373737"
	text_color = "green"

	root.config(bg=main_color)
	status_bar.config(bg=main_color, fg=text_color)
	my_text.config(bg=second_color)
	toolbar_frame.config(bg=main_color)
	# toolbar buttons
	bold_button.config(bg=second_color)
	italics_button.config(bg=second_color)
	redo_button.config(bg=second_color)
	undo_button.config(bg=second_color)
	color_text_button.config(bg=second_color)
	# file menu colors
	file_menu.config(bg=main_color, fg=text_color)
	edit_menu.config(bg=main_color, fg=text_color)
	color_menu.config(bg=main_color, fg=text_color)
	options_menu.config(bg=main_color, fg=text_color)


# Turn Off Night Mode:
def night_off():
	main_color = "SystemButtonFace"
	second_color = "SystemButtonFace"
	text_color = "black"

	root.config(bg=main_color)
	status_bar.config(bg=main_color, fg=text_color)
	my_text.config(bg="white")
	toolbar_frame.config(bg=main_color)
	# toolbar buttons
	bold_button.config(bg=second_color)
	italics_button.config(bg=second_color)
	redo_button.config(bg=second_color)
	undo_button.config(bg=second_color)
	color_text_button.config(bg=second_color)
	# file menu colors
	file_menu.config(bg=main_color, fg=text_color)
	edit_menu.config(bg=main_color, fg=text_color)
	color_menu.config(bg=main_color, fg=text_color)
	options_menu.config(bg=main_color, fg=text_color)





toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

my_frame = Frame(root)
my_frame.pack(pady=5)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)

my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)
my_text.pack()

text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As...", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Print File", command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy", command=lambda: copy_text(False), accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste             ", command=lambda: paste_text(False), accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="(Ctrl+y)")
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=lambda: select_all(True), accelerator="(Ctrl+a)")
edit_menu.add_command(label="Clear", command=clear_all)

# Add Color Menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Selected Text", command=text_color)
color_menu.add_command(label="All Text", command=all_text_color)
color_menu.add_command(label="Background", command=bg_color)

# Add Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Night Mode On", command=night_on)
options_menu.add_command(label="Night Mode Off", command=night_off)


# Add Status Bar To Bottom Of App
status_bar = Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)

# Edit Bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
# Select Binding
root.bind('<Control-A>', select_all)
root.bind('<Control-a>', select_all)


#fee = "tututuana"
#my_label = Label(root, text=fee[:-1]).pack()

# Create Buttons

# Bold Button
bold_button = Button(toolbar_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=0, sticky=W, padx=5, pady=5)
# Italics Button
italics_button = Button(toolbar_frame, text="Italics", command=italics_it)
italics_button.grid(row=0, column=1, padx=5, pady=5)

# Undo/Redo Buttons
undo_button = Button(toolbar_frame, text="Undo", command=my_text.edit_undo)
undo_button.grid(row=0, column=2, padx=5, pady=5)
redo_button = Button(toolbar_frame, text="Redo", command=my_text.edit_redo)
redo_button.grid(row=0, column=3, padx=5, pady=5)

# Text Color
color_text_button = Button(toolbar_frame, text="Text Color", command=text_color)
color_text_button.grid(row=0, column=4, padx=5, pady=5)


root.mainloop()
