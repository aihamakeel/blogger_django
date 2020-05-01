import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", palette="pastel", color_codes=True) 
sns.mpl.rc("figure", figsize=(10,6))

#opening the vector map
shp_path = "chicago\\geo_export_5db1e669-e342-4804-869c-65f538273d03.shp"
#shp_path = "District_boundary\\District_Boundary.shp"
#reading the shape file by using reader function of the shape lib
sf = shp.Reader(shp_path)
len(sf.shapes())
sf.records()