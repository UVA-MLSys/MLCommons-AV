import os

dir_path = '../kitti/testing/'
pc_path_list = os.listdir(dir_path+'velodyne_reduced')
calib_path_list = os.listdir(dir_path+'calib')
img_path_list = os.listdir(dir_path+'image_2')

print('done')
