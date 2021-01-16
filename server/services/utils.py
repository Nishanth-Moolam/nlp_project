import os
import config


def make_folder(folder_name):
    os.mkdir(config.server_path+'/static/uploads/'+folder_name)


def save_file(file, folder_name, file_name):
    file.save(os.path.join(config.server_path +
                                '/static/uploads/'+folder_name, file_name))
