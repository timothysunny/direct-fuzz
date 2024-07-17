import requests
import argparse
from termcolor import colored
from tqdm import tqdm
import re

def load_wordlist(path):
    try:
        with open(path, 'r') as file:
            return [line.strip() for line in file]
    except Exception as e:
        print(f"Error loading wordlist: {e}")
        exit(1)

def direct_brute(url, word, useragent):
    directory = f"{url.rstrip('/')}/{word}"
    headers = {"User-Agent": useragent} if useragent else {}
    try:
        r = requests.get(directory, headers=headers)
        size_kb = len(r.content) / 1024
        status_code = r.status_code
        if status_code in [200, 201, 204]:
            return colored(f'Status: {status_code}, Size: {size_kb:.2f} KB - /{word}', 'green')
        elif status_code in [301, 302, 307]:
            return colored(f'Status: {status_code}, Size: {size_kb:.2f} KB - /{word}', 'yellow')
        elif status_code in [400, 401, 403, 405, 429]:
            return colored(f'Status: {status_code}, Size: {size_kb:.2f} KB - /{word}', 'red')
        elif status_code in [500, 502, 503, 504]:
            return colored(f'Status: {status_code}, Size: {size_kb:.2f} KB - /{word}', 'magenta')
    except requests.RequestException as e:
        return colored(f'Error: {e} - /{word}', 'magenta')
    return None

def save_output(output, filename):
    if filename:
        with open(filename, 'a') as file:
            file.write(output + '\n')

def remove_color_codes(text):
    return re.sub(r'\x1b\[[0-9;]*m', '', text)

def print_header():
    print(colored(r"""
______ ___________ _____ _____ _____  ______ _   _  ______ ______
|  _  \_   _| ___ \  ___/  __ \_   _| |  ___| | | ||___  /|___  /
| | | | | | | |_/ / |__ | /  \/ | |   | |_  | | | |   / /    / / 
| | | | | | |    /|  __|| |     | |   |  _| | | | |  / /    / /  
| |/ / _| |_| |\ \| |___| \__/\ | |   | |   | |_| |./ /___./ /___
|___/  \___/\_| \_\____/ \____/ \_/   \_|    \___/ \_____/\_____/                                                                                                       
    """, 'cyan'))
    print(colored("DIRECT FUZZ v.01", 'yellow'))
    print(colored("Usage: python direct_blow.py -u <URL> -w <wordlist> [--user-agent <USER_AGENT>] [-o <output_file>]", 'yellow'))
    print("\n" + "="*60 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Brute Forcer")
    parser.add_argument("-u", "--url", required=True, help="URL")
    parser.add_argument("-w", required=True, help="Wordlist")
    parser.add_argument("--user-agent", required=False, help="User-Agent")
    parser.add_argument("-o", "--output", required=False, help="Output") 

    args = parser.parse_args()

    print_header()
    wordlist = load_wordlist(args.w)
    try:
        if args.output:
            open(args.output, 'w').close()  
        results = []
        with tqdm(total=len(wordlist), desc="Progress", unit="req") as pbar:
            for word in wordlist:
                result = direct_brute(args.url, word, args.user_agent)
                if result:
                    results.append(result)
                    tqdm.write(result)
                    if args.output:
                        save_output(remove_color_codes(result), args.output)
                pbar.update(1)
        if args.output:
            with open(args.output, 'w') as file:
                file.write("\n".join(remove_color_codes(result) for result in results))
    except KeyboardInterrupt:
        print(colored("\nPROCESS ENDED BY USER.", 'red'))
    except requests.RequestException:
        print("Check Connection")

if __name__ == "__main__":
    main()
