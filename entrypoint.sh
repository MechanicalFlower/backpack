#!/bin/sh

# Go to the workdir
cd $GITHUB_WORKSPACE

# Split arguments by space
arguments=($@)

# Run magic combo
magic_combo "${arguments[@]}"
