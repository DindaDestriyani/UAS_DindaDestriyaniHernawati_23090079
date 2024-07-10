class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa
    
    def set_nama(self, nama):
        self.nama = nama
    
    def set_warna(self, warna):
        self.warna = warna
    
    def set_rasa(self, rasa):
        self.rasa = rasa
    
    def information(self):
        return f"Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"


class Mangga(Buah):
    def __init__(self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        self.vitamin = vitamin