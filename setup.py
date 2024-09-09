from setuptools import setup, find_packages
setup(
name='pymium',
version='0.3.5',
author='Z3N',
author_email='iliya.souri7890@example.com',
description='Windows application creator',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.11',
install_requires=["pywebview"]
)
