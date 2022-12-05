from typing import Tuple, Union

from keras.models import load_model
from matplotlib import image
from matplotlib import pyplot
import numpy as np

model = load_model('model.h5')

image = image.imread('test.jpg')
# summarize shape of the pixel array
print(image.dtype)
print(image.shape)
# display the array of pixels as an image
pyplot.imshow(image)
pyplot.show()
image = image.reshape((1,) + image.shape)
print(image.shape)

result = model.predict(image)

# print(type(result[0]))
vlz = np.float32(result[0])[0][0]
print(vlz)
# print(np.float32(result[0])[0][0])
# print(float(result[1]))
