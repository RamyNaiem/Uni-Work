import requests
from pathlib import Path
import base64

def download_newest_c_cpp_file(user, repo, subpath, branch='main'):
    """Download the newest C/C++ file from a specified directory in a GitHub repository."""
    # Get the latest commits affecting the subpath
    commits_url = f"https://api.github.com/repos/{user}/{repo}/commits?path={subpath}&sha={branch}"
    commits_response = requests.get(commits_url)

    if commits_response.status_code == 200:
        commits_data = commits_response.json()
        for commit in commits_data:
            # Fetch details for each commit to get the files list
            commit_detail_url = commit['url']
            commit_detail_response = requests.get(commit_detail_url)

            if commit_detail_response.status_code == 200:
                commit_detail_data = commit_detail_response.json()
                if 'files' in commit_detail_data:
                    for file in commit_detail_data['files']:
                        if file['filename'].endswith(('.c', '.cpp')):
                            file_url = file['raw_url']
                            download_file(file_url, file['filename'])
                            return  # Stop after downloading the newest file
                else:
                    print("No files data found in commit details.")
            else:
                print(f"Failed to retrieve commit details: {commit_detail_response.status_code}")
        print("No new .c or .cpp files found in recent commits.")
    else:
        print(f"Failed to retrieve commits: {commits_response.status_code} {commits_response.text}")

def download_file(url, file_path):
    """Download a file from a GitHub raw URL and save it locally."""
    response = requests.get(url)
    if response.status_code == 200:
        local_file_path = Path('waiting') / Path(file_path).name
        local_file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(local_file_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {file_path} to {local_file_path}")
    else:
        print(f"Failed to download file: {response.status_code} {response.text}")

# Example usage
download_newest_c_cpp_file('MisterfailLP', 'GradProject', 'Codes/', 'main')
