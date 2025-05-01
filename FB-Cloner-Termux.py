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
    print("       Coded by: YourName | For Education Only")
    print("="*60 + RESET)
    print("""
[1] Start Cloning
[2] View Successful Clones
[3] Select SIM Provider
[4] Select Country
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
    choice = int(input("Select SIM number: "))
    sim_choice = sim_list[choice - 1]
    print(f"Selected SIM: {sim_choice}")

def select_country():
    global country_choice
    print("\nAvailable Countries:")
    for i, country in enumerate(country_list, 1):
        print(f"[{i}] {country}")
    choice = int(input("Select Country number: "))
    country_choice = country_list[choice - 1]
    print(f"Selected Country: {country_choice}")

def start_cloning():
    ids = []
    print("\nEnter FB ID|pass (type 'done' to finish):")
    while True:
        entry = input(">> ")
        if entry.lower() == 'done':
            break
        if '|' in entry:
            ids.append(entry.strip())
        else:
            print("Invalid format.")

    print("\nCloning started...\n")
    results = []
    for i, data in enumerate(ids):
        fb_id, fb_pass = data.split('|')
        print(f"[{i+1}] Cloning {fb_id}...", end=" ", flush=True)
        time.sleep(random.uniform(0.4, 0.9))
        status = random.choice(["Success", "Failed", "Already Cloned", "Try Again"])
        if status == "Success":
            print(GREEN + "✓ Success" + RESET)
            result = f"{sim_choice} | {country_choice} | {fb_id} | {fb_pass}"
            results.append(result)
        else:
            print(RED + f"× {status}" + RESET)

    if results:
        with open("cloned_success.txt", "a") as f:
            for r in results:
                f.write(r + "\n")
        print(GREEN + f"\n[✓] {len(results)} IDs saved to cloned_success.txt" + RESET)

def view_results():
    print("\nSaved Successful Clones:\n")
    try:
        with open("cloned_success.txt", "r") as f:
            for line in f.readlines():
                print(line.strip())
    except FileNotFoundError:
        print("No results found.")

def clear_results():
    open("cloned_success.txt", "w").close()
    print("All saved results cleared.")

# MAIN MENU LOOP
while True:
    banner()
    opt = input("Select option [1-7]: ")
    if opt == '1':
        start_cloning()
    elif opt == '2':
        view_results()
    elif opt == '3':
        select_sim()
    elif opt == '4':
        select_country()
    elif opt == '5':
        print("\nFake FB Cloner v1.0\nMade for fun/testing.\nNot real hacking tool.")
    elif opt == '6':
        clear_results()
    elif opt == '7':
        print("Exiting... Bye.")
        break
    else:
        print("Invalid choice.")
    input("\nPress Enter to return to menu...")
