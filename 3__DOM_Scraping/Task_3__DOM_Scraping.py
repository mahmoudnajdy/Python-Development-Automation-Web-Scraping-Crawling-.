from playwright.sync_api import sync_playwright
import requests
import base64
import json

all_images_base64 = []
visible_images_base64 = []
visible_texts = []

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # open the website
    page.goto(r"https://egypt.blsspainglobal.com/Global/CaptchaPublic/GenerateCaptcha?data=4CDiA9odF2%2b%2bsWCkAU8htqZkgDyUa5SR6waINtJfg1ThGb6rPIIpxNjefP9UkAaSp%2fGsNNuJJi5Zt1nbVACkDRusgqfb418%2bScFkcoa1F0I%3d")

    page.wait_for_load_state("networkidle")

    # get all image elements
    images = page.locator("img").all()

    for img in images:

        src = img.get_attribute("src")
        
        ###########################
        if src:

            if src.startswith("data:image"):

                img_base64 = src.split(",")[1]
                all_images_base64.append(img_base64)

                if img.is_visible():
                    visible_images_base64.append(img_base64)

            elif src.startswith("http"): # as there is any http

                response = requests.get(src)
                img_base64 = base64.b64encode(response.content).decode("utf-8")

                all_images_base64.append(img_base64)

                if img.is_visible():
                    visible_images_base64.append(img_base64)
        
    # save all images
    with open(r"E:\ABM_Task_solution_repo\Task_3__DOM_Scraping\allimages.json", "w") as f:
        json.dump(all_images_base64, f)

    # save visible images
    with open(r"E:\ABM_Task_solution_repo\Task_3__DOM_Scraping\visible_images_only.json", "w") as f:
        json.dump(visible_images_base64, f)

    # extract visible text instructions
    texts = page.locator("body *").all()

    for element in texts:

        try:
            if element.is_visible():

                text = element.inner_text().strip()

                if text:
                    visible_texts.append(text)

        except:
            pass

    with open(r"E:\ABM_Task_solution_repo\Task_3__DOM_Scraping\visible_texts.json", "w") as f:
        json.dump(visible_texts, f)

    browser.close()