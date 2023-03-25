#!/bin/bash

set -ex
printf "\nsource ~/.bashrc.1\n" >> ~/.bashrc

poetry install
echo 'Finished setup!'
