import os

for filename in os.listdir():
    if filename.endswith('PNG'):
        new_name = filename.split('.')[0] + '.png'
        os.rename(filename, new_name)