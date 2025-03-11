import requests
import time


def stop_server(server_url):
    try:
        response = requests.get(server_url)
        if response.status_code == 200:
            print(f"Server at {server_url} stopped successfully.")
        else:
            print(f"Error: Server at {server_url} returned status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error trying to stop the server at {server_url}: {e}")

        if __name__ == '__main__':
            stop_server('http://127.0.0.1:5000/stop_server')
            time.sleep(2)
            'http://127.0.0.1:5001/stop_server'
