import numpy as np
from PIL import Image


arrImage=np.array(Image.open("aksSlide.jpg"))

# darkest and lightest pixels
min=np.min(arrImage)
max=np.max(arrImage)

# Make a LUT
LUT=np.zeros(256,dtype=np.uint8)
LUT[min:max+1]=np.linspace(start=0,stop=255,num=(max-min)+1,endpoint=True,dtype=np.uint8)

# Apply LUT and save resulting image
Image.fromarray(LUT[npImage]).save('aksbehtar.jpg')
