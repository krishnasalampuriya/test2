# Dataset downloader 1.0 
#author - Kanishka Mankar

# -*- coding: utf-8 -*-

#!wget images.cocodataset.org/annotations/annotations_trainval2017.zip

#!unzip /content/annotations_trainval2017.zip

#!pip install pycocotools


"""###Clean Code Class

This code can work anywhere but is designed to be used in colab

Download annotations file and give the path of annotations file to while creating objects

install pycocotools

then you can use it on any platform
"""

from pycocotools.coco import COCO
import requests
import os
import time
import random
class DownloadCoco:
  def __init__(self,annot_path):
    self.path = ""
    self.coco = COCO(annot_path)
    self.anot_dict1 = {15: 'bench',62: 'chair',63: 'couch',64: 'potted plant', 65: 'bed',
            67: 'dining table',70: 'toilet',72: 'tv',78: 'microwave',79: 'oven',80: 'toaster',81: 'sink',82: 'refrigerator',
            85: 'clock',86: 'vase'}
  
  def show_current_annotations(self):
    for i in self.anot_dict1.keys():
      print(self.anot_dict1[i])
  
  def save_coco_location(self,path):
    if (path[-1]!='/'):
      print("please end path with \"/\"")
      return
    os.mkdir(path)
    self.path = path
    print(f"dataset will be saved at path {self.path}")

  def change_annot_dict(self,annot_dict):
    self.anot_dict1 = annot_dict 
    print("Annotation dictionary changed")
  
  def CatImages(self,category,n_samples=500):
    # Specify a list of category names of interes
    catIds = self.coco.getCatIds(catNms=[category])
    # Get the corresponding image ids and images using loadImgs
    imgIds = self.coco.getImgIds(catIds=catIds)
    images = self.coco.loadImgs(imgIds)
    if (n_samples<=len(images)):
      images_n = random.sample(images,n_samples)
    else:
      print(f"length of original list {len(images)} is less than {n_samples} returning original")
      return images
    return images_n

  def saveImgs(self,catId,images,path):
    start = time.time()
    print(f"Number of images in {catId} is {len(images)}")
    for im in images:
      img_data = requests.get(im['coco_url']).content
      with open(path+ im['file_name'], 'wb') as handler:
          handler.write(img_data)
    print("Execution time for {} is {:.3f} seconds".format(catId,time.time()-start))

  def custom_coco(self):
    dl = len(self.anot_dict1.keys())
    print("######## starting download ########")
    for i,key in enumerate(self.anot_dict1.keys()):
      path = self.path+self.anot_dict1[key]
      os.mkdir(path)
      images = self.CatImages(self.anot_dict1[key]) #change number of download samples here
      self.saveImgs(self.anot_dict1[key],images,path+'/')
      print(f"--- {i+1} in {dl} ---")


#Example 

#first download dataset annotations

"""
   by using this command in colab 
   !wget images.cocodataset.org/annotations/annotations_trainval2017.zip
   
   unzip the files by using following command
   !unzip /content/annotations_trainval2017.zip
   
   Install pycoco tools if not installed
   !pip install pycocotools

"""
#download_dataset = DownloadCoco("/content/annotations/instances_train2017.json")

#download_dataset.save_coco_location("/content/coco_images/")

#download_dataset.custom_coco()

