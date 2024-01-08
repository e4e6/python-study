import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('assets\images\gif-kirby.gif')

plt.imshow(img)
plt.show()