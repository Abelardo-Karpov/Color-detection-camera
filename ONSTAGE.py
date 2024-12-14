import numpy as np
import cv2

# Prende la camara
webcam = cv2.VideoCapture(1)


# Loop, continuamente convierte frames de bgr a hsv
while (1):
    ## Asigna variable a los frames
    _, imageFrame = webcam.read()
    ## Convierte los frames bgr a hsv y los asigna a variable
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)


    # Define rango de colores
    ## Rangos color rojo
    red_lower = np.array([170, 130, 100], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    ## Define la mascara
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    # Funcion en variable para detectar color en particular
    kernal = np.ones((5, 5), "uint8")

    ## color rojo
    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, imageFrame, mask=red_mask)

    # Creando contornos para seguir al color seleccionado, mascaras de seguimiento y añadimos texto
    ## Color rojo
    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            #investigar que hace boundingrect
            x, y, w, h = cv2.boundingRect(contour)
            #imageframe pq es un visual que se mostrara ahi
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                        (x + w, y + h),
                                        (0, 0, 255), 2)
            cv2.putText(imageFrame, "Color Rojo", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))

    cv2.imshow("Color Detection", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break
    




