# encoding=utf8
'''
查看和显示nii文件
'''

import matplotlib

matplotlib.use('TkAgg')

from matplotlib import pylab as plt
import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D

# name = 'ADNI_002_S_5018_MR_Resting_State_fMRI_br_raw_20130517101805634_4704_S189764_I372812.nii' 84
# name = 'ADNI_002_S_5018_MR_Resting_State_fMRI_br_raw_20130517101808694_2034_S189764_I372812.nii' 74
name = 'ADNI_002_S_5018_MR_Resting_State_fMRI_br_raw_20130517101810284_2966_S189764_I372812.nii'   #26
example_filename = 'D:\\philips_dcm\\AD\\002_S_5018\\Resting_State_fMRI\\2013-05-16_12_20_33.0\\S189764\\'+name
img = nib.load(example_filename)
print(img)
print(img.header['session_error'])  # 输出头信息

# width, height, queue = img.dataobj.shape
#
# OrthoSlicer3D(img.dataobj).show()
#
# num = 1
# for i in range(0, queue, 10):
#     img_arr = img.dataobj[:, :, i]
#     plt.subplot(5, 4, num)
#     plt.imshow(img_arr, cmap='gray')
#     num += 1
#
# plt.show()
