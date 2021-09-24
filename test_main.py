import os

def data_file_present():
    return os.path.exists('./data.zip')

def is_model_present():
    return os.path.exists('./model.h5')
