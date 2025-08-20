# tugas-pwl-4

# Pyramid Movie Database

Ini adalah proyek sederhana yang menggunakan Pyramid untuk mengelola sebuah database film.

## Persyaratan

- Python 3.6 atau lebih baru
- Pyramid
- PyMySQL (atau driver database MySQL lainnya)

## Instalasi

1. Clone repositori ini:
git clone https://github.com/naufaldewanto37/tugas-pwl-4.git

2. Install dependensi:
pip install -r requirements.txt

3. Inisiasi database:
cd models
python models.py


## Penggunaan

1. Jalankan aplikasi:

pserve development.ini

2. Aplikasi akan berjalan di `http://localhost:6543`.

3. Gunakan Postman atau alat sejenisnya untuk melakukan permintaan HTTP untuk menambah, membaca, memperbarui, atau menghapus film dari database.

## Endpoint API

- **POST /movies**: Tambahkan film baru ke database.
- **GET /movies**: Baca daftar semua film dalam database.
- **PUT /movies/{id}**: Perbarui film berdasarkan ID.
- **DELETE /movies/{id}**: Hapus film berdasarkan ID.

## Contoh Data Film

Anda dapat menggunakan data berikut sebagai contoh untuk menambahkan film melalui API:

```json
 {"title": "Inception", "year": 2010},
 {"title": "The Matrix", "year": 1999},
 {"title": "Avengers: Endgame", "year": 2019},
 {"title": "The Godfather", "year": 1972},
 {"title": "The Dark Knight", "year": 2008},
 {"title": "Forrest Gump", "year": 1994},
 {"title": "Fight Club", "year": 1999},
 {"title": "Pulp Fiction", "year": 1994},
 {"title": "Shawshank Redemption", "year": 1994},
 {"title": "Interstellar", "year": 2014}

