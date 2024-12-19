import numpy as np
import cv2


def create_mask(_color_lower, _color_upper):
    color_lower = np.array(_color_lower, np.uint8)
    color_upper = np.array(_color_upper, np.uint8)
    ## Define la mascara
    color_mask = cv2.inRange(hsvFrame, color_lower, color_upper)
    return color_mask




# Prende la camara
webcam = cv2.VideoCapture(2)

# Loop, continuamente convierte frames de bgr a hsv
while (1):
    ## Asigna variable a los frames
    _, imageFrame = webcam.read()
    ## Convierte los frames bgr a hsv y los asigna a variable
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)


    red_mask = create_mask([170, 130, 100], [180, 255, 255])
    green_mask = create_mask([40, 150, 20], [70, 255, 255])
    blue_mask = create_mask([110, 180, 0], [116, 255, 255])
    orange_mask = create_mask([2.5, 140, 100], [13, 255, 255])
    yellow_mask = create_mask([17.5, 100, 100], [30, 255, 255])
    cyan_mask = create_mask([95, 112, 120], [108, 255, 255])
    purple_mask = create_mask([118, 100, 100], [130, 255, 255])
    black_mask = create_mask([0, 0.2, 0.2], [0, 32, 32])
    pink_mask = create_mask([135, 100, 100], [160, 255, 255])
    gray_mask = create_mask([0, 0, 0], [80, 80, 80])


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