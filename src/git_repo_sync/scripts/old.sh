#!/bin/bash -u
set -o errtrace
set -o pipefail

repositories=(
  repo1
  repo2
  repo3
  repo4
  repo5
  repo6
)


for r in ${repositories[@]}; do
  cd /data/git

  echo ""
  echo "Clone project if not exist"

  if [ -d "$r" ]; then
      echo $r exist
    else
      echo $r not exist
      git clone git@bitbucket.org:org/$r.git
  fi

  cd $r

  git remote set-url origin git@bitbucket.org:org/$r.git
  git remote -v

  echo ""
  echo "Checkout all remote branches"
  for remote in `git branch -r | grep -v /HEAD`; do git checkout --track $remote ; done

  echo ""
  echo "Fetch all commits and tags"
  git fetch --all
  git fetch --tags
  git pull --all

  echo ""
  echo "Set remote url to GitLab"
  git remote set-url origin ssh://git@gitlab.customer.com:30022/org/$r.git
  git remote -v

  echo ""
  echo "Push all commits and tags"
  git push --all
  git push --tags
done