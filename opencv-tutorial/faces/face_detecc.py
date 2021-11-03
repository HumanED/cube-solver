import cv2 as cv

# haar cascades try to detect faces by seeing the edges of an image

haar_cascade = cv.CascadeClassifier("haar_face.xml")

def find_face(img, scale_factor, min_neighbours, show = True, disp_colour = (0, 255, 0), thickness = 1):

    grey_img = img

    if (len(img.shape) == 3):
        grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img_rect = haar_cascade.detectMultiScale(grey_img, scaleFactor = scale_factor, minNeighbors = min_neighbours)

    print(f"Faces found: {len(img_rect)}")

    if (show):
        img_copy = img.copy()
        for (x,y,w,h) in img_rect:
            cv.rectangle(img_copy, pt1 = (x,y), pt2 = (x+w, y+h), color = disp_colour, thickness = thickness)

        cv.imshow("Just Face It", img_copy)
        cv.waitKey(0)

def find_face_path(img_path, scale_factor, min_neighbours, show = True, disp_colour = (0, 255, 0), thickness = 1):
    img = cv.imread(img_path)

    find_face(img, scale_factor, min_neighbours, show, disp_colour, thickness)

find_face_path("group.jpeg", scale_factor = 1.1, min_neighbours = 3, thickness = 4)
