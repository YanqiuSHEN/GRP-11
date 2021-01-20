#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
import matplotlib.pyplot as plt
from std_srvs.srv import Empty


class LoadFeature(object):

    def __init__(self):
    
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.camera_callback)
        self.bridge_object = CvBridge()
        self.bottle_found = rospy.ServiceProxy('/bottle', Empty)

    def camera_callback(self,data):
        try:
            # We select bgr8 because its the OpenCV encoding by default
            cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
        except CvBridgeError as e:
            print(e)
        

        image_1 = cv2.imread('/home/user/catkin_ws/src/student_pkg/challenge_2/image/coke_can.png',1)
        image_2 = cv_image
        image_1 = cv2.resize(image_1,(400,300))#changer photo size
        image_2 = cv2.resize(image_2,(400,300))

        # Creating a red mask to only see the red
        min_red = np.array([40,0,0])
        max_red = np.array([255,200,200])
        hsv = cv2.cvtColor(image_2, cv2.COLOR_BGR2HSV)
        mask_r = cv2.inRange(hsv, min_red, max_red)

        #cv2.imwrite('/home/user/catkin_ws/src/vision/ressources/image_1.jpg',image_1)
        #cv2.imwrite('/home/user/catkin_ws/src/vision/ressources/image_2.jpg',image_2)
        #cv2.imwrite('/home/user/catkin_ws/src/vision/ressources/mask_r.jpg',mask_r)
        #Initialize the ORB Feature detector 
        orb = cv2.ORB_create(nfeatures = 1000)

        #Make a copy of the original image to display the keypoints found by ORB
        #This is just a representative
        preview_1 = np.copy(image_1)
        preview_2 = np.copy(image_2)

        # Red filter on the picture
        res_r = cv2.bitwise_and(preview_2, preview_2, mask= mask_r)
      
        #Create another copy to display points only
        dots = np.copy(image_1)

        #Extract the keypoints from both images
        train_keypoints, train_descriptor = orb.detectAndCompute(image_1, None)
        test_keypoints, test_descriptor = orb.detectAndCompute(res_r, None)

        #Draw the found Keypoints of the main image
        cv2.drawKeypoints(image_1, train_keypoints, preview_1, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.drawKeypoints(image_1, train_keypoints, dots, flags=2)

        #############################################
        ################## MATCHER ##################
        #############################################

        #Initialize the BruteForce Matcher
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

        #Match the feature points from both images
        try:
            matches = bf.match(train_descriptor, test_descriptor)
            self.bottle_found()
            #The matches with shorter distance are the ones we want.
            matches = sorted(matches, key = lambda x : x.distance)
        
            #Catch some of the matching points to draw
            good_matches = matches[:]

            #Parse the feature points
            train_points = np.float32([train_keypoints[m.queryIdx].pt for m in good_matches]).reshape(-1,1,2)
            test_points = np.float32([test_keypoints[m.trainIdx].pt for m in good_matches]).reshape(-1,1,2)

            #Create a mask to catch the matching points 
            #With the homography we are trying to find perspectives between two planes
            #Using the Non-deterministic RANSAC method
            M, mask = cv2.findHomography(train_points, test_points, cv2.RANSAC, 5.0)

            #Catch the width and height from the main image
            h,w = res_r.shape[:2]

            #Create a floating matrix for the new perspective
            pts = np.float32([[0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)

            #Create the perspective in the result 
            dst = cv2.perspectiveTransform(pts,M)
        except:
            print "No bottle"

        cv2.imshow('Img',image_1)

        cv2.imshow('Points',preview_1)
        
        cv2.imshow('Detection',image_2)       

        cv2.waitKey(1)

    def prove(self):
        for self.x in range(4,1001,18):
            for y in range (1,500):
                print (self.x)
                rospy.sleep(0.0001) 

def main():
    load_feature_object = LoadFeature()
    rospy.init_node('load_feature_node', anonymous=True)
    
    load_feature_object.prove()
    try:
        rospy.spin()
        
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()