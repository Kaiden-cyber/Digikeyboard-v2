# Digikeyboard-v2

A second-generation C2 (Command and Control) server project for Digispark that completely overhauls server and client connections by routing requests through HTTP.

*If you want to check out v1 click [here](https://github.com/Kaiden-cyber/DigiKeyboard-project)*

**DISCLAIMER**: This project is purely for educational purposes. I do not condone the use of this code for malicious intent.

## Overview

### How It Works

The victim computer pings the server every second (configurable to prevent system overload) to check for new commands. When the client computer sends a command to the server, it's stored on a webpage with a random MD5 hash identifier.

**Key Features:**
- **Hidden endpoints**: Random hash values hide webpages from wordlist scanners
- **Stealth homepage**: AI-generated retro website homepage disguises the C2 server
- **Cross-network communication**: Commands can be sent across networks globally

## Improvements Over v1

**v1 Limitations:**
- Only worked on the same local network
- No directory persistence between commands
- No server logging

**v2 Enhancements:**
- **Global access**: Free hosting via Cloudflare tunnel enables worldwide command sending
- **Directory persistence**: Maintains directories across commands for improved shell experience
- **Server logging**: Monitors and stores all server requests

## Known Drawbacks

- **Detection risk**: The Python code on victim systems will trigger security alarms with proper controls in place
  - *Note*: This program is designed for educational purposes, not malicious use
- **Data exposure**: If secret webpages are discovered, all stored information is visible in plaintext

## Setup Instructions

### Prerequisites

Install the following on the server computer (can be the same as client computer):
- `fastapi`
- `uvicorn`
- Cloudflare tunnels

### Installation Steps

1. **Start the FastAPI server with logging:**
```bash
   uvicorn main:app --host 127.0.0.1 --port 8000 --log-level info 2>&1 | tee Logs/fastapi_$(date +%Y-%m-%d_%H-%M-%S).log
```

2. **Create a public URL with Cloudflare:**
```bash
   cloudflared tunnel --url http://localhost:8000
```

3. **Deploy victim code:**
   - Install the victim code on the target computer
   - Run the victim script

4. **Run client code:**
   - Run the python client file
   - Send your commands

---
