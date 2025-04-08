#!/bin/zsh

TARGET=./

autoflake \
	--remove-all-unused-imports \
	--ignore-init-module-imports \
	--in-place \
	--recursive \
	--exclude "venv" \
	$TARGET

pyclean $TARGET

isort --profile black $TARGET

black --line-length 120 $TARGET

exit 0
