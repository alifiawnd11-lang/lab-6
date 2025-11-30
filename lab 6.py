import math

# a(x): mengembalikan x^2
a = lambda x: x**2

# b(x, y): akar(x^2 + y^2)
b = lambda x, y: math.sqrt(x*2 + y*2)

# c(*args): rata-rata
c = lambda *args: sum(args) / len(args)

# d(s): menghapus duplikasi karakter dan menggabungkannya
d = lambda s: "".join(set(s))

# Contoh pemanggilan
print(a(5))          # 25
print(b(3, 4))       # 5.0
print(c(1, 2, 3, 4)) # 2.5
print(d("hello"))