import cv2 as cv
"""

Thsi function returns a resized Video or Photo
Inputs : Frame and Scale
Output : Resized Frame

"""
def rescaleVideo(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeResolution (width, height):           # Changes resolution of live videos
    videoCapture.set(3, width)
    videoCapture.set(4, height)
img = cv.imread('J:\Photos\Emma watson\cvSample.jpg')
rescaledImage = rescaleVideo(img)
cv.imshow('Emma', img)
cv.imshow('Emma Rescaled', rescaledImage)

videoCapture = cv.VideoCapture(0)                # 0 refrences web cam
"""

Capture and display Video
Plays a Video Frame by Frame for 20 seconds or quits when 'd' is hit

"""
capture = cv.VideoCapture('J:\Anime\Days\AnimePahe_Days_TV_-_05_720p_HorribleSubs.mp4')
while True:
    isTrue, frame =capture.read()               # isTrue - Checks if there is a frame; frame Captures the frame
    frame_resized = rescaleVideo(frame)         # Rescales the output frame
    cv.imshow('Video', frame)                   # prints the frames
    cv.imshow('Resized Video', frame_resized)
    if cv.waitKey(3000) & 0xFF==ord('d'):       # waitkey() will allow us to move to the next function after pressing any key for 3000 ms
        break
capture.release()
cv.destroyAllWindows()                          # Destroys all windows when the script is closed

#cv.waitKey(0)