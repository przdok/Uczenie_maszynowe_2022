import cv2
import numpy as np

film = cv2.VideoCapture(
    "C:\\Users\\Dell\\Google Drive\\Z mega\\Informatyka - materialy wlasne\\Rok III\\Semestr V\\Uczenie maszynowe\\one round kam4.MP4")

aktualnaKlatka = 1
img_array = []
while(True):
    bul, klatka = film.read()
    

    if bul:
        height, width, layers = klatka.shape
        size = (width, height)
        nazwa = "C:\\Users\\Dell\\Google Drive\\Z mega\\Informatyka - materialy wlasne\\Rok III\\Semestr V\\Uczenie maszynowe\\dane\\klatka " + \
            str(aktualnaKlatka) + ".jpg"
        klatka_hsv = cv2.cvtColor(klatka, cv2.COLOR_BGR2HSV)
        low_red1 = np.array([169, 170, 20])
        high_red1 = np.array([179, 255, 255])
        red_mask1 = cv2.inRange(klatka_hsv, low_red1, high_red1)

        low_red2 = np.array([0, 170, 20])
        high_red2 = np.array([9, 255, 255])
        red_mask2 = cv2.inRange(klatka_hsv, low_red2, high_red2)

        red_mask = cv2.bitwise_or(red_mask1, red_mask2)

        low_blue = np.array([112, 170, 20])
        high_blue = np.array([126, 255, 255])
        blue_mask = cv2.inRange(klatka_hsv, low_blue, high_blue)

        maska = cv2.bitwise_or(blue_mask, red_mask)
        klatka = cv2.bitwise_and(klatka, klatka, mask = maska)

        img_array.append(klatka)
        aktualnaKlatka = aktualnaKlatka + 1
    else:
        break
film = cv2.VideoWriter("C:\\Users\\Dell\\Google Drive\\Z mega\\Informatyka - materialy wlasne\\Rok III\\Semestr V\\Uczenie maszynowe\\dane\\efekt.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 50, size)
for i in range(len(img_array)):
    film.write(img_array[i])
film.release()
cv2.destroyAllWindows()