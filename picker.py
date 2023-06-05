import cv2
import numpy as np
import os
import util

left_clicks = list()
img = np.array([])
imgs_history = []

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global left_clicks
        global img
        global imgs_history

        left_clicks.append([x, y])
        
        if len(imgs_history) > 0:
            new_img = imgs_history[len(imgs_history) - 1].copy()
        else: 
            new_img = img.copy()
        cv2.circle(new_img, (x,y), radius=5, color=(255, 0, 0), thickness=2)
        imgs_history.append(new_img)
        cv2.imshow('image', new_img)

def manual_label(file_path: str):
    global img
    img = cv2.imread(file_path)
    cv2.imshow('image',img)
    cv2.setMouseCallback('image', click_event)
    while True:
        key = cv2.waitKey(0) & 0xFF
        if key == 27:
            break
        if key == ord('c') and len(left_clicks) > 0:
            left_clicks.pop()
            imgs_history.pop()
            if len(imgs_history) > 0:
                cv2.imshow('image', imgs_history[len(imgs_history) - 1])
            else:
                cv2.imshow('image', img)

    cv2.destroyAllWindows()
    left_clicks.clear()

if __name__ == "__main__":
    imgs = []
    img_dir = "mahjong_img"
    for file in os.listdir(img_dir):
        file_path = os.path.join(img_dir, file)
        if file_path.endswith(".HEIC"):
            util.heic_to_jpg(file_path, keep=False)

    # for file in os.listdir(img_dir):
    #     file_path = os.path.join(img_dir, file)
    #     manual_label(file_path)
