import os
import time
import random

GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    clear()
    print(CYAN + "="*60)
    print("  █████▒▒ FAKE FB CLONER v1.0 ▒▒█████")
    print("       Coded by: RedRoom | For Education Only")
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

sim_list = ["Grameenphone", "Robi", "Jio", "Airtel", "Banglalink"]
country_list = ["Bangladesh", "India", "Pakistan", "USA"]
sim_choice = sim_list[0]
country_choice = country_list[0]

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

def start_cloning():
    ids = []
    print(YELLOW + "\n[+] Auto-generating 50 demo FB IDs..." + RESET)
    for i in range(50):
        ids.append(f"10000{random.randint(11111111, 99999999)}|pass{random.randint(100,999)}")
    print(f"{YELLOW}[+] 50 Demo IDs Loaded Automatically!{RESET}")

    print(CYAN + "\nCloning started...\n" + RESET)
    results = []
    for i, data in enumerate(ids):
        fb_id, fb_pass = data.split('|')
        print(f"{YELLOW}[{i+1}] Cloning {fb_id}..." + RESET)
        
        for p in range(0, 101, 5):
            show_progress_bar(p)
            time.sleep(random.uniform(0.3, 0.5))  # Simulate longer cloning
        print()

        status = random.choice(["Success", "Failed", "Already Cloned", "Try Again"])
        if status == "Success":
            print(GREEN + f"   ✓ Success | {fb_id} | {fb_pass}" + RESET)
            result = f"{sim_choice} | {country_choice} | {fb_id} | {fb_pass}"
            results.append(result)
        else:
            print(RED + f"   × {status} | ID: {fb_id}" + RESET)
        print("-" * 50)

    if results:
        with open("cloned_success.txt", "a") as f:
            for r in results:
                f.write(r + "\n")
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

# MAIN MENU LOOP
while True:
    banner()
    opt = input("Select option [1-7]: ").strip()
    if not opt:
        print(RED + "Please enter a valid option number (1-7)." + RESET)
    elif opt == '1':
        start_cloning()
    elif opt == '2':
        view_results()
    elif opt == '3':
        select_sim()
    elif opt == '4':
        select_country()
    elif opt == '5':
        print(YELLOW + "\nFake FB Cloner v1.0\nThis is a simulation tool for educational use only.\nIt does NOT hack or access any real accounts.\n" + RESET)
    elif opt == '6':
        clear_results()
    elif opt == '7':
        print("Exiting... Bye.")
        break
    else:
        print(RED + "Invalid choice." + RESET)
    input("\nPress Enter to return to menu...")
