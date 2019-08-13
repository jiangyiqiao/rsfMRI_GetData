import os
# lsits = os.listdir('G:\\philips_dcm\\AD\\131_S_5138\\Resting_State_fMRI\\2013-04-02_15_35_32.0\\S187198')
# lists = [i.split('_')[11] for i in lsits ]
# lists = list(map(int,lists))
# lists = sorted(lists,reverse = False)
# print(lists)

aa = os.listdir('G:\\philips_dcm\\AD\\131_S_5138\\Resting_State_fMRI\\2013-04-02_15_35_32.0\\2.NIFTI')
a = [i.split('_')[11] for i in aa ]

print(sorted(list(map(int,a)),reverse = False))
print(len(sorted(list(map(int,a)),reverse = False)))

aa = os.listdir('G:\\philips_dcm\\AD\\131_S_5138\\Resting_State_fMRI\\2013-07-02_12_00_53.0\\2.NIFTI')
a = [i.split('_')[11] for i in aa ]

print(sorted(list(map(int,a)),reverse = False))
print(len(sorted(list(map(int,a)),reverse = False)))


aa = os.listdir('D:\\philips_dcm\\AD\\002_S_5018\\Resting_State_fMRI\\2013-05-16_12_20_33.0\\S189764')
a = [i.split('_')[11] for i in aa ]

print(sorted(list(set(map(int,a))),reverse = False))
print(len(sorted(list(set(map(int,a))),reverse = False)))