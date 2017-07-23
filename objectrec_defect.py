"""
Version 1.0 without GUI.

This program may need to be modified to run on Python 2.7. Some libraries(PIL) may not be installed.

This project uses OpenCV libraries for identifying different objects trained and identifying minor defects.
We have used only Open Source tools for development. Spyder(Python 3.6) as our primary IDE and Fedora 24.
The project was completed within one month as part of our internship.
Here 'Hero' and 'Boxer' are name of the objects we were supposed to identify. Whose images we cannot provide for testing.
Please train and add your own object and change the name accordingly.

We will be releasing next version soon with GUI.

"""

import cv2
import numpy as np
import time
import os
from datetime import datetime
from PIL import Image


#function in which object identification and fault detection is done.

def callback():
    
    #importing the cascades of the object to identified. You can create your own cascade using openCV.
	
    boxer_cascade=cv2.CascadeClassifier('C:\\Users\\tushar\\Desktop\\Mutha\\cascade_boxer.xml')
    hero_cascade=cv2.CascadeClassifier('C:\\Users\\tushar\\Desktop\\Mutha\\cascade_hero.xml')
    


    #Camera source for your program. For using system camera use '0'.
    cam_source = 0
    
    cap = cv2.VideoCapture(cam_source)
    boxer_count=0
    hero_count=0
    
	# Imports system time for terminating the program automatically after 5 seconds. 
  
    termination_time_system1 = datetime.now()
    termination_time_start = termination_time_system1.second % 5
    print ("start",termination_time_start)
    
	#synchronising the time with system time. 
    time.sleep(1)
  
	
    while True:
        
        # Imports system time and compares with termination_time_system1
		
        termination_time_system2 = datetime.now()
        termination_time_check = termination_time_system2.second % 5
        print ("current",termination_time_check)      
        select = 0
        
        ret, img = cap.read()
		
        if ret is True:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            boxer = boxer_cascade.detectMultiScale(gray,1.3,5)
            hero = hero_cascade.detectMultiScale(gray,1.3,5)
       
			# For loop is used of identifying object. You can add as many loops depending on number of objects.
			
            for (x,y,w,h) in boxer:
                font = cv2.FONT_HERSHEY_SIMPLEX
                #cv2.putText(img,'BOXER',(x-w, y-h), font,0.5, (0,255,255), 1,cv2.LINE_AA)
                #cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                print ("boxer_",boxer_count)
                boxer_count=boxer_count+1
        
  
            for (x,y,w,h) in hero:
                #cls()
                font = cv2.FONT_HERSHEY_SIMPLEX
                #cv2.putText(img,'HERO',(x-w, y-h), font,0.5, (0,255,255), 1,cv2.LINE_AA)
                #cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,255), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                print ("hero_        ",hero_count)
                hero_count=hero_count+1            
        
            cv2.imshow('Detecting', img)
            k = cv2.waitKey(30) & 0xff
            if k == 27 or termination_time_start == termination_time_check:
              break
      
    
    ret,img=cap.read()
    #cv2.imshow('capture.jpg',img)
	
	#stores the final output result in home directory.
    cv2.imwrite('C:\\Users\\tushar\\Desktop\\Mutha\\capture.jpg',img)
       
    cap.release()
    cv2.destroyAllWindows()
    
    #depending on which object is found select variable is assigned.
    
    if(boxer_count>hero_count):
     print("Boxer found")
     select=2
	 
    elif (boxer_count<hero_count):
     print("Hero found")
     select=1
	 
    else:
     print("No object detected")
     if(select==0):
      app.infoBox("title", "NO object found")
     
  
	
    img_rgb = cv2.imread('capture.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    
	#templates of the object in which defect is to be found is present in this array. 
    template_array2 = ["temp1_2.jpg","ipadboxer.jpg"]
    
    if select == 1:
        item = template_array2[0]
    if select == 2:
        item = template_array2[1]
        
    template=cv2.imread(item,2)
    w, h = template.shape[::-1]
	
	#algorithm to match actual job with template for identifying defects.
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
	
	#setting is the threshold is one important thing to do. 0.7~0.75 is optimal.
    threshold = 0.75
    loc = np.where( res >= threshold)
    counter1 = 0
    temp_ptx=999
    temp_pty=999
	
	#compare pixels colors at a particular location
    for pt in zip(*loc[::-1]):
            
        im = Image.open("C:\\Users\\tushar\\Desktop\\Mutha\\capture.jpg")
        rgb_im = im.convert('RGB')
            
        ptx = int(pt[0] + w - 2)
        pty = int(pt[1] + h )
        #converts negative pixel difference 
        posx = abs(temp_ptx - ptx)
        posy = abs(temp_pty - pty)
            
        if posx >5 and posy >5:
            print(ptx,pty)
            temp_ptx = ptx
            temp_pty = pty
            r, g, b = rgb_im.getpixel((ptx,pty))
            print ("RGB",r, g, b)
			
            if r>200 and g<50 and b<50:	#red colour range
                continue
            else:
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
                counter1 = counter1 +1
            
    cv2.imwrite('res1.jpg',img_rgb)
    print ("first ",counter1) 
    cv2.waitKey()
	
	#display output
    if(select==1 and counter1==1):
        app.infoBox("title", "hero passed")
    if(select==2 and counter1==5):
        app.infoBox("title", "boxer passed")
    if(select==1 and counter1 != 1):
        app.infoBox("title", "fault detected in hero")
    if(select==2 and counter1 != 5):
        app.infoBox("title", "fault detected in boxer")
 

callback()
app.go()