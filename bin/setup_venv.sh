#!/usr/bin/env bash

PROJECT=conveyor-flask-app
PYTHON=python3

THIS_VENV="/var/tmp/venvs/$PROJECT"
VENVS_DIR=$(dirname $THIS_VENV)

if [[ -e $THIS_VENV/bin/activate ]]; then
  echo -e "Run the following to activate venv:\n source $THIS_VENV/bin/activate\n"
  exit
fi

mkdir -pv $VENVS_DIR

$PYTHON -m venv $THIS_VENV --system-site-packages

source $THIS_VENV/bin/activate

python -m pip install --upgrade pip && pip install -U wheel && pip install -U setuptools
pip install -r requirements.txt

echo "Created venv: $THIS_VENV"
echo -e "Run the following to activate venv:\n source $THIS_VENV/bin/activate\n"