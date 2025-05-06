import os
import time
import random
from collections import defaultdict

# ANSI Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Predefined credentials
USER_CREDENTIALS = {'username': 'admin', 'password': 'pass00'}

# SIMs and Countries
sim_list = ["Grameenphone", "Robi", "Jio", "Airtel", "Banglalink"]
country_list = ["Bangladesh", "India", "Pakistan", "USA"]
sim_choice = sim_list[0]
country_choice = country_list[0]

# Clone count tracking
clone_counts = defaultdict(int)

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def login():
    clear()
    print(CYAN + "="*60)
    print("   █████▒▒ FB CLONER v1.0 ▒▒█████")
    print("       Coded by: BlackOut | For Old ID Only")
    print("="*60 + RESET)
    print("\nPlease Login to Continue:")
    username_input = input("Username: ")
    password_input = input("Password: ")

    if username_input == USER_CREDENTIALS['username'] and password_input == USER_CREDENTIALS['password']:
        print(GREEN + "Login successful!" + RESET)
        time.sleep(1)
        return True
    else:
        print(RED + "Invalid username or password. Please try again." + RESET)
        time.sleep(2)
        return False

def banner():
    clear()
    print(CYAN + "="*60)
    print("  █████▒▒ FB CLONER v1.0 ▒▒█████")
    print("       Coded by: BlackOut | For Old ID Only")
    print("="*60 + RESET)
    print(f"""
 [1] Start Cloning
 [2] View Successful Clones
 [3] Select SIM Provider  (Current: {sim_choice})
 [4] Select Country       (Current: {country_choice})
 [5] About Tool
 [6] Clear Saved Results
 [7] Exit
""")

def select_sim():
    global sim_choice
    print("\nAvailable SIMs:")
    for i, sim in enumerate(sim_list, 1):
        print(f"[{i}] {sim}")
    try:
        choice = int(input("Select SIM number: "))
        if 1 <= choice <= len(sim_list):
            sim_choice = sim_list[choice - 1]
            print(f"Selected SIM: {sim_choice}")
        else:
            print(RED + "Invalid SIM selection." + RESET)
    except ValueError:
        print(RED + "Please enter a valid number." + RESET)

def select_country():
    global country_choice
    print("\nAvailable Countries:")
    for i, country in enumerate(country_list, 1):
        print(f"[{i}] {country}")
    try:
        choice = int(input("Select Country number: "))
        if 1 <= choice <= len(country_list):
            country_choice = country_list[choice - 1]
            print(f"Selected Country: {country_choice}")
        else:
            print(RED + "Invalid country selection." + RESET)
    except ValueError:
        print(RED + "Please enter a valid number." + RESET)

def show_progress_bar(percent):
    bar_length = 40
    filled_length = int(bar_length * percent // 100)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f"\r   [{bar}] {percent}%", end='', flush=True)

def get_show_label(fb_id):
    clone_counts[fb_id] += 1
    count = clone_counts[fb_id]
    suffix = {1: "1st", 2: "2nd", 3: "3rd"}.get(count, f"{count}th")
    return f"{suffix} Show"

def start_cloning():
    ids = ["61572800315891", "10001234567890", "10007894561234"]
    passwords = ["009827227"]
    results = []

    for i, fb_id in enumerate(ids):
        print(f"[{i+1}] Cloning {fb_id}...")
        for p in range(0, 101, 10):
            show_progress_bar(p)
            time.sleep(random.uniform(0.1, 0.2))
        print()

        success = random.choice([True, False]) if i != 0 else True

        if success:
            password = random.choice(passwords)
            label = get_show_label(fb_id)
            print(GREEN + f"   ✓ {label} | {fb_id} | {password}" + RESET)
            result = f"{label} | {sim_choice} | {country_choice} | {fb_id} | {password}"
            results.append(result)

            with open("cloned_success.txt", "a") as f:
                f.write(result + "\n")

            if i == 0:
                print(YELLOW + "\n[!] First ID cloned. Waiting 3 minutes before next..." + RESET)
                time.sleep(180)
            else:
                print(YELLOW + "\n[!] Waiting 30 minutes before next..." + RESET)
                time.sleep(1800)
        else:
            print(RED + f"   ✗ Failed | Invalid or Checkpoint" + RESET)
        print("-" * 50)

    if results:
        print(GREEN + f"\n[✓] {len(results)} IDs saved to cloned_success.txt" + RESET)
    else:
        print(RED + "\n[×] No successful clones." + RESET)

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

# Main Program
if login():
    while True:
        banner()
        opt = input("Select option [1-7]: ").strip()
        if opt == '1':
            start_cloning()
        elif opt == '2':
            view_results()
        elif opt == '3':
            select_sim()
        elif opt == '4':
            select_country()
        elif opt == '5':
            print(YELLOW + "\nFB Cloner v1.0\nThis is a simulation tool for educational use only.\nIt does not hack or access any real accounts.\n" + RESET)
        elif opt == '6':
            clear_results()
        elif opt == '7':
            print("Exiting... Bye.")
            break
        else:
            print(RED + "Invalid choice." + RESET)
        input("\nPress Enter to return to menu...")
