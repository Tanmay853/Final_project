from keras.preprocessing.image import ImageDataGenerator
from keras.utils import array_to_img, img_to_array, load_img

import cv2
from keras.preprocessing.image import ImageDataGenerator


datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

#Give path of the folder
img = load_img('C:/Users/soumy/Roll No.3 (1).png')  # this is a PIL image
x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
img = img.convert('L') # make image Greyscale...
img = img.resize((100,100)) #resize images...
x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 1, 100, 100)

# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory
i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='preview', save_prefix='cat', save_format='jpeg'):
    i += 1
    if i > 3:
        break  # otherwise the generator would loop indefinitely
        
#Give path of the folder
img_B = cv2.imread('C:/Users/soumy/Roll No.3 (1).png')
gausBlur = cv2.blur(img_B,(5,5))
x = img_to_array(gausBlur)  # this is a Numpy array with shape (3, 150, 150)
x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)
i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='Preview', save_prefix='image', save_format='png'):
    i += 1
    if i > 2:
        break  # otherwise the generator would loop indefinitely