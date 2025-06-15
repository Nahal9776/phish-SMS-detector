from detector.classify import is_phishing

print("Phish SMS Detector")
print("-------------------")

while True:
    msg = input("Enter SMS text (or 'q' to quit): ")
    if msg.lower() == 'q':
        break

    if is_phishing(msg):
        print("⚠️  This message is likely a phishing attempt.")
    else:
        print("✅  This message appears to be safe.")

