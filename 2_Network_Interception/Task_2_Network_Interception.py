from playwright.sync_api import sync_playwright
from valid_token_from_Task_1 import VAL_TOKEN

URL = "https://cd.captchaaiplus.com/turnstile.html"

# token captured from TASK 1
VALID_TOKEN = f"{VAL_TOKEN()}"

def intercept_turnstile(route, request):

    if "challenges.cloudflare.com/turnstile" in request.url:

        print("Turnstile blocked:", request.url)

        route.abort()

    else:

        route.continue_()


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    # intercept requests
    page.route("**/*", intercept_turnstile)

    # capture console logs
    page.on("console", lambda msg: print("Console:", msg.text))

    page.goto(URL)

    page.wait_for_timeout(3000)

    print("Page loaded without captcha")

    # inject token into hidden textarea
    page.evaluate(f"""
        () => {{
            let textarea = document.querySelector('[name="cf-turnstile-response"]');

            if(!textarea){{
                textarea = document.createElement("textarea");
                textarea.name = "cf-turnstile-response";
                textarea.style.display = "none";
                document.body.appendChild(textarea);
            }}

            textarea.value = "{VALID_TOKEN}";
        }}
    """)

    print("Token injected")

    # click submit
    # page.click("button[type='submit']")
    butto = page.wait_for_selector("input[value='Submit']")
    butto.click()

    page.wait_for_timeout(10000)

    print("Check page for success message")

    browser.close()