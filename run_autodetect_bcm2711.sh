#!/bin/bash
set -e

if [[ $# != 5 ]]; then
  echo "Usage: $0 max_ticks num_test 0 each_run output_name" >&2
  exit 1
fi
if [[ $(uname -s) != Linux || $(uname -m) != aarch64 ]]; then
  echo "BCM2711 benchmarks require AArch64 Linux." >&2
  exit 1
fi
command -v gcc >/dev/null || { echo "gcc is required." >&2; exit 1; }
machine=arm64

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

if [[ $vic_num != 0 || $cache_size != 32768 || $cache_asso != 2 || $cache_line != 64 ]]; then
  echo "Require BCM2711 machine ID 0 and L1D geometry 32768/2/64." >&2
  exit 1
fi

rm -f ./benchmark_output/"$output_name".*

./run_bcm2711.sh "$machine" "$max_cycle" "$cache_size" "$cache_asso" "$cache_line" "$num_test" "$vic_num" "$probe_size" "$each_run" "$output_name"
