import requests
def check_status(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.ConnectionError:
        return 503
    except requests.exceptions.Timeout:
        return 408
if __name__ == "__main__":
    url = "https://gruchi"
    status_code = check_status(url)
    print(status_code)
