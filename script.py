import os
from execute_commands import execute_command
from git_commands import GitCommands
import json

PROXY = "http://proxy.iiit.ac.in:8080"
os.environ["HTTP_PROXY"] = PROXY
os.environ["HTTPS_PROXY"] = PROXY

git = GitCommands()

def rename_file(src_name, dest_name):
    cmd = "mv %s %s" % (src_name, dest_name)
    (ret_code, output) = execute_command(cmd)
    print "rename is done"
    return ret_code

def rsync_files(src_path, dest_path):
    print "******copying license file********"
    cmd = "rsync -avz %s %s" % (src_path, dest_path)
    (ret_code, output) = execute_command(cmd)
    return ret_code

def add_repo_changes(repo_name):
    try:
        repo_path = os.getcwd() + "/vlead-repos/" + repo_name
        cmd = "git -C %s add license.org" % (repo_path)
        execute_command(cmd)
    except Exception as e:
        print str(e)

def commit_changes(repo_name):
    commit_msg = "'added licensing file'"
    repo_path = os.getcwd() + "/vlead-repos/" + repo_name
    cmd = "git -C %s commit -m %s" % (repo_path, commit_msg)
    print cmd
    try:
        execute_command(cmd)
    except Exception as e:
        return

def push_changes(repo_name):
    print "******push***********"
    repo_path = os.getcwd() + "/" + repo_name
    cmd = "git -C %s push origin master" % (repo_path)
    print cmd
    try:
        git_creden()
        execute_command(cmd)

    except Exception as e:
        return
    
def git_repo_pusher():
    pwd = os.getcwd()
    file_path = pwd + "/vlead-repos.json"
    with open(file_path) as data_file:
        data = json.load(data_file)
    for repo_url in data:
        repo_name = repo_url["repo_name"]
        repo_url = repo_url["repo_url"]
        if git.repo_exists(repo_name):
            print "%s already exists pulling" % (repo_name)
            #git.pull_repo(repo_name, "master")
            
        else:
            print "Cloning repo %s" % (repo_url)
            git.clone_repo(repo_url, repo_name)
        src_path = pwd + "/index.org"
        dest_path = pwd + "/vlead-repos/" + repo_name + "/license.org"
        rsync_files(src_path, dest_path)
        add_repo_changes(repo_name)
        commit_changes(repo_name)
print git_repo_pusher()
