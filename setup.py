from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='meteojo',
    version='0.0.1',
    url='https://github.com/j0hanj0han/meteojo.git',
    author='j0hanj0han',
    author_email='author@gmail.com',
    description='get open weather data easily',
    packages=find_packages(),    
    install_requires=requirements,
)