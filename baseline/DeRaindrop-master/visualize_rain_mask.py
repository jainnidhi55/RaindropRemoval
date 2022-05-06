import numpy as np
import cv2
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--img_mask_path", type=str)
    args = parser.parse_args()
    return args

def save_rain_mask(img_mask_path):
    img_npy = np.load('rain_masks/' + img_mask_path)
    img_npy = np.squeeze(img_npy, 1)
    img_npy = np.transpose(img_npy, (1, 2, 0))
    img_npy = img_npy * 255

    path_to_save = 'visualize_rain_masks/' + img_mask_path.split('.')[0] + '.jpg'
    print("path: ", path_to_save)
    cv2.imwrite(path_to_save, img_npy)

if __name__ == '__main__':
    print("reached step 1")
    args = get_args()
    print("args: ", args)
    save_rain_mask(args.img_mask_path)






