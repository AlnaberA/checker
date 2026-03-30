import requests
from bs4 import BeautifulSoup
import sys

URL = "https://housegardens.cranbrook.edu/events/photo-sessions"
TARGET_DATE = "June 7"

def check():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(URL, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text().lower()

    print("Checking page...")

    if TARGET_DATE.lower() in text:
        print(f"{TARGET_DATE} found on page")

        if "sold out" not in text:
            print(f"🚨 {TARGET_DATE} might be AVAILABLE!")

            # Exit with error so GitHub Actions can detect it
            sys.exit(1)
        else:
            print(f"{TARGET_DATE} is listed but sold out")
    else:
        print(f"{TARGET_DATE} not found")

    print("Done.")

if __name__ == "__main__":
    check()