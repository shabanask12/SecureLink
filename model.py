import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

import features


class PhishingDetector:
    def __init__(self):
        self.model = RandomForestClassifier(
            n_estimators=200,
            max_depth=15,
            class_weight="balanced",
            random_state=42
        )
        self.scaler = StandardScaler()
        self.feature_extractor = features.FeatureExtractor()

    def prepare_features(self, urls):
        features_list = []
        for url in urls:
            extracted = self.feature_extractor.extract_features(url)
            features_list.append(extracted)
        return pd.DataFrame(features_list)

    def train(self, urls, labels):
        X = self.prepare_features(urls)

        X_train, X_test, y_train, y_test = train_test_split(
            X, labels, test_size=0.2, random_state=42
        )

        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        self.model.fit(X_train_scaled, y_train)

        y_pred = self.model.predict(X_test_scaled)
        report = classification_report(y_test, y_pred, zero_division=0)
        print(report)

        return report

    def predict(self, url):
        features = self.feature_extractor.extract_features(url)
        features_df = pd.DataFrame([features])

        features_scaled = self.scaler.transform(features_df)

        probability = self.model.predict_proba(features_scaled)[0][1]

        # 🔥 LOWER THRESHOLD
        is_phishing = probability > 0.3

        return {
            "is_phishing": is_phishing,
            "probability": probability,
            "features": features
        }

    def save_model(self, filepath="phishing_model.pkl"):
        joblib.dump(
            {
                "model": self.model,
                "scaler": self.scaler
            },
            filepath
        )
        print(f"Model saved to {filepath}")
