import os
import scipy.io
import numpy as np
# 讀取所有fMRI文件
# fMRI文件路徑

def get_MultiScan(fmri_filepath,label_class):

    count = 0
    persons= []
    ROIdatas = []
    dates = []
    baks = []
    labels = []
    for dirpaths, dirnames, filenames in os.walk(fmri_filepath):
        datas = np.zeros((130, 116), dtype=np.float)
        dirpath = dirpaths.split('\\')
        if len(dirpath) == 6 and dirpath[2] != '.git':

            label = dirpath[2]
            person = dirpath[3]
            date = dirpath[4]
            bak = dirpath[5]
            if label == label_class:
                # if person in persons:
                #     continue
                count += 1
                persons.append(person)
                print(dirpath)
            else:
                continue

            i = 0
            for filename in filenames:
                if filename.startswith('ROISignals_ROISignal_') and filename.endswith('.mat'):
                    data = scipy.io.loadmat(os.path.join(dirpaths, filename))
                    ROISignals = data['ROISignals']
                    datas[i] = ROISignals
                    i += 1
            if np.all(datas[0] == 0):
                print('pppppppppp')
                continue

            ROIdatas.append(datas)
            baks.append(bak)
            labels.append(label)
            dates.append(date)

    print(count)
    scipy.io.savemat(os.path.join('../data/', 'ROISignals_'+label_class+'.mat'), {'persons':persons,'labels':labels,\
                                                                                                'datas':ROIdatas,'dates':dates,'baks':baks})

def combine_mat():

    # label1 = 'NC'
    # label2 = 'EMCI'
    # label1 = 'EMCI'
    # label2 = 'LMCI'
    #
    # fmri_file1 = '../data/ROISignals_' + label1 +'.mat'
    # fmri_file2 = '../data/ROISignals_' + label2 + '.mat'
    #
    #
    # data1 = scipy.io.loadmat(fmri_file1)
    # data2 = scipy.io.loadmat(fmri_file2)
    #
    # persons = np.hstack((data1['persons'],data2['persons']))          # 垂直组合
    # dates = np.hstack((data1['dates'],data2['dates']))
    # baks = np.hstack((data1['baks'],data2['baks']))
    # labels = np.hstack((data1['labels'], data2['labels']))
    # datas = np.vstack((data1['datas'], data2['datas']))
    #
    # scipy.io.savemat(os.path.join('../data/','ROISignals_' + label1 + '_' + label2 +'.mat'),\
    #                  mdict={'persons':persons,'dates':dates,'baks':baks,'labels':labels,'datas':datas})



    label1 = 'NC'
    label2 = 'EMCI'
    label3 = 'LMCI'

    fmri_file1 = '../data/ROISignals_NC.mat'
    fmri_file2 = '../data/ROISignals_EMCI.mat'
    fmri_file3 = '../data/ROISignals_LMCI.mat'

    data1 = scipy.io.loadmat(fmri_file1)
    data2 = scipy.io.loadmat(fmri_file2)
    data3 = scipy.io.loadmat(fmri_file3)

    persons = np.hstack((data1['persons'],data2['persons'],data3['persons']))          # 垂直组合
    dates = np.hstack((data1['dates'],data2['dates'],data3['dates']))
    baks = np.hstack((data1['baks'],data2['baks'],data3['baks']))
    labels = np.hstack((data1['labels'], data2['labels'], data3['labels']))
    datas = np.vstack((data1['datas'], data2['datas'], data3['datas']))

    print (len(data3['persons']),len(persons))

    scipy.io.savemat(os.path.join('../data/','ROISignals_' + label1 + '_' + label2 + '_' + label3 +'.mat'),\
                     mdict={'persons':persons,'dates':dates,'baks':baks,'labels':labels,'datas':datas})


if __name__=='__main__':
    fmri_filepath = 'F:\ROI_datas'

    # label_classes = ['NC','EMCI','LMCI','AD']
    # label_classes = ['LMCI']
    # for label_class in label_classes:
    #     get_MultiScan(fmri_filepath, label_class)
    combine_mat()
