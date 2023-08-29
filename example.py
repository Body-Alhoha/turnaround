from utils import solver
import time
from playwright.sync_api import sync_playwright
import concurrent.futures
import colorama

def solve_test():
    with sync_playwright() as playwright:
        s = solver.Solver(playwright, headless=False)
        while True:
            current_time = time.time()
            captcha = s.solve("https://modrinth.com/auth/sign-up", "0x4AAAAAAAHWfmKCm7cUG869", invisible=True) # using the same solver instance dispense us from launching a new browser every time
            if captcha == "failed":
                print(f"{colorama.Fore.WHITE}[{colorama.Fore.RED}-{colorama.Fore.WHITE}] Failed to solve captcha")
                continue
            print(f"{colorama.Fore.WHITE}[{colorama.Fore.GREEN}+{colorama.Fore.WHITE}] Solved {captcha[0:40]} in {colorama.Fore.GREEN}{time.time() - current_time}{colorama.Fore.WHITE} seconds")


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        for i in range(2):
            print(f"{colorama.Fore.WHITE}[{colorama.Fore.GREEN}+{colorama.Fore.WHITE}] Starting thread {colorama.Fore.GREEN}{i+1}{colorama.Fore.WHITE}")
            executor.submit(solve_test)
    
if __name__ == "__main__":
    main()