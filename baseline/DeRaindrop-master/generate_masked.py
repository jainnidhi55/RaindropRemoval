import cv2
import os
import argparse

binary_mask_pattern = '{}_rain_rain_maskbinary.jpg'

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str) # black or white
    parser.add_argument("--mask_dir", type=str)
    parser.add_argument("--mask_out_dir", type=str)
    parser.add_argument("--input_dir", type=str)
    parser.add_argument("--output_dir", type=str)
    parser.add_argument("--thresh", type=int, required=True)
    args = parser.parse_args()
    return args

def generate_masked(args):
    thresh_dir = 'thresh_{}'.format(args.thresh)
    mask_dir = os.path.join(args.mask_dir, thresh_dir)
    out_dir = os.path.join(args.output_dir, thresh_dir)
    mask_out_dir = os.path.join(args.mask_out_dir, thresh_dir)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    if not os.path.exists(mask_out_dir):
        os.makedirs(mask_out_dir)
    for filename in os.listdir(args.input_dir):
        try:
            img = cv2.imread(os.path.join(args.input_dir, filename))
            # get mask
            filename_mask = filename[:-4] + '_rain_maskbinary.jpg'
            mask = cv2.imread(os.path.join(mask_dir, filename_mask))
            # hole as white
            if args.mode == 'white':
                img[mask == 0] = 255
                mask[mask == 0] = 2
                mask[mask == 1] = 0
                mask[mask == 2] = 1
            else:
                img[mask == 1] = 255
            filename_out = filename[:-4] + '_masked.png'
            filename_mask_out = filename[:-4] + '_mask.png'
            cv2.imwrite(os.path.join(out_dir, filename_out), img)
            cv2.imwrite(os.path.join(mask_out_dir, filename_out), mask * 255)
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    args = get_args()
    generate_masked(args)