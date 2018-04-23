import os
import json
from execute_commands import execute_command

GIT_CLONE_LOC =  os.getcwd() + "/vlead-repos/"

class GitCommands:

    git_clone_loc = None

    def __init__(self):
        self.git_clone_loc = GIT_CLONE_LOC

    def get_git_clone_loc(self):
        return self.git_clone_loc

    def construct_repo_name(self, lab_src_url):
        repo = lab_src_url.split('/')[-1]
        repo_name = (repo[:-4] if repo[-4:] == ".git" else repo)
        return str(repo_name)

    def repo_exists(self, repo_name):
        return os.path.isdir(self.git_clone_loc + repo_name)

    def clone_repo(self, lab_src_url, repo_name):
        print lab_src_url
        clone_cmd = "git clone %s %s%s" % (lab_src_url, self.git_clone_loc,
                                           repo_name)
        try:
            (ret_code, output) = execute_command(clone_cmd)
        except Exception, e:
            raise e

    def pull_repo(self, repo_name, version):
        repo = self.git_clone_loc + repo_name
        pull_cmd = "git -C %s pull origin %s" % (repo, version)
        try:
            (ret_code, output) = execute_command(pull_cmd)
        except Exception, e:
            raise e

    def reset_repo(self, repo_name):
        repo = self.git_clone_loc + repo_name
        reset_cmd = "git --git-dir=%s/.git --work-tree=%s reset --hard" % (repo, repo)
        try:
            (ret_code, output) = execute_command(reset_cmd)
        except Exception, e:
            raise e

    def checkout_version(self, repo_name, version=None):
        repo = self.git_clone_loc + repo_name
        if version is None:
            version = "master"
        checkout_cmd = "git --git-dir=%s/.git --work-tree=%s checkout %s" % (repo, repo, version)
        try:
            (ret_code, output) = execute_command(checkout_cmd)
        except Exception, e:
            raise e



if __name__ == '__main__':
    git = GitCommands()
    lab_src_url = "https://github.com/Virtual-Labs/computer-programming-iiith.git"
    try:
        repo_name = git.construct_repo_name(lab_src_url)
        if git.repo_exists(repo_name):
            #  reset_repo(repo_name)
            git.pull_repo(repo_name)
        else:
            git.clone_repo(lab_src_url, repo_name)
            git.checkout_version(repo_name, None)
    except Exception, e:
        print str(e)
