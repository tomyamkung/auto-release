import git
import datetime

# date
date = datetime.datetime.now()

# clone
url = 'git@github.com:tomyamkung/test-app-b.git'
to_path = 'checkout-repo'
git.Repo.clone_from(
    url,
    to_path,
    branch='main')
repo = git.Repo(to_path)

# checkout new branch
repo.git.branch() 
repo.git.branch('new_branch') 
repo.git.checkout('new_branch')

# update version
with open('checkout-repo/test.txt', 'wt') as fp:
    fp.write(str(date))

# git add    
repo.git.add('test.txt')

# git commit
repo.git.commit('test.txt','-m','\"auto-commit\"')

# git push
repo.git.push ('origin', 'new_branch')
