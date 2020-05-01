import numpy as np
from scipy import ndimage
import cv2 as cv

def matlab_style_gauss2D(size=3, sigma=1):
    """ Generate a 2D Gaussian filter of the specified sigma
    
    Params: 
        size (int) filter size
        sigma (float) standard deviation
    Returns: f (np.array) gaussian filter
    """
    
    d = (size - 1.)/2.
    y, x = np.ogrid[-d:d+1, -d:d+1]
    f = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )/np.pi*2.*sigma*sigma
    f[f < np.finfo(f.dtype).eps*f.max()] = 0

    # normalization
    f = f/f.sum() if f.sum() !=0 else f

    return f

def filterWithGaussian(im, sigma):
    """ Apply 2D Gaussian filter of the specified sigma to the input image
    
    Params:
    - im: (np.ndarray) input image grayscale or RGB
    - sigma: (int) sigma for 2D Gaussian filter
    
    Return:
    - smoothed_im: (np.ndarray) smoothed image
    """
    # Cast im to int16 to avoid overflow when apply filter
    im = im.astype(np.float64)
    channel = 3 if len(im.shape) == 3 else 1
    
    fil = matlab_style_gauss2D(31, sigma)
    if channel == 1:
        smoothed_im = ndimage.correlate(im, fil, mode='constant')
    else:
        smoothed_im = np.empty_like(im)
        smoothed_im[:,:,0] = ndimage.correlate(im[:,:,0], fil, mode='constant')
        smoothed_im[:,:,1] = ndimage.correlate(im[:,:,1], fil, mode='constant')
        smoothed_im[:,:,2] = ndimage.correlate(im[:,:,2], fil, mode='constant')

    return smoothed_im

def replaceNonWorkingArea(original_path, mask_path, processed_path, output_name, sigma):
    """ Replace the non-working area of the output image (from our model) with the non-working
    area of the original image using the provided mask. A 2D Gaussian filter is applied on
    the mask to smooth the sharp edges on the resulting image. The resulting final image will be save to
    output_name path.
    
    Params:
    - original_path: path to the original image
    - mask_path: path to the mask of the original image
    - processed_path: path to the output image (from our model)
    - output_name: desire path and name of the final image to be saved
    
    """
    original = cv.imread(original_path, cv.IMREAD_UNCHANGED)
    processed = cv.imread(processed_path, cv.IMREAD_UNCHANGED)
    mask = cv.imread(mask_path, cv.IMREAD_UNCHANGED)
    mask = (mask/255).astype(np.uint8)
    inv_mask = 1 - mask
    
    # apply Gaussian filter
    mask = filterWithGaussian(mask, sigma)
    inv_mask = filterWithGaussian(inv_mask, sigma)
    
    final = np.multiply(processed, mask) + np.multiply(original, inv_mask)
    final = np.clip(final, 0.0, 255.0)
    cv.imwrite(output_name, final.astype(np.uint8))
