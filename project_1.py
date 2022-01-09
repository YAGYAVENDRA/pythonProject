# project aim : filter mix file and make seperate folders for all type of file and move all repective file in repective folders


import os, shutil

all_extensions = {
    'Image_extension' : ('.jpeg','.jpg','.png','.jpge','.al','.gif','.row'),
    'Video_extension' : ('.mp4','.mkv','.wmv','.avi'),
    'Document_extension' : ('.doc','.pdf','.PDF','.txt','.xls','docx','.html','.py','.java','.ppsx','.pptx'),
    'Audio_extension' : ('.mp3','.m4a','.wav','.flac')
}

user_path = input('Enter your path : ')

def file_finder(folder_path,file_excetension):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_excetension:
            if file.endswith(extension):
                files.append(file)

    return files

for file_type, file_ex_tuple in all_extensions.items():
    folder_name = file_type.split('_')[0] + 'file'
    folder_path = os.path.join(user_path,folder_name)
    try:
        os.mkdir(folder_path)
    except FileExistsError:
        print(f'{folder_name} folder is already exist')
    for iteam in (file_finder(user_path,file_ex_tuple)):
        iteam_path = os.path.join(user_path,iteam)
        iteam_new_path = os.path.join(folder_path,iteam)
        shutil.move(iteam_path,iteam_new_path)

