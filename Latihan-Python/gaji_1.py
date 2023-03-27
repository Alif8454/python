# Input gaji per jam dan jumlah jam kerja per minggu
gaji_per_jam = float(input("Masukkan gaji per jam: "))
jam_kerja_per_minggu = float(input("Masukkan jumlah jam kerja per minggu: "))

# Hitung gaji per minggu dan per bulan
gaji_per_minggu = gaji_per_jam * jam_kerja_per_minggu
gaji_per_bulan = gaji_per_minggu * 4

# Tampilkan hasil perhitungan
print("Gaji per minggu: ", gaji_per_minggu)
print("Gaji per bulan: ", gaji_per_bulan)
