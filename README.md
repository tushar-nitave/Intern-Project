# Intern-Project
##### Tushar Nitave, Durgesh Reddiyar, Pranav Shah

### 1. Overview
___
<p>In this project we have developed a machine learning module using Open Computer Vision which will be used to identify different jobs different jobs. Variety of machine learning approaches were examined to solve job and defect identification problem. Also we have developed a small module to identify visual defects in given job. This project was basically done for a manufacturing company.</p>

<br>

### 2. Working Environment
___
<p>Our project is completely open source. We have used open source operating system like Fedora and other open source tools and libraries like Spyder, OpenCV. We used Python 3.6 as our base language for developing source code.  The system will run on Raspberry Pi, which can be mounted at any required place. Suitable place for would be near to conveyer belt on which various kinds of jobs will be moving on. The Raspberry Pi would be connected to a camera which would be placed above the conveyer line.The video captured by camera would be feed to Raspberry Pi for processing, the result of Raspberry Pi will be display on screen and required further actions will be taken on.</p>

<br>

### 3. Haar  Cascade
___
<p>Haar-cascade is an object detection algorithm used to locate faces, pedestrians, objects and facial expressions in an image. In Haar-cascade, the system is provided with several numbers of positive images (like images of various jobs to be identified) and negative images (images that are not jobs but can be anything else like chair, table, wall, etc.), and the feature selection is done along with the classifier training using Adaboost and Integral images.</p>

  #### Generating Haar cascade
  
  <sub>For generating  Haar cascade, a proper working directory is prepared. This directory contains  one positive image — object to      identified, negative images, one vector file and a cascade file. Using OpenCV libraries the cascade file is generated in the working directory which will be then used for further process. 
</sub>
  <br><sub>It has to be noted that every object will have a different cascade, and needs to be trained separately. Training time for cascade will depend on system used for training (generally 5-6 hours for one cascade). During training of the cascade we can see the acceptance ratio of positive images. A well trained cascade should have acceptance ratio in power of 10-5 . If the model is trained beyond this, it will be overtrained and will not be able to identify the object unless exact same condition are provided. Hence overtraining of models should be avoided. At the end of training XML file is generated (cascade.xml) which contains all the metadata and other information about training. Fig. 2 shows generation of cascade file. 
</sub>

  #### Using Haar Cascade in Python
  
  <sub>The generated haar cascade is then used in python script which will be installed on Raspberry Pi 3. This python script contains all the necessary code for identifying object and finding the defect. Cascade file is imported along with OpenCV  libraries. Multiple cascade files related to different objects can be imported in a single program which allows us to write a single program for multiple objects.
</sub>

<br>

### 4. Conclusions
___

<p>We have utilized the techniques of artificial intelligence(Image Processing) for training a machine so that it can identify the given object. We used haar cascading technique for training the machine. The main and one of the important aspect of this project was that we used all the open source tools for development.</p>

