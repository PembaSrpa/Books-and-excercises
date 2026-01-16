import subprocess

def git_push(message):
    try:
        # 1. Stage all changes
        subprocess.run(["git", "add", "."], check=True)

        # 2. Commit with the provided message
        subprocess.run(["git", "commit", "-m", message], check=True)

        # 3. Push to the current branch
        # (Assuming 'origin' is your remote and your branch is set up)
        subprocess.run(["git", "push"], check=True)

        print("Successfully pushed to Git!")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while pushing: {e}")

# Usage
message = "5.ipynb"
git_push(message)
