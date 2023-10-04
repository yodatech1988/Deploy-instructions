```python
import os
import subprocess

def install_repo(repo_url):
    repo_name = repo_url.split("/")[-1]
    clone_command = f"git clone {repo_url}"
    os.system(clone_command)
    os.chdir(repo_name)
    install_command = "pip install -r requirements.txt"
    os.system(install_command)
    os.chdir("..")

def main():
    repos = [
        "https://github.com/Significant-Gravitas/AutoGPT",
        "https://github.com/Significant-Gravitas/Auto-GPT-Plugins",
        "https://github.com/gorilla-llm/gorilla-cli",
        "https://github.com/e2b-dev/e2b",
        "https://github.com/e2b-dev/awesome-ai-agents",
        "https://github.com/e2b-dev/llm-code-interpreter",
        "https://github.com/e2b-dev/awesome-sdks-for-ai-agents",
        "https://github.com/e2b-dev/e2b-cookbook"
    ]
    for repo in repos:
        install_repo(repo)

if __name__ == "__main__":
    main()
```