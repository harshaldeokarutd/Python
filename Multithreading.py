import requests
from threading import Thread, Lock
import json
import time


def search_and_count(url, count_dict):
    response = requests.get(url)
    print('fetching data from ' + url)
    text = json.dumps(response.text)

    mutex.acquire()  # Lock the shared dictionary
    for i in text:
        if i in count_dict:
            count_dict[i] += 1
    mutex.release()  # Release the lock


if __name__ == "__main__":
    mutex = Lock()  # Mutex for thread-safe dictionary updates
    start = time.time()

    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    alphabets_dict = {ch: 0 for ch in alphabets}  # Initialize the dictionary

    # Create and start threads
    threads = []
    for i in range(1000, 1021):
        url = f'https://www.rfc-editor.org/rfc/rfc{i}.txt'
        thread = Thread(target=search_and_count, args=(url, alphabets_dict))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    end = time.time()

    print(alphabets_dict)  # Print the final count dictionary
    print("Done, time taken:", end - start)