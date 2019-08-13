import shutil
import os

# dirpath = 'D:\\philips_dcm\\EMCI\\'
# outfile = open('../data/filename_EMCI.txt','w')
# dirpath = 'D:\\philips_dcm\\NC\\'
# outfile = open('../data/filename_NC.txt','w')
dirpath = 'F:\\philips_dcm\\LMCI\\'
outfile = open('../data/filename_LMCI.txt','w')
# dirpath = 'D:\\philips_dcm\\AD\\'
# outfile = open('../data/filename_AD.txt','w')
count = 0

dirnames = os.listdir(dirpath)




for dirname in dirnames:
    # print(dirname)
    for filenames in os.listdir(os.path.join(dirpath,dirname)):
        # print(filenames)
        for filename in os.listdir(os.path.join(dirpath,dirname,filenames)):
            print(filename)
            for file in os.listdir(os.path.join(dirpath,dirname,filenames,filename)):
                print(file)
                if file == '2.NIFTI':
                    continue
                outfile.write(dirname+' '+filename+'    '+file+'   '+filenames+'\n')