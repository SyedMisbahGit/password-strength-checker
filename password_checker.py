import re

def check_strength(password):
    strength = 0
    remarks = ""

    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    if strength <= 2:
        remarks = "Weak"
    elif strength == 3 or strength == 4:
        remarks = "Moderate"
    else:
        remarks = "Strong"

    return strength, remarks

if __name__ == "__main__":
    try:
        password = input("🔐 Enter your password: ")
        score, remark = check_strength(password)
        print(f"\nStrength Score: {score}/5 → {remark}")
    except KeyboardInterrupt:
        print("\n[!] Exiting program.")
