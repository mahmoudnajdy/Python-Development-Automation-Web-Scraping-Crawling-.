# Python-Development-Automation-Web-Scraping-Crawling-.

This repository contains solutions for an automation and system design assessment.  
The tasks focus on browser automation, network interception, DOM analysis, and distributed system architecture.

The implementation primarily uses **Playwright with Python**.

---

# Repository Structure
```
automation-assessment/
│
├── 1_automation_stealth/
│   ├── task1.py
│   └── README.md
│
├── 2_network_interception/
│   ├── task2.py
│   └── README.md
│
├── 3_dom_scraping/
│   ├── task3.py
│   ├── allimages.json
│   ├── visible_images_only.json
│   └── visible_texts.json
└── README.md
```

Each task is organized in a separate directory to keep the implementation clean and easy to review.

---

Environment Setup
=================

Requirements
------------

*   Python 3.10+
    
*   Playwright
    
*   Requests
    

Install dependencies:

```   
pip install playwright requests
 ```

Install Playwright browsers:

```  
playwright install
 ```

Task 1 — Automation & Stealth Assessment
========================================

Objective
---------

Automate interaction with a Turnstile CAPTCHA demo page and retrieve the verification token using **Playwright**.

Target page:

```  
https://cd.captchaaiplus.com/turnstile.html 
```

Key Requirements
----------------

*   Run in **headless and headed modes**
    
*   Complete verification
    
*   Extract Turnstile token
    
*   Retry **10 attempts**
    
*   Achieve **≥60% success rate**
    
*   Record video demonstration
    

Implementation Approach
-----------------------

The script performs the following steps:

1.  Launch Chromium using Playwright
    
2.  Navigate to the Turnstile demo page
    
3.  Wait for CAPTCHA verification
    
4.  Submit the form
    
5.  Extract the Turnstile token from the hidden field:
    

```
cf-turnstile-response
```

1.  Repeat the process 10 times
    
2.  Compute the final success rate
    

### Example Output
```
Attempt 1: Success
Attempt 2: Success
Attempt 3: Failed
 ...
Success Rate: 70%
```

Task 2 — Network Interception
=============================

Objective
---------

Demonstrate network interception by preventing the Turnstile CAPTCHA from loading and injecting a valid token captured from Task 1.

Key Concepts
------------

*   Request interception
    
*   Script blocking
    
*   Token injection
    
*   DOM manipulation
    

Implementation
--------------

The solution intercepts network requests using Playwright's routing system.

The CAPTCHA script from **Cloudflare** is blocked before loading.

Example logic:

```
Intercept request
        ↓
Detect Turnstile script
        ↓
Abort request  
```

Once the CAPTCHA is prevented from loading:

1.  Extract relevant parameters
    
2.  Inject a valid token into:
    

```
textarea[name="cf-turnstile-response"]  
```

1.  Submit the form
    
2.  Confirm successful verification
    

This demonstrates the ability to manipulate client-side CAPTCHA flows for testing purposes.

Task 3 — DOM Scraping & Data Extraction
=======================================

Objective
---------

Extract CAPTCHA-related resources from a dynamically generated page and convert them to structured data.

Target endpoint:

```
https://egypt.blsspainglobal.com/...GenerateCaptcha  
```

Extracted Data
--------------

The script collects:

1.  **All images on the page**
    
2.  **Visible images only**
    
3.  **Visible text instructions**
    

Data Processing
---------------

Images are converted to **Base64 encoding** and stored in JSON format.

Example output files:

```
allimages.json
visible_images_only.json
visible_texts.json 
```

Example JSON structure:
```
[
"iVBORw0KGgoAAAANSUhEUgAA...",    "R0lGODlhPQBEAPeoAJosM..."
  ]  
```
This approach ensures images can be stored and processed independently of the original source.


Key Technologies Used
=====================

*   **Playwright**
    
*   **Python**

*   JSON data processing
    
*   Browser network interception
    
*   Distributed system architecture
    

Notes
=====

Some automation steps may behave differently depending on:

*   network conditions
    
*   browser fingerprinting
    
*   CAPTCHA detection heuristics
    

The implementation demonstrates the core technical concepts required for the tasks.

Author
======

Automation assessment implementation using Python and Playwright.
