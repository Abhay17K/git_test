1import os
import subprocess

# Set the number of commits you want to create
num_commits = 400
repo_path = 'C:/Users/shreya_mishra/IdeaProjects/psl_test_repo_1'  # Replace with your repo's path

# Navigate to the git repository
os.chdir(repo_path)

# Function to run a git command and capture its output
def run_git_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout

# Function to create a file, stage it, and commit
def create_commit(i):
    # Create a dummy file with content
    file_name = f"file_{i}.txt"
    with open(file_name, 'w') as f:
        f.write(f"This is the content of commit number {i}\n")
    
    # Stage the file
    run_git_command(['git', 'add', file_name])
    
    # Commit the file
    commit_message = f"Commit number {i}"
    run_git_command(['git', 'commit', '-m', commit_message])
    
    print(f"Created commit {i} with file {file_name}")

# Loop to create multiple commits
for i in range(1, num_commits + 1):
    create_commit(i)

print(f"Created {num_commits} dummy commits!")
