import os

os.system('''python S3_Gfilter_3cor_none.py H_Bulk_count_average.txt H_FR_count_average.txt H_WR_count_average.txt none''')
os.system('''python S3_Gfilter_3cor_none.py M_Bulk_count_average.txt M_FR_count_average.txt M_WR_count_average.txt none''')
os.system('''python S3_Gfilter_3cor_none.py S_Bulk_count_average.txt S_FR_count_average.txt S_WR_count_average.txt none''')

os.system('''Rscript S4_pic_3cor_none.R H_3filternone.txt count''')
os.system('''Rscript S4_pic_3cor_none.R M_3filternone.txt count''')
os.system('''Rscript S4_pic_3cor_none.R S_3filternone.txt count''')

