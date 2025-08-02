# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 00:45:07 2025

@author: ashai
"""

import re

PHISHING_KEYWORDS = [
    "verify your account",
    "update your bank details",
    "your mtn momo account will be blocked",
    "click here to claim your prize",
    "suspicious login attempt",
    "ghana revenue authority",
    "bank of ghana",
    "login immediately",
    "you have won",
    "urgent attention required"
]

SUSPICIOUS_DOMAINS = [
    "ghananationalbank-update.com",
    "momo-security-check.net",
    "ghrevenue-service.org",
    "bog-support.xyz",
    "mtn-cashbonus.click"
]

def detect_phishing(text):
    detected_keywords = []
    for keyword in PHISHING_KEYWORDS:
        if re.search(re.escape(keyword), text, re.IGNORECASE):
            detected_keywords.append(keyword)

    found_urls = re.findall(r'https?://[^\s]+', text)
    flagged_urls = [url for url in found_urls if any(domain in url for domain in SUSPICIOUS_DOMAINS)]

    return detected_keywords, flagged_urls

# ✅ Test example in Jupyter or interactive environment
test_text = """
Dear Customer,

Due to unusual activity, your MTN MoMo account will be blocked within 24 hours.
To avoid this, please verify your account here:
https://mtn-cashbonus.click/verify-now

Sincerely,
MTN Security Team
"""

keywords, urls = detect_phishing(test_text)

print("\n🔍 Phishing Scan Report (Ghana Edition):\n")

if keywords:
    print("⚠️ Suspicious Keywords Found:")
    for kw in keywords:
        print(f" - {kw}")
else:
    print("✅ No suspicious keywords found.")

if urls:
    print("\n⚠️ Suspicious URLs Detected:")
    for url in urls:
        print(f" - {url}")
else:
    print("\n✅ No suspicious URLs found.")
