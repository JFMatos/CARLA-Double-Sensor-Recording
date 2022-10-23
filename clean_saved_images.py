import os
from glob import glob
import numpy as np



def check_differences(dir1, dir2):
    pathnames = glob(dir1+'*')
    file_names_dir1 = [os.path.basename(path) for path in pathnames]

    pathnames = glob(dir2+'*')
    file_names_dir2 = [os.path.basename(path) for path in pathnames]

    diff_dir1 = np.setdiff1d(file_names_dir1, file_names_dir2)
    diff_dir2 = np.setdiff1d(file_names_dir2, file_names_dir1)

    for filename_dir1 in diff_dir1:
        os.remove(os.path.join(dir1, filename_dir1))
    
    for filename_dir2 in diff_dir2:
        os.remove(os.path.join(dir2, filename_dir2))




check_differences('SS_CityScapes_out/', 'RGB_out/')