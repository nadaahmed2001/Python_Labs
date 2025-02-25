import json
import re
import hashlib
from datetime import datetime

USER_FILE = "users.json"
PROJECT_FILE = "projects.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def validate_phone(phone):
    return bool(re.match(r"^(010|011|012|015)\d{8}$", phone)) # Egyptian phone numbers start with 010, 011, 012, or 015 followed by 8 digits

def register():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email format!")
        return

    password = input("Enter Password: ")
    confirm_password = input("Confirm Password: ")

    if password != confirm_password:
        print("Passwords do not match!")
        return

    phone = input("Enter Mobile Number: ")
    if not validate_phone(phone):
        print("Invalid Egyptian phone number!")
        return

    hashed_password = hash_password(password)

    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": hashed_password,
        "phone": phone
    }

    # Save user to file
    try:
        with open(USER_FILE, "r") as file:
            users = json.load(file) # Load existing users from file if it exists, json.load() reads the json file and converts it to a python dictionary
    except FileNotFoundError:
        users = []

    users.append(user)

    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4) # json.dump() writes the python dictionary to the json file, indent=4 makes the json file more readable

    print("Registration Successful! You can now login.")

def login():
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    hashed_password = hash_password(password)

    try:
        with open(USER_FILE, "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("No users registered.")
        return None

    for user in users:
        if user["email"] == email and user["password"] == hashed_password:
            print(f"Welcome, {user['first_name']}!")
            return email
        
    print("Invalid email or password!")
    return None

def create_project(user_email):
    title = input("Enter Project Title: ")
    details = input("Enter Project Details: ")
    target = input("Enter Fundraising Target (EGP): ")

    if not target.isdigit() or int(target) <= 0:
        print("Invalid target amount!")
        return

    start_date = input("Enter Start Date (YYYY-MM-DD): ")
    end_date = input("Enter End Date (YYYY-MM-DD): ")

    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d") # strptime() converts a string to a datetime object
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        if end_date <= start_date:
            print("End date must be after start date!")
            return
    except ValueError: # ValueError means the date format is invalid
        print("Invalid date format!")
        return

    project = {
        "title": title,
        "details": details,
        "target": int(target),
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
        "owner": user_email
    }

    try:
        with open(PROJECT_FILE, "r") as file:
            projects = json.load(file)
    except FileNotFoundError:
        projects = []

    projects.append(project)

    with open(PROJECT_FILE, "w") as file:
        json.dump(projects, file, indent=4)

    print("Project created successfully!")

def view_projects():
    try:
        with open(PROJECT_FILE, "r") as file:
            projects = json.load(file)
    except FileNotFoundError:
        print("No projects found.")
        return

    for i, project in enumerate(projects, 1): # This loop will iterate over the projects list and print each project
        print(f"\nProject {i}:")
        print(f"Title: {project['title']}")
        print(f"Details: {project['details']}")
        print(f"Target: {project['target']} EGP")
        print(f"Start Date: {project['start_date']}")
        print(f"End Date: {project['end_date']}")
        print(f"Owner: {project['owner']}")

def delete_project(user_email):
    try:
        with open(PROJECT_FILE, "r") as file:
            projects = json.load(file)
    except FileNotFoundError:
        print("No projects found.")
        return

    title = input("Enter the title of the project to delete: ")
    
    for project in projects:
        if project["title"] == title and project["owner"] == user_email:
            projects.remove(project)
            with open(PROJECT_FILE, "w") as file:
                json.dump(projects, file, indent=4)
            print("Project deleted successfully!")
            return

    print("Project not found or you do not have permission to delete it.")

# Main menu
def main():
    print("Welcome to the Crowd-Funding Console App")
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            user_email = login()
            if user_email:
                while True:
                    print("\n1. Create Project\n2. View Projects\n3. Delete Project\n4. Logout")
                    action = input("Choose an option: ")

                    if action == "1":
                        create_project(user_email)
                    elif action == "2":
                        view_projects()
                    elif action == "3":
                        delete_project(user_email)
                    elif action == "4":
                        break
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
