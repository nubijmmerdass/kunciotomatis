Penjelasan:

lock_time: Waktu dalam detik sebelum komputer dikunci.
lock_computer: Fungsi yang mengunci komputer menggunakan fungsi LockWorkStation dari ctypes.windll.user32.
reset_timer: Fungsi yang mengatur ulang timer setiap kali ada aktivitas dari pengguna.
main: Fungsi utama yang membuat timer dan memeriksa input dari pengguna setiap detik. Jika ada aktivitas, timer akan diatur ulang. Jika pengguna menghentikan program dengan Ctrl+C, timer akan dibatalkan.
Catatan:

Program ini menggunakan fungsi LockWorkStation, yang hanya tersedia di sistem operasi Windows. Jika Anda menggunakan sistem operasi lain, Anda perlu mencari metode yang sesuai untuk mengunci komputer di sistem operasi tersebut.
Untuk pengguna non-Windows, mungkin perlu menggunakan modul atau library tambahan yang sesuai dengan sistem operasi yang digunakan.
