#!/usr/bin/sh 

if command -v apt-get &> /dev/null; then
    pack_man="sudo apt-get install "
    auto="-y"
    sudo apt install pip
elif command -v yum &> /dev/null; then
    pack_man="sudo yum install"
    auto=""
elif command -v dnf &> /dev/null; then
    pack_man="sudo dnf install"
    auto=""
elif command -v pacman &> /dev/null; then
    pack_man="sudo pacman -S"
    auto="--noconfirm"
else
    echo "Unsupported package manager. Please install Python manually."
    exit 1
fi
$pack_man $auto python3
pip install psutil requests os itertools


