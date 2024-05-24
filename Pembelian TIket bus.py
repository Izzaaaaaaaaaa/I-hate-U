def home():
    pass
print("              <<========== Pembelian Tiket BUS ===========>>")
print()
print("                <<========== Terminal INTR ===========>>     ")
print()
print("                  <<========== Kota Tujuan ===========>>     ")
print("              ===============================================")

def rute_keberangkatan():
    routes = {
        1: {"route": "Jakarta - Bandung", "price": 100.000},
        2: {"route": "Jakarta - Surabaya", "price": 200.000},
        3: {"route": "Jakarta - Yogyakarta", "price": 130.000},
        4: {"route": "Jakarta - Lampung", "price": 250.000},
        5: {"route": "Jakarta - Padang", "price": 500.000},
        6: {"route": "Jakarta - Bandung", "price": 150.000},
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


