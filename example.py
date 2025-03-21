from utils import solver
import time
from playwright.sync_api import sync_playwright
import concurrent.futures
import colorama

colorama.init(autoreset=True)  # Ensures colors reset after each print statement

def solve_test():
    with sync_playwright() as playwright:
        s = solver.Solver(playwright, headless=False)
        while True:
            start_time = time.time()
            captcha = s.solve("https://modrinth.com/auth/sign-up", "0x4AAAAAAAHWfmKCm7cUG869", invisible=True)
            
            if captcha == "failed":
                print(f"[{colorama.Fore.RED}-{colorama.Fore.WHITE}] Failed to solve captcha")
                continue
            
            elapsed_time = round(time.time() - start_time, 2)
            print(f"[{colorama.Fore.GREEN}+{colorama.Fore.WHITE}] Solved {captcha[:40]} in {colorama.Fore.GREEN}{elapsed_time}{colorama.Fore.WHITE} seconds")

def main():
    num_threads = 2  # Define number of threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        for i in range(num_threads):
            print(f"[{colorama.Fore.GREEN}+{colorama.Fore.WHITE}] Starting thread {colorama.Fore.GREEN}{i+1}{colorama.Fore.WHITE}")
            executor.submit(solve_test)

if __name__ == "__main__":
    main()
