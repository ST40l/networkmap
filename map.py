import networkx as nx
import matplotlib.pyplot as plt

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

# Ağ haritasını çizelim
pos = nx.spring_layout(G, seed=42)  # Rastgele düzlem yerleşimi için tohum belirtelim
edge_labels = {(sehir1, sehir2): f"{mesafe} km" for sehir1, sehir2, mesafe in baglantilar}

nx.draw_networkx_nodes(G, pos, node_size=800, node_color='skyblue')
nx.draw_networkx_edges(G, pos, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

plt.title("Türkiye Şehirleri Ağ Haritası")
plt.axis('off')  # Eksenleri gösterme
plt.show()
