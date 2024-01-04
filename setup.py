from setuptools import find_packages,setup

setup(
    name='BikePricePrediction',
    version='0.0.1',
    author='suraj panigrahi',
    author_email='surajpanigrahi296@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)