import requests
import time
from colorama import init, Style, Fore



init(autoreset=True)


# Banner with colored lines
banner = """
\033[38;2;255;0;0m██╗    ██╗ ██████╗ ██╗     ███████╗    ██████╗  ██████╗ ████████╗    
\033[38;2;255;51;0m██║    ██║██╔═══██╗██║     ██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝    
\033[38;2;255;102;0m██║ █╗ ██║██║   ██║██║     █████╗      ██████╔╝██║   ██║   ██║       
\033[38;2;255;153;0m██║███╗██║██║   ██║██║     ██╔══╝      ██╔══██╗██║   ██║   ██║       
\033[38;2;255;204;0m╚███╔███╔╝╚██████╔╝███████╗██║         ██████╔╝╚██████╔╝   ██║       
\033[38;2;255;255;0m ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝         ╚═════╝  ╚═════╝    ╚═╝       
"""
print(banner)

# User input
uid = int(input(Fore.RED + "Enter Free Fire UID: "))

# Simulate fetching data animation
print(Fore.YELLOW + "Fetching data... ", end="")
for _ in range(10):
    print(".", end="", flush=True)
    time.sleep(1)  # Simulate 1 second per dot
print()  # Move to the next line after the dots

# API request to get player info
url = f"https://projects-fox-apis.vercel.app/player_info?uid={uid}&key=Fox-7CdxP"

response = requests.get(url)

if response.status_code == 200:
    # If the request is successful, print the response in an organized format
    player_info = response.json()

    print(Fore.GREEN + "\nPlayer Information:")
    print(Fore.YELLOW + f"Player Name: {player_info['player_name']}")  # This will display in Arabic (if available)
    print(Fore.CYAN + f"Player ID: {player_info['player_id']}")
    print(Fore.CYAN + f"Account Creation Date: {player_info['account_creation_date']}")
    print(Fore.MAGENTA + f"Player Level: {player_info['level']}")
    print(Fore.MAGENTA + f"Booyah Pass Level: {player_info['booyah_pass_level']}")
    print(Fore.BLUE + f"Clan Name: {player_info['clan_name']}")
    print(Fore.BLUE + f"Clan Level: {player_info['clan_level']}")
    print(Fore.BLUE + f"Clan Members: {player_info['clan_members']}")
    print(Fore.BLUE + f"Clan Leader Name: {player_info['clan_leader_name']}")
    print(Fore.BLUE + f"Clan Leader ID: {player_info['clan_leader_id']}")
    print(Fore.BLUE + f"Clan Leader Level: {player_info['clan_leader_level']}")
    print(Fore.BLUE + f"Clan Leader Likes: {player_info['clan_leader_likes']}")
    print(Fore.YELLOW + f"In Clan: {player_info['in_clan']}")
    print(Fore.YELLOW + f"Player Likes: {player_info['likes']}")
    print(Fore.YELLOW + f"Pet Name: {player_info['pet_name']}")
    print(Fore.YELLOW + f"Server: {player_info['server']}")
    print(Fore.YELLOW + f"Clan ID: {player_info['clan_id']}")
    print(Fore.GREEN + f"Bio:{player_info['bio']}")

    # Asking user if they want to access the main menu
    main_menu_choice = input(Fore.GREEN + "\nDo you want to access the main menu (yes / no)? ").strip().lower()
    if main_menu_choice == "yes":
        print(Fore.CYAN + "Accessing main menu...")
        # Add your main menu code here
    else:
        print(Fore.RED + "Exiting... Goodbye!")
else:
    print(Fore.RED + "Failed to fetch data. Error code:", response.status_code)
