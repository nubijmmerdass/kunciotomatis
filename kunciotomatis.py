import ctypes
import time
from threading import Timer

# Waktu dalam detik sebelum komputer dikunci (misalnya 300 detik = 5 menit)
lock_time = 300

def lock_computer():
    # Mengunci komputer menggunakan sistem Windows
    ctypes.windll.user32.LockWorkStation()

def reset_timer():
    global timer
    timer.cancel()
    timer = Timer(lock_time, lock_computer)
    timer.start()

def main():
    global timer
    timer = Timer(lock_time, lock_computer)
    timer.start()

    try:
        while True:
            # Memeriksa input dari pengguna setiap detik
            time.sleep(1)
            reset_timer()
    except KeyboardInterrupt:
        timer.cancel()
        print("Program dihentikan oleh pengguna.")

if __name__ == "__main__":
    main()
