import os
def rename_files(file_dir,extension) :
    #get files from the folder
    file_list=os.listdir(file_dir)
    os.chdir(file_dir)
    for file in file_list:
        name,ext=file.split('.')
        os.rename(file,name+"."+extension)
        


    
