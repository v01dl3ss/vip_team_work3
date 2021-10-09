import cv2
from utility import utils
from matplotlib import pyplot as plt
import numpy as np
import glob
from matplotlib import pyplot as plt


if __name__ == '__main__':
    images_path = glob.glob("resources/images/*.jpg")
    for image_path in images_path:
        img = cv2.imread(image_path)
        img = cv2.resize(img, (400, 770))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        shirt = img[150:350, :]
        trouser = img[400:550, 70:325]

        # Shirt
        print("Shirt main color: ")
        h_shirt = shirt[:, :, 0]
        hist_h_shirt = [0] * 256  # frequency of each h value
        hist_s_shirt = [0] * 256  # frequency of each s value
        hist_v_shirt = [0] * 256  # frequency of each v value

        for i in h_shirt:
            for k in i:
                hist_h_shirt[k] = hist_h_shirt[k] + 1;

        most_h_value_shirt = 0
        most_h_frequency_shirt = hist_h_shirt[0]
        for i in range(1, 180):
            if hist_h_shirt[i] > most_h_frequency_shirt:
                most_h_value_shirt = i
                most_h_frequency_shirt = hist_h_shirt[i]
        print(str(most_h_value_shirt) + "-> H:" + str(most_h_value_shirt * 2))

        lower = np.array([most_h_value_shirt, 0, 0])
        upper = np.array([179, 255, 255])
        mask = cv2.inRange(shirt, lower, upper)
        shirtPicked = cv2.bitwise_and(shirt, shirt, mask=mask)
        cv2.imshow("shirt_picked", shirtPicked)

        s_shirt = shirtPicked[:, :, 1]
        v_shirt = shirtPicked[:, :, 2]
        for i in s_shirt:
            for k in i:
                hist_s_shirt[k] = hist_s_shirt[k] + 1;

        for i in v_shirt:
            for k in i:
                hist_v_shirt[k] = hist_v_shirt[k] + 1;

        most_s_value_shirt = 1
        most_s_frequency_shirt = hist_s_shirt[1]
        for i in range(1, 256):
            if hist_s_shirt[i] > most_s_frequency_shirt:
                most_s_value_shirt = i
                most_s_frequency_shirt = hist_s_shirt[i]
        print(str(most_s_value_shirt) + "-> S:" + str(most_s_value_shirt * 0.39))

        most_v_value_shirt = 1
        most_v_frequency_shirt = hist_v_shirt[1]
        for i in range(1, 256):
            if hist_v_shirt[i] > most_v_frequency_shirt:
                most_v_value_shirt = i
                most_v_frequency_shirt = hist_v_shirt[i]
        print(str(most_v_value_shirt) + "-> V:" + str(most_v_value_shirt * 0.39))

        plt.plot(hist_h_shirt, color='r', label="h")
        plt.plot(hist_s_shirt, color='g', label="s")
        plt.plot(hist_v_shirt, color='b', label="v")
        plt.legend()
        plt.show()
        # Trouser
        print("Trouser main color: ")
        h_trouser = trouser[:, :, 0]
        hist_h_trouser = [0] * 256  # frequency of each h value
        hist_s_trouser = [0] * 256  # frequency of each s value
        hist_v_trouser = [0] * 256  # frequency of each v value

        for i in h_trouser:
            for k in i:
                hist_h_trouser[k] = hist_h_trouser[k] + 1;

        most_h_value_trouser = 0
        most_h_frequency_trouser = hist_h_trouser[0]
        for i in range(1, 180):
            if hist_h_trouser[i] > most_h_frequency_trouser:
                most_h_value_trouser = i
                most_h_frequency_trouser = hist_h_trouser[i]
        print(str(most_h_value_trouser) + "-> H:" + str(most_h_value_trouser * 2))

        lower = np.array([most_h_value_trouser, 0, 0])
        upper = np.array([179, 255, 255])
        mask = cv2.inRange(trouser, lower, upper)
        trouserPicked = cv2.bitwise_and(trouser, trouser, mask=mask)
        cv2.imshow("trouser_picked", trouserPicked)

        s_trouser = trouserPicked[:, :, 1]
        v_trouser = trouserPicked[:, :, 2]
        for i in s_trouser:
            for k in i:
                hist_s_trouser[k] = hist_s_trouser[k] + 1
        for i in v_trouser:
            for k in i:
                hist_v_trouser[k] = hist_v_trouser[k] + 1

        most_s_value_trouser = 1
        most_s_frequency_trouser = hist_s_trouser[1]
        for i in range(1, 256):
            if hist_s_trouser[i] > most_s_frequency_trouser:
                most_s_value_trouser = i
                most_s_frequency_trouser = hist_s_trouser[i]
        print(str(most_s_value_trouser) + "-> S:" + str(most_s_value_trouser * 0.39))

        most_v_value_trouser = 1
        most_v_frequency_trouser = hist_v_trouser[1]
        for i in range(1, 256):
            if hist_v_trouser[i] > most_v_frequency_trouser:
                most_v_value_trouser = i
                most_v_frequency_trouser = hist_v_trouser[i]
        print(str(most_v_value_trouser) + "-> V:" + str(most_v_value_trouser * 0.39) + '\n')

        plt.plot(hist_h_trouser, color='r', label="h")
        plt.plot(hist_s_trouser, color='g', label="s")
        plt.plot(hist_v_trouser, color='b', label="v")
        plt.legend()
        plt.show()
        # Waite
        cv2.waitKey(0)
