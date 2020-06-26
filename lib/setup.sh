#!/bin/bash

export GIT_SSH_COMMAND="ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"

echo ${GITHUB_SSH_CREDENTIALS} > id_rsa
chmod 600 id_rsa
ssh-add id_rsa

echo ${PYPI_REPO_CONFIG} > ~/.pypirc

pip install -y twine

python setup.py upload
