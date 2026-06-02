import json

DATA_FILE = "watchlist.json"


def load_watchlist():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_watchlist():
    with open(DATA_FILE, "w") as file:
        json.dump(watchlist, file)

watchlist = load_watchlist()

def show_menu():
    print("\n ===== INVESTMENT TRACKER =====")
    print("1. View Watchlist")
    print("2. Add Company")
    print("3. Exit")

def view_watchlist():
    if len(watchlist) == 0:
        print("\n ===== WATCHLIST EMPTY =====")
    else:
        print("\nWatchlist")
        for i, company in enumerate(watchlist, start=1):
            print(f"[{i}] {company}")

def add_company():
    name = input("\nEnter company name: ")
    watchlist.append(name)
    save_watchlist()
    print(f"{name} added to watchlist")

while True:
    show_menu()
    choice = input("\nChoose an option (1-3): ")
    if choice == "1":
        view_watchlist()
    elif choice == "2":
        add_company()
    elif choice == "3":
        print("Exiting Investment Tracker")
        break
    else:
        print("Invalid option. Try again")