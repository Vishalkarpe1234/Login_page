import tkinter as tk
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["Demo"]
collection = db["users"]

def register():
    username = username_entry.get()
    password = password_entry.get()

    # Check if the username already exists in the database
    if collection.find_one({"username": username}):
        print("Username already exists! Please choose another.")
    else:
        # Insert the new user into the database
        user_data = {"username": username, "password": password}
        collection.insert_one(user_data)
        print("Registration successful!")
        open_login_page()

def open_login_page():
    # Close the registration window
    registration_window.withdraw()

    # Create the login window
    login_window = tk.Toplevel()
    login_window.title("Login Page")
    login_window.geometry("300x200")
    login_window.configure(bg="black")

    def login():
        username = login_username_entry.get()
        password = login_password_entry.get()

        # Check if the username exists in the database
        user = collection.find_one({"username": username})

        if user and user["password"] == password:
            print("Login successful!")
            login_window.withdraw()
            open_dashboard()
        else:
            print("Login failed!")

    # Labels and Entry for Login
    login_username_label = tk.Label(login_window, text="Username:", fg="white", bg="black")
    login_username_label.pack()
    login_username_entry = tk.Entry(login_window, bg="gray", fg="white")
    login_username_entry.pack()

    login_password_label = tk.Label(login_window, text="Password:", fg="white", bg="black")
    login_password_label.pack()
    login_password_entry = tk.Entry(login_window, show="*", bg="gray", fg="white")
    login_password_entry.pack()

    login_button = tk.Button(login_window, text="Login", command=login, bg="white", fg="black")
    login_button.pack()

    # Run the login page event loop
    login_window.mainloop()

def open_dashboard():
    # Create the dashboard window
    dashboard_window = tk.Toplevel()
    dashboard_window.title("Dashboard")
    dashboard_window.geometry("300x200")
    dashboard_window.configure(bg="black")

    def logout():
        print("Logging out...")
        dashboard_window.destroy()
        registration_window.deiconify()

    # Logout Button
    logout_button = tk.Button(dashboard_window, text="Logout", command=logout, bg="white", fg="black")
    logout_button.pack(pady=10)

    # Run the dashboard event loop
    dashboard_window.mainloop()

# Create the main application window
registration_window = tk.Tk()
registration_window.title("Registration Page")
registration_window.geometry("300x200")
registration_window.configure(bg="black")

# Labels and Entry for Registration
username_label = tk.Label(registration_window, text="Username:", fg="white", bg="black")
username_label.pack()
username_entry = tk.Entry(registration_window, bg="gray", fg="white")
username_entry.pack()
 
password_label = tk.Label(registration_window, text="Password:", fg="white", bg="black")
password_label.pack()
password_entry = tk.Entry(registration_window, show="*", bg="gray", fg="white")
password_entry.pack()

register_button = tk.Button(registration_window, text="Register", command=register, bg="white", fg="black")
register_button.pack()

registration_window.mainloop()
