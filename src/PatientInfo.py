import csv
import numpy as np
from scipy import io
import argparse

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("--info", type=str, default='NC')
args = parser.parse_args()

'''
总结病人信息
i.	Male/Female 数量
ii.	Age (Mean ± SD)
iii.	MMSE (Mean ± SD)

'''
if args.info == 'NC':
    fileName = '../data/ADNI_PHILIPS_CN_6_11_2019.csv'
    ROI_data = '../data/ROISignals_NC.mat'
elif args.info == 'EMCI':
    fileName = '../data/ADNI_philips_eMCI_6_11_2019.csv'
    ROI_data = '../data/ROISignals_EMCI.mat'
elif args.info == 'LMCI':
    fileName = '../data/ADNI_philips_LMCI_6_11_2019.csv'
    ROI_data = '../data/ROISignals_LMCI.mat'
elif args.info == 'AD':
    fileName = '../data/ADNI_philips_AD_6_10_2019.csv'
    ROI_data = '../data/ROISignals_AD.mat'
else:
    assert "not incorrect info, selected in NC/EMCI/LMCI/AD"

Partdatas = io.loadmat(ROI_data)
PartSubjects = Partdatas['persons']
PartDates = Partdatas['dates']

# 修改日期格式
for i in range(len(PartDates)):
    PartDates[i] = PartDates[i].split('_')[0].replace('-', '/')
    if PartDates[i][5] == '0':
        PartDates[i] = PartDates[i][6:] + '/' + PartDates[i][:4]
    else:
        PartDates[i] = PartDates[i][5:] + '/' + PartDates[i][:4]


sample_nums = len(PartSubjects)

count = 0
AllSubjects = []
Sexes = []
Ages = []
Female = 0
Male = 0

for num in range(len(PartDates)):
    with open(fileName, newline='') as csvfile:
        Inforeader = csv.reader(csvfile)
        for row in Inforeader:
            subject = row[1]
            date = row[9]

            if PartSubjects[num] == subject and PartDates[num] == date:
                # print(subject, date)
                count += 1

                if row[3] == 'F':
                    Female += 1
                else:
                    Male += 1
                Age = int(row[4])
                Ages.append(Age)
                break

# print(sample_nums)
# print(len(Ages))
# print(Ages)

print('Patients Info about mean +- std of Female/Male and Age : ', Male, '/', Female, np.mean(Ages), '+-', np.std(Ages))
