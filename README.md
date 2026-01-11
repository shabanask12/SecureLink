🔐 SecureLink: ML-Based Phishing URL Detection

SecureLink is a machine learning system designed to detect phishing URLs by analyzing lexical features. Unlike traditional blacklist methods, it uses a Random Forest Classifier to predict the probability of a URL being malicious based on patterns, making it effective against zero-day phishing attacks.

The system prioritizes Recall over Accuracy to strictly minimize False Negatives (missed attacks).

🚀 Key Features

Real-Time Analysis: Extracts features from raw URL strings instantly.

Probability-Based Scoring: Returns a risk score (0–1) rather than a simple Yes/No.

Custom Sensitivity: Implements a tunable decision threshold (default > 0.3) for stricter security.

Hybrid Logic: Capable of combining ML predictions with rule-based overrides (IP checks, blacklists).

🧠 Machine Learning Approach

1. Feature Engineering

Raw text URLs are converted into numerical vectors. Key features include:

Feature Category

Examples Extracted

Structural

URL length, Domain length, Directory depth

Statistical

Count of digits, special chars (@, -, ?), subdomains

Keyword-based

Presence of "login", "verify", "secure", "bank"

Anomalies

IP address usage, Suspicious TLDs (.xyz, .cf)

2. Model Selection

We utilize a Random Forest Classifier because:

It handles non-linear relationships between URL features effectively.

It is robust against overfitting compared to single Decision Trees.

It provides reliable predict_proba() outputs for risk scoring.

3. Evaluation Strategy

Standard accuracy is misleading in security contexts. We focus on:

Recall: To ensure actual phishing links are caught.

F1-Score: To balance precision and recall in imbalanced datasets.

Thresholding: The classification threshold is set to 0.3 (instead of 0.5) to aggressively flag potential threats.

🛠️ Installation & Usage

Clone the repository:

git clone [https://github.com/yourusername/SecureLink.git](https://github.com/yourusername/SecureLink.git)
cd SecureLink


Install dependencies:

pip install -r requirements.txt


Generate Synthetic Dataset (Optional):

python app.py


Run the Detector:

python main.py


📂 Project Structure

SecureLink/
├── main.py            # CLI entry point for testing URLs
├── model.py           # Model training and prediction logic
├── features.py        # Feature extraction engine
├── app.py             # Synthetic data generator
├── data/              # Storage for training datasets
└── README.md          # Project documentation


🚀 Future Roadmap

[ ] Integration with Flask/FastAPI for REST API access.

[ ] Web Dashboard for visualizing threat metrics.

[ ] SHAP analysis to explain why a URL was flagged.

👤 Author

Shabana
Aspiring Software & Machine Learning Engineer
