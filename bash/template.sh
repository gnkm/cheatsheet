#! /usr/bin/env bash

# print the usage and exit
print_usage_and_exit () {
	cat <<____USAGE 1>&2
Usage   : ${0##*/} <arg1> <arg2> ...
{descriptions}
positional parameters:
  arg1: description of arg1
  arg2: description of arg2
  ...
____USAGE
	exit 1
}

# main script starts here
