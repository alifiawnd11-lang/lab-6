# lab-6
# README
 fungsi Python yang melakukan operasi
 sederhana dan manipulasi string.
## Fungsi
### 1. a(x)
Mengembalikan nilai kuadrat dari x.
 python
def a(x):
    return x**2
### 2. b(x, y)
Menghitung akar kuadrat dari jumlah kuadrat x dan y.
 python
def b(x, y):
    return math.sqrt(x**2 + y**2)
### 3. c(*args)
Mengembalikan nilai rata-rata dari argumen yang diberikan.
 python
def c(*args):
    return sum(args)/len(args)
### 4. d(s)
Menghapus karakter duplikat dalam sebuah string lalu menggabungkannya
kembali.
python
def d(s):
    return "".join(set(s))
## Contoh Penggunaan
python
print(a(5))          # 25
print(b(3, 4))       # 5.0
print(c(1, 2, 3))    # 2.0
print(d("hello"))    
