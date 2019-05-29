import cv2
import xlwt
from datetime import datetime
from xlrd import open_workbook
from xlutils.copy import copy
from pathlib import Path

## for quit press q and for making entery in database press w
print "For quit press q and for make entery in excel file press w"

filename='filename';

# Method for making entery in excel file
def output(filename, sheet,num, name, present):
    my_file = Path('attendance_files/'+filename+str(datetime.now().date())+'.xls')
    if my_file.is_file():
        rb = open_workbook('attendance_files/'+filename+str(datetime.now().date())+'.xls')
        book = copy(rb)
        sh = book.get_sheet(0)
        # file exists
    else:
        book = xlwt.Workbook()
        sh = book.add_sheet(sheet)
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                         num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
    #variables = [x, y, z]
    #x_desc = 'Display'
    #y_desc = 'Dominance'
    #z_desc = 'Test'
    #desc = [x_desc, y_desc, z_desc]
    sh.write(0,0,datetime.now().date(),style1)


    col1_name = 'Student Name'
    col2_name = 'Present'

    sh.write(1,0,col1_name,style0)
    sh.write(1, 1, col2_name,style0)

    sh.write(num+1,0,name)
    sh.write(num+1, 1, present)
    #You may need to group the variables together
    #for n, (v_desc, v) in enumerate(zip(desc, variables)):
    fullname=filename+str(datetime.now().date())+'.xls'
    book.save('attendance_files/'+fullname)
    return fullname


# Method to draw boundary around the detected feature
def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
    # Converting image to gray-scale
    gray_img =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detecting features in gray-scale image, returns coordinates, width and height of features
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
    coords = []
    id = 0
    # drawing rectangle around the feature and labeling it
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

        id,confi = clf.predict(gray_img[y:y+h, x:x+w])
        #change confi variable according to percentage shown in output window
        if(confi < 35):
            if id == 1:
                cv2.putText(img, "Sahil" + str(confi), (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                if cv2.waitKey(1) & 0xFF == ord('w'):
                	id = 'Sahil'
                	filename = output('attendance', 'class1', 1, id, 'yes')
            elif id == 2:
                cv2.putText(img, "Roubal" + str(confi), (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                if cv2.waitKey(1) & 0xFF == ord('w'):
                	id = 'Roubal'
                	filename = output('attendance', 'class1', 2, id, 'yes')
            #add more id's
        else:
            cv2.putText(img, "not found", (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8,color, 1, cv2.LINE_AA)
        
        coords = [x, y, w, h]
    return coords

def recognize(img, elf, faceCascade):
    color = {"blue": (255, 0, 0), "red": (0, 0, 255), "green": (0, 255, 0), "white": (255, 255, 255)}
    coords = draw_boundary(img, faceCascade, 1.1, 10, color["white"], "Face", clf)
    return img


# Loading classifiers
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyesCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
noseCascade = cv2.CascadeClassifier('Nariz.xml')
mouthCascade = cv2.CascadeClassifier('Mouth.xml')

clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier.yml")

# Capturing real time video stream. 0 for built-in web-cams, 0 or -1 for external web-cams
video_capture = cv2.VideoCapture(0)

img_id = 0

while True:
    # Reading image from video stream
    _, img = video_capture.read()
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    img = recognize(img, clf, faceCascade)
    
    # Writing processed image in a new window
    cv2.imshow("face detection", img)

    img_id += 1


# releasing web-cam
video_capture.release()
# Destroying output window
cv2.destroyAllWindows()