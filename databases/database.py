from tkinter import *
import sqlite3

entries = {}

fields_root = {
    'f_name': (0, "First Name"),
    'l_name': (1, "Last Name"),
    'address': (2, "Address"),
    'city': (3, "City"),
    'state': (4, "State"),
    'zipcode': (5, "ZipCode"),
}

fields_editor = {
    'f_name_editor': (0, "First Name"),
    'l_name_editor': (1, "Last Name"),
    'address_editor': (2, "Address"),
    'city_editor': (3, "City"),
    'state_editor': (4, "State"),
    'zipcode_editor': (5, "ZipCode"),
}

def showFields(rootVal, fields, entries):

    for fieldName, (row, text) in fields.items():
        label = Label(rootVal, text=text)
        label.grid(row=row, column=0, padx=5, pady=5)

        entry = Entry(rootVal, width=30)
        entry.grid(row=row, column=1)
        
        entries[fieldName] = entry

    return entries

def saveChanges(entries):
    conn = sqlite3.connect('databases\\address_book.db')
    c = conn.cursor()

    c.execute("""UPDATE addresses SET
            first_name = :f_name_editor,
            last_name = :l_name_editor,
            address = :address_editor,
            city = :city_editor,
            state = :state_editor,
            zipcode = :zipcode_editor
        """,
        {
            'f_name_editor': entries['f_name_editor'].get(),
            'l_name_editor': entries['l_name_editor'].get(),
            'address_editor': entries['address_editor'].get(),
            'city_editor': entries['city_editor'].get(),
            'state_editor': entries['state_editor'].get(),
            'zipcode_editor': entries['zipcode_editor'].get()
        })

    conn.commit()
    conn.close()        

def update():
    editor = Tk()
    editor.title("Update a Record")
    editor.geometry("400x600")
    
    editor_entries = showFields(editor, fields_editor, entries)
    
    conn = sqlite3.connect('databases\\address_book.db')
    c = conn.cursor()
    
    targetId = target_entry.get()
    c.execute("SELECT * FROM addresses WHERE oid = " + targetId)
    records = c.fetchall()
    

    for record in records:
        editor_entries['f_name_editor'].insert(0, record[0])
        editor_entries['l_name_editor'].insert(0, record[1])
        editor_entries['address_editor'].insert(0, record[2])
        editor_entries['city_editor'].insert(0, record[3])
        editor_entries['state_editor'].insert(0, record[4])
        editor_entries['zipcode_editor'].insert(0, record[5])
    
    
    save_changes = Button(editor, text="Save Changes", command=lambda: saveChanges(entries)).grid(row=11, column=0, columnspan=2, padx=10, ipadx=135)
    
def delete():
    conn = sqlite3.connect('databases\\address_book.db')
    c = conn.cursor()
    
    targetId = target_entry.get()
    c.execute("DELETE FROM addresses WHERE oid=?" , (targetId),)

    conn.commit()
    conn.close()
    
def submit(entries):

    conn = sqlite3.connect('databases\\address_book.db')
    c = conn.cursor()

    c.execute("""
        INSERT INTO addresses VALUES (
            :f_name,
            :l_name,
            :address,
            :city,
            :state,
            :zipcode
        )""",
        {
            'f_name': entries['f_name'].get(),
            'l_name': entries['l_name'].get(),
            'address': entries['address'].get(),
            'city': entries['city'].get(),
            'state': entries['state'].get(),
            'zipcode': entries['zipcode'].get()
        })

    conn.commit()
    conn.close()

    for entry in entries.values():
        entry.delete(0, END) 


def show():
    conn = sqlite3.connect('databases\\address_book.db')
    c = conn.cursor()
    
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    
    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[-1]) + '\n'
    
    label = Label(root, text=print_records).grid(row=12, column=0, columnspan=2)
    
    conn.commit()
    conn.close()

root = Tk()
root.title('Databases')

conn = sqlite3.connect('databases\\address_book.db')

target_entry = Entry(root, width=30)
target_entry.grid(row=9, column=1, padx=20)
target = Label(root, text="Target Value")
target.grid(row=9, column=0) 

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode text
        )""")
conn.commit()
conn.close()


entries = showFields(root, fields_root, entries)

submit_button = Button(root, text="Submit", command=lambda: submit(entries))
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=152)

show_button = Button(root, text="Show Record", command=show)
show_button.grid(row=7, column=0, columnspan=2, padx=10, ipadx=137)

delete_button = Button(root, text="Delete Record", command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

update_button = Button(root, text="Update Query", command=update)
update_button.grid(row=11, column=0, columnspan=2, padx=10, ipadx=135)

root.mainloop()