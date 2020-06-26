#!/bin/bash

set -x

export GIT_SSH_COMMAND="ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"

echo -e ${GITHUB_SSH_CREDENTIALS} > id_rsa_base64
sed -i 's/^ //g' id_rsa_base64
base64 -d id_rsa_base64 > id_rsa
cat id_rsa
chmod 600 id_rsa
ssh-add id_rsa

echo -e ${PYPI_REPO_CONFIG} > ~/.pypirc_base64
sed -i 's/^ //g' ~/.pypirc_base64
base64 -d ~/.pypirc_base64 > ~/.pypirc
cat ~/.pypirc

pip install twine

python setup.py upload
