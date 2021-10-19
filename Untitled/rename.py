#https://www.youtube.com/watch?v=SqvVm3QiQVk&t=40s

import os

def rename():
    i = 0
    print('Input file path : ')
    path = input('')
    #print(path)
    for filename in os.listdir(path):
        expected_output = 't' + str(i) + '.jpg'
        file_source = path + filename
        os.rename(file_source, expected_output)
        i += 1
    
if __name__ == '__main__':
    rename()