🔐 SecureLink: ML-Based Phishing URL Detection System

SecureLink is a machine learning–driven system for detecting phishing URLs by analyzing lexical and structural patterns in URLs.
Unlike traditional blacklist-based approaches, SecureLink leverages a Random Forest Classifier to identify malicious links, making it effective against zero-day phishing attacks.

The system is designed with a security-first mindset, prioritizing Recall over Accuracy to minimize False Negatives (missed phishing threats).

🚀 Key Features

Real-Time URL Analysis
Instantly extracts features from raw URL strings without external lookups.

Probability-Based Risk Scoring
Outputs a phishing probability score (0–1) instead of a binary decision.

Configurable Sensitivity
Uses a tunable decision threshold (default: 0.3) to aggressively flag suspicious URLs.

Hybrid Detection Logic
Supports integration of ML predictions with rule-based checks (e.g., IP-based URLs, known blacklists).

🧠 Machine Learning Approach
1. Feature Engineering

Raw URLs are transformed into numerical feature vectors. Extracted features include:

Feature Category	Examples
Structural	URL length, domain length, directory depth
Statistical	Count of digits, special characters (@, -, ?), number of subdomains
Keyword-Based	Presence of terms like login, verify, secure, bank
Anomalies	IP-based URLs, suspicious TLDs (.xyz, .cf)
2. Model Selection

A Random Forest Classifier is used because:

It captures non-linear relationships between URL features effectively

It is less prone to overfitting compared to single decision trees

It provides reliable predict_proba() outputs for probabilistic risk scoring

3. Evaluation Strategy

In cybersecurity applications, accuracy alone is misleading. SecureLink emphasizes:

Recall – to ensure phishing URLs are not missed

F1-Score – to balance precision and recall on imbalanced datasets

Threshold Tuning – classification threshold set to 0.3 (instead of 0.5) for stricter detection

🛠️ Installation & Usage
Clone the Repository
git clone https://github.com/shabanask12/SecureLink.git
cd SecureLink

Install Dependencies
pip install -r requirements.txt

(Optional) Generate Synthetic Dataset
python app.py

Run the Phishing Detector
python main.py

📂 Project Structure
SecureLink/
├── main.py        # CLI entry point for URL testing
├── model.py       # Model training and prediction logic
├── features.py    # URL feature extraction engine
├── app.py         # Synthetic dataset generator
├── data/          # Training and test datasets
└── README.md      # Project documentation

🚀 Future Enhancements

 REST API integration using Flask or FastAPI

 Web dashboard for phishing analytics and visualization

 SHAP-based explainability for model predictions

👤 Author

Shabana
Software Engineer & Machine Learning Practitioner
