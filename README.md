# turnaround
Utilizes [playwright](https://playwright.dev/) to automatically solve [Turnstile](https://www.cloudflare.com/products/turnstile/)

## Installation
pip install -r requirements.txt

## Usage
```py
with sync_playwright() as playwright:
    s = solver.Solver(playwright, headless=False) # creates a new solver object
    captcha = s.solve("https://modrinth.com/auth/sign-up", "0x4AAAAAAAHWfmKCm7cUG869", invisible=True) # first argument is the website url & second one is the website sitekey
    # s.solve will return "failed" if it failed to solve the captcha.
    print(captcha)
    s.terminate() # terminates the browser
```


If you want to use the solver in a loop, keep the same solver object and use it over again to not instantiate a new browser each time, look at [example.py](https://github.com/Body-Alhoha/turnaround/blob/main/example.py)

Feel free to contribute
