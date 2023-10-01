from setuptools import setup, find_packages

setup(
    name='e2b',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'botocore',
        'awscli',
        'paramiko',
        'scp',
        'numpy',
        'pandas',
        'requests',
        'beautifulsoup4',
        'lxml',
        'AutoGPT',
        'gorilla-cli',
        'awesome-ai-agents',
        'llm-code-interpreter',
        'awesome-sdks-for-ai-agents',
        'e2b-cookbook'
    ],
    entry_points={
        'console_scripts': [
            'e2b=e2b.e2b:main',
        ],
    },
)