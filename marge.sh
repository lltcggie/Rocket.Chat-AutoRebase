#! /bin/bash
# Merge pushes to development branch to stable branch
if [ $# -ne 4 ] ; then
    echo "Usage: merge.sh <GIT_USER> <GIT_PASS> <GIT_URL> <GIT_UPSTREAM_URL>"
    exit 1;
fi

GIT_USER="$1"
GIT_PASS="$2"
GIT_URL="$3"
GIT_UPSTREAM_URL="$4"

PUSH_URL="https://$GIT_USER:$GIT_PASS@${GIT_URL:8}"

git clone $GIT_URL git_tmp || exit $?

cd git_tmp
git remote add upstream $GIT_UPSTREAM_URL || exit $?
git fetch --tags upstream || exit $?
git remote set-url origin $PUSH_URL || exit $?
cd ..

python `dirname $0`/marge.py || exit $?
