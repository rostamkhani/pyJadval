from setuptools import setup, find_packages
import os

rootpath = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    return open(os.path.join(rootpath, *parts)).read()

setup(
    name='pyJadval',
    version='0.1',
    description='Displaying DataFrame data in tables with versatile and powerful features for quick and easy data exploration in notebooks, such as sorting, column rearrangement, searching, grouping, and other functionalities. A good alternative to the print function for DataFrame .',
    author='Aref Rostamkhani',
    author_email='aref.rostamkhani@gmail.com',
    keywords="data visualization",
    url="https://github.com/rostamkhani/pyJadval",
    long_description="{}".format(read("README.rst")),
    long_description_content_type="text/x-rst",
    platforms="any",
    packages=find_packages(),
    package_dir={'proj': 'src'}

)