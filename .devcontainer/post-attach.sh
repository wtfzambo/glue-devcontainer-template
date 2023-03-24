#!/bin/bash

set -ex

git config --list | grep "safe.directory=$(pwd)" || git config --global --add safe.directory $(pwd)
