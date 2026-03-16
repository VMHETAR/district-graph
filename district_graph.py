import geopandas as gpd

gdf = gpd.read_file("district.shp")

print(gdf.head())
print(len(gdf))

import networkx as nx

G = nx.Graph()

for idx, row in gdf.iterrows():
    G.add_node(idx, name=row["district"])

for i, geom in enumerate(gdf.geometry):
    neighbors = gdf[gdf.geometry.touches(geom)].index
    
    for n in neighbors:
        G.add_edge(i, n)