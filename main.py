import data_loader as utils
from model import PhishingDetector


def main():
    urls, labels = utils.load_data()

    detector = PhishingDetector()
    detector.train(urls, labels)
    detector.save_model()

    while True:
        url = input("\nEnter URL (or 'quit' to exit): ")
        if url.lower() == "quit":
            break

        url = utils.preprocess_url(url)
        result = detector.predict(url)

        print("-------------------")
        print(f"Is it phishing: {result['is_phishing']}")
        print(f"Probability: {result['probability']:.2f}")


if __name__ == "__main__":
    main()
