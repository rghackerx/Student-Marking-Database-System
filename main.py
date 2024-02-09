# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MP-SMS - A Multi-Purpose Student Marka Management System  -- Credits : RGHacker
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import customtkinter as ctk
from tkinter import filedialog
import tkinter as tk
# from PIL import Image, ImageTk
import pymongo
import string as st

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# GUI Functions
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def success_msg_win(num):
    win = ctk.CTk()
    win.title("PoP-Up")
    win.geometry("300x150")

    if num == True:
        label = ctk.CTkLabel(win, text="Data Uploaded Successfully", font=("Arial", 12))
        label.pack(pady=10)
    else: 
        label = ctk.CTkLabel(win, text="Data Deleted Successfully", font=("Arial", 12))
        label.pack(pady=10)
        
    button_1 = ctk.CTkButton(win, text='Exit', width=20, command=win.destroy)
    button_1.pack(pady=5)
    
    win.mainloop()
    
# - - - - - Main GUI Window- - - - - - #
def create_gui():
    main = ctk.CTk()
    main.configure(bg='black')
    main.title("STUDENT MARKS MANAGEMENT SYSTEM")
    main.geometry("450x200")

    label = ctk.CTkLabel(main, text="Student Management System", font=("Arial", 13))
    label.pack(pady=10)

    button_insertion = ctk.CTkButton(main, text='1. Insertion of Student Records', width=30,
                                  command=insertion_menu)
    button_insertion.pack(pady=5)

    button_deletion = ctk.CTkButton(main, text='2. Deletion of Previous Record', width=30,
                                  command=win_data_deletion)
    button_deletion.pack(pady=5)

    button_marks = ctk.CTkButton(main, text='3. Marks Insertion', width=30,
                               command=man_marks_gui)
    button_marks.pack(pady=5)

    button_1 = ctk.CTkButton(main, text='Exit', width=20, command=exit)
    button_1.pack(pady=5)    

    main.mainloop()
    
def win_data_deletion():
    win = ctk.CTk()
    win.title("Student Management System")
    win.geometry("400x200")

    label = ctk.CTkLabel(win, text="Select One of them", font=("Arial", 12))
    label.pack(pady=10)
    
    button_1 = ctk.CTkButton(win, text='1. Delete the database', width=20, command=dataDeletion)
    button_1.pack(pady=5)
    button_2 = ctk.CTkButton(win, text='2. Delete the records', width=20, command=man_dataDeletion)
    button_2.pack(pady=5)
    button_2 = ctk.CTkButton(win, text='3. Manual Delete', width=20, command=win_man_deletion)
    button_2.pack(pady=5)
    button_3 = ctk.CTkButton(win, text='Exit', width=20, command=win.destroy)
    button_3.pack(pady=5)
    
    win.mainloop() 

def man_marks_gui():
    win = ctk.CTk()
    win.title("Student Management System")
    win.geometry("400x200")

    label = ctk.CTkLabel(win, text="Marks Insertion", font=("Arial", 12))
    label.pack(pady=10)
    
    button_1 = ctk.CTkButton(win, text='1. Whole Class', width=20, command=lambda: open_file_dialog(2))
    button_2 = ctk.CTkButton(win, text='2. Insert by USN', width=20, command=lambda: open_file_dialog(3))
    button_4 = ctk.CTkButton(win, text='3. Insert by Name', width=20, command=lambda: open_file_dialog(4))
    button_3 = ctk.CTkButton(win, text='Exit', width=20, command=win.destroy)
    
    button_1.pack(pady=5)
    button_2.pack(pady=5)
    button_4.pack(pady=5)
    button_3.pack(pady=5)
    
    win.mainloop() 
    win.destroy()
    
def open_file_dialog(user_choice):
    file_path = filedialog.askopenfilename()  
    
    if user_choice == 1:
            dataEntry(file_path)
    elif user_choice == 2:
            marksInsertion(file_path)
    elif user_choice == 3:
            man_marksInsertion(file_path)
    elif user_choice == 4:
            man_update_marks(file_path)

        
            
def insertion_menu():
     win = ctk.CTk()
     win.title("Select the option")
     win.geometry("350x200")
     button_1 = ctk.CTkButton(win, text='1. Upload File', width=20, command=lambda: open_file_dialog(1))
     button_2 = ctk.CTkButton(win, text='2. Solo Insert', width=20, command=solo_insert_win)
     button_3 = ctk.CTkButton(win, text='Exit', width=20, command=win.destroy)
     button_1.pack(pady=5)
     button_2.pack(pady=5)
     button_3 = ctk.CTkButton(win, text='Exit', width=20, command=win.destroy)
     button_3.pack(pady=5)
    
     win.mainloop() 
     win.destroy()
    
def solo_insert_win():
    win = ctk.CTk()
    win.title("Fill up the Fields")
    win.geometry("450x350")

    id_label = ctk.CTkLabel(win, text="Id:")
    id_label.pack()
    id_entry = ctk.CTkEntry(win)
    id_entry.pack()

    registration_label = ctk.CTkLabel(win, text="Registration No:")
    registration_label.pack()
    registration_entry = ctk.CTkEntry(win) 
    registration_entry.pack()
    
    name_label = ctk.CTkLabel(win, text="Name:")
    name_label.pack()
    name_entry = ctk.CTkEntry(win) 
    name_entry.pack()
    
    usn_label = ctk.CTkLabel(win, text="USN:")
    usn_label.pack()
    usn_entry = ctk.CTkEntry(win) 
    usn_entry.pack()

    # Submit button
    button_submit = ctk.CTkButton(win, text="Submit", command=lambda: solo_insert(id_entry.get(), registration_entry.get(), name_entry.get(), usn_entry.get()))
    button_submit.pack()
    win.mainloop()  
    
def win_man_deletion():
    win = ctk.CTk()
    win.title("Enter USN")
    win.geometry("400x300")
    usn_label = ctk.CTkLabel(win, text="USN:")
    usn_label.pack()
    usn_entry = ctk.CTkEntry(win) 
    usn_entry.pack()

    # Submit button
    button_submit = ctk.CTkButton(win, text="Submit", command=lambda: man_deletion(usn_entry.get()))
    button_submit.pack()
    button_exit = ctk.CTkButton(win, text='Exit', command=win.destroy)
    button_exit.pack()


    win.mainloop()
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Application Login   
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def solo_insert(id, registration, name, usn):
    id = int(id)
    search_query = {
        '$or': [
            {'_id': id},
            {'admission_no': usn},
            {'USN': usn}  
        ]
    }
    
    existing_doc = collection.find_one(search_query)

    if existing_doc:
        win = ctk.CTk()   
        win.title("Data Already Exist")
        win.geometry("400x300")
        usn_label = ctk.CTkLabel(win, text=f"Note: Data you inserted is already exist! ")
        usn_label.grid(row=2, column=0, padx=10, pady=5, sticky='w') 
        button_1 = ctk.CTkButton(win, text='Exit', command=win.destroy)
        button_1.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        win.mainloop() 
        win.destroy() 
        
    else:
        insert_data = {'_id': id, 'registration': registration, 'admission_no': usn, 'name': name}
        
        collection.insert_one(insert_data)

        success_msg_win(True)   
    

def marksInsertion(filename):
    with open(filename,'r') as newFile:
        values = newFile.readlines()
        for i in range(len(values)):
                mark = values[i]
                old = {"_id":i+1}
                new = {"$set": {"marks":mark}}
                collection.update_one(old,new)
        success_msg_win(True)   

        
# Delete the full database
def dataDeletion():
    client.drop_database("students")
    success_msg_win(False)

# Delete the given entries
def man_dataDeletion():
        filename = filedialog.askopenfilename()  # Opens file dialog to select a file
        with open(filename,'r') as newFile:
         data = newFile.readlines()
         for i in range(len(data)):
             a = data[i].split()
             rec = {"addmission_no":a[0]}
             collection.delete_one(rec)  
         success_msg_win(False)

# manual delete with usn function
def man_deletion(usn):
    usn = str(usn)
    usn = usn.upper()
    usn_main = {'addmission_no': usn}
    data = collection.find_one(usn_main)
    if data != None:
        win = ctk.CTk()   
        win.title("Details of the student")
        win.geometry("400x300")
            
        name_label = ctk.CTkLabel(win, text=f"ID: {data['_id']}")
        name_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        
        name_label = ctk.CTkLabel(win, text=f"Name: {data['name']}")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        
        usn_label = ctk.CTkLabel(win, text=f"Admission No: {data['addmission_no']}")
        usn_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        
        button_delete = ctk.CTkButton(win, text="Delete", command=lambda: man_delete(usn))
        button_delete.grid(row=3, column=0, padx=10, pady=5, sticky='w') 
        
        button_repeat = ctk.CTkButton(win, text="Search Again", command=win_man_deletion)
        button_repeat.grid(row=3, column=6, padx=10, pady=5, sticky='w') 
            
        win.mainloop()   
    else:
        win = ctk.CTk()   
        win.title("404 Not Found!")
        win.geometry("400x300")
        usn_label = ctk.CTkLabel(win, text=f"Note: Oh- oh! No data matched with USN {usn}")
        usn_label.grid(row=2, column=0, padx=10, pady=5, sticky='w') 
        button_1 = ctk.CTkButton(win, text='Exit', command=win.destroy)
        button_1.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        win.mainloop() 
        win.destroy()  

def man_delete(usn):
    usn = {'addmission_no': usn}
    collection.find_one_and_delete(usn)
    success_msg_win(False)

        
def man_marksInsertion(filename):
        with open(filename,'r') as marksData:
            a = marksData.readlines()
            for i in range(len(a)):
                b = a[i].split()
                mark = b[1]
                old = {'addmission_no':b[0]}
                new = {'$set':{'marks':mark}}
                collection.update_one(old,new)
            success_msg_win(True)   
    

def dataEntry(filename):
    with open(filename, 'r') as fyle:
        data = fyle.readlines()
    
        for i in range(len(data)):
            reg_no = data[i].split()[0]
            add_no = data[i].split()[1]
            name = ' '.join(data[i].split()[2:])
            insertData = {'_id': i+1, 'registration':reg_no,'addmission_no':add_no,'name':name}
            collection.insert_one(insertData)
        success_msg_win(True)  
        
def  man_update_marks(file_path):
    with open(file_path,'r') as fyle:
        data = fyle.readlines()
        for i in range(len(data)):
            name = ' '.join(data[i].split()[1:])
            mark = data[i].split()[0]
            filter_document = {'name': name}
            update_document = {'$set': {'marks': mark}}
            result = collection.update_one(filter_document, update_document, upsert=True)
        success_msg_win(True)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Main Function           
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":
    insertData = {}
    #connection building
    conn = "mongodb://localhost:27017/"
    client = pymongo.MongoClient(conn)
    #database creation
    db = client['students']
    #collection creation
    collection = db['myCollection']
    create_gui()

            
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CLI Mode           
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
'''
#Application UI Module - Terminal
print("\n* * * * * * * Student Marking Management Systems * * * * * * *\n")
print("1. Insertion of Student Records\n2. Deletion of Previous record\n3. Marks Insertion\n")
userInput =  int(input("(*)Choose any one from give above:- "))

if userInput == 1:
    filename = input("Enter the filename: ")
    dataEntry(filename)
elif userInput == 2:
    dataDeletion()
elif userInput == 3:
    print("1. For all class\n2. For some students")
    var = int(input("(*)Enter :- "))
    if var == 1:
        filename = input("Enter File name: ")
        marksInsertion(filename)
    elif var == 2:
        file = input("Enter the file name: ")
        man_marksInsertion(file)
'''
