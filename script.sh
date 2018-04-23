
# !/bin/env bash
# -*- mode: shell-script -*-

for j in vlead-repos/*;    # stores the repo value in j as an array
do 

    echo "Pushing $j";      # prints repo_name
    cd $j;                  # shifts dir to repo_name, checks the status, gives commit message and will push to git organization   
    git push origin master ;
    git config credential.helper store
    pwd
    cd ../..                 # back to the repos dir
    # echo "Finished $j";    # passes message
done
