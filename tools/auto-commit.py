import git
import datetime

# date
date = datetime.datetime.now()

# clone
url = 'git@github.com:tomyamkung/test-app-a.git'
to_path = 'checkout-repo'
git.Repo.clone_from(
    url,
    to_path,
    branch='main')
repo = git.Repo(to_path)

# checkout new branch
repo.git.branch() 
repo.git.branch(str(date)) 
repo.git.checkout(str(date))

# update version
with open('checkout-repo/test.txt', 'wt') as fp:
    fp.write(str(date))

# git add    
repo.git.add('test.txt')

# git commit
repo.git.commit('test.txt','-m','\"auto-commit\"')

# git push
repo.git.push ('origin', str(date))
