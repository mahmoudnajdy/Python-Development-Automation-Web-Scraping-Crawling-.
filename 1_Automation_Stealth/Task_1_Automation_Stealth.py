from seleniumbase import SB
from playwright.sync_api import sync_playwright
import time

URL = "https://cd.captchaaiplus.com/turnstile.html"

turnstile_tokens =[]

with SB(uc=True, headed=True) as sb:

    # launch undetected browser
    driver = sb.driver

    # get debugging port
    port = driver.capabilities["goog:chromeOptions"]["debuggerAddress"]

    with sync_playwright() as p:
        
        for i in range(1,11):

            browser = p.chromium.connect_over_cdp(f"http://{port}")
            context = browser.contexts[0]
            page = context.pages[0]
            page.goto(URL)
            
            page.mouse.move(300,300)  ######
            page.mouse.move(600,400)  ########
            page.wait_for_timeout(2000)  ##########
            time.sleep(5)
            
            butto = page.wait_for_selector("input[value='Submit']")
            butto.click()
            time.sleep(5)
            
            token = page.locator("[name='cf-turnstile-response']").input_value()
            turnstile_tokens.append(token)

            
            
for i,tok in enumerate(turnstile_tokens) :
    print("#"*100)
    print(f"Tok_num[{i+1}]=>{tok}")
    
print("@"*100)
print(f"############# Success rate is => [[{(len(turnstile_tokens)/10 )*100} %]] #############")