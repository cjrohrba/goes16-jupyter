from netCDF4 import Dataset
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Read in Level 2 NetCDF
g16nc = Dataset('OR_ABI-L2-CMIPM2-M3C02_G16_s20172671215318_e20172671215375_c20172671215452.nc', 'r')
ref_ch2 = g16nc.variables['CMI'][:]
g16nc.close()
g16nc = None

### Plot reflectance
##fig = plt.figure(figsize=(6,6),dpi=200)
##im = plt.imshow(ref_ch2, vmin=0.0, vmax=1.0, cmap='Greys_r')
##cb = fig.colorbar(im, orientation='horizontal')
##cb.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
##cb.set_label('Level 2 Reflectance')
##plt.show()

# Apply the formula to adjust reflectance gamma
ref_gamma = np.sqrt(ref_ch2)

# Plot gamma adjusted reflectance
fig = plt.figure()#figsize=(6,6),dpi=200)
im = plt.imshow(ref_gamma, vmin=0.0, vmax=1.0, cmap='Greys_r')
##cb = fig.colorbar(im, orientation='horizontal')
##cb.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
##cb.set_label('Reflectance Gamma Adjusted')
plt.show()
