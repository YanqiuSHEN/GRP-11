#!/usr/bin/env python
import cv2
import numpy as np

img variable image
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v= cv2.split(hsv)
ret_h, th_h = cv2.threshold(h,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Remplissage des contours (équivalent à un opérateur morpho de Fermeture)
im_floodfill = th.copy()
h, w = th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
cv2.floodFill(im_floodfill, mask, (0,0), 255)
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
th = th | im_floodfill_inv

# Détection des objets
contours, hierarchy = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for i in range (0, len(contours)) :
    mask_BB_i = np.zeros((len(th),len(th[0])), np.uint8)
    x,y,w,h = cv2.boundingRect(contours[i])
    cv2.drawContours(mask_BB_i, contours, i, (255,255,255), -1)
    BB_i=cv2.bitwise_and(img,img,mask=mask_BB_i)