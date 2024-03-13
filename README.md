# Prediksi Harga Rumah Berbasis Data Cuaca

## Tujuan
Tujuan dari proyek ini adalah untuk mengembangkan sebuah aplikasi prediksi harga rumah berbasis data cuaca. Aplikasi ini menggunakan machine learning untuk memprediksi harga rumah berdasarkan beberapa fitur, seperti luas tanah, luas bangunan, jumlah kamar tidur, jumlah kamar mandi, serta kondisi cuaca seperti suhu, kelembaban, dan kecepatan angin.

## Algoritma
Proyek ini menggunakan algoritma regresi linear untuk memprediksi harga rumah berdasarkan fitur-fitur yang disebutkan di atas. Regresi linear digunakan untuk memodelkan hubungan antara variabel independen (fitur-fitur) dengan variabel dependen (harga rumah).

Selain itu, proyek ini juga menggunakan metode klasterisasi K-Means untuk mengelompokkan data properti berdasarkan kondisi cuaca. Metode klasterisasi ini membantu dalam memahami pola-pola yang mungkin terdapat pada data cuaca yang mempengaruhi harga rumah.

## Library yang Digunakan
Proyek ini menggunakan beberapa library Python, antara lain:
- Pandas: Digunakan untuk manipulasi dan analisis data.
- NumPy: Digunakan untuk operasi numerik dan array.
- Scikit-learn: Digunakan untuk mengimplementasikan algoritma machine learning seperti regresi linear dan K-Means.
- Tkinter: Digunakan untuk membuat antarmuka grafis pengguna (GUI) aplikasi.

## GUI (Antarmuka Pengguna Grafis)
Antarmuka aplikasi dibangun menggunakan modul Tkinter dari Python. Antarmuka ini sederhana dan intuitif, memungkinkan pengguna untuk memasukkan data properti dan data cuaca, dan kemudian mendapatkan prediksi harga rumah serta informasi tentang kelompok cuaca properti.

## Cara Menggunakan Aplikasi
Preconditions: Pengguna sudah menginstall library-library yang digunakan ke dalam komputer lokal

1. Jalankan aplikasi dengan menjalankan script `main.py`.
2. Isi semua kolom input properti dan input cuaca sesuai dengan informasi yang diminta.
3. Klik tombol "Prediksi Harga Properti".
4. Aplikasi akan menampilkan prediksi harga rumah serta informasi kelompok cuaca properti.

## Catatan Penting
- Pastikan semua input yang dimasukkan sudah valid sebelum melakukan prediksi.
- Aplikasi ini hanya memberikan perkiraan harga rumah berdasarkan data yang dimasukkan. Prediksi sebenarnya dapat dipengaruhi oleh faktor-faktor lain yang tidak dimasukkan dalam model.

## Kontribusi
Kontribusi terhadap proyek ini sangat dianjurkan. Jika Anda menemukan masalah atau memiliki saran untuk peningkatan, silakan buka *issue* atau *pull request* di repositori GitHub ini.

## Lisensi
Proyek ini dilisensikan di bawah [Kelompok-03 Pembelajaran Mesin S1-Informatika 2021](LICENSE).
