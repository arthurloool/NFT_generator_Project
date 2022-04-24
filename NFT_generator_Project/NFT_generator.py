# Combine multiple layer of image and generate a sets of NFT

import glob
from PIL import Image
import os
import sys

# Image layer (from background to top)
home_folder = os.getcwd()
save_folder = home_folder + r'\\NFT_save_folder\\'
layer_max = 10

# Check for non empty layer folder
non_empty_layer_list = []
for i in range(0,layer_max):
    layer_no = str(i)
    if glob.glob(home_folder + '\image_layer_' + layer_no + '\*.png') != []:
        non_empty_layer_list.append(home_folder + '\image_layer_' + layer_no)
    elif non_empty_layer_list == []:
        print('All folders are empty. Please check your layer folders.')
        sys.exit()

# print('The image in the following folder is going to use for NFT generation' + '\n' + str(non_empty_layer_list))

# Test for image merge and save to save folder

'''layer_0 = glob.glob(home_folder + '\image_layer_0' + '\*.png')
print('Opening'+layer_0[0])
im_0 = Image.open(layer_0[0])

layer_1 = glob.glob(home_folder + '\image_layer_1' + '\*.png')
print('Opening'+layer_1[0])
im_1 = Image.open(layer_1[0])

im_merge = Image.new('RGBA',im_0.size)
im_merge.paste(im_0,(0,0),im_0)
im_merge.paste(im_1,(0,0),im_1)
im_merge.save(save_folder + '001.png')'''

# Dictionary
# Key: Non empty layer folder path
# Value: list of image path within the folder

nft_dict = {}
for layer in non_empty_layer_list:
    image_list = glob.glob(layer + '\*.png')
    nft_dict.setdefault(str(layer), image_list)


