import hashlib
import base64

def generate_short_url(long_url: str, length: int = 6) -> str:
    """Generate a short URL from a long URL using Base62 encoding."""
    hash_obj = hashlib.md5(long_url.encode())  # Create hash
    base64_encoded = base64.urlsafe_b64encode(hash_obj.digest()).decode()  # Encode to Base64
    short_url = base64_encoded[:length]  # Trim to required length
    return short_url

if __name__ == "__main__":
    url = input("Enter a long URL: ")
    print("Short URL:", generate_short_url(url))
