import re
from urllib.parse import urlparse
import data_loader as utils


class FeatureExtractor:
    def __init__(self):
        self.trusted_domains = {
            "google.com", "youtube.com", "github.com",
            "microsoft.com", "amazon.com", "facebook.com",
            "twitter.com", "linkedin.com", "apple.com"
        }

    def extract_features(self, url):
        url = utils.preprocess_url(url)
        parsed = urlparse(url)
        domain = parsed.netloc.lower()

        if domain.startswith("www."):
            domain = domain[4:]

        subdomain_count = len(domain.split(".")) - 1

        features = {
            "domain_length": len(domain),
            "is_trusted_domain": domain in self.trusted_domains,
            "subdomain_count": subdomain_count,
            "has_www": parsed.netloc.startswith("www."),

            "url_length": len(url),
            "path_length": len(parsed.path),
            "query_length": len(parsed.query),
            "fragment_length": len(parsed.fragment),
            "path_depth": len([x for x in parsed.path.split("/") if x]),

            "dots_count": domain.count("."),
            "digits_count": sum(c.isdigit() for c in url),
            "special_chars_count": sum(not c.isalnum() for c in url),

            "has_ip_address": bool(re.match(r"\d+\.\d+\.\d+\.\d+", domain)),
            "has_at_symbol": "@" in url,
            "has_double_slash": "//" in parsed.path,
            "has_dash_in_domain": "-" in domain,
            "has_https": url.startswith("https://"),

            "has_suspicious_words": self._check_suspicious_words(url),
            "excessive_subdomains": subdomain_count > 3,
            "suspicious_tld": self._check_suspicious_tld(domain),
        }

        return features

    def _check_suspicious_words(self, url):
        suspicious = [
            "login", "signin", "verify", "secure", "account",
            "update", "confirm", "banking", "password", "credential"
        ]
        url = url.lower()
        return any(word in url for word in suspicious)

    def _check_suspicious_tld(self, domain):
        suspicious_tlds = {".tk", ".ml", ".ga", ".cf", ".gq", ".xyz"}
        return any(domain.endswith(tld) for tld in suspicious_tlds)
