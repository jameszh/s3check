from setuptools import setup

with open('README.md') as file:
    readme = file.read()

setup(
    name='s3check',
    version='0.0.1',
    url='www.github.com/jameszh/s3check',
    license='license',
    author='James Zhang',
    packages=["s3check"],
    long_description=readme,
    description='Check access permissions (LIST/WRITE/READ/DELETE) within a specified S3 bucket',
    install_requires=['click', 'boto3'],
    entry_points={
        'console_scripts': ['s3check=s3check.s3check:main']
    },
    include_package_data=True,
    zip_safe=False
)
