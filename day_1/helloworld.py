import math

print(2 + 3) # addition/penjumlahan(+)
print(3 - 2) # subtraction/pengurangan(-)
print(2 * 3) # multiplication/perkalian(*)
print(3 / 2) # division/pembagian(/)
print(3 % 2) # modulo/persamaan sisa bagi(%)
print(3 ** 2) # exponentiation/pangkat(**)
print(3 // 2) # floor division/pembagian bulat(//)

print("Name : Harana Harda")
print("Family Name : Samtodiharjo")
print("Country : Indonesia")
print("I am enjoying 30 days of Python")

#Cek tipe data
print(type(2)) # int/integer
print(type(2.5)) # float
print(type("2")) # str/string
print(type(True)) # bool/boolian
print(type(1 + 3j)) # complex/kompleks
print(type([1,2,3])) # list
print(type({'nama': 'John'})) # dict/dictionary

#point 1
x1 = 2
y1 = 3
# point 2
x2 = 10
y2 = 8

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Euclidean Distance: {distance}")

