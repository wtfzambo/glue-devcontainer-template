#!/bin/bash

set -ex
printf "\nsource ~/.bashrc.1\n" >> ~/.bashrc

poetry install --no-root
echo 'Finished setup!'
