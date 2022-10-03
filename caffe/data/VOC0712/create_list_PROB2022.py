import glob, os,  csv
from pathlib import Path

dataset_type = {'trainval': 'SEP_2022_Train', 'test': 'SEP_2022_Test'}
ROOT_DIR = os.path.abspath(os.curdir)
dataset_dir = os.path.join(Path.home(), 'data/VOCdevkit')

img_list_train = glob.glob('{}/{}/JPEGImages/*.jpg'.format(dataset_dir, dataset_type['trainval']))
img_list_test = glob.glob('{}/{}/JPEGImages/*.jpg'.format(dataset_dir, dataset_type['test']))
print('New Train: ',  len(img_list_train), 'New Test:', len(img_list_test))

# [os.system('rm -rf data/VOC0712/{}'.format(i)) for i in ['trainval.txt', 'test.txt' 'test_name_size.txt']]
# Preparing old VOC Data
# os.system('bash data/VOC0712/create_list.sh')


def write_to_csv(filename, data):  # writes the given data to the csv filename provided
    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
    csvfile.close()


for i in img_list_train:
    name = os.path.basename(i).replace('.jpg', '')
    write_to_csv(os.path.join(ROOT_DIR, 'data/VOC0712/trainval.txt'),
                 ['{}/JPEGImages/{}.jpg {}/Annotations/{}.xml'.format(dataset_type['trainval'], name,
                                                                      dataset_type['trainval'], name)])
for i in img_list_test:
    name = os.path.basename(i).replace('.jpg', '')
    write_to_csv(os.path.join(ROOT_DIR, 'data/VOC0712/test.txt'),
                 ['{}/JPEGImages/{}.jpg {}/Annotations/{}.xml'.format(dataset_type['test'], name,
                                                                      dataset_type['test'], name)])

os.system('bash data/VOC0712/create_list_VOC2022.sh')
os.system('bash data/VOC0712/create_data.sh')
