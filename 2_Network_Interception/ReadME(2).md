# Task 2 — Network Interception

## Overview

This task demonstrates how to intercept and manipulate network requests using **Playwright**.

The goal is to prevent the Turnstile CAPTCHA from loading, capture its configuration parameters, and manually inject a previously captured token to complete verification.

---

## Target Page


https://cd.captchaaiplus.com/turnstile.html


This page loads a **Cloudflare Turnstile CAPTCHA** widget through an external script.

---

## Objectives

The implementation performs the following steps:

- Open the target page using Playwright
- Intercept network requests
- Detect the Turnstile script request
- Block the CAPTCHA script from loading
- Capture CAPTCHA configuration details
- Inject a valid Turnstile token captured from Task 1
- Submit the form and verify successful validation

---

## Key Concepts Demonstrated

- Network request interception
- Script blocking
- DOM manipulation
- Token injection

---

## Interception Workflow

The solution uses Playwright's request routing feature.

```
Browser Request
↓
Playwright Route Interception
↓
Detect Turnstile Script
↓
Abort Request
```

By blocking the CAPTCHA script, the widget never loads.

---

## Token Injection

Since the CAPTCHA is prevented from loading, the script manually injects a valid token into the hidden form field used by Turnstile.

Target field:


textarea[name="cf-turnstile-response"]


Example injected value:


0.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


After the token is injected, the form is submitted and the server validates the token successfully.

---

## Execution Flow

```
Launch Browser
↓
Intercept Turnstile Script
↓
Block CAPTCHA Loading
↓
Inject Valid Token
↓
Submit Form
↓
Verification Successful
```

---

## Technologies Used

- Python
- Playwright
- Network interception
- Browser automation

---

## How to Run

### Install dependencies

```bash
pip install playwright

Install browser binaries:

playwright install
Run the script
python task2.py
Demonstration

A demonstration video is included showing:

CAPTCHA script being blocked

Token injection

Successful verification after form submission

Outcome

This task demonstrates how browser automation tools can intercept and modify network behavior to control client-side flows and test CAPTCHA verification mechanisms.


---
