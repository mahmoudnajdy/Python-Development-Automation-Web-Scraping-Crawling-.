README — Task 1 (Automation Stealth Assessment)
# Task 1 — Automation Stealth Assessment

## Overview

This task focuses on automating interaction with a CAPTCHA-protected page and extracting the verification token using browser automation.

The implementation uses **Python with Playwright** to navigate to a Cloudflare Turnstile demo page, complete verification, submit the form, and retrieve the generated Turnstile token.

The script performs multiple attempts and calculates the final success rate of the automation process.

---

## Target Page


https://cd.captchaaiplus.com/turnstile.html


This page contains a **Cloudflare Turnstile CAPTCHA** widget that generates a verification token upon successful validation.

---

## Objectives

The automation script performs the following tasks:

- Launch the browser using Playwright
- Navigate to the Turnstile CAPTCHA demo page
- Wait for CAPTCHA verification
- Submit the form
- Extract the generated Turnstile token
- Repeat the process **10 times**
- Calculate the **final success rate**
- Demonstrate execution in **both headed and headless modes**

---

## Implementation Approach

The script follows this workflow:


Launch Browser
↓
Open Target Page
↓
Wait for CAPTCHA Verification
↓
Submit Form
↓
Extract Turnstile Token
↓
Repeat Process (10 Attempts)
↓
Calculate Success Rate


The Turnstile verification token is extracted from the hidden form field:


cf-turnstile-response


Example token:


0.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


---

## Example Output


Attempt 1: Success
Attempt 2: Success
Attempt 3: Failed
Attempt 4: Success
...
Final Success Rate: 70%


---

## Technologies Used

- Python
- Playwright
- Browser automation techniques

---

## How to Run

### Install dependencies

```bash
pip install playwright

Install browser binaries:

playwright install
Run the script
python task1.py
Notes

The success rate may vary depending on:

network conditions

browser fingerprinting

CAPTCHA verification behavior

Demonstration videos showing the automation attempts are included in the repository.

Outcome

The implementation successfully demonstrates automated interaction with a CAPTCHA-protected page and token extraction using Playwright automation.
