import os,sys,csv,cv2
import pandas as pd
from csv import DictWriter
from rich import print


class Utils:
    def __init__(self,image,data) -> None:
        self.namerow = ["name","corner","speed"]
        self.image_name = ''
        self.image = image
        self.data = data        
        self.save_img_path = '/home/fptlap/Documents/build_data/data/images'
        

    def export_to_csv(self) :
        num = 0
        for row in open('data/log.csv'):
            num += 1
        
        self.image_name = '{}_img_car_gazebo_record.jpg'.format(str(num + 1))
        self.save_img(data=[self.image_name,self.image])
        with open('data/log.csv', 'a') as file:
            writer = DictWriter(file,fieldnames=self.namerow)
            dict = {"name":self.image_name,"corner":self.data[0],"speed":self.data[1]}
            writer.writerow(dict)
            print(dict)
    
    def save_img(self,data) -> None:
        cv2.imwrite(filename=os.path.join(self.save_img_path, data[0]),img=data[1])
        print(os.path.join(self.save_img_path, data[0]))
    
    
        







