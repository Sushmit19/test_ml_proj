from setuptools import find_packages,setup
from typing import List

hyphen_e_dot = '-e .'
def get_package(file_path:str)->List[str]:
    '''
    Fetch all package names from requirements.txt
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]
    if hyphen_e_dot in requirements:
        requirements.remove(hyphen_e_dot)

setup(
    name='test_ml_proj',
    version='0.0.1',
    author='Susmit',
    author_email='sushmitgawade@gmail.com',
    packages=find_packages(),
    install_requires=['pandas','numpy']
)