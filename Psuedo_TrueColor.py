# Resize Redband to match with blue and veggie
# Rebin function from https://stackoverflow.com/questions/8090229/resize-with-averaging-or-rebin-a-numpy-2d-array
def rebin(a, shape):
    sh = shape[0],a.shape[0]//shape[0],shape[1],a.shape[1]//shape[1]
    return a.reshape(sh).mean(-1).mean(1)

from netCDF4 import Dataset
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

g16nc = Dataset('OR_ABI-L2-CMIPM2-M3C01_G16_s20172661340312_e20172661340369_c20172661340426.nc', 'r')
ref_1 = g16nc.variables['CMI'][:]
g16nc.close()
g16nc = None
ref_gamma_1 = np.sqrt(ref_1)

# Read in Level 2 NetCDF
g16nc = Dataset('OR_ABI-L2-CMIPM2-M3C02_G16_s20172661340312_e20172661340369_c20172661340441.nc', 'r')
ref_ch2 = g16nc.variables['CMI'][:]
g16nc.close()
g16nc = None
ref_gamma = np.sqrt(ref_ch2)

# Load Channel 3 - Veggie Near IR & do gamma adjustment
g16nc = Dataset('OR_ABI-L2-CMIPM2-M3C03_G16_s20172661340312_e20172661340369_c20172661340429.nc', 'r')
ref_3 = g16nc.variables['CMI'][:]
g16nc.close()
g16nc = None
ref_gamma_3 = np.sqrt(ref_3)

ref_gamma_2 = rebin(ref_gamma, [1000, 1000])

### Plot gamma adjusted reflectance channel 1
##fig = plt.figure(figsize=(6,6),dpi=200)
##im = plt.imshow(ref_gamma_1, vmin=0.0, vmax=1.0, cmap='Greys_r')
##cb = fig.colorbar(im, orientation='horizontal')
##cb.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
##cb.set_label('Ch01 - Reflectance')
##plt.show()

### Plot gamma adjusted reflectance channel 3
##fig = plt.figure(figsize=(6,6),dpi=200)
##im = plt.imshow(ref_gamma_3, vmin=0.0, vmax=1.0, cmap='Greys_r')
##cb = fig.colorbar(im, orientation='horizontal')
##cb.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
##cb.set_label('Ch03 - Reflectance')
##plt.show()

##geocolor = np.stack([ref_gamma_2, ref_gamma_3, ref_gamma_1], axis=2)
##fig = plt.figure(figsize=(6,6),dpi=200)
##im = plt.imshow(geocolor)
##plt.title('GeoColor - Red - Veggie - Blue')
##plt.show()

# Tone down green
# Derived from Planet Labs data, CC > 0.9
ref_gamma_true_green = 0.48358168 * ref_gamma_2 + 0.45706946 * ref_gamma_1 + 0.06038137 * ref_gamma_3

truecolor = np.stack([ref_gamma_2, ref_gamma_true_green, ref_gamma_1], axis=2)
fig = plt.figure(figsize=(6,6),dpi=200)
im = plt.imshow(truecolor)
plt.title('TrueColor - Red - Psuedo-Green - Blue')
plt.show()
