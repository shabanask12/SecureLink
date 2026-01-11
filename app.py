import random
import pandas as pd

# Output file
OUTPUT_FILE = "phishing_urls.xlsx"

# Counts
TOTAL_URLS = 5000
PHISHING_COUNT = TOTAL_URLS // 2
SAFE_COUNT = TOTAL_URLS // 2

# Patterns
suspicious_words = [
    "login", "verify", "secure", "account",
    "update", "confirm", "banking", "password"
]

fake_domains = [
    "facebook", "google", "paypal", "amazon",
    "microsoft", "apple", "linkedin"
]

suspicious_tlds = [".xyz", ".cf", ".ml", ".tk", ".ga"]

safe_domains = [
    "google.com", "github.com", "amazon.in",
    "microsoft.com", "apple.com", "linkedin.com",
    "wikipedia.org", "openai.com"
]

data = []

# -------------------------
# Generate PHISHING URLs
# -------------------------
for _ in range(PHISHING_COUNT):
    domain = random.choice(fake_domains)
    word = random.choice(suspicious_words)
    tld = random.choice(suspicious_tlds)

    url_type = random.choice(["domain", "ip", "subdomain"])

    if url_type == "domain":
        url = f"http://{domain}-{word}-support{tld}/login"
    elif url_type == "subdomain":
        url = f"http://{word}.secure.{domain}.account{tld}/verify"
    else:  # IP based
        ip = f"{random.randint(10,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
        url = f"http://{ip}/{word}"

    data.append([1, url])

# -------------------------
# Generate SAFE URLs
# -------------------------
for _ in range(SAFE_COUNT):
    domain = random.choice(safe_domains)
    path = random.choice(["", "/about", "/docs", "/blog", "/products"])
    protocol = random.choice(["https://", "http://"])

    url = f"{protocol}{domain}{path}"
    data.append([0, url])

# Shuffle dataset
random.shuffle(data)

# Create DataFrame
df = pd.DataFrame(data, columns=["label", "url"])

# Save to Excel
df.to_excel(OUTPUT_FILE, index=False)

print(f"✅ Dataset created: {OUTPUT_FILE}")
print(f"Total URLs: {len(df)}")
print(df["label"].value_counts())
