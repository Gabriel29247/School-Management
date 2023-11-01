import tkinter as tk
from tkinter import messagebox
import mysql.connector as sql
from prettytable import PrettyTable
global currentUser
currentUser = None

def create_loading_screen():
    loading_screen = tk.Tk()
    loading_screen.title("Loading...")
    loading_screen.geometry("300x100")

    loading_screen.withdraw()
    messagebox.showinfo("LearnSys", "Please wait while the program connects to the database.")

    try:
        global conn
        conn = sql.connect(
            host="sql12.freemysqlhosting.net",
            user="sql12657119",
            password="",
            database="sql12657119")
        print(conn.is_connected())
        loading_screen.destroy()
        create_main_window()

    except Exception as e:
        messagebox.showerror("Connection Error", "Unable to connect to the database.")
        print(e)
        loading_screen.destroy()

def create_main_window():
    # Create the main window
    global root
    root = tk.Tk()
    root.title("Welcome back!")
    root.configure(bg="#333333")  # Set the background color to dark gray (hex code)
    root.iconbitmap("assets/logo.ico")
    # Calculate the window size and position
    window_size = 400  # Set the desired window size (in pixels)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_size) // 2
    y = (screen_height - window_size) // 2
    root.geometry(f"{window_size}x{window_size}+{x}+{y}")

    # Use Verdana Bold for titles and Verdana for other text
    title_font = ("Verdana Bold", 16)
    text_font = ("Verdana", 12)

    # Create a frame to hold the contents with padding
    frame = tk.Frame(root, bg="#333333")
    frame.pack(pady=20)

    # Create and place widgets with customized colors and button width
    title_label = tk.Label(frame, text="LearnSys", font=title_font, bg="#333333", fg="white")
    title_label.pack(pady=10)

    subheading_label = tk.Label(frame, text="Enter your info to get started.", font=text_font, bg="#333333", fg="white")
    subheading_label.pack(pady=5)

    username_label = tk.Label(frame, text="👤 Username:", font=text_font, bg="#333333", fg="white")
    username_label.pack(pady=(10, 5))  # Lower the username label
    global username_entry
    username_entry = tk.Entry(frame, font=text_font, bg="#333333", fg="white", insertbackground="purple", bd=2, relief=tk.GROOVE)
    username_entry.pack(pady=5)  # Lower the username entry field

    password_label = tk.Label(frame, text="🔒 Password:", font=text_font, bg="#333333", fg="white")
    password_label.pack(pady=(10, 5))  # Lower the password label
    global password_entry
    password_entry = tk.Entry(frame, show="*", font=text_font, bg="#333333", fg="white", insertbackground="purple", bd=2, relief=tk.GROOVE)
    password_entry.pack(pady=5)  # Lower the password entry field

    login_button = tk.Button(frame, text="Login", command=login, font=text_font, bg="green", fg="white", width=15, bd=0)
    login_button.pack(pady=10)

    # Rounded corners for the Login button
    login_button.config(relief=tk.RAISED)

    # Start the GUI event loop
    root.mainloop()

def create_gradient_button(master, text, command, gradient_color, font, width, bd=0):
    button = tk.Button(master, text=text, command=command, font=font, width=width, bd=bd)
    
    # Configure button properties
    button.configure(
        relief=tk.FLAT,
        borderwidth=0,
        highlightthickness=0,
        activebackground=gradient_color[1],
        bg=gradient_color[0],
        fg="white"
    )

    # Hover effect
    def on_enter(event):
        button.configure(bg=gradient_color[1])

    def on_leave(event):
        button.configure(bg=gradient_color[0])

    # Bind hover events
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    return button
# Now you can use create_gradient_button to create gradient buttons in your admin frame function:
'''def create_admin_frame(master):
    admin_frame = tk.Toplevel(master)
    admin_frame.title("Admin Panel")

    admin_frame.configure(bg='#333333')

    # Calculate the window size and position
    window_width = 800  # Increased window width (in pixels)
    window_height = 600  # Increased window height (in pixels)
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    admin_frame.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Use stylish fonts and colors
    title_font = ("Helvetica", 28, "bold")
    text_font = ("Helvetica", 16)

    # Create a frame with padding
    frame = tk.Frame(admin_frame, bg='#333333')
    frame.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")
    nav_options = ["Add","Search","Remove","Publish"]
    # Create a horizontal navigation bar
    nav_frame = tk.Frame(frame, bg='#1C2833')
    nav_frame.grid(row=0, column=0, sticky="ew")

    # Define gradient button colors for the navigation bar
    option_colors = [
        ("#2E86C1", "#21618C"),  # Light to dark blue gradient
        ("#E74C3C", "#C0392B"),  # Light to dark red gradient
        ("#F39C12", "#D35400"),  # Light to dark orange gradient
        ("#9B59B6", "#8E44AD")   # Light to dark purple gradient
    ]

    # Create gradient buttons for navigation bar
    for i, (option, option_color) in enumerate(zip(nav_options, option_colors)):
        create_gradient_button(nav_frame, option, lambda o=option: on_nav_option_click(o), option_color, text_font, 20).grid(row=0, column=i, padx=5, pady=5)

    # Create a Treeview widget
    tree = ttk.Treeview(frame, columns=("Name", "Description"))
    tree.heading("#1", text="Name")
    tree.heading("#2", text="Description")
    tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # Configure column weights for responsive resizing
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)

    # Start the GUI event loop
    admin_frame.mainloop()
'''

def makeshift():
    cursor = conn.cursor()
    while currentUser[1] == "RootAdmin":
        
        print(f"Welcome to School Management System. You are currently logged in as {currentUser[1]}")
        print("Your actions: ")
        print("1. Add Record")
        print("2. View Record")
        print("3. Delete Record")
        print("4. Publish Notice")
        print("5. View Notice")

        choice = int(input("Enter choice: "))
        
        if choice == 1:
            identity = input("Enter identity (student/teacher): ")
            username = input("Enter username: ")
            password = input("Enter password: ")

            query = "INSERT INTO users (identity, username, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (identity, username, password))
            conn.commit()
            print("Record added successfully.")
                
        elif choice == 2:
            cursor.execute("SELECT * FROM users")
            records = cursor.fetchall()
            
            if not records:
                print("No records found.")
            else:
                table = PrettyTable(["ID", "Identity", "Username", "Password"])
                for record in records:
                    table.add_row(record)
                print(table)
        elif choice == 3:
            id_to_delete = input("Enter the ID of the record to delete: ")
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query, (id_to_delete,))
            conn.commit()
            print("Record deleted successfully.")
        elif choice == 4:
            notice_text = input("Enter the notice text: ")
            query = "INSERT INTO notices (notice) VALUES (%s)"
            cursor.execute(query, (notice_text,))
            conn.commit()
            print("Notice added successfully.")
        elif choice == 5:
            cursor.execute("SELECT * FROM notices")
            records = cursor.fetchall()
            
            if not records:
                print("No notices found.")
            else:
                table = PrettyTable(["Notice Text"])
                for record in records:
                    table.add_row(record)
                print(table)
    else:
        print("Student/Teacher, this part is still under development! Check back later.")
def login():
    global currentUser

    username = username_entry.get()
    password = password_entry.get()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))

    info = cursor.fetchall()
    if info == []:
        messagebox.showerror("Login Unsuccessful", "No user found!")
    else:
        correct_pass = info[0][2]
        if password == correct_pass:
            currentUser = (info[0][0], info[0][1], info[0][2])
            messagebox.showinfo("Login Successful", "Successfully logged in!")
            messagebox.showinfo("Note","UI is currently under development.\nPlease check your shell.")

            root.withdraw()
            makeshift()
            '''if info[0][1] == 'RootAdmin':
                root.withdraw()  # Hide the main window
                create_admin_frame(root)  # Pass the main window as an argument to the admin frame function
                root.destroy()'''
        else:
            messagebox.showerror("Login Unsuccessful", "Incorrect Password")

            
'''
def create_add_record_frame(master):
    add_record_frame = tk.Toplevel(master)
    add_record_frame.title("Add Record")

    # Gradient background
    bg_color = ("#3498DB", "#1E272E")  # Light blue to dark blue-gray gradient
    add_record_frame.configure(bg=bg_color[0])

    # Calculate the window size and position
    window_size = 400  # Set the desired window size (in pixels)
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    x = (screen_width - window_size) // 2
    y = (screen_height - window_size) // 2
    add_record_frame.geometry(f"{window_size}x{window_size}+{x}+{y}")

    # Use stylish fonts and colors
    title_font = ("Helvetica", 20, "bold")
    text_font = ("Helvetica", 12)

    # Create a frame with padding
    frame = tk.Frame(add_record_frame, bg=bg_color[0])
    frame.pack(pady=20)

    # Identity field
    identity_label = tk.Label(frame, text="Identity", font=text_font, bg=bg_color[0], fg="white")
    identity_label.pack(pady=5)
    identity_entry = tk.Entry(frame, font=text_font, bg="#333333", fg="white", insertbackground="purple", bd=2, relief=tk.GROOVE)
    identity_entry.pack(pady=10)

    # Username and Password fields
    username_label = tk.Label(frame, text="👤 Username", font=text_font, bg=bg_color[0], fg="white")
    username_label.pack(pady=5)
    username_entry = tk.Entry(frame, font=text_font, bg="#333333", fg="white", insertbackground="purple", bd=2, relief=tk.GROOVE)
    username_entry.pack(pady=10)

    password_label = tk.Label(frame, text="🔒 Password", font=text_font, bg=bg_color[0], fg="white")
    password_label.pack(pady=5)
    password_entry = tk.Entry(frame, show="*", font=text_font, bg="#333333", fg="white", insertbackground="purple", bd=2, relief=tk.GROOVE)
    password_entry.pack(pady=10)

    # Create a button to submit the form (You can customize the command accordingly)
    submit_button = tk.Button(frame, text="Submit", command=submit_add_record, font=text_font, bg="#2ECC71", fg="white", width=15, bd=0)
    submit_button.pack(pady=20)

    # Rounded corners for the Submit button
    submit_button.config(relief=tk.RAISED)

    # Start the GUI event loop
    add_record_frame.mainloop()

def submit_add_record():
    # Implement the logic to handle the submitted record
    # You can access the values from identity_entry, username_entry, and password_entry
    pass

def delete_record():
    global conn

    record_id = input("Enter record ID to delete: ")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM records WHERE id = %s", (record_id,))
    conn.commit()
    messagebox.showinfo("Success", "Record deleted successfully!")
    pass 

def view_records():
    global conn

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM records")
    records = cursor.fetchall()

    if not records:
        messagebox.showinfo("No Records", "No records found.")
    else:
        for record in records:
            print(record)
    pass

def publish_notice():
    global conn

    notice = input("Enter notice to publish: ")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notices (notice) VALUES (%s)", (notice,))
    conn.commit()
    messagebox.showinfo("Success", "Notice published successfully!")
    pass
'''
create_loading_screen()
