#!/usr/bin/env bash

readonly PROGNAME=$(basename $0)
readonly PROGDIR=$(readlink -m $(dirname $0))
readonly ARGS=("$@")

readonly USERNAME=${ARGS[0]}
readonly PASSWORD=${ARGS[1]}
readonly DATABASENAME=${ARGS[2]}

main(){
    for file in *.sql
        do
	        run_pg_bench $file
        done
}

run_pg_bench(){
    local file=$1
    echo "Query: ${file}"
    echo -e "------------------------"
    export PGPASSWORD=${PASSWORD}; pgbench -U $USERNAME -h localhost -f $file -n $DATABASENAME
    echo -e "\n"
}

main
