import numpy as np
import sys
import cv2
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from PIL import Image
import glob

def video():
    cap = cv2.VideoCapture('cfd.mp4')
    count = 0
    while cap.isOpened():
        ret,frame = cap.read()
        cv2.imshow('window-name',frame)
        cv2.imwrite("frame%d.jpg" % count, frame)
        count = count + 1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        # set to 100 frames or else it'll give you a million
        #if count == 100:
        #    return
    cap.release()
    cv2.destroyAllWindows()

def image(start_frame,end_frame):
    video()
    vid_frames = glob.glob('frame*')
    angles_out = []

    #for a in range(len(vid_frames)):
    for a in range(start_frame, end_frame):
        im = cv2.imread(vid_frames[a])
        imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray,127,255,0)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        width, height = Image.open(vid_frames[a]).size

        img = np.zeros((height,width,3), np.uint8)
        #img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

        angles = []

        #loop through all contours
        for i in range(len(contours)):
            #need contours with 5 or more reference points to fitEllipse which gets the angle orientation
            if(len(contours[i]) >= 5):
                img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
                (x,y),(MA,ma),angle = cv2.fitEllipse(contours[i])
                if(angle == 0.0):
                    continue
                else:
                    if angle < 100:
                        angle = 0
                    else:
                        angle = 1
                    #print('Angle: %.2f' % angle)
                    angles.append(angle)
            else:
                img = cv2.drawContours(img, contours, -1, (0,0,0), 3)


        num_bins = 2
        n, bins, patches = plt.hist(angles, num_bins, facecolor='blue', alpha=0.5)
        plt.show()

        # All angles of every frame
        angles_out.append(angles)
        #print(angles)

        #cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        #cv2.imshow('image', img)
        #cv2.waitKey(0)
        cv2.destroyAllWindows()

    return end_frame


# only do this for first time to get all frames

start_frame = 50
end_frame = 100
image(start_frame,end_frame)
