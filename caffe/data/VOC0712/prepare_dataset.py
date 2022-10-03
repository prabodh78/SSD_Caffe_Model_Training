import os
import glob
import cv2

output_dataset_path = '/home/prabodh/data/VOCdevkit'
train_path = os.path.join(output_dataset_path, 'SEP_2022_Train')
test_path = os.path.join(output_dataset_path, 'SEP_2022_Test')

train_xml_path = os.path.join(train_path, 'Annotations')
test_xml_path = os.path.join(test_path, 'Annotations')

train_jpg_path = os.path.join(train_path, 'JPEGImages')
test_jpg_path = os.path.join(test_path, 'JPEGImages')

[os.system('mkdir -p {}'.format(i)) for i in [train_jpg_path, train_xml_path, test_jpg_path, test_xml_path]]

dir_path = '/home/prabodh/workspace/Person_Detector/Person_Dataset_2022'
xml_files = glob.glob(os.path.join(dir_path, 'xml/*'))
print(len(xml_files))

steps = int(len(xml_files) / (len(xml_files) * 0.2))
print(steps)

# # Copy all data
# for xml_f in xml_files:
#     if os.path.exists(xml_f.replace('xml', 'jpg')):
#         # print(xml_f)
#         # print(xml_f.replace('xml', 'jpg'))
#         os.system('cp {} {}/'.format(xml_f, train_xml_path))
#         os.system('cp {} {}/'.format(xml_f.replace('xml', 'jpg'), train_jpg_path))

for xml_f in glob.glob(os.path.join(train_xml_path, '*'))[::steps]:
    if os.path.exists(xml_f.replace('xml', 'jpg').replace('Annotations', 'JPEGImages')):
        # print(xml_f)
        # print(xml_f.replace('xml', 'jpg'))
        os.system('mv {} {}/'.format(xml_f, test_xml_path))
        os.system('mv {} {}/'.format(xml_f.replace('xml', 'jpg').replace('Annotations', 'JPEGImages'), test_jpg_path))
