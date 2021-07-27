#!/usr/bin/env bash

function fun1() {

  #oldstate=$(set +o)
  #set +x

  echo 113 # 1> /dev/null

  #set -vx; eval "$oldstate"
  #set -x

  return 34
}

function fun2() {
  fun1
  local ret=$?
  echo return value of fun1 is $ret
  local res=$(fun1)
  echo result value of fun1 is $res
}

fun2
