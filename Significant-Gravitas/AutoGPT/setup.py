from setuptools import setup, find_packages

setup(
    name='AutoGPT',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'torch',
        'transformers',
        'boto3',
        'botocore'
    ],
    entry_points={
        'console_scripts': [
            'autogpt=AutoGPT:main',
        ],
    },
    package_data={
        '': ['*.txt', '*.py'],
    },
    author="Significant Gravitas",
    author_email="info@significantgravitas.com",
    description="AutoGPT is an AGI Agent able to perform tasks on AWS EC2 Linux YUM",
    keywords="AutoGPT AGI Agent AWS EC2 Linux YUM",
    url="https://github.com/Significant-Gravitas/AutoGPT"
)