import git

# clone
url = 'git@github.com:tomyamkung/test-app-a.git'
to_path = 'checkout-repo'
git.Repo.clone_from(
    url,
    to_path,
    branch='main')

# update version
with open('checkout-repo/test.txt', 'wt') as fp:
    fp.write('add-string')

# git add    
repo.git.add('test.txt')

# git commit
repo.git.commit('test.txt', message='update', author='releaser')

# git push
repo.git.push ('origin', 'main')
