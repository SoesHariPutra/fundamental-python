from modularization import hitung_segitiga, hitung_harga_diskon

print('Main', hitung_segitiga(10, 3))
print('Main', hitung_harga_diskon(100000, 0.1))
exit(0)

"""
Komentar panjang
"""
print("Hello World!")
# variables type
gedung = "BPK"
tinggi = 8
PI = "Private Investigator"
pi = 3.14
is_alive = True
is_alive = "XXX"
#tinggi = True # tipe variable bs berubah2
print(gedung)
print(tinggi)
print(pi)
print(PI, is_alive)

# list
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu']
print(hari)
print(hari[0])
print(hari[len(hari)-1])

#dictionary
antonim = {}
antonim['tinggi'] = 'pendek'
antonim['gelap'] = 'terang'
antonim['jauh'] = 'dekat'
print('Antonim dari jauh adalah', antonim['jauh'])

#SEQUENTIAL FLOW


#CONTROL FLOW/IF
if is_alive == True:
    print('Hidup')

if is_alive and tinggi > 7:
    print('Hidup, ketinggian, jadi mati')

if is_alive == True:
    print('Hidup')
elif is_alive == False:
    print('Mati')
else:
    print('Ga Jelas')

#LOOP
#MENGULANG KODE BEBERAPA KALI SAMPAI KONDISI TERTENTU
#FOR untuk perulangan yang pasti
for i in range (0, 3):
    print(i)

#WHILE
#Digunakan untuk perulangan yang jumlahnya tidak pasti
#namun kondisi berhentinya pasti
i = 0
while is_alive:
    print('Hidup')
    i = i + 1
    if i == 10:
        is_alive = False

#FOR UNTUK LIST
for h in hari:
    print(hari)

for h in range(0, len(hari)-1):
    print(hari(h))