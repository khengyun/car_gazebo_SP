#   THINK BEFORE RUN THIS FUCKING FILE __ GOODLUCK __

import os, shutil
# path to your image folder
folder_image = '/home/fptlap/Documents/build_data/data/images'
for filename in os.listdir(folder_image):
    file_path = os.path.join(folder_image, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

open('data/log.csv', 'w')