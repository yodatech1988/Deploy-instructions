from setuptools import setup, find_packages

setup(
    name='awesome-sdks-for-ai-agents',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'requests',
        'boto3',
    ],
    entry_points={
        'console_scripts': [
            'awesome_sdks=awesome_sdks_for_ai_agents.awesome_sdks:main',
        ],
    },
    package_data={
        'awesome_sdks_for_ai_agents': ['*.txt', '*.md'],
    },
    include_package_data=True,
    author='e2b-dev',
    author_email='e2b@dev.com',
    description='A collection of awesome SDKs for AI agents',
    keywords='AI SDKs',
    url='https://github.com/e2b-dev/awesome-sdks-for-ai-agents'
)