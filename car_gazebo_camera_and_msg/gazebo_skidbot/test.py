



from IPython.display import display
from PIL import Image
import random
import cv2
import numpy as np

def my_imread(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image 
def img_preprocess(image):
    height, _, _ = image.shape
    image = image[int(height/2):,:,:]  # remove top half of the image, as it is not relevant for lane following
    image = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)  # Nvidia model said it is best to use YUV color space
    image = cv2.GaussianBlur(image, (3,3), 0)
    image = cv2.resize(image, (200,66)) # input image size (200,66) Nvidia model
    image = image / 255 # normalizing
    return image

def image_data_generator(image_paths, steering_angles, batch_size, is_training):
    while True:
        batch_images = []
        batch_steering_angles = []
        
        for i in range(batch_size):
            random_index = random.randint(0, len(image_paths) - 1)
            print(random_index)
            print(steering_angles)

            # image_path = image_paths[random_index]
            image = my_imread(image_paths[random_index])
            # steering_angle = steering_angles[random_index]
           
            
            image = img_preprocess(image)
            batch_images.append(image)
            # batch_steering_angles.append(steering_angle)
            
        yield( np.asarray(batch_images))




from keras.models import load_model



model_output_dir= "/media/fptlab/workspace/car/car_train/models"

    
def predict_and_summarize(X):
    model = load_model(f'{model_output_dir}/lane_navigation_check.h5')
    Y_pred = model.predict(X)

    return Y_pred









import matplotlib.pyplot as plt




image_h = "hoang_data_2/data_003_-71_-42.png"
image_k = 1
Hoang_test=[]
# display(Image.open(image_x))

# X_test_x, y_test_y = next(image_data_generator(image_h, 1, 0, False))

# display(X_test_x)

# model = load_model(f'{model_output_dir}/lane_navigation_check.h5')
# hoang_angle = model.predict(X_test_x)
# print(hoang_angle)

def testm(image_paths):
    n_tests = 100

    Hoang_test.append(image_paths)

    Hoang_test_test = next(image_data_generator(Hoang_test, [50], 1, False))

    Hoang_y_pred = predict_and_summarize(Hoang_test_test)

    return Hoang_y_pred[0][0]-90

    # n_tests_show = 2
    # fig, axes = plt.subplots(n_tests_show, 1, figsize=(10, 4 * n_tests_show))
    # for i in range(n_tests_show):
    #     axes[i].imshow(Hoang_test_test[i])
    #     axes[i].set_title(f"predicted angle={int(Hoang_y_pred[i])}")
    

# model = load_model(f'{model_output_dir}/lane_navigation_check.h5')
# hoang_angle = model.predict(X_train_batch)
# print(hoang_angle)