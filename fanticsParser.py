import os
import subprocess
from urllib.parse import urlparse
from tqdm import tqdm
import webbrowser
import time
import platform
import random
import pyfiglet

class Color:
    RED = "\033[1;31m"
    GREEN = "\033[1;32m"
    CYAN = "\033[1;36m"
    ORANGE = "\033[1;33m"
    PURPLE = "\033[1;35m"  
    BLUE = "\033[1;34m"    
    YELLOW = "\033[1;33m"  



def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

def print_banner():
    clear_screen()
    banner_text = '''
'''+Color.GREEN+''' _____           _   _          ____                          
'''+Color.RED+'''|  ___|_ _ _ __ | |_(_) ___ ___|  _ \ __ _ _ __ ___  ___ _ __ 
'''+Color.CYAN+'''| |_ / _` | '_ \| __| |/ __/ __| |_) / _` | '__/ __|/ _ \ '__|
'''+Color.YELLOW+'''|  _| (_| | | | | |_| | (__\__ \  __/ (_| | |  \__ \  __/ |   
'''+Color.BLUE+'''|_|  \__,_|_| |_|\__|_|\___|___/_|   \__,_|_|  |___/\___|_|   
'''+Color.PURPLE+'''                                                              
'''+Color.GREEN+'''
'''
    print(f"{Color.RED}{banner_text}")
    print(f"{Color.GREEN}============================")
    print(f"{Color.RED}[+] {Color.GREEN}Coded By @SalfiHacker")
    print(f"{Color.RED}[+] {Color.GREEN}Gift From Cyber Fantics & Z-Bl4ck-H4t")
    print(f"{Color.RED}[+] {Color.GREEN}Use It Responsibly!")
    print(f"{Color.GREEN}============================")

def open_social_media_channel(channel_url):
    webbrowser.open(channel_url)

def display_social_media_options():
    print_banner()
    options = {
        "1": "https://t.me/cyberfantics",
        "2": "https://instagram.com/cyberfantics",
        "3": "https://whatsapp.com/channel/0029VaFE5Dv5Ejy2MaydYm3Z",
        "4": "main_menu",
        "0": "exit_program"
    }

    user_choice = input(f"{Color.RED}╔═══[{Color.GREEN}Choose A Number{Color.RED}]\n{Color.RED}╚══》 {Color.GREEN}")

    if user_choice in options:
        if options[user_choice] == "main_menu":
            main_menu()
        elif options[user_choice] == "exit_program":
            exit_program()
        else:
            open_social_media_channel(options[user_choice])
    else:
        main_menu()


# Define a list of quotes
QUOTES = [
    "Hacking is the art of exploration and discovery.",
    "A true hacker never stops learning and evolving.",
    "In the world of hacking, curiosity is your greatest asset.",
    "To hack is to challenge the status quo and question everything.",
    "Hacking is not just about breaking into systems; it's about understanding them.",
    "The best hackers are those who use their skills for positive change.",
    "Hacking is a mindset that seeks to innovate and improve.",
    "In the digital realm, hackers are the architects of change.",
    "A hacker's creativity knows no bounds; they turn ideas into reality.",
    "To hack is to embrace uncertainty and navigate through the unknown.",
    "Hacking is a journey of continuous exploration and problem-solving.",
    "A hacker's code is a reflection of their ingenuity and skill.",
    "Hacking is the pursuit of knowledge without boundaries.",
    "The best hackers understand that security is a process, not a product.",
    "In hacking, persistence and determination lead to breakthroughs.",
    "To hack is to see beyond the surface and uncover hidden possibilities.",
    "A hacker's greatest weapon is their ability to adapt and learn.",
    "Hacking is not just about finding flaws; it's about finding solutions.",
    "The essence of hacking lies in the elegance of the code.",
    "Hackers believe in the power of collaboration and shared knowledge.",
    "In hacking, every challenge is an opportunity to learn and grow.",
    "To hack is to question, explore, and redefine what is possible.",
    "Hacking is the art of turning dreams into digital realities.",
    "A hacker's curiosity fuels their quest for understanding and improvement.",
    "Hacking is about making things work better, not just breaking them.",
    "The true measure of a hacker is their ability to create, not just disrupt.",
    "In the world of hacking, ideas are the most valuable currency.",
    "To hack is to see the beauty in complexity and find simplicity within.",
    "Hacking is a journey where every line of code tells a story.",
    "A hacker is someone who can turn chaos into order with elegance.",
    "Hacking is a never-ending exploration of the infinite possibilities of code.",
    "The best hackers understand the power of sharing knowledge with the community.",
    "To hack is to dance with uncertainty and create harmony from chaos.",
    "In hacking, innovation is the key to overcoming challenges.",
    "Hacking is the art of turning obstacles into stepping stones.",
    "A hacker's creativity is unleashed through the lines of code they write.",
    "Hacking is the pursuit of understanding and manipulating the digital world.",
    "To hack is to turn vulnerability into strength and weakness into opportunity.",
    "In the realm of hacking, ideas have the power to change the world.",
    "Hacking is not just about breaking barriers; it's about building bridges.",
    "A hacker's code is their canvas, and the keyboard is their brush.",
    "To hack is to question the impossible and redefine the possible.",
    "Hacking is a journey where every challenge is a puzzle waiting to be solved.",
    "A hacker's mindset sees possibilities where others see limitations.",
    "In hacking, every line of code is a stroke of creativity.",
    "To hack is to blend art and science into a symphony of innovation.",
    "Hacking is the art of turning challenges into triumphs.",
    "A hacker's legacy is the positive impact they leave on the digital landscape.",
    "In hacking, every keystroke is a note in the melody of creation.",
    "To hack is to think outside the box and redefine the rules.",
    "Hacking is the pursuit of knowledge for the sake of understanding.",
    "A hacker's toolset is fueled by curiosity, determination, and creativity.",
    "Hacking is not just about finding answers; it's about asking the right questions.",
    "To hack is to challenge assumptions and question the status quo.",
    "In hacking, every problem is a puzzle waiting to be solved.",
    "A hacker's mind is a canvas where ideas are transformed into code.",
    "Hacking is the art of turning complexity into simplicity.",
    "To hack is to explore the limitless possibilities of the digital realm.",
    "In hacking, every challenge is an opportunity to learn.",
    "A hacker's journey is paved with curiosity, innovation, and resilience.",
    "Hacking is the art of seeing things from a different perspective.",
    "To hack is to question everything and accept nothing at face value.",
    "In hacking, every problem is a puzzle waiting to be solved.",
    "A hacker's legacy is the positive impact they leave on the digital landscape.",
    "Hacking is a journey where every challenge is a puzzle waiting to be solved.",
    "A hacker's mindset sees possibilities where others see limitations.",
    "In hacking, every line of code is a stroke of creativity.",
    "To hack is to blend art and science into a symphony of innovation.",
    "Hacking is the art of turning challenges into triumphs.",
    "A hacker's legacy is the positive impact they leave on the digital landscape.",
    "In hacking, every keystroke is a note in the melody of creation.",
    "To hack is to think outside the box and redefine the rules.",
    "Hacking is the pursuit of knowledge for the sake of understanding.",
    "A hacker's toolset is fueled by curiosity, determination, and creativity.",
    "Hacking is not just about finding answers; it's about asking the right questions.",
    "To hack is to challenge assumptions and question the status quo.",
    "In hacking, every problem is a puzzle waiting to be solved.",
    "A hacker's mind is a canvas where ideas are transformed into code.",
    "Hacking is the art of turning complexity into simplicity.",
    "To hack is to explore the limitless possibilities of the digital realm.",
    "In hacking, every challenge is an opportunity to learn.",
    "A hacker's journey is paved with curiosity, innovation, and resilience.",
    "Hacking is the art of seeing things from a different perspective.",
    "To hack is to question everything and accept nothing at face value.",
    "In the realm of code, curiosity is the currency of power.",
    "Information is the most valuable currency in the digital world.",
    "In every system, there's a vulnerability waiting to be exploited.",
    "Never underestimate the power of social engineering.",
    "For a black hat, every obstacle is just a new challenge.",
    "The thrill of the hack is in the chase, not the catch.",
    "In the world of hacking, adaptability is key.",
    "Patience is the black hat's greatest weapon.",
    "With great knowledge comes great exploitation.",
    "Security through obscurity is a hacker's best friend.",
    "For a black hat, every network is a playground.",
    "Persistence pays off in the world of hacking.",
    "In hacking, innovation often comes from necessity.",
    "Never reveal your full hand in the game of cybercrime.",
    "The art of hacking lies in turning vulnerabilities into advantages.",
    "In hacking, anonymity is armor.",
    "Never trust the surface; always dig deeper.",
    "In the digital realm, there are no limits, only barriers waiting to be breached.",
    "For a black hat, every firewall is just a speed bump.",
    "In hacking, knowledge is power, but discretion is survival.",
    "A successful hack requires both skill and cunning.",
    "The best hacks leave no trace.",
    "In hacking, creativity is the mother of all exploits.",
    "Every piece of code is a potential weapon in the hands of a skilled hacker.",
    "For a black hat, ethics are merely obstacles to be overcome.",
    "In the world of hacking, arrogance can be a fatal flaw.",
    "A black hat knows that the weakest link in any system is often the human element.",
    "Never underestimate the value of a well-placed backdoor.",
    "In hacking, the end justifies the means.",
    "For a black hat, the thrill of the unknown is irresistible.",
    "In hacking, the only limit is one's imagination.",
    "Every encryption has a vulnerability; it's just a matter of finding it.",
    "For a black hat, anonymity is both a shield and a sword.",
    "In hacking, knowledge is the ultimate currency.",
    "The true power of hacking lies in its ability to disrupt.",
    "In the digital world, nothing is ever truly secure.",
    "A black hat thrives in the shadows.",
    "For a black hat, every system is a puzzle waiting to be solved.",
    "In hacking, the line between genius and madness is often blurred.",
    "Exploiting a vulnerability is an art form in the world of hacking.",
    "For a black hat, every challenge is an opportunity.",
    "In hacking, there are no rules, only guidelines.",
    "Every system has its weak points; it's just a matter of finding them.",
    "For a black hat, fear is a tool to be wielded.",
    "In hacking, timing is everything.",
    "A black hat knows that knowledge is power, but discretion is survival.",
    "For a black hat, every lock has a key; it's just a matter of finding it.",
    "In hacking, the only limits are the ones you impose on yourself.",
    "Every firewall has a loophole; it's just a matter of exploiting it.",
    "For a black hat, every obstacle is an opportunity.",
    "In hacking, the thrill of discovery is addictive.",
    "A black hat knows that patience is a virtue.",
    "For a black hat, every network is a web waiting to be spun.",
    "In hacking, precision is key.",
    "Every system has its vulnerabilities; it's just a matter of exploiting them.",
    "For a black hat, every challenge is a chance to prove one's prowess.",
    "In hacking, innovation is born from necessity.",
    "The best hackers leave no trace of their presence.",
    "In hacking, the key to success is stealth.",
    "For a black hat, every exploit is a work of art.",
    "In hacking, persistence is rewarded.",
    "Every encryption can be cracked; it's just a matter of time.",
    "For a black hat, every security measure is a puzzle waiting to be solved.",
    "In hacking, anonymity is both a blessing and a curse.",
    "The true power of hacking lies in its ability to manipulate.",
    "For a black hat, every obstacle is just another test of skill.",
    "In hacking, knowledge is both a weapon and a shield.",
    "Every system has its flaws; it's just a matter of exploiting them.",
    "For a black hat, every challenge is an opportunity to excel.",
    "In hacking, the line between right and wrong is often blurred.",
    "The best hackers are masters of deception.",
    "In hacking, the thrill of the chase is just as important as the prize.",
    "For a black hat, every vulnerability is a potential exploit.",
    "In hacking, the only certainty is uncertainty.",
    "Every network has its weak points; it's just a matter of finding them.",
    "For a black hat, every obstacle is just another puzzle to be solved.",
    "In hacking, the key to success is adaptability.",
    "The best hackers are always one step ahead.",
    "In hacking, the only limit is one's imagination.",
    "For a black hat, every system is a target waiting to be breached.",
    "In hacking, knowledge is power, but discretion is survival.",
    "Every firewall can be bypassed; it's just a matter of finding the right method.",
    "For a black hat, every challenge is an opportunity to prove one's skill.",
    "In hacking, innovation is born from adversity.",
    "The greatest hackers leave no trace of their presence.",
    "In hacking, anonymity is both a strength and a weakness.",
    "For a black hat, every exploit is a chance to push the boundaries.",
    "In hacking, persistence is key to success.",
    "Every encryption has a weakness; it's just a matter of exploiting it.",
    "For a black hat, every security measure is a challenge to be overcome.",
    "In hacking, the thrill of discovery is unmatched.",
    "A black hat knows that patience is often the key to success.",
    "For a black hat, every network is a puzzle waiting to be solved.",
    "In hacking, precision is everything.",
    "Every system has its vulnerabilities; it's just a matter of finding them.",
    "For a black hat, every challenge is an opportunity to shine.",
    "In hacking, innovation is fueled by ambition.",
    "The best hackers operate in the shadows.",
    "In hacking, the key to success lies in stealth.",
    "For a black hat, every exploit is a masterpiece.",
    "In hacking, persistence always pays off.",
    "Every encryption can be broken; it's just a matter of time and effort.",
    "For a black hat, every security measure is a puzzle waiting to be solved.",
    "In hacking, anonymity is both a blessing and a curse.",
    "The true power of hacking lies in its ability to manipulate.",
    "For a black hat, every obstacle is just another test of skill.",
    "In hacking, knowledge is both a weapon and a shield.",
    "Every system has its flaws; it's just a matter of exploiting them.",
    "For a black hat, every challenge is an opportunity to excel.",
    "In hacking, the line between right and wrong is often blurred.",
    "The best hackers are masters of deception.",
    "In hacking, the thrill of the chase is just as important as the prize.",
    "For a black hat, every vulnerability is a potential exploit.",
    "In hacking, the only certainty is uncertainty.",
    "Every network has its weak points; it's just a matter of finding them.",
    "For a black hat, every obstacle is just another puzzle to be solved.",
    "In hacking, the key to success is adaptability.",
    "The best hackers are always one step ahead.",
    "In hacking, the only limit is one's imagination.",
    "For a black hat, every system is a target waiting to be breached.",
    "In hacking, knowledge is power, but discretion is survival.",
    "Every firewall can be bypassed; it's just a matter of finding the right method.",
    "For a black hat, every challenge is an opportunity to prove one's skill.",
    "In hacking, innovation is born from adversity.",
    "The greatest hackers leave no trace of their presence.",
    "In hacking, anonymity is both a strength and a weakness.",
    "For a black hat, every exploit is a chance to push the boundaries.",
    "In hacking, persistence is key to success.",
    "Every encryption has a weakness; it's just a matter of exploiting it.",
    "For a black hat, every security measure is a challenge to be overcome.",
    "In hacking, the thrill of discovery is unmatched.",
    "A black hat knows that patience is often the key to success.",
    "For a black hat, every network is a puzzle waiting to be solved.",
    "In hacking, precision is everything.",
    "Every system has its vulnerabilities; it's just a matter of finding them.",
    "For a black hat, every challenge is an opportunity to shine.",
    "In hacking, innovation is fueled by ambition.",
    "The best hackers operate in the shadows.",
    "In hacking, the key to success lies in stealth.",
    "For a black hat, every exploit is a masterpiece.",
    "In hacking, persistence always pays off.",
    "Every encryption can be broken; it's just a matter of time and effort."
]


# Other functions and class definition here...


def download_files():
    print_banner()
    url_to_download = input(f"{Color.GREEN}[*] {Color.RED}Enter the URL to download files: {Color.GREEN}")
    folder_name = urlparse(url_to_download).hostname.replace(':', '_').replace('/', '_')
    folder_path = os.path.join(os.getcwd(), folder_name)

    os.makedirs(folder_path, exist_ok=True)
    os.chdir(folder_path)

    readme_info = """
    Follow Cyber Fantics:
    - Telegram Channel: https://t.me/cyberfantics
    - WhatsApp Channel: https://whatsapp.com/channel/0029VaFE5Dv5Ejy2MaydYm3Z
    
    Follow Z-BL4CX-H4T:
    - Telegram Channel: https://t.me/Z_BL4CX_H4T
    """
    with open("readme.txt", "w") as readme_file:
        readme_file.write(readme_info)

    try:
        command = ['wget', '-r', '-np', '-nH', '--no-check-certificate', '--cut-dirs=2', '--no-parent', '--reject', 'index.html*', url_to_download]
        
        process = subprocess.Popen(
            command,
            shell=False,
            bufsize=1,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        # Display quotes while downloading
        while process.poll() is None:  # While the process is still running
            quote = random.choice(QUOTES)
            clear_screen()
            print_banner()
            print(f"\n{Color.ORANGE}[-] {Color.CYAN}Enjoy the quotes while downloading:{Color.ORANGE}[{Color.GREEN} {url_to_download}{Color.ORANGE}]\n\t{Color.CYAN}[+] {Color.ORANGE}{quote}\n")
            time.sleep(15)  # Adjust the delay as needed

        # Initialize progress bar after the download starts
        total_size = int(subprocess.check_output(['du', '-sb', folder_path]).split()[0].decode('utf-8'))
        with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024, desc='Downloading', ncols=None) as pbar:
            # Update progress bar after the download completes
            for line in iter(process.stdout.readline, ''):
                pbar.update(len(line.encode('utf-8')))

            process.communicate()  # Wait for the download to complete

        clear_screen()
        print_banner()
        if process.returncode == 0:
            print(f'{Color.RED} [-] {Color.GREEN}Download Complete')
            input()
        else:
            print(f"{Color.CYAN} [-] {Color.RED}Error during download. ")
            error_message = process.stderr.read()
            if error_message:
                print(error_message)
            else:
                print("No error details available.")
    except subprocess.CalledProcessError as e:
        clear_screen()
        print_banner()
        print(f"{Color.CYAN} [-] {Color.RED}Error during download: {e}")
    finally:
        os.chdir(os.getcwd())




def main_menu():
    while True:
        clear_screen()
        print_banner()
        user_choice = input(f"""
    {Color.GREEN}[1] {Color.RED}Enter 1 For Files
    {Color.GREEN}[2] {Color.RED}Enter 2 For About
    {Color.GREEN}[3] {Color.RED}Enter 3 For Exit {Color.CYAN}

    {Color.RED}[-] {Color.CYAN}""")

        if user_choice in {'1', '01'}:
            download_files()
        elif user_choice in {'2', '02'}:
            display_social_media_options()
        elif user_choice in {'3', '03'}:
            exit_program()

def exit_program():
    clear_screen()
    print_banner()
    print(f"{Color.RED}Goodbye! {Color.GREEN}Thanks for using FanticsParser.")
    exit()

if __name__ == "__main__":
    main_menu()

