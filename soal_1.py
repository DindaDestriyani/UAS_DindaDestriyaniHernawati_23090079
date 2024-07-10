def main():
    mahasiswa = []
    
    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        
        mahasiswa.append({'NIM': nim, 'Nama': nama})
        
        tambah_lagi = input("Ingin tambah lagi? (y/n): ")
        if tambah_lagi.lower() != 'y':
            break
    
    print("\n")
    print("Data Mahasiswa:")
    for data in mahasiswa:
        print(f"NIM: {data['NIM']}, Nama: {data['Nama']}")
    
    print("Selesai")

if __name__ == "__main__":
    main()
