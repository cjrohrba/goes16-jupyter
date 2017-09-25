from netCDF4 import Dataset
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

g16nc = Dataset('OR_ABI-L1b-RadM2-M3C02_G16_s20172661325312_e20172661325369_c20172661325405.nc', 'r')
radiance = g16nc.variables['Rad'][:]
g16nc.close()
g16nc = None

##fig = plt.figure(figsize=(6,6),dpi=200)
##im = plt.imshow(radiance, cmap='Greys_r')
##cb = fig.colorbar(im, orientation='horizontal')
##cb.set_ticks([1, 100, 200, 300, 400, 500, 600])
##cb.set_label('Radiance (W m-2 sr-1 um-1)')
##plt.show()

# http://www.goes-r.gov/products/ATBDs/baseline/Imagery_v2.0_no_color.pdf 
# Define some constants needed for the conversion. From the pdf linked above
Esun_Ch_02 = 663.274497
d2 = 0.3

# Apply the formula to convert radiance to reflectance
ref = (radiance * np.pi * d2) / Esun_Ch_02

# Make sure all data is in the valid data range
ref = np.maximum(ref, 0.0)
ref = np.minimum(ref, 1.0)

# Plot reflectance
fig = plt.figure(figsize=(6,6),dpi=200)
im = plt.imshow(ref, vmin=0.0, vmax=1.0, cmap='Greys_r')
cb = fig.colorbar(im, orientation='horizontal')
cb.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
cb.set_label('Reflectance')
plt.show()
