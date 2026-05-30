import subprocess

def check_repo(repo_path):
    """Checks the status of a Git repository.

    Args:
        repo_path: The path to the repository.

    Returns:
        A list of strings, where each string represents a line of output from the
        `git status` command.
    """

    output = subprocess.check_output(["git", "status"], cwd=repo_path)
    return output.decode("utf-8").splitlines()

def main():
    """Monitors the local GitHub repositories."""

    # Get a list of all of the local GitHub repositories.
    repos = subprocess.check_output(["git", "config", "--local", "--list"]).decode("utf-8").splitlines()

    # Check the status of each repository.
    for repo in repos:
        print("Checking repository:", repo)
        output = check_repo(repo)

        # Print the output from the `git status` command.
        for line in output:
            print(line)

if __name__ == "__main__":
    main()