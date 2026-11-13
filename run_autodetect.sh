#!/bin/bash
set -e

case $(uname -m) in
  "x86_64")
    machine=x86
    ;;
esac

cache0_type=$(cat /sys/devices/system/cpu/cpu0/cache/index0/type)
cache1_type=$(cat /sys/devices/system/cpu/cpu0/cache/index1/type)
if [[ "$cache0_type" == "Data" ]]; then
  cache_path="/sys/devices/system/cpu/cpu0/cache/index0"
elif [[ "$cache1_type" == "Data" ]]; then
  cache_path="/sys/devices/system/cpu/cpu0/cache/index1"
else
  exit 1
fi

# machine=$1
max_cycle=$1
cache_size=$(awk '{gsub(/K/, ""); print $0 * 1024}' $cache_path/size)
cache_asso=$(cat $cache_path/ways_of_associativity)
cache_line=$(cat $cache_path//coherency_line_size)
num_test=$2
vic_num=$3
probe_size="3"
each_run=$4
output_name=${5}

rm -f ./benchmark_output/$output_name.*

./run.sh $machine $max_cycle $cache_size $cache_asso $cache_line $num_test $vic_num $probe_size $each_run $output_name