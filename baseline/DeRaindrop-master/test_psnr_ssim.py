import skimage
import cv2
from skimage.measure import compare_psnr, compare_ssim
import os 
import statistics

predict_dir = 'res_thresh80'
gt_dir = 'train/gt'

def calc_psnr(im1, im2):
    im1_y = cv2.cvtColor(im1, cv2.COLOR_BGR2YCR_CB)[:, :, 0]
    im2_y = cv2.cvtColor(im2, cv2.COLOR_BGR2YCR_CB)[:, :, 0]
    return compare_psnr(im1_y, im2_y)

def calc_ssim(im1, im2):
    im1_y = cv2.cvtColor(im1, cv2.COLOR_BGR2YCR_CB)[:, :, 0]
    im2_y = cv2.cvtColor(im2, cv2.COLOR_BGR2YCR_CB)[:, :, 0]
    return compare_ssim(im1_y, im2_y)


psnr = []
ssim = []
for name in os.listdir(predict_dir):
    idx = name.split('_')[0]
    img2 = cv2.imread(os.path.join(predict_dir, idx+'_rain.png'))
    img1 = cv2.imread(os.path.join(gt_dir, idx+'_clean.png'))

    print(os.path.join(predict_dir, idx+'_rain.png'))
    psnr.append(calc_psnr(img1, img2))
    ssim.append(calc_ssim(img1, img2))

psnr = statistics.mean(psnr)
ssim = statistics.mean(ssim)
print('psnr', psnr)
print('ssim', ssim)