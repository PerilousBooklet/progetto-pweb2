#!/usr/bin/bash
tmux new -s django -d
tmux send-keys -t django './build.sh' C-m
tmux attach -t django

