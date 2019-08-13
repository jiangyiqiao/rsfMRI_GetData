import shutil
import os

dirpath = 'D:\\philips_dcm\\AD\\ADNI'

ROI_dirpath = 'G:\ROI_datas\\AD\\1'
dirnames = os.listdir(dirpath)

for dirname in dirnames:
    print(dirname)
    for filenames in os.listdir(os.path.join(dirpath,dirname)):
        print(filenames)
        for filename in os.listdir(os.path.join(dirpath,dirname,filenames)):
            print(filename)
            if os.path.exists(os.path.join(ROI_dirpath, dirname)) == False:
                os.mkdir(os.path.join(ROI_dirpath, dirname))
            if os.path.exists(os.path.join(ROI_dirpath, dirname, filename)) == False:
                os.mkdir(os.path.join(ROI_dirpath, dirname, filename))
            if os.path.exists(os.path.join(ROI_dirpath, dirname, filename,'8.ROI')) == False:
                os.mkdir(os.path.join(ROI_dirpath, dirname, filename,'8.ROI'))
            # raise SystemExit