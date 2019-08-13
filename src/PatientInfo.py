import csv
import numpy as np
from scipy import io,stats


'''
总结病人信息
i.	Male/Female 数量
ii.	Age (Mean ± SD)
iii.	MMSE (Mean ± SD)

'''

# fileName = '../data/ADNI_PHILIPS_CN_6_11_2019.csv'
# ROI_data = '../data/ROISignals_NC.mat'

# fileName = '../data/ADNI_philips_eMCI_6_11_2019.csv'
# ROI_data = '../data/ROISignals_EMCI.mat'

fileName = '../data/ADNI_philips_LMCI_6_11_2019.csv'
ROI_data = '../data/ROISignals_LMCI.mat'


# fileName = '../data/ADNI_philips_AD_6_10_2019.csv'
# ROI_data = '../data/ROISignals_AD.mat'

# csv_data = pd.read_csv(fileName)  # 读取csv数据


Partdatas = io.loadmat(ROI_data)
PartSubjects = Partdatas['persons']
PartDates = Partdatas['dates']

# 修改日期格式
for i in range(len(PartDates)):
    PartDates[i] = PartDates[i].split('_')[0].replace('-','/')
    if PartDates[i][5] == '0':
        PartDates[i] = PartDates[i][6:]+'/'+PartDates[i][:4]
    else:
        PartDates[i] = PartDates[i][5:] + '/' + PartDates[i][:4]
# print(PartSubjects)
# print(PartDates)

sample_nums = len(PartSubjects)


count = 0
AllSubjects = []
Sexes = []
Ages = []
Female = 0
Male = 0
# for num in range(len(PartDates)):
#     print(PartSubjects[num],PartDates[num])
#
# print('pppppppppp')

# # 检查部分
# with open(fileName, newline='') as csvfile:
#     Inforeader = csv.reader(csvfile)
#     for row in Inforeader:
#         subject = row[0]
#         date = row[5]
#
#         AllSubjects.append(subject)
#
# for num in range(len(PartDates)):
#     if PartSubjects[num] not in AllSubjects:
#         print(PartSubjects[num],PartDates[num])
# raise SystemExit
# Subject ID	Phase	Sex	Research Group	Archive Date	Study Date	Age	MMSE Total Score	Modality	Description	Imaging Protocol	Image ID
for num in range(len(PartDates)):
    with open(fileName, newline='') as csvfile:
        Inforeader = csv.reader(csvfile)
        for row in Inforeader:
            # print(row)
            subject = row[1]
            date = row[9]

            # print(subject,date)
            if PartSubjects[num] == subject and PartDates[num] == date:
                print(subject,date)
                count += 1
                # print('count-',count)

                if row[3] == 'F':
                    Female += 1
                else:
                    Male += 1
                Age = int(row[4])
                Ages.append(Age)
                break

print (sample_nums)
print(len(Ages))
print(Ages)

print('Patients Info about mean +- std of Female/Male and Age : ',Male,'/',Female,np.mean(Ages),'+-',np.std(Ages))




# NC age:
# [91, 82, 82, 83, 95, 96, 77, 77, 78, 78, 79, 80, 72, 73, 73, 73, 74, 75, 77, 74, 75, 75, 75, 76, 74, 74, 74, 76, 67, 67, 68, 73, 74, 71, 74, 75, 76, 74, 70, 79, 77, 78, 78, 79, 72, 72, 73, 74, 78, 78, 79, 79, 80, 71, 72, 72, 73, 79, 80, 80, 80, 69, 70, 71, 86, 76, 70, 66, 79, 69, 69, 80, 72, 80, 80, 81, 82, 84, 84, 84, 86, 66, 73]

# EMCI age:
