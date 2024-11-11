import subprocess
import os


def get_applications(file_path):
    applications = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():
                    name, path = line.split('=', 1)
                    applications[name.strip().lower()] = path.strip()
    except FileNotFoundError:
        print("File not Found...")
    return applications


def open_applications(app_name, applications):
    if app_name in applications:
        app_path = applications[app_name]
        if os.path.exists(app_path):
            print(f"Opening {app_name}...")
            subprocess.Popen([app_path])
        else:
            print(f"Path for {app_name} does not exist: {app_path}")
    else:
        print(f"{app_name} is not listed. Please add it to the text file.")


if __name__ == "__main__":
    file_path = input("Enter the path to the applications file: ").strip()
    applications = get_applications(file_path)

    if applications:
        while True:
            print("\nAvailable applications:")
            for app in applications.keys():
                print(f"- {app}")

            app_to_open = input(
                "\nEnter the name of the application to open (or type 'exit' to quit): ").strip().lower()
            if app_to_open == "exit":
                print("Exiting program.")
                break
            open_applications(app_to_open, applications)
    else:
        print("No applications found. Please check the text file.")
