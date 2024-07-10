data_mahasiswa = [
    ["Mahasiswa1", 90, 80],
    ["Mahasiswa2", 50, 60],
    ["Mahasiswa3", 65, 70]
]

total_nilai_algoritma = 0
total_nilai_matematika_numerik = 0
jumlah_mahasiswa = len(data_mahasiswa)

rata_rata_mahasiswa = []

for mahasiswa in data_mahasiswa:
    nama = mahasiswa[0]
    nilai_algoritma = mahasiswa[1]
    nilai_matematika_numerik = mahasiswa[2]
    
    total_nilai_algoritma += nilai_algoritma
    total_nilai_matematika_numerik += nilai_matematika_numerik
    
    rata_rata = (nilai_algoritma + nilai_matematika_numerik) / 2
    rata_rata_mahasiswa.append((nama, rata_rata))


rata_rata_algoritma = total_nilai_algoritma / jumlah_mahasiswa
rata_rata_matematika_numerik = total_nilai_matematika_numerik / jumlah_mahasiswa

print(f"Rata-rata nilai Algoritma: {rata_rata_algoritma:.2f}")
print(f"Rata-rata nilai Matematika Numerik: {rata_rata_matematika_numerik:.2f}")

print("\nRata-rata nilai untuk setiap mahasiswa:")
for nama, rata_rata in rata_rata_mahasiswa:
    print(f"{nama}: {rata_rata:.2f}")
