class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
        print(f"Pesanan '{item}' telah ditambahkan ke dalam antrian.")
    
    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong, tidak ada pesanan yang dapat dihapus.")
            return None
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def display(self):
        if self.is_empty():
            print("Antrian kosong.")
        else:
            print("Antrian pesanan saat ini:")
            for item in self.items:
                print(item)

def main():
    antrian_pesanan = Queue()
    
    antrian_pesanan.enqueue("Pesanan 1: Lele Goreng")
    antrian_pesanan.enqueue("Pesanan 2: Bebek Goreng")
    antrian_pesanan.enqueue("Pesanan 3: Ayam Goreng")
    
    antrian_pesanan.display()
    
    print("\nMenghapus pesanan dari antrian...")
    antrian_pesanan.dequeue()
    
    antrian_pesanan.display()

if __name__ == "__main__":
    main()