# Naura Aisha Zahira (2311104078)
def home():
    pass
print("<<========== Pembelian Tiket BUS ===========>>")
print()
print("<<========== Terminal INTR ===========>>")
print()
print("<<========== Kota Tujuan ===========>>")

def cetak():
    print("===============================================")
    cetak()

def rute_keberangkatan():
    routes = {
        1: {"route": "Jakarta - Bandung", "price": 100000},
        2: {"route": "Jakarta - Surabaya", "price": 200000},
        3: {"route": "Jakarta - Yogyakarta", "price": 130000},
        4: {"route": "Jakarta - Lampung", "price": 250000},
        5: {"route": "Jakarta - Padang", "price": 500000},
        6: {"route": "Jakarta - Bandung", "price": 150000},
    }
    print("Rute yang Tersedia: ")
    for key, value in routes.items():
        print(f"{key}. {value['route']} (IDR {value['price']})")
    return routes
    
def jadwal_keberangkatan(route_id):
    jadwal = {
        1: ["08:00", "12:00", "16:00"],
        2: ["09:00", "13:00", "17:00"],
        3: ["07:00", "11:00", "15:00"],
        4: ['08:15', '22:48', '04:27'],
        5: ['00:09', '17:05', '20:18'],
        6: ['03:44', '12:50', '15:00'],
    }
    print("Jadwal Tersedia: ")
    for i, schedule in enumerate(jadwal[route_id], start=1):
        print(f"{i}. {schedule}")
    return jadwal[route_id]
#izzaty dan Tiur
tempat_duduk = [0] * 40

def tampilkan_tempat_duduk():
    print("Tempat Duduk Bus:")
    for i in range(len(tempat_duduk)):
        status = 'Tersedia' if tempat_duduk[i] == 0 else 'Dipesan'
        print(f'Tempat Duduk {i + 1}: {status}')
    return tempat_duduk

def pesan_tempat_duduk(nomor_tempat_duduk):
    if tempat_duduk[nomor_tempat_duduk - 1] == 0:
        tempat_duduk[nomor_tempat_duduk - 1] = 1
        print(f'Tempat duduk {nomor_tempat_duduk} berhasil dipesan.')
    else:
        print(f'Tempat duduk {nomor_tempat_duduk} sudah dipesan oleh orang lain.')

def batalkan_reservasi(nomor_tempat_duduk):
    if tempat_duduk[nomor_tempat_duduk - 1] == 1:
        tempat_duduk[nomor_tempat_duduk - 1] = 0
        print(f'Reservasi tempat duduk {nomor_tempat_duduk} berhasil dibatalkan.')
    else:
        print(f'Tempat duduk {nomor_tempat_duduk} belum dipesan.')
# Rengganis Tantri Pramudita(2311104065)
def data_penumpang(jumlah_tiket):
    data = []
    for i in range(jumlah_tiket):
        print(f"\nMasukkan data penumpang ke-{i+1}:")
        nama = str(input("Nama Penumpang: "))
        nik = int(input("NIK: "))
        telepon = int(input("Nomor Telepon: "))
        email = input("Alamat Email: ")
        if "@" not in email :
            raise ValueError("Email harus menggunakan '@'.")
        else:
            ()
        data.append({
            "nama": nama,
            "nik": nik,
            "telepon": telepon,
            "email": email
        })
    return data
#izzaty dan Tiur
def main():
    while True:
        print("\nMenu:")
        print("1. Tampilkan Tempat Duduk")
        print("2. Pesan Tempat Duduk")
        print("3. Batalkan Reservasi")
        print("4. Keluar")

        pilihan = int(input("Pilih opsi: "))

        if pilihan == 1:
            tampilkan_tempat_duduk()
        elif pilihan == 2:
            nomor_tempat_duduk = int(input("Masukkan nomor tempat duduk yang ingin dipesan: "))
            if 1 <= nomor_tempat_duduk <= len(tempat_duduk):
                pesan_tempat_duduk(nomor_tempat_duduk)
            else:
                print("Nomor tempat duduk tidak valid.")
        elif pilihan == 3:
            nomor_tempat_duduk = int(input("Masukkan nomor tempat duduk yang ingin dibatalkan: "))
            if 1 <= nomor_tempat_duduk <= len(tempat_duduk):
                batalkan_reservasi(nomor_tempat_duduk)
            else:
                print("Nomor tempat duduk tidak valid.")
        elif pilihan == 4:
            print("Terima kasih telah menggunakan layanan kami.")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
# Tiurma Grace Angelina (2311104042)
while True:
        routes = rute_keberangkatan()
        try:
            route_id = int(input("Pilih rute berdasarkan nomor: "))
            if route_id not in routes:
                print("Pilihan rute tidak valid.")
                continue

            waktu_keberangkatan = jadwal_keberangkatan(route_id)
            pilih_waktu_keberangkatan = int(input("Pilih jadwal berdasarkan nomor: "))

            if pilih_waktu_keberangkatan not in range(1, len(waktu_keberangkatan) + 1):
                print("Pilihan jadwal tidak valid.")
                continue

            jumlah_tiket = int(input("Masukkan jumlah tiket: "))
            if jumlah_tiket <= 0:
                print("Jumlah tiket tidak valid.")
                continue

            total = routes[route_id]["price"] * jumlah_tiket
            penumpang = data_penumpang(jumlah_tiket)
 #izzaty dan tiur
            tampilkan_tempat_duduk()
            for _ in range(jumlah_tiket):
                while True:
                    nomor_tempat_duduk = int(input("Masukkan nomor tempat duduk yang ingin dipesan: "))
                    if 1 <= nomor_tempat_duduk <= len(tempat_duduk):
                        if tempat_duduk[nomor_tempat_duduk - 1] == 0:
                            pesan_tempat_duduk(nomor_tempat_duduk)
                            break
                        else:
                            print("Tempat duduk sudah dipesan, silakan pilih yang lain.")
                    else:
                        print("Nomor tempat duduk tidak valid, silakan coba lagi.")               
# Izzaty zahara BR Barus (2311104052)
            print("\nRingkasan Pemesanan:")
            print(f"Rute: {routes[route_id]['route']}")
            print(f"Jadwal: {waktu_keberangkatan[pilih_waktu_keberangkatan - 1]}")
            print(f"Jumlah Tiket: {jumlah_tiket}")
            print(f"Total Harga: IDR {total}")

            for i, penumpang in enumerate(penumpang, start=1):
                print(f"\nData Penumpang {i}: ")
                print(f"Nama: {penumpang['nama']}")
                print(f"NIK: {penumpang['nik']}")
                print(f"Nomor Telepon: {penumpang['telepon']}")
                print(f"Alamat Email: {penumpang['email']}")

            konfirmasi_pemesanan = input("Konfirmasi pemesanan? (Ya/Tidak): ").lower()
            if konfirmasi_pemesanan == "ya":
                print("Pemesanan dikonfirmasi. Terima kasih atas pembelian Anda!")
            else:
                print("Pemesanan dibatalkan.")

            lanjut_pemesanan = input("Apakah Anda ingin melakukan pemesanan lagi? (Ya/Tidak): ").lower()
            while lanjut_pemesanan not in ["ya", "tidak"]:    
                lanjut_pemesanan = input("Mohon masukkan jawaban yang valid: (Ya/Tidak): ").lower()
            if lanjut_pemesanan == "tidak":
                print("Terima kasih telah menggunakan sistem kami.")
                exit()
            else:
                print("Silakan melakukan pemesanan lagi.")
        except ValueError:
            print("Input tidak valid, silakan coba lagi.")

        