```python
import os
import subprocess

# List of repositories to be installed
repositories = [
    "https://github.com/Significant-Gravitas/AutoGPT",
    "https://github.com/Significant-Gravitas/Auto-GPT-Plugins",
    "https://github.com/gorilla-llm/gorilla-cli",
    "https://github.com/e2b-dev/e2b",
    "https://github.com/e2b-dev/awesome-ai-agents",
    "https://github.com/e2b-dev/llm-code-interpreter",
    "https://github.com/e2b-dev/awesome-sdks-for-ai-agents",
    "https://github.com/e2b-dev/e2b-cookbook"
]

def install_repo(repo_url):
    # Clone the repository
    subprocess.check_call(["git", "clone", repo_url])

    # Extract the repo name from the URL
    repo_name = repo_url.split("/")[-1]

    # Change to the repo directory
    os.chdir(repo_name)

    # Install the requirements if the file exists
    if os.path.exists("requirements.txt"):
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])

    # Run the setup if the file exists
    if os.path.exists("setup.py"):
        subprocess.check_call(["python", "setup.py", "install"])

    # Change back to the parent directory
    os.chdir("..")

def main():
    for repo in repositories:
        install_repo(repo)

if __name__ == "__main__":
    main()
```