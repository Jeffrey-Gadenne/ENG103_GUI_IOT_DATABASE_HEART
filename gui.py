from tkinter import *
from tkinter import ttk 
from tkinter.scrolledtext import ScrolledText
#from PIL import Image, ImageTk
import sqlite3
import hrcalc
from hrcalc import *


root = Tk()
root.geometry('500x500')
root.title("ENG103 Heart data")


patient = StringVar()
txtstarttime = StringVar()
txtweight = StringVar()

db = sqlite3.connect('form.db')

cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS health (starttime TEXT,name TEXT, weight TEXT, heartrate TEXT)")
db.commit()

now = datetime.now()
current_time = (now.strftime("%Y-%m-%d %H:%M:%S"))

#Main Frame
main_frame = Frame(root, width=2500, height=500)
main_frame.pack(fill=BOTH, expand=True)

#Canvas
my_canvas = Canvas(main_frame, bg="dark green", width=2500, height=500,scrollregion=(0,0,500,500))


my_scrollbar = Scrollbar(main_frame, orient=VERTICAL)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_scrollbar.configure(command=my_canvas.yview)
#my_canvas.config(width=500, height=500)

#Configure Canvas 
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
my_canvas.pack(side=LEFT, fill=BOTH, expand=True)

#main app x scrolling 

my_scrollbarx = Scrollbar(main_frame, orient=HORIZONTAL)
my_scrollbarx.pack(side=BOTTOM, fill=X)
my_scrollbarx.configure(command=my_canvas.xview)
#my_canvas.config(width=500, height=500)

#Configure Canvas 
my_canvas.configure(xscrollcommand=my_scrollbarx.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
my_canvas.pack(side=BOTTOM, fill=BOTH, expand=True)

#Frame inside canvas
second_frame = Frame(my_canvas, width=2300, height=768, bg = "wheat1")


#adding second frame to window in canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

#form.configure(background)
#render = PhotoImage(file = 'images\\background\\background.png')
#img = Label(second_frame, image = render)
#img.place(x = 0, y= 0)

#display current time 
now = datetime.now()
current_time = (now.strftime("%Y-%m-%d %H:%M:%S"))

def time_start():
    start_time_entry = Entry(second_frame, textvar=txtstarttime, fg = "Ghost White", bg = "dark green")
    start_time_entry.place(x=68, y=60)
    start_time_entry.insert(INSERT, current_time)

time_start()
start_label_name = Label(second_frame,fg = "Ghost White", bg = "dark green",text="start time" ,width=20,font=("bold", 10))
start_label_name.place(x=68,y=40,)
start_time_label = Label(second_frame, text=current_time, fg = "Ghost White", bg = "dark green",width=20,font=("bold", 10))
start_time_label.place(x=68, y=60)

label_2 = Label(second_frame,fg = "Ghost White", bg = "dark green", text="weight",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

weight = Entry(second_frame,textvar=txtweight)
weight.place(x=240,y=180)

# group of widgets
patiententry_label = Label(second_frame,fg = "Ghost White", bg = "dark green", text="Patients Name",width=20,font=("bold", 10))
patiententry_label.place(x=68,y=220)

patiententry = Entry(second_frame, width=50, textvar=patient)
patiententry.place(x=240, y=240)

txtheartrate = Text(second_frame, height=5, width=55, wrap=WORD)
scr = Scrollbar(second_frame)
scr.config(command=txtheartrate.yview)
txtheartrate.config(yscrollcommand=scr.set)
txtheartrate.pack(side=LEFT)
with open("heart.txt", "r") as hearts:
    for line in hearts:
        txtheartrate.insert(INSERT, line.strip())
txtheartrate.insert(END,"\n")
scr.pack(side="right", fill="y", expand=True)
scr.place(x=510, y=500)
txtheartrate.pack(side="left", fill="both", expand=True)
txtheartrate.place(x=68, y=480)
txtheartrate.bind("<1>", lambda event: txtheartrate.focus_set())

txttempread = Text(second_frame, height=5, width=55, wrap=WORD)
scr = Scrollbar(second_frame)
scr.config(command=txttempread.yview)
txttempread.config(yscrollcommand=scr.set)
txttempread.pack(side=LEFT)
with open("temperature.txt", "r") as tempe:
    for line in tempe:
        txttempread.insert(INSERT, line.strip())
txttempread.insert(END,"\n")
scr.pack(side="right", fill="y", expand=True)
scr.place(x=510, y=300)
txttempread.pack(side="left", fill="both", expand=True)
txttempread.place(x=68, y=280)
txttempread.bind("<1>", lambda event: txttempread.focus_set())



#table of data header labels 
data_frame = Frame(second_frame, width=1200, height=500, borderwidth="3", relief="groove")
data_frame.place(x=800, y=0)

my_canvas_data = Canvas(data_frame, bg="Ghost White", width=1200, height=500,scrollregion=(0,0,500,500))


my_scrollbar_data = Scrollbar(data_frame, orient=VERTICAL)
my_scrollbar_data.pack(side=RIGHT, fill=Y)
my_scrollbar_data.configure(command=my_canvas_data.yview)

#Configure Canvas 
my_canvas_data.configure(yscrollcommand=my_scrollbar.set)
my_canvas_data.bind('<Configure>', lambda e: my_canvas_data.configure(scrollregion = my_canvas_data.bbox("all")))
my_canvas_data.pack(side=LEFT, fill=BOTH, expand=True)

#x scrolling data

my_scrollbar_data = Scrollbar(data_frame, orient=HORIZONTAL)
my_scrollbar_data.pack(side=BOTTOM, fill=X)
my_scrollbar_data.configure(command=my_canvas_data.xview)

#Configure X Canvas 
my_canvas_data.configure(xscrollcommand=my_scrollbar.set)
my_canvas_data.bind('<Configure>', lambda e: my_canvas_data.configure(scrollregion = my_canvas_data.bbox("all")))
my_canvas_data.pack(side=TOP, fill=BOTH, expand=True)

#Frame inside canvas
information_frame = Frame(my_canvas_data, width=1200, height=1300, bg = "Ghost white")


#adding second frame to window in canvas
my_canvas_data.create_window((0,0), window=information_frame, anchor="nw")

accession_id_header = Label (information_frame, text='Accession ID', bg="Dark Green", fg="Ghost White", font="Lato 12 bold", padx=5, pady=5, borderwidth="2", relief="groove")
accession_id_header.grid(row=0, column=0, sticky=N+S+E+W)

starttime_header = Label (information_frame, text='Start Time', bg="Dark Green", fg="Ghost White", font="Lato 12 bold", padx=5, pady=5, borderwidth="2", relief="groove")
starttime_header.grid(row=0, column=1, sticky=N+S+E+W)

patient_name_header = Label (information_frame, text='Patient Name', width=20, bg="Dark Green", fg="Ghost White", font="Lato 12 bold", padx=5, pady=5, borderwidth="2", relief="groove")
patient_name_header.grid(row=0, column=2, sticky=N+S+E+W)

weight_header = Label (information_frame, text='Weight', bg="Dark Green", fg="Ghost White", font="Lato 12 bold", padx=5, pady=5, borderwidth="2", relief="groove")
weight_header.grid(row=0, column=3, sticky=N+S+E+W)

heartrate_header = Label (information_frame, text='heartrate', width=30, bg="Dark Green", fg="Ghost White", font="Lato 12 bold", padx=5, pady=5, borderwidth="2", relief="groove")
heartrate_header.grid(row=0, column=4, sticky=N+S+E+W)



#row data increment
conn = sqlite3.connect('form.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM health')
rowsid = cursor.fetchall()
acc_id_row = int(1)
def refresh():



    
    acc_id = int(acc_id_row)

    
    while acc_id <= 1 : 
        for acc_id in range(30):
            
            acc_id = int(acc_id) + 1 
            conn = sqlite3.connect('form.db')
            cursor = conn.cursor()
            cursor.execute('SELECT rowid, rowid FROM health WHERE rowid = ?',(acc_id,))
            records = cursor.fetchall()
            print(records)

            #starttime 
            
            cursor.execute('SELECT starttime FROM health WHERE rowid = ?',(acc_id,))
            starttimes = cursor.fetchall()
            print(starttimes)
            
            cursor.execute('SELECT name FROM health WHERE rowid = ?',(acc_id,))
            names = cursor.fetchall()
            print(names)
            
            #weight
            cursor.execute('SELECT weight FROM health WHERE rowid = ?',(acc_id,))
            weights = cursor.fetchall()
            print(weights)
            
            
            #heartdetails
            cursor.execute('SELECT heartrate FROM health WHERE rowid = ?',(acc_id,))
            heartrates = cursor.fetchall()
            print(heartrates)
                      


            for accs_id in records:
                
                

                for row in records[0]:
                                
                
                    #data 
                    accession_id_header = Label (information_frame, text=acc_id, bg="Ghost White", fg="black", font="Lato 10 bold", padx=5, pady=5, borderwidth="2", relief="groove")
                    accession_id_header.grid(row=acc_id, column=0, sticky=N+S+E+W)

                    
                    starttime_header = Label (information_frame, text=starttimes, bg="Ghost White", fg="black", font="Lato 10 bold", padx=5, pady=5, borderwidth="2", relief="groove")
                    starttime_header.grid(row=acc_id, column=1, sticky=N+S+E+W)
                    
                    patient_name_header = Label (information_frame, text=names, width=20, bg="Ghost White", fg="black", font="Lato 10 bold", padx=5, pady=5, borderwidth="2", relief="groove")
                    patient_name_header.grid(row=acc_id, column=2, sticky=N+S+E+W)
                        
                    weight_header = Label (information_frame, text=weights, bg="Ghost White", fg="black", font="Lato 10 bold", padx=5, pady=5, borderwidth="2", relief="groove")
                    weight_header.grid(row=acc_id, column=3, sticky=N+S+E+W)

            
                    heartrate_header = Label (information_frame, text=heartrates, width=30, bg="Ghost White", fg="black", font="Lato 10 bold", padx=5, pady=5, borderwidth="2", relief="groove")
                    heartrate_header.grid(row=acc_id, column=4, sticky=N+S+E+W)


                

            
            

refresh()          


conn.commit()




# still need to add the update fields section






def submit():
    


    
    a_starttime = txtstarttime.get()
    a_name = patient.get()
    a_weight = txtweight.get()
    a_heart = txtheartrate.get(1.0, END)
    conn = sqlite3.connect('form.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO health(starttime, weight, name, heartrate) VALUES(?,?,?,?)',(a_starttime, a_weight, a_name, a_heart))
        db.close()


    #clear the onscreen fields 
    patiententry.delete(0, END)
    txtheartrate.delete(1.0, END)
    refresh()
    time_start()    

    
Button(second_frame, text='Submit',width=20,bg='Green',fg='white', activebackground='blue', activeforeground='black', relief='raised', command=submit).place(x=180, y=700)

    
root.mainloop()
