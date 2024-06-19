The “Face Recognition-based Attendance System” is an attendance management system developed using 
Python and OpenCV. This system aims to automate the attendance process in educational institutions or 
organizations by leveraging the power of computer vision and machine learning.
The system operates by capturing live video feed from a webcam or any other suitable camera source. It 
then processes each frame using OpenCV, a popular computer vision library in Python, to detect and 
recognize human faces. The face detection algorithm identifies the presence of faces within the frame, 
while the face recognition algorithm matches the detected faces with pre-registered faces in the system's 
database. Here are the algorithms used in the making of this system:

Haar cascade Algorithm:
It is a machine learning based approach where a cascade function is trained from a lot of
positive and negative images (where positive images are those where the object to be
detected is present, negative are those where it is not). It is then used to detect objects in
other images. Luckily, OpenCV offers pre-trained Haar cascade algorithms, organized into 
categories (faces, eyes and so forth), depending on the images they have been trainedon.

LBPH Algorithm:
Local Binary Pattern (LBP) is a simple yet very efficient texture operator which labels
the pixels of an image by thresholding the neighborhood of each pixel and considers the
result as a binary number. It has further been determined that when LBP is combined with
histograms of oriented gradients (HOG) descriptor, it improves the detection performance 
considerably on some datasets.

Face landmark estimation algorithm:
Face landmark estimation is an algorithmic process 
that involves detecting and localizing key facial features in an image or video, such as the 
position of the eyes, nose, mouth, and other facial landmarks. The purpose of this algorithm is 
to accurately identify and track these landmarks for various applications, including facial 
recognition, emotion analysis, virtual reality, and augmented reality.

Convolutional Neural Network (CNN):
A Convolutional Neural Network (CNN) is a type 
of deep learning algorithm that is particularly well-suited for image recognition and 
processing task. It is particularly effective in tasks related to computer vision, including 
image classification, object detection, and image segmentation.
The architecture of a CNN is composed of multiple layers, typically including convolutional 
layers, pooling layers, and fully connected layers. These layers are stacked together to form a 
deep network that can learn hierarchical representations of the input data.

SVM Classifier: 
A Support vector Machine (SVM) classifier is a supervised machine 
learning algorithm that is primarily used for binary classification tasks, although it can be 
extended to handle multi-class problems as well. SVMs are known for their effectiveness in 
separating data into distinct classes by finding an optimal hyperplane that maximally 
separates the data points of different classes.
The basic principle of an SVM is to map input data points into a higher-dimensional feature 
space and then find the hyperplane that best separates the data points of different classes. The 
hyperplane is chosen such that the margin, which is the distance between the hyperplane and 
the nearest data points of each class (called support vectors), is maximized.
Once the SVM classifier is trained, it can be used to predict the class labels of new, unseen data 
points by evaluating which side of the hyperplane they fall on. The decision boundary is 
determined by the support vectors, which are the data points that lie closest to the hyperplane.
SVMs have several advantages, including their ability to handle high-dimensional data, their 
robustness to overfitting, and their effectiveness in handling small training datasets. However, 
SVMs can be computationally expensive, especially with large datasets, and they may require 
careful selection of hyperparameters, such as the regularization parameter (C) and the kernel 
parameters.


Results:


![image](https://github.com/pyr0-man1ac/FaceDetectionSystem/assets/120567662/b4ba46a7-4cdc-48fe-b1fa-054647220cc8)
![Screenshot_20-6-2024_12540_](https://github.com/pyr0-man1ac/FaceDetectionSystem/assets/120567662/a59f4bc4-69ab-4e7b-a852-84b889f8f75d)

