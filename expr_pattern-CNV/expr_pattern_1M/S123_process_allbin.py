import os

H = ['test_H_Bulk', 'test_H_FR2', 'test_H_WR']
M = ['test_M_ERR_Bulk', 'test_M_ERR_FR', 'test_M_ERR_WR']
S = ['test_S_ERR_Bulk', 'test_S_ERR_FR', 'test_S_ERR_WR']
P1 = ['patient_4M_ERR']
P2 = ['patient_4M_SRR']
D1 = ['SIDR_4M']
D2 = ['SIDR_all']
ll = H+M+S
#ll = P
#ll = D2

for i in ll:
    os.system('''python segcopy.py %s/infercnv.observations.txt''' % (i))
    os.system('''python bounds_allbin.py %s''' % (i))
    os.system('''Rscript pic.R %s/segcopy2 %s/bounds_allbin''' % (i, i))

