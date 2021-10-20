import os
#https://www.youtube.com/watch?v=SqvVm3QiQVk&t=40s
def renamer():
    print('Please input your file source path (Ex. C:\Directory\) : ')
    src_path = input('>')
    print(src_path)
    
    isdir = os.path.isdir(src_path)
    
    if isdir is True:
        print('Please input your new file name : ')
        new_name = input('>')
        
        print('Please input your new file format (.jpg): ')
        file_format = input('>')
        
        i = 1
        for filename in os.listdir(src_path):
            src_file = src_path + filename
            dst = new_name + ' ' + str(i) + file_format
            dst = src_path + dst
            os.rename(src_file, dst)
            i += 1
        
    else:
        print('Sorry, your directory does not exist.')
        print('Do you want to try again ? (type "y" to try again)')
        try_again = input('>')
        if try_again == 'y':
            renamer()
        else:
            exit()
        
if __name__ == '__main__':
    renamer()
