# 15 PUZZLE SOLVER

## Penyelesaian Persoalan 15-Puzzle dengan Algoritma Branch and Bound

## Tentang Program

Branch and Bound merupakan algoritma yang digunakan untuk menyelesaikan persoalan optimisasi dengan memanfaatkan bound atau batasan yang ditentukan menggunakan fungsi pembatas. Dalam pembangkitan simpul, setiap simpul akan diberi sebuah nilai cost. Simpul berikutnya yang akan di-expand tidak lagi berdasarkan urutan pembangkitannya seperti pada BFS, tetapi simpul yang memiliki cost yang paling kecil.
Program ini akan menggunakan pendekatan algoritma Branch and Bound untuk menyelesaikan persoalan 15-Puzzle.

## How to run

### Requirments

1. Python, dapat didownload di https://www.python.org/
2. Python library, Dapat didownload menggunakan python package installer (pip) dengan menggunakan command:

```
  pip install <nama_library>
```

Python library yang digunakan pada program ini sudah terinstall saat menginstall python (library bawaan):

- copy
- bisect
- random
- time
- tkinter
- threading

### Cara menjalankan program

Untuk menjalankan program dapat dilakukan dengan menjalankan file **15PuzzleSolver.exe** yang terdapat didalam folder bin.  
  
  
Alternatif lain untuk menjalankan program:  
Program dapat dijalankan dengan melakukan run pada file gui.py yang akan menampilkan graphical user interface (GUI) dari program yang dibuat.
Untuk menjalankan program dari command line, gunakan command:

```
  python gui.py
```

Untuk menjalankan program pada console (tanpa GUI) dapat dilakukan dengan uncomment potongan kode pada bagian bawah Puzzle15.py, kemudian menjalankan program dengan command:

```
  python Puzzle15.py
```

**Dianjurkan untuk menjalankan program dengan GUI karena memiliki fitur yang lebih lengkap.**

## About Me

Program dibuat oleh:  
 Nama : Vincent Ho  
 NIM : 13520093  
 Kelas : K03
