from setuptools import setup, find_packages

setup(
    name='e2b-cookbook',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Significant-Gravitas-AutoGPT @ git+https://github.com/Significant-Gravitas/AutoGPT.git',
        'Significant-Gravitas-Auto-GPT-Plugins @ git+https://github.com/Significant-Gravitas/Auto-GPT-Plugins.git',
        'gorilla-llm-gorilla-cli @ git+https://github.com/gorilla-llm/gorilla-cli.git',
        'e2b-dev-e2b @ git+https://github.com/e2b-dev/e2b.git',
        'e2b-dev-awesome-ai-agents @ git+https://github.com/e2b-dev/awesome-ai-agents.git',
        'e2b-dev-llm-code-interpreter @ git+https://github.com/e2b-dev/llm-code-interpreter.git',
        'e2b-dev-awesome-sdks-for-ai-agents @ git+https://github.com/e2b-dev/awesome-sdks-for-ai-agents.git',
    ],
    entry_points={
        'console_scripts': [
            'e2b-cookbook=e2b-cookbook.cookbook:main',
        ],
    },
)