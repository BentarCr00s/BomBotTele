import requests
import threading

def send_message():
    url = ""
    params = {
        'parse_mode': 'markdown',
        'chat_id': '',
        'text': 'Jangan Jadi Penipu Bang Mening kita Ngobrol'
    }

    response = requests.post(url, params=params)

    print(response.status_code)
    print(response.json())

# Define the number of threads and loops
num_threads = 100
num_loops = 100

# Create threads
threads = []

for _ in range(num_threads):
    thread = threading.Thread(target=send_message)
    threads.append(thread)

# Start threads
for thread in threads:
    thread.start()

# Join threads (wait for all threads to finish)
for thread in threads:
    thread.join()
