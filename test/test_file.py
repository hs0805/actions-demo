import test_main

def test_data_file_present():
    assert test_main.data_file_present() == False

def test_is_model_present():
    assert test_main.is_model_present() == False
