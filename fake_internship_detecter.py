def detect_fake_internship(message):
    suspicious_keywords = [
        "registration fee",
        "security deposit",
        "pay to apply",
        "limited seats",
        "urgent",
        "immediate joining",
        "earn money fast",
        "whatsapp only",
        "no interview",
        "guaranteed placement"
    ]

    suspicious_domains = [
        "@gmail.com",
        "@yahoo.com",
        "@outlook.com"
    ]

    risk_score = 0
    reasons = []
    msg_lower = message.lower()

    for word in suspicious_keywords:
        if word in msg_lower:
            risk_score += 2
            reasons.append(f"Suspicious phrase detected: '{word}'")
    if "@" in msg_lower:
        for domain in suspicious_domains:
            if domain in msg_lower:
                risk_score += 1
                reasons.append("Uses free email domain")

    if risk_score >= 6:
        risk_level = "HIGH RISK"
    elif risk_score >= 3:
        risk_level = "MEDIUM RISK"
    else:
        risk_level = "LOW RISK"

    return risk_level, reasons

print("=== Fake Internship Offer Detector ===\n")
message = input("Paste internship message/email:\n\n")
risk, reasons = detect_fake_internship(message)
print("\nAnalysis Result")
print("Risk Level:", risk)

if reasons:
    print("Reasons:")
    for r in reasons:
        print("-", r)
else:
    print("No major suspicious patterns detected.")