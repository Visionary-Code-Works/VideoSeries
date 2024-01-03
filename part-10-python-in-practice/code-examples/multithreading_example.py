# multithreading_example.py

import threading
import time

def print_numbers():
    """ Function to print numbers from 1 to 5 """
    for i in range(1, 6):
        time.sleep(1)
        print(f"Number: {i}")

def print_letters():
    """ Function to print letters from A to E """
    for letter in ['A', 'B', 'C', 'D', 'E']:
        time.sleep(1.5)
        print(f"Letter: {letter}")

def main():
    # Creating threads
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    # Starting threads
    thread1.start()
    thread2.start()

    # Joining threads: Wait for threads to complete before finishing main thread
    thread1.join()
    thread2.join()

    print("Finished Multithreading Example")

if __name__ == '__main__':
    main()
