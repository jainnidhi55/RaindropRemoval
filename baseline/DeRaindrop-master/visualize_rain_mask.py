import numpy as np
import cv2
import argparse
import os

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str)
    parser.add_argument("--output_dir", type=str)
    parser.add_argument("--threshold", type=int)
    args = parser.parse_args()
    return args

def save_rain_mask(img_mask_path):
    img_npy = np.load('rain_masks/' + img_mask_path)
    img_npy = np.squeeze(img_npy, 1)
    img_npy = np.transpose(img_npy, (1, 2, 0))
    img_npy = img_npy * 255

    path_to_save = 'visualize_rain_masks/' + img_mask_path.split('.')[0] + '.jpg'
    # print("path: ", path_to_save)
    cv2.imwrite(path_to_save, img_npy)

def save_binary_rain_mask(input_dir, output_dir, threshold):

    input_list = sorted(os.listdir(args.input_dir))
    for curr_input in input_list:
        img_name = curr_input.split('.')[0]

        # print(input_dir + curr_input)
        img_npy = np.load(input_dir + curr_input)
        img_npy = np.squeeze(img_npy, 1)
        img_npy = np.transpose(img_npy, (1, 2, 0))
        img_npy = img_npy * 255

        img_npy[img_npy < threshold] = 0
        img_npy[img_npy >= threshold] = 1

        # path_to_save = 'visualize_rain_masks/' + img_mask_path.split('.')[0] + str(threshold) + '.jpg'
        path_to_save = args.output_dir + '/thresh_' + str(threshold) + '/' + img_name + 'binary.jpg'
        print(path_to_save)
        cv2.imwrite(path_to_save, img_npy)

if __name__ == '__main__':
    print("reached step 1")
    args = get_args()
    print("args: ", args)
    save_binary_rain_mask(args.input_dir, args.output_dir, args.threshold)






