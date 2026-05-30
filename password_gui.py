from tkinter import *
from password import PassWord
from tkinter import messagebox
import pyperclip #This is to copy generated password to clipboard
import json
# ---------------------------- CONSTANTS ------------------------------- #
GRAY = '#999999'
BURG = '#6B2346'
WHITE = '#fafafa'
FONT_NAME = 'Century Gothic'

# Import custom password class. Unnecessary to do but extra practice on creating and using classes
pass_word = PassWord()

window = Tk()
window.title(f'{' ' * 130}Password Manager')
window.minsize(width=500, height=500)
window.config(padx=80, pady=100, bg= BURG)

canvas = Canvas(width=450, height=320, bg=BURG, highlightthickness=0)
# manager_img =PhotoImage(file='passkey_300dp_46152F_FILL0_wght400_GRAD0_opsz48.png')
manager_img =PhotoImage(file='white_lock.png')
canvas.create_image(250, 140, image=manager_img)
pass_text = canvas.create_text(215, 260, text='Password Manager', font=(FONT_NAME, 15, 'bold'), fill=WHITE)
canvas.grid(column=1, row=0)

# Website Label and Entry
website_label = Label(text='Website:', font= (FONT_NAME, 15, 'bold'), bg=BURG, fg=WHITE)
website_label.grid(column=0, row=1)

# website_entry = Entry(width=40, font=(FONT_NAME, 22))
website_entry = Entry(width=28, font=(FONT_NAME, 22))
website_entry.grid(column=1, row=1, pady=7)

# This function does the following:
# 1. Creates a dictionary to neatly format website, username and password info
# When the 'Add' button is clicked:
# 2. Produces error message if email and/or website entry box is blank
# 3. Produces a dialog box if all fields have text confirming user on the info about to be saved
# 4. Writes info to txt file
# Empties website and password fields
def add_password():
    p_dict = {
        website_entry.get(): {
            'Username': email_entry.get(),
            'Password': pass_word.nwpswrd,
        }
    }
    if len(email_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showerror(title='Empty Field Detected', message="Please don't leave any fields empty!")
    else:
        with open('password.json', 'r') as file:
            contents = json.load(file)
        if website_entry.get() in contents:
            password_override = messagebox.askyesno(title='Password Found', message=f'The following info has been found for {website_entry.get()}:\nUsername: {contents[website_entry.get()]['Username']}\nPassword: {contents[website_entry.get()]['Password']}\n\nDo you want to override the found credentials?')
            is_ok = False
        elif website_entry.get() not in contents:
            is_ok = messagebox.askokcancel(title=website_entry.get(), message=f'These are the details entered: \nUsername: {email_entry.get()}\nPassword: {pass_word.nwpswrd}\nIs it ok to save? ')  # Outputs a boolean
        if is_ok or password_override:
            try:
                with open('password.json', 'r') as file:
                    contents = json.load(file)
            except FileNotFoundError:
                with open('password.json', 'w') as file:
                    json.dump(p_dict, file, indent=4)
            else:
                contents.update(p_dict)
                with open('password.json', 'w') as file:
                    json.dump(contents, file, indent=4)
            finally:
                website_entry.delete(0, 'end')
                pswd_entry.delete(0, 'end')


# This function generates the random password using the password class, copies to the clipboard and types it in the password entry box
def write_password():
    pass_word.gen_password()
    pyperclip.copy(pass_word.nwpswrd)
    pswd_entry.insert(INSERT, pass_word.nwpswrd)

def search():
    try:
        with open('password.json', 'r') as file:
            contents = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data File Found')
    else:
        try:
            messagebox.showinfo(title=f'{website_entry.get()}', message=f'Email: {contents[website_entry.get()]['Username']}\nPassword: {contents[website_entry.get()]['Password']}')
        except KeyError:
            messagebox.showerror(title='Error', message='No details for the website exists.')

# Website search
website_search = Button(width=20, height=2, font=(FONT_NAME, 11, 'bold'), bg=WHITE, text= 'Search', command=search)
website_search.grid(column=2, row=1, pady=5)

# Email/Username Label and Entry
email_label = Label(text='Email/Username:', font= (FONT_NAME, 15, 'bold'), bg=BURG, fg=WHITE)
email_label.grid(column=0, row=2, pady=5)

email_entry = Entry(width=40, font=(FONT_NAME, 22))
email_entry.grid(column=1, row=2, pady=7, columnspan=2)
# usr = email_entry.get()

# Password Label and Entry
pswd_label = Label(text='Password:', font= (FONT_NAME, 15, 'bold'), bg=BURG, fg= WHITE)
pswd_label.grid(column=0, row=3, pady=5)

pswd_entry = Entry(width=28, font=(FONT_NAME, 22))
pswd_entry.grid(column=1, row=3, pady=5)

# Generate Password Button
# pswd_button = Button(text='Generate Password', font= (FONT_NAME, 11, 'bold'), width=21, bg=WHITE, command=pass_word.gen_password)
pswd_button = Button(text='Generate Password', font= (FONT_NAME, 11, 'bold'), width=20, height=2, bg=WHITE, command=write_password)
pswd_button.grid(column=2, row=3, pady=5)

# Add Button
pswd_button = Button(text='Add', font= (FONT_NAME, 11, 'bold'), width=71, bg=WHITE, command=add_password)
pswd_button.grid(column=1, row=4, pady=5, columnspan=2)


window.mainloop()