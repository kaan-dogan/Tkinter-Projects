from tkinter import *
import mysql.connector
import csv

entries = {}

def export(data):
    with open('crm/customers.csv', 'w') as f:
        w = csv.writer(f, dialect='excel', delimiter=';')
        for records in data:
            w.writerow(records)

def show(criteria):
    target_window = Tk()
    
    target_value = entries['target'].get()
    if criteria == 'name':
        sql_command = f"SELECT * FROM customers WHERE first_name = + '{target_value}'"
    elif criteria == 'user_id':
        sql_command = "SELECT * FROM customers WHERE user_id = " + target_value
    
    my_cursor.execute(sql_command)
    results = my_cursor.fetchall()
    
    frame = LabelFrame(target_window)
    frame.grid(row=0, column=0, columnspan=3, padx=5)
    
    for index, label_text in enumerate(labels_root):
        header_label = Label(frame, text=label_text, font=('Helvetica', 10, 'bold'))
        header_label.grid(row=0, column=index, padx=5, pady=5)
    for row_index, result in enumerate(results):
        row_index += 1
        for col_index, field in enumerate(result):
            data_label = Label(frame, text=str(field))
            data_label.grid(row=row_index, column=col_index, padx=5, pady=5)    
    
def showall():
    my_cursor.execute("SELECT * FROM customers")
    results = my_cursor.fetchall()
    
    results_window = Tk()
    
    frame = LabelFrame(results_window)
    frame.grid(row=0, column=0, columnspan=3, padx=5)

    for index, label_text in enumerate(labels_root):
        header_label = Label(frame, text=label_text, font=('Helvetica', 10, 'bold'))
        header_label.grid(row=0, column=index, padx=5, pady=5)

    for row_index, result in enumerate(results):
        row_index += 1
        for col_index, field in enumerate(result):
            data_label = Label(frame, text=str(field))
            data_label.grid(row=row_index, column=col_index, padx=5, pady=5)

    csv_button = Button(results_window, text="Export to Excel (csv Format)", command=lambda: export(results), font=('Helvetica', 10, 'bold'))
    csv_button.grid(row=1, column=0, padx=5, pady=5, sticky=W)

labels_root = [
    'First Name',
    'Last Name',
    'ZipCode',
    'Price Paid',
    'User Id',
    'E-mail',
    'Address Line 1',
    'Address Line 2',
    'City',
    'State',
    'Country',
    'Phone',
    'Payment Method',
    'Discount Code'
]

def create_fields(rootVal, LabelList, entries):
    for label_text in LabelList:
        label = Label(rootVal, text=label_text, font=('Helvetica', 10, 'bold'))
        label.grid(row=LabelList.index(label_text) + 1, column=0, padx=5, pady=5, sticky=W)

        entry = Entry(rootVal)
        entry.grid(row=LabelList.index(label_text) + 1, column=1)
        
        entries[label_text] = entry
        
        target_entry = Entry(rootVal)
        target_entry.grid(row=4, column=3, sticky=E)
        entries['target'] = target_entry
        
def add(fields):
    
    sql_command = "INSERT INTO customers (first_name, last_name, zipcode, price_paid, user_id, email, address_1, address_2, city, state, country, phone, payment_method, discount_code) VALUES( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = []
    for field in fields: 
        values.append(entries[field].get())
    
    my_cursor.execute(sql_command, values)
    mydb.commit()
    clear()

def clear():
    for index in range(len(labels_root)):
        entries[labels_root[index]].delete(0, END)

root = Tk()
root.title('CRM')
# root.geometry("200x400")

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password123',
    database='customers'
)

my_cursor = mydb.cursor()

my_cursor.execute("""CREATE TABLE IF NOT EXISTS customers(
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    zipcode VARCHAR(7),
    price_paid DECIMAL(10, 2),
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255),
    address_1 VARCHAR(255),
    address_2 VARCHAR(255),
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(255),
    phone VARCHAR(255),
    payment_method VARCHAR(50),
    discount_code VARCHAR(255)
    )""")
mydb.commit()

label = Label(root, text="Customer Database", font=25)
label.grid(row = 0, column = 0, columnspan=2)

create_fields(root, labels_root, entries)

Button1 = Button(root, text="Add Customer to the Database", font=('Helvetica', 10, 'bold'), command=lambda: add(labels_root))
Button1.grid(row = 1, column = 3, columnspan=2, padx=5, ipadx=20)

Button2 = Button(root, text="Clear Fields", font=('Helvetica', 10, 'bold'), command=clear)
Button2.grid(row = 2, column = 3, columnspan=2, padx=5, ipadx=78)

Button3 = Button(root, text="Show All Customers", font=('Helvetica', 10, 'bold'), command=showall)
Button3.grid(row =3, column = 3, columnspan=2, ipadx=52)

targetLabel =Label(root, text="Target:", font=('Helvetica', 10, 'bold'))
targetLabel.grid(row=4, column=3, sticky=W, padx=5)

# target = Entry(root)
# target.grid(row=4, column=3, sticky=E)

Button4 = Button(root, text="Show Customer (by Name)", font=('Helvetica', 10, 'bold'), command=lambda: show('name'))
Button4.grid(row =5, column = 3, columnspan=2, ipadx=35)

Button5 = Button(root, text="Show Customer (by User ID)", font=('Helvetica', 10, 'bold'), command=lambda: show('user_id'))
Button5.grid(row =6, column = 3, columnspan=2, ipadx=35)

root.mainloop()
