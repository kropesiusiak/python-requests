# https://github.com/kropesiusiak/python-requests

import requests
import time

def send_request(url, headers, counter):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(f"Request {counter} successful! Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending request {counter}: {e}")

def main():
    target_url = input("Enter the target URL: ")
    num_requests = int(input("Enter the number of requests to send: "))
    delay_seconds = float(input("Enter the delay between requests (in seconds): "))
    
    # You can customize headers based on your needs
    headers = {
        'User-Agent': 'Your User Agent',
        'Content-Type': 'application/json',  # Modify content type if needed
    }

    for i in range(1, num_requests + 1):
        send_request(target_url, headers, i)
        time.sleep(delay_seconds)  # Add delay between requests

if __name__ == "__main__":
    main()
