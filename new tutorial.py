from tkinter import *
from tkinter import ttk
import sqlite3
import os 
import csv
import sqlite3 as sql
from PIL import ImageTk,Image
from tkinter import messagebox

window=Tk()
label=Label(window,text="Login",font=('arial',18,'bold'),bg='gold2',fg='white')
label.pack(side=TOP,fill=X)
label=Label(window,text="",font=('arial',10,'bold'),bg='gold2',fg='white')
label.pack(side=BOTTOM,fill=X)
canvas=Canvas(window,width=400,height=400)
image=ImageTk.PhotoImage(Image.open("11.jpg"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
label=Label(window,text='Name',font=('arial',12,'bold'),bg='white',fg='black')
label.place(x=170,y=40)
label=Label(window,text='Password',font=('arial',12,'bold'),bg='white',fg='black')
label.place(x=170,y=90)

name_entry=StringVar()
name_entry=ttk.Entry(window,textvariable=name_entry)
name_entry.place(x=270,y=40)
name_entry.focus()
pass_entry=StringVar()
pass_entry=ttk.Entry(window,textvariable=pass_entry,show='*')
pass_entry.place(x=270,y=90)

def Login():
	a = name_entry.get()
	b = pass_entry.get()
	if a =='admin' and b == 'admin':
		window.destroy()
		window2=Tk()
		window2.title('Sign_up form')
		window2.geometry("400x400+420+170")
		label=Label(window2,text="Sign_up Form",font=('arial',18,'bold'),bg='gold2',fg='white')
		label.pack(side=TOP,fill=X)
		label=Label(window2,text="",font=('arial',18,'bold'),bg='gold2',fg='white')
		label.pack(side=BOTTOM,fill=X)
		label=Label(window2,text='User Name',font=('arial',10,'bold'))
		label.place(x=50,y=60)
		label=Label(window2,text='City',font=('arial',10,'bold'))
		label.place(x=50,y=100)
		label=Label(window2,text='Postal code',font=('arial',10,'bold'))
		label.place(x=50,y=140)

		entry1=StringVar()
		entry1=ttk.Entry(window2,textvariable=entry1)
		entry1.place(x=160,y=60)
		entry2=StringVar()
		entry2=ttk.Entry(window2,textvariable=entry2)
		entry2.place(x=160,y=100)
		entry3=StringVar()
		entry3=ttk.Entry(window2,textvariable=entry3)
		entry3.place(x=160,y=140)

		def createdatabase():
			conn=sqlite3.connect('database1.db')
			c=conn.cursor()
			conn.execute('''CREATE TABLE IF NOT EXISTS users(Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
				Name TEXT NOT NULL, City TEXT NOT NULL,Postalcode TEXT NOT NULL 
				);''')
			conn.commit()
			conn.commit()
			conn.close()

		createdatabase()

		def save_to_database():
			conn=sqlite3.connect('database1.db')
			c=conn.cursor()
			c.execute('INSERT INTO users(Name,City,Postalcode) VALUES (?,?,?)',(entry1.get(),entry2.get(),entry3.get()))
			conn.commit()
			print('saved')


		btn2=ttk.Button(window2,text='Save',command=save_to_database)
		btn2.place(x=160,y=180,width=90,height=35)


		def Export():
			conn=sql.connect('database1.db')
			cursor=conn.cursor()
			cursor.execute("SELECT * FROM users")
			with open("users.csv","w")as csv_file:
				csv_writer=csv.writer(csv_file,delimiter="\t")
				csv_writer.writerow([i[0] for i in cursor.description])
				csv_writer.writerows(cursor)
			dir_path =os.getcwd() + "/users.csv"
			messagebox.showinfo('success','Exported Successfully')

		btn2=ttk.Button(window2,text='Export to csv',command=Export)
		btn2.place(x=160,y=220,width=90,height=35)




	else:
		messagebox.showerror('Error','Password or username is incorrect')

btn=ttk.Button(window,text='Login',command=Login)
btn.place(x=270,y=130,width=120,height=40)






window.title("Login Screen")
window.geometry("400x400+420+170")
window.mainloop()