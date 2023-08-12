import networkx as nx

# Boş bir yönlendirilmemiş graf oluşturalım
G = nx.Graph()

# Şehirleri düğüm olarak ekleyelim
sehirler = ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya', 'Adana', 'Eskişehir']
G.add_nodes_from(sehirler)

# Şehirler arası bağlantıları ve mesafeleri ekleyelim
baglantilar = [
    ('İstanbul', 'Ankara', 350),
    ('İstanbul', 'İzmir', 550),
    ('İstanbul', 'Bursa', 150),
    ('Ankara', 'İzmir', 450),
    ('Ankara', 'Bursa', 300),
    ('İzmir', 'Bursa', 250),
    ('İzmir', 'Antalya', 450),
    ('İzmir', 'Adana', 600),
    ('Bursa', 'Antalya', 350),
    ('Bursa', 'Adana', 550),
    ('Antalya', 'Adana', 200),
    ('Ankara', 'Eskişehir', 100),
    ('Eskişehir', 'İstanbul', 280),
]

for sehir1, sehir2, mesafe in baglantilar:
    G.add_edge(sehir1, sehir2, mesafe=mesafe)

# Bağlantı mesafelerini yazdıralım
for sehir1, sehir2, mesafe in baglantilar:
    print(f"{sehir1} ile {sehir2} arası mesafe: {mesafe} km")
