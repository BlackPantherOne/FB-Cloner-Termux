import os
import time
import random
import json
from datetime import datetime

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

# File paths for settings, logs, and credentials
settings_file = "settings.json"
log_file = "cloning_log.txt"
credentials_file = "credentials.json"

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def load_settings():
    if os.path.exists(settings_file):
        with open(settings_file, 'r') as f:
            settings = json.load(f)
    else:
        settings = {
            'sim_choice': "Grameenphone",
            'country_choice': "Bangladesh",
            'theme': "light"
        }
        save_settings(settings)
    return settings

def save_settings(settings):
    with open(settings_file, 'w') as f:
        json.dump(settings, f)

def load_credentials():
    if os.path.exists(credentials_file):
        with open(credentials_file, 'r') as f:
            credentials = json.load(f)
    else:
        credentials = {
            'username': 'admin',  # Default username
            'password': 'password123'  # Default password
        }
        save_credentials(credentials)
    return credentials

def save_credentials(credentials):
    with open(credentials_file, 'w') as f:
        json.dump(credentials, f)

def login():
    credentials = load_credentials()
    print("Please log in.")
    username_input = input("Username: ")
    password_input = input("Password: ")
    
    if username_input == credentials['username'] and password_input == credentials['password']:
        print(GREEN + "Login successful!" + RESET)
        return True
    else:
        print(RED + "Invalid username or password. Try again." + RESET)
        return False

def banner(settings):
    clear()
    theme = settings['theme']
    theme_color = CYAN if theme == 'light' else '\033[1;37;40m'
    print(theme_color + "="*60)
    print("  █████▒▒ FAKE FB CLONER v1.0 ▒▒█████")
    print("       Coded by: YourName | For Education Only")
    print("="*60 + RESET)
    print(f"""
[1] Start Cloning
[2] View Successful Clones
[3] Select SIM Provider
[4] Select Country
[5] About Tool
[6] Clear Saved Results
[7] Change Theme (Current: {theme.capitalize()})
[8] Exit
""")

sim_list = ["Grameenphone", "Robi", "Jio", "Airtel", "Banglalink"]
country_list = ["Bangladesh", "India", "Pakistan", "USA"]

def select_sim(settings):
    print("\nAvailable SIMs:")
    for i, sim in enumerate(sim_list, 1):
        print(f"[{i}] {sim}")
    choice = int(input("Select SIM number: "))
    if 1 <= choice <= len(sim_list):
        settings['sim_choice'] = sim_list[choice - 1]
        save_settings(settings)
        print(f"Selected SIM: {settings['sim_choice']}")
    else:
        print(RED + "Invalid SIM selection." + RESET)

def select_country(settings):
    print("\nAvailable Countries:")
    for i, country in enumerate(country_list, 1):
        print(f"[{i}] {country}")
    choice = int(input("Select Country number: "))
    if 1 <= choice <= len(country_list):
        settings['country_choice'] = country_list[choice - 1]
        save_settings(settings)
        print(f"Selected Country: {settings['country_choice']}")
    else:
        print(RED + "Invalid country selection." + RESET)

def show_progress_bar(percent):
    bar_length = 40
    filled_length = int(bar_length * percent // 100)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f"\r   [{bar}] {percent}%", end='', flush=True)

def start_cloning(settings):
    ids = []
    print("\nEnter FB ID|pass (type 'done' to finish or 'demo' for 50 demo IDs):")
    while True:
        entry = input(">> ")
        if entry.lower() == 'done':
            break
        elif entry.lower() == 'demo':
            for i in range(50):
                ids.append(f"10000{random.randint(11111111, 99999999)}|pass{random.randint(100,999)}")
            print(f"{YELLOW}[+] 50 Demo IDs Loaded!{RESET}")
            break
        elif '|' in entry:
            ids.append(entry.strip())
        else:
            print(RED + "Invalid format. Use: 1000111222333|password" + RESET)

    print(CYAN + "\nCloning started...\n" + RESET)
    results = []
    for i, data in enumerate(ids):
        fb_id, fb_pass = data.split('|')
        print(f"{YELLOW}[{i+1}] Cloning {fb_id}..." + RESET)

        for p in range(0, 101, 10):
            show_progress_bar(p)
            time.sleep(0.1)
        print()

        status = random.choice(["Success", "Failed", "Already Cloned", "Try Again"])
        if status == "Success":
            print(GREEN + f"   ✓ Success | {fb_id} | {fb_pass}" + RESET)
            result = f"{settings['sim_choice']} | {settings['country_choice']} | {fb_id} | {fb_pass}"
            results.append(result)
            log_cloning_status(fb_id, fb_pass, "Success")
        else:
            print(RED + f"   × {status} | ID: {fb_id}" + RESET)
            log_cloning_status(fb_id, fb_pass, "Failed")
        print("-" * 50)

    if results:
        with open("cloned_success.txt", "a") as f:
            for r in results:
                f.write(r + "\n")
        print(GREEN + f"\n[✓] {len(results)} IDs saved to cloned_success.txt" + RESET)
    else:
        print(RED + "\n[×] No successful clones." + RESET)

def log_cloning_status(fb_id, fb_pass, status):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as f:
        f.write(f"[{timestamp}] {status} | {fb_id} | {fb_pass}\n")

def view_results():
    print("\nSaved Successful Clones:\n")
    if os.path.exists("cloned_success.txt"):
        with open("cloned_success.txt", "r") as f:
            data = f.read().strip()
            if data:
                print(data)
            else:
                print("No results to show.")
    else:
        print("No results found.")

def clear_results():
    open("cloned_success.txt", "w").close()
    print("All saved results cleared.")

def change_theme(settings):
    current_theme = settings['theme']
    new_theme = 'light' if current_theme == 'dark' else 'dark'
    settings['theme'] = new_theme
    save_settings(settings)
    print(f"Theme changed to {new_theme.capitalize()}.")

# MAIN LOGIN LOOP
if login():
    settings = load_settings()
    while True:
        banner(settings)
        opt = input("Select option [1-8]: ").strip()
        if opt == '1':
            start_cloning(settings)
        elif opt == '2':
            view_results()
        elif opt == '3':
            select_sim(settings)
        elif opt == '4':
            select_country(settings)
        elif opt == '5':
            print(YELLOW + "\nFake FB Cloner v1.0\nThis is a simulation tool for educational use only.\nIt does NOT hack or access any real accounts.\n" + RESET)
        elif opt == '6':
            clear_results()
        elif opt == '7':
            change_theme(settings)
        elif opt == '8':
            print("Exiting... Bye.")
            break
        else:
            print(RED + "Invalid choice." + RESET)
        input("\nPress Enter to return to menu...")
