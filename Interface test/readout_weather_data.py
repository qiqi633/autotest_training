
import yaml,os
import pytest
import codecs
import io

@pytest.fixture()
def ret_weather_data(file_name):
    # file_path = os.getcwd() + os.sep + 'interface test' + os.sep + file_name + '.yml'
    file_path = os.getcwd() + os.sep + file_name + '.yml'
    print("read data from : %s"%file_path)
    with io.open(file_path, 'r' ,encoding='GBK') as f:
        return yaml.load(f)