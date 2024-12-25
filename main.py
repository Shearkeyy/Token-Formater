import base64, json
from colorama import Fore, init
init()

formatter = str(input(f"{Fore.YELLOW}Enter The Formatter You Want In Between Email and Email's Password: {Fore.RESET}"))
tokens = [line.rstrip("\n") for line in open("tokens.txt", "r")]
for token in tokens:
    splited = token.split(":")
    email_data = splited[0]
    decoded_bytes = json.loads(base64.b64decode(email_data).decode("utf-8"))
    email = decoded_bytes["email"]
    email_password = decoded_bytes["password"]
    password = splited[1]
    token = splited[2]
    
    with open("formatted.txt","a") as f:
        f.write(f"{email}{formatter}{email_password}:{password}:{token}" +"\n")
        f.close()
input(f"\n{Fore.MAGENTA}FORMATTED!{Fore.RESET} PRESS ENTER TO EXIT!")