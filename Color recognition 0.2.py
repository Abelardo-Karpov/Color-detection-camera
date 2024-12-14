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

    ## Rangos color verde
    green_lower = np.array([40, 150, 20], np.uint8)
    green_upper = np.array([70, 255, 255], np.uint8)
    ## Define la mascara
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    ## Rangos color azul
    blue_lower = np.array([110, 180, 0], np.uint8)
    blue_upper = np.array([116, 255, 255], np.uint8)
    ## Define la mascara
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    ## Rangos color naranja
    orange_lower = np.array([2.5, 140, 100], np.uint8)
    orange_upper = np.array([13, 255, 255], np.uint8)
    ## Define la mascara
    orange_mask = cv2.inRange(hsvFrame, orange_lower, orange_upper)

    ## Rangos color amarillo
    yellow_lower = np.array([17.5, 100, 100], np.uint8)
    yellow_upper = np.array([30, 255, 255], np.uint8)
    ## Define la mascara
    yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper) 

    ## Rangos color celeste
    cyan_lower = np.array([95, 112, 120], np.uint8)
    cyan_upper = np.array([108, 255, 255], np.uint8)
    ## Define la mascara
    cyan_mask = cv2.inRange(hsvFrame, cyan_lower, cyan_upper)

    ## Rangos color morado
    purple_lower = np.array([118, 100, 100], np.uint8)
    purple_upper = np.array([130, 255, 255], np.uint8)
    ## Define la mascara
    purple_mask = cv2.inRange(hsvFrame, purple_lower, purple_upper)

    ## Rangos color negro
    black_lower = np.array([0, 0.2, 0.2], np.uint8)
    black_upper = np.array([0, 32, 32], np.uint8)
    ## Define la mascara
    black_mask = cv2.inRange(hsvFrame, black_lower, black_upper)

    ## Rangos color rosa
    pink_lower = np.array([135, 100, 100], np.uint8)
    pink_upper = np.array([160, 255, 255], np.uint8)
    ## Define la mascara
    pink_mask = cv2.inRange(hsvFrame, pink_lower, pink_upper)

    ## Rangos color gris
    gray_lower = np.array([0, 0, 0], np.uint8)
    gray_upper = np.array([80, 80, 80], np.uint8)
    ## Define la mascara
    gray_mask = cv2.inRange(hsvFrame, pink_lower, pink_upper)   


    # Funcion en variable para detectar color en particular
    kernal = np.ones((5, 5), "uint8")

    ## color rojo
    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, imageFrame, mask=red_mask)

    ## color verde
    green_mask = cv2.dilate(green_mask, kernal)
    res_green = cv2.bitwise_and(imageFrame, imageFrame, mask=green_mask)

    ## color blue
    blue_mask = cv2.dilate(blue_mask, kernal)
    res_blue = cv2.bitwise_and(imageFrame, imageFrame, mask=blue_mask)

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

            cv2.putText(imageFrame, "Red Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))

    ## Color verde
    contours, hierarchy = cv2.findContours(green_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (0, 255, 0), 2)

            cv2.putText(imageFrame, "Green Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 255, 0))

    ## Color azul
    contours, hierarchy = cv2.findContours(blue_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 2)

            cv2.putText(imageFrame, "Blue Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 0))

    ## Color naranja
    contours, hierarchy = cv2.findContours(orange_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (6, 100, 255), 2)

            cv2.putText(imageFrame, "Orange Color", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (6, 100, 255))

    ## Color amarillo
    contours, hierarchy = cv2.findContours(yellow_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (6, 255, 255), 2)

            cv2.putText(imageFrame, "Yellow Color", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (6, 255, 255))

    ## Color celeste
    contours, hierarchy = cv2.findContours(cyan_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (255, 255, 0), 2)

            cv2.putText(imageFrame, "Cyan Color", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 255, 150))

    ## Color morado
    contours, hierarchy = cv2.findContours(purple_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (128, 0, 128), 2)

            cv2.putText(imageFrame, "Purple Color", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (128, 0, 128))

    ## Color rosa
    contours, hierarchy = cv2.findContours(pink_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 255), 2)

            cv2.putText(imageFrame, "Pink Color", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 255))

    ## Color negro
    contours, hierarchy = cv2.findContours(black_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (0, 2, 2), 2)

            cv2.putText(imageFrame, "Black Color", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 2, 2))

    ## Color gris
    contours, hierarchy = cv2.findContours(gray_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (128, 128, 128), 2)

            cv2.putText(imageFrame, "Gray Color", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (128, 128, 128))


    # Iniciar programa
    ## muestra el programa con el nombre Color Detection y las frames modificadas
    cv2.imshow("Color Detection", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break