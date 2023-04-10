import random
import cv2
from keras.models import load_model
import numpy as np

def img_preprocess(image):
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    height, _, _ = image.shape
    print("image.shape: ",image.shape)
    image = image[int(height/2):,:,:]  # remove top half of the image, as it is not relevant for lane following
    image = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)  # Nvidia model said it is best to use YUV color space
    image = cv2.GaussianBlur(image, (3,3), 0)
    image = cv2.resize(image, (200,66)) # input image size (200,66) Nvidia model
    image = image / 255 # normalizing
    cv2.imshow("image",image)
    cv2.waitKey(4)
    return image



def predict_and_summarize(X,Y):
    model = load_model('/home/fptlab/Documents/car_gazebo_SP/car_gazebo_camera_and_msg/gazebo_skidbot/model.h5')
    Y_pred = model.predict(X)
    return Y_pred
def my_imread(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image 

def image_data_generator(image_paths, steering_angles, batch_size=2, is_training=False):
    while True:
        batch_images = []
        batch_steering_angles = []
        
        for i in range(batch_size):
            random_index = random.randint(0, len(image_paths) - 1)
            image = image_paths[random_index]
            image = my_imread(image_paths[random_index])
            steering_angle = steering_angles[random_index]
              
            image = img_preprocess(image)
            batch_images.append(image)
            batch_steering_angles.append(steering_angle)
            
        yield( np.asarray(batch_images), np.asarray(batch_steering_angles))

