
# Snake Game

## Abstrak
Proyek ini adalah implementasi permainan Snake menggunakan bahasa pemrograman Python dengan bantuan modul Pygame untuk grafis dan modul Tkinter untuk dialog pop-up. Permainan ini mengikuti aturan klasik Snake, di mana pemain mengontrol ular yang bergerak di sekitar layar untuk memakan apel yang muncul secara acak. Setiap kali ular memakan apel, panjang ular bertambah dan skor pemain meningkat. Pemain harus menghindari menabrak dinding atau tubuh ular sendiri, yang akan menyebabkan permainan berakhir. Dalam kondisi Game Over, pemain diberikan opsi untuk keluar dari permainan atau memulai kembali. Penggunaan Tkinter memberikan antarmuka dialog yang interaktif saat pemain memilih untuk keluar dari permainan.

##Bahasa Pemrograman
Python: Bahasa utama yang digunakan untuk mengembangkan permainan ini. Python dipilih karena kemudahan penggunaannya dan ketersediaan pustaka yang kuat untuk pengembangan permainan dan antarmuka grafis.
Tools yang Digunakan
Pygame: Sebuah modul Python yang digunakan untuk membuat aplikasi multimedia dan permainan. Pygame menyediakan berbagai fungsi untuk menangani grafik, suara, dan input dari pemain.

Tkinter: Pustaka standar Python untuk membuat antarmuka pengguna grafis (GUI). Dalam proyek ini, Tkinter digunakan untuk menampilkan dialog konfirmasi saat pemain memilih untuk keluar dari permainan.

Random: Modul standar Python yang digunakan untuk menghasilkan posisi apel secara acak di dalam permainan.

##Dokumentasi
Inisialisasi dan Pengaturan Layar
pygame.init(): Inisialisasi semua modul Pygame.
screen_width dan screen_height: Menentukan ukuran layar permainan.
gameDisplay = pygame.display.set_mode((screen_width, screen_height)): Mengatur tampilan layar dengan ukuran yang telah ditentukan.
pygame.display.set_caption('Snake Game'): Memberikan judul pada jendela permainan.
Warna dan Ukuran Blok
Warna yang digunakan adalah white, black, red, dan green dengan nilai RGB masing-masing.
block_size menentukan ukuran setiap segmen ular dan apel.
snake_speed menentukan kecepatan gerak ular.
Fungsi Permainan
snake(snake_list): Menggambar ular di layar berdasarkan koordinat segmen yang ada di snake_list.
pesan_layar(psn, color): Menampilkan pesan di tengah layar.
tampilkan_skor(skor): Menampilkan skor pemain di pojok kiri atas layar.
tampilkan_popup(): Menampilkan dialog konfirmasi menggunakan Tkinter untuk memastikan pemain ingin keluar dari permainan.
Game Loop
gameLoop(): Fungsi utama yang menjalankan permainan, mencakup pengaturan awal, pengendalian ular, penanganan tabrakan, penambahan skor, dan kondisi Game Over.
Loop permainan utama menangani input pengguna, memperbarui posisi ular, memeriksa tabrakan, dan menggambar ulang layar.
Penanganan Input dan Tabrakan
Pemain mengontrol arah ular menggunakan tombol panah.
Permainan berakhir jika ular menabrak dinding atau dirinya sendiri.
Restart dan Quit
Saat Game Over, pemain dapat menekan 'Q' untuk keluar atau 'C' untuk memulai ulang permainan.
tampilkan_popup() digunakan untuk mengonfirmasi keputusan pemain jika mereka memilih untuk keluar.
