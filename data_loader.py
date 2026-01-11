import os
import pandas as pd


def preprocess_url(url):
    if not url:
        return ""
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
    return url.lower().strip()


def load_data():
    base_dir = os.path.dirname(__file__)

    # 🔥 LOOK FOR FILE IN PROJECT ROOT FIRST
    possible_paths = [
        os.path.join(base_dir, "data", "phishing_urls.csv.xlsx"),
        os.path.join(base_dir, "data", "phishing_urls.xlsx"),
        os.path.join(base_dir, "phishing_urls.xlsx"),
        os.path.join(base_dir, "phishing_urls.csv"),
    ]

    file_path = None
    for path in possible_paths:
        if os.path.exists(path):
            file_path = path
            break

    print("Checked paths:")
    for p in possible_paths:
        print(" -", p, "=>", os.path.exists(p))

    if file_path is None:
        raise FileNotFoundError("❌ Dataset file not found anywhere. Move it into SecureLink or SecureLink/data")

    print("✅ Using dataset:", file_path)

    # Read Excel or CSV automatically
    if file_path.endswith(".xlsx"):
        data = pd.read_excel(file_path)
    else:
        data = pd.read_csv(file_path)

    data.columns = ["label", "url"]

    print("Total URLs loaded:", len(data))
    print(data["label"].value_counts())

    return data["url"].tolist(), data["label"].tolist()
