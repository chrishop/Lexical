#!/usr/bin/env bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python3
python3 -m pip install py-bcrypt
python3 -m pip install pygame
echo INSTALLATION COMPLETE