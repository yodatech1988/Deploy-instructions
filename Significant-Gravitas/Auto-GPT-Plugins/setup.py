from setuptools import setup, find_packages

setup(
    name='Auto-GPT-Plugins',
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
            'plugin1=AutoGPT_Plugins.plugin1:main',
            'plugin2=AutoGPT_Plugins.plugin2:main',
        ],
    },
    package_data={
        '': ['*.txt', '*.md'],
    },
    author='Significant Gravitas',
    author_email='info@significantgravitas.com',
    description='Plugins for AutoGPT',
    keywords='AutoGPT Plugins',
    url='https://github.com/Significant-Gravitas/Auto-GPT-Plugins'
)