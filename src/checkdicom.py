import os
import nibabel as nib
import shutil

# dirpath = 'D:\\philips_dcm\\AD\\'
# dirnames = os.listdir(dirpath)
# for dirname in dirnames:
#     # print(dirname)
#     for filenames in os.listdir(os.path.join(dirpath,dirname)):
#         # print(filenames)
#         for filename in os.listdir(os.path.join(dirpath,dirname,filenames)):
#             print(filename)
#             for file in os.listdir(os.path.join(dirpath,dirname,filenames,filename)):
#                 print(file)
#                 raise SystemExit
88
filepath = 'D:\\philips_dcm\\LMCI\\136_S_4848\Resting_State_fMRI\\2012-10-15_08_49_32.0\\2.NIFTI'
filenames = os.listdir(filepath)


session_errors = []
aa = []

for filename in filenames:
    if filename.startswith('ADNI'):
    # if filename.startswith('aADNI'):
    #     if os.path.exists(os.path.join(filepath,filename.replace('aADNI','ADNI'))):
    #         continue
    #     else:
    #         os.remove(os.path.join(filepath,filename))
        img = nib.load(os.path.join(filepath,filename))
        session_error = img.header['session_error']
        # print(img)
        # raise SystemExit
        if session_error < 11:
            print(session_error)
            print(filename)
            os.remove(os.path.join(filepath,filename))
            # os.remove(os.path.join(filepath,'a'+filename))

        # session_errors.append(str(session_error))

    # print()  # 输出信息

# print(session_errors)