#!/bin/bash
set -e

#
# This file is the top script file to generate and evaluate benchmark code
#
# Copyright (C) 2020
# Author: Shuwen Deng <shuwen.deng@yale.edu>
# Date:   02.04.2020
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
#
#

machine=$1
max_cycle=$2
cache_size=$3
cache_asso=$4
cache_line=$5
num_test=$6
vic_num=$7
probe_size=$8
each_run=$9
output_name=${10}

if [[ $# != 10 ]]; then
	echo "Usage: $0 arm64 max_ticks 32768 2 64 num_test 0 3 each_run output_name" >&2
	exit 1
fi
if [[ $(uname -s) != Linux || $(uname -m) != aarch64 ]]; then
	echo "BCM2711 benchmarks require AArch64 Linux." >&2
	exit 1
fi
command -v gcc >/dev/null || { echo "gcc is required." >&2; exit 1; }
if [[ $machine != arm64 || $vic_num != 0 || $cache_size != 32768 || $cache_asso != 2 || $cache_line != 64 || $probe_size != 3 ]]; then
	echo "Require arm64, BCM2711 machine ID 0, L1D geometry 32768/2/64, and probe_size 3." >&2
	exit 1
fi
echo "Timing values and max_ticks use CNTVCT_EL0 ticks, not CPU cycles. EL0 DC CIVAC access must be kernel-permitted." >&2

rm -rf gen_output
mkdir gen_output
mkdir -p benchmark_output

cp run_sub_bcm2711.sh gen_output/

gcc -std=gnu99 -o gen_vulnerabilities_bcm2711 gen_vulnerabilities_bcm2711.c
./gen_vulnerabilities_bcm2711 "$machine" "$max_cycle" "$cache_size" "$cache_asso" "$cache_line" "$num_test" "$vic_num" "$probe_size" "$each_run"

cd gen_output
./run_sub_bcm2711.sh "$output_name"
