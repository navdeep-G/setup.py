#!/bin/bash

set -x

export GIT_SSH_COMMAND="ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"

echo -e ${GITHUB_SSH_CREDENTIALS//&/\\n} > id_rsa
#sed -i 's/^ //g' id_rsa
cat id_rsa
chmod 600 id_rsa
ssh-add id_rsa

echo -e ${PYPI_REPO_CONFIG//&/\\n} > ~/.pypirc
sed -i 's/\\ / /g' ~/.pypirc
ls -l ~/.pypirc
cat ~/.pypirc

pip install twine

python setup.py upload
