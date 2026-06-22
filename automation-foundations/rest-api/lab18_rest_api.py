import requests

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    with requests.Session() as s:
         s.headers.update({"User-Agent": "network-engineering-mastery"})
         try:
           r= s.get(url,timeout=10)
           r.raise_for_status()
           repos=r.json()
  
           for repo in repos:
              print(f"{repo['name']}: {repo['description']}")
              


         except requests.exceptions.Timeout:
             print("Request timed out")
         except requests.exceptions.HTTPError as e:
            print(f"HTTP error: {e}")
         except requests.exceptions.RequestException as e:
            print(f"Something went wrong: {e}")


def get_repo_languages(username,repo):
    url = f"https://api.github.com/repos/{username}/{repo}/languages"
    
    with requests.Session() as s:
         s.headers.update({"User-Agent": "network-engineering-mastery"})
        
         try:
           r= s.get(url,timeout=10) 
           r.raise_for_status()
           languages=r.json()
           print(languages)              


         except requests.exceptions.Timeout:
            print("Request timed out")
         except requests.exceptions.HTTPError as e:
             print(f"HTTP error: {e}")
         except requests.exceptions.RequestException as e:
            print(f"Something went wrong: {e}")
 
def main():

    get_repos("arjun8282")
    get_repo_languages("arjun8282","network-engineering-mastery")

if __name__ == "__main__":
     main()

