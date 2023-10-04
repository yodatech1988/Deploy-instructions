from setuptools import setup, find_packages

setup(
    name='awesome-ai-agents',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'tensorflow',
        'keras',
        'torch',
        'gym',
        'stable-baselines3',
        'ray[rllib]'
    ],
    entry_points={
        'console_scripts': [
            'awesome-ai-agents=awesome_ai_agents:main',
        ],
    },
    package_data={
        'awesome_ai_agents': ['*.txt', '*.md'],
    },
    include_package_data=True,
    author='e2b-dev',
    author_email='e2b@dev.com',
    description='A collection of awesome AI agents',
    keywords='AI agents reinforcement learning deep learning',
    url='https://github.com/e2b-dev/awesome-ai-agents'
)