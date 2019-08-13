import shutil
import os
# srcPath = 'G:\\DataProcess_fMRI\\ADNI_only_fMRI_218'
#
# desPath = 'G:\\DataProcess_fMRI\\ADNI_only_fMRI_218\\0.5'
#
# txtfile = os.path.abspath('../data/list.txt')
# files = []
# with open(txtfile,'r') as f:
#     for line in f:
#         filedir = line.strip().split('-')[0].replace('rp_af','')
#         try:
#             shutil.move(os.path.join(srcPath,filedir),desPath)
#         except:
#             continue

# 移动文件，区分每步骤


# filename = 'D:\philips_dcm\AD.txt'
# dirpath = 'D:\philips_dcm\ROI_datas\AD'
#
# with open(filename,'r') as f:
#     for line in f:
#         names = line.strip().split('\\')
#         print(names)
#         if os.path.exists(os.path.join(dirpath,names[0])) == False:
#             os.mkdir(os.path.join(dirpath,names[0]))
#         if os.path.exists(os.path.join(dirpath,names[0],names[2])) == False:
#             os.mkdir(os.path.join(dirpath,names[0],names[2]))
#         if os.path.exists(os.path.join(dirpath,names[0],names[2],'8.ROI')) == False:
#             os.mkdir(os.path.join(dirpath,names[0],names[2],'8.ROI'))

dirpath = 'D:\\philips_dcm\\LMCI\\ADNI_philips_LMCI\\'
dirnames = os.listdir(dirpath)


# print(dirnames)
for dirname in dirnames:
    for dir in os.listdir(os.path.join(dirpath,dirname)):
        datefiles = os.listdir(os.path.join(dirpath,dirname,dir))
        for date in datefiles:
            if os.path.exists(os.path.join(dirpath, dirname, dir, date,'2.NIFTI')) == False:
                os.mkdir(os.path.join(dirpath, dirname, dir, date,'2.NIFTI'))
                # raise SystemExit




# for dirpath, dirnames, filenames in os.walk(dirPath):
#     print(dirpath)
#     print(dirnames)
#     if count == 3:
#         raise SystemExit
#     count += 1
#

# for dirname in dirnames:
#     if os.path.isfile(os.path.join(dirpath, dirname)):
#         continue
#     if os.path.exists(os.path.join(dirpath, dirname, '1.Dicom')) == False:
#         os.mkdir(os.path.join(dirpath, dirname, '1.Dicom'))
#     if os.path.exists(os.path.join(dirpath, dirname, '2.NIFTI')) == False:
#         os.mkdir(os.path.join(dirpath, dirname, '2.NIFTI'))
#     if os.path.exists(os.path.join(dirpath, dirname, '3.SliceTiming')) == False:
#             os.mkdir(os.path.join(dirpath, dirname, '3.SliceTiming'))
#     if os.path.exists(os.path.join(dirpath, dirname, '4.Realignment')) == False:
#         os.mkdir(os.path.join(dirpath, dirname, '4.Realignment'))
#     if os.path.exists(os.path.join(dirpath, dirname, '5.Normalize')) == False:
#         os.mkdir(os.path.join(dirpath, dirname, '5.Normalize'))
#     if os.path.exists(os.path.join(dirpath, dirname, '6.Smooth')) == False:
#         os.mkdir(os.path.join(dirpath, dirname, '6.Smooth'))
#     if os.path.exists(os.path.join(dirpath, dirname, '7.Coregister')) == False:
#         os.mkdir(os.path.join(dirpath, dirname, '7.Coregister'))
#     # if os.path.exists(os.path.join(dirpath, dirname, 'ROI')) == True:
#     #     os.rename(os.path.join(dirpath,dirname,'ROI'),os.path.join(dirpath,dirname,'8.ROI'))  # 文件或目录都是使用这条命令
#     if os.path.exists(os.path.join(dirpath, dirname, '8.ROI')) == False:
#         os.mkdir(os.path.join(dirpath, dirname, '8.ROI'))



# for dirname in dirnames:
#     for filenames in os.listdir(os.path.join(dirpath,dirname,'Resting_State_fMRI')):
# #         if filenames.startswith('S'):
# #             # print(filenames,os.path.join(dirpath,dirname,filenames))
#             for filename in os.listdir(os.path.join(dirpath,dirname,'Resting_State_fMRI',filenames)):
#                 if filename.startswith('S'):
#                     for file in os.listdir(os.path.join(dirpath, dirname, 'Resting_State_fMRI', filenames,filename)):
# #                 if filename.startswith('rswraf'):
#                     # print(filename)
#                     shutil.move(os.path.join(dirpath,dirname,filenames,filename),os.path.join(dirpath, dirname,'7.Coregister',filename))
#                 if filename.startswith('swraf'):
#                     # print(filename)
#                     shutil.move(os.path.join(dirpath,dirname,filenames,filename),os.path.join(dirpath, dirname,'6.Smooth',filename))
#                 if filename.startswith('wraf'):
#                     # print(filename)
#                     shutil.move(os.path.join(dirpath,dirname,filenames,filename),os.path.join(dirpath, dirname,'5.Normalize',filename))
#                 if filename.startswith('raf') or filename.startswith('y_meanaf'):
#                     # print(filename)
#                     shutil.move(os.path.join(dirpath,dirname,filenames,filename),os.path.join(dirpath,dirname, '4.Realignment',filename))
#                         if filename.startswith('as'):
#                             # print(filename)
#                             shutil.move(os.path.join(dirpath, dirname, 'Resting_State_fMRI', filenames, filename,file),
#                                         os.path.join(dirpath, dirname, 'Resting_State_fMRI', filenames, filename,'3.SliceTiming', filename))

                    # shutil.move(os.path.join(dirpath,dirname,filenames,filename),os.path.join(dirpath, dirname,'3.SliceTiming',filename))
#                 if filename.startswith('meanaf') or filename.startswith('rp_af'):
#                     # print(filename)
#                     shutil.move(os.path.join(dirpath,dirname,filenames,filename),os.path.join(dirpath, dirname,'3.SliceTiming',filename))
#                         if file.startswith('as'):
#                             # print(dirpath,dirname,'Resting_State_fMRI', filenames,file)
#
#                             shutil.move(os.path.join(dirpath,dirname,'Resting_State_fMRI', filenames,filename,file),os.path.join(dirpath, dirname,'Resting_State_fMRI', filenames,'2.NIFTI',file))
#                             # raise SystemExit
#                 if filename.startswith('ADNI'):
#                     # print(filename)
#                     shutil.move(os.path.join(dirpath,dirname,filenames,filename),os.path.join(dirpath,dirname,'1.Dicom',filename))
#                 count += 1
#                 print(filename)
#                 # if count ==10:
#                 #     break



