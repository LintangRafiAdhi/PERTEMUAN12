class DaftarNilaiMahasiswa:
    def __init__(self):
        self.daftar_nilai = []

    def tambah(self, nama, nilai):
        data_mahasiswa = {'nama': nama, 'nilai': nilai}
        self.daftar_nilai.append(data_mahasiswa)
        print(f"Data mahasiswa {nama} dengan nilai {nilai} telah ditambahkan.")

    def tampilkan(self):
        print("\nDaftar Nilai Mahasiswa:")
        for data in self.daftar_nilai:
            print(f"Nama: {data['nama']}, Nilai: {data['nilai']}")

    def hapus(self, nama):
        for data in self.daftar_nilai:
            if data['nama'] == nama:
                self.daftar_nilai.remove(data)
                print(f"Data mahasiswa {nama} telah dihapus.")
                return
        print(f"Data mahasiswa {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        for data in self.daftar_nilai:
            if data['nama'] == nama:
                data['nilai'] = nilai_baru
                print(f"Data mahasiswa {nama} telah diubah menjadi nilai {nilai_baru}.")
                return
        print(f"Data mahasiswa {nama} tidak ditemukan.")

# Contoh penggunaan
daftar_nilai_mahasiswa = DaftarNilaiMahasiswa()

daftar_nilai_mahasiswa.tambah("Lintang", 85)
daftar_nilai_mahasiswa.tambah("afif", 90)
daftar_nilai_mahasiswa.tambah("nabil", 78)

daftar_nilai_mahasiswa.tampilkan()

daftar_nilai_mahasiswa.hapus("afif")
daftar_nilai_mahasiswa.tampilkan()

daftar_nilai_mahasiswa.ubah("lintang", 95)
daftar_nilai_mahasiswa.tampilkan()
