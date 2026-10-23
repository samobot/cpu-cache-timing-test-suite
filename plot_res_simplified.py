#
# This file plot benchmark running results for 9 machine configurations
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


import matplotlib.pyplot as plt
import csv
import sys

params = {'legend.fontsize': 15,
		  'legend.handlelength': 2,
		  #'legend.frameon': False,
		  'axes.titlesize'      : 18,
		  'axes.labelsize'      : 15}
plt.rcParams.update(params)

if ((len(sys.argv))<=1):
	print ("Please add string after the python script to indicate machine and running information as the naming of the dot diagrams")
	exit(1)

vul_num=88
x = []

y_srv1_dup = []

y_srv1 = []

y_srv1_1 = []

y_srv1_2 = []

x_1=[]
x_2=[]
x_single_1 = []
x_single_2 = []

outer_x=[]
outer_grids = []
grids = []
grids_2 = []

outer_counter=0
counter=0
step=0

x_single = []
y_srv1_single = []

y_read=[[], [], [], [], [], [], [], [], [], [], []] 
y_write=[[], [], [], [], [], [], [], [], [], [], []]
y_ccinv=[[], [], [], [], [], [], [], [], [], [], []]
y_clflush=[[], [], [], [], [], [], [], [], [], [], []]
y_hyper=[[], [], [], [], [], [], [], [], [], [], []]
y_time=[[], [], [], [], [], [], [], [], [], [], []]
y_inner=[[], [], [], [], [], [], [], [], [], [], []]
y_hasatt=[[], [], [], [], [], [], [], [], [], [], []]
x_read=[]
grids_read=[]
x_write=[]
grids_write=[]
x_ccinv=[]
grids_ccinv=[]
x_clflush=[]
grids_clflush=[]
x_hyper=[]
grids_hyper=[]
x_time=[]
grids_time=[]
x_inner=[]
grids_inner=[]
x_hasatt=[]
grids_hasatt=[]

with open('benchmark_output/srv1_gen_v16_recon_fix.output.res.tran','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=' ')
	for row in plots:
		if row==[]:
			grids.append(counter)
			outer_grids.append(outer_counter)
		else:
			if(row==['222']):
				y_srv1_dup.append(-2)
			elif(int(row[0], 2)==2):
				y_srv1.append(1+step)
				y_srv1_dup.append(1+step)
				x.append(counter)
				counter = counter + 1
			else:
				y_srv1.append(0+step)
				y_srv1_dup.append(0+step)
				x.append(counter)
				counter = counter + 1
			outer_x.append(outer_counter)
			outer_counter = outer_counter + 1
step = step +2

#print grids


for i in range(554):
	y_srv1_1.append(y_srv1[i])
	x_1.append(x[i])

for i in range(554, 1094):
	y_srv1_2.append(y_srv1[i])
	x_2.append(x[i]-554)

for i in range(vul_num//2):
	x_single_1.append(i+1)
	x_single_2.append(i+vul_num/2+1)
	grids_2.append(grids[i+vul_num//2]-554)

inner_counter=0
inner_bound = grids[0]
for i in range(vul_num):
	x_single.append(i)
	y_srv1_single.append(y_srv1[inner_counter]-6)
	inner_counter = inner_counter + 1
	if i!=0:
		inner_bound = grids[i] - grids[i-1]
	for j in range(inner_bound-1):
		y_srv1_single[i] = y_srv1_single[i] or (y_srv1[inner_counter]-6)
		inner_counter = inner_counter + 1
	y_srv1_single[i] = y_srv1_single[i] + 6

#print outer_grids
#print vul_num

# read
inner_counter=0
inner_bound = outer_grids[0]
for i in range(88//2):
	grids_read.append(outer_grids[i]/2)
	if i!=0:
		inner_bound = outer_grids[i] - outer_grids[i-1]
	if (inner_bound==8):
		for j in range(inner_bound//2):
			x_read.append(inner_counter//2)
			y_read[3].append(y_srv1_dup[inner_counter])
			inner_counter = inner_counter + 1+1
	elif (inner_bound==16):
		for j in range(inner_bound//4):
			x_read.append(inner_counter//2)
			x_read.append(inner_counter//2+1)
			y_read[3].extend((y_srv1_dup[inner_counter], y_srv1_dup[inner_counter+1]))
			inner_counter = inner_counter + 2+2

# write
inner_counter=0
inner_bound = outer_grids[0]
for i in range(88//2):
	grids_write.append(outer_grids[i]/2)
	if i!=0:
		inner_bound = outer_grids[i] - outer_grids[i-1]
	if (inner_bound==8):
		for j in range(inner_bound//2):
			x_write.append(inner_counter//2)
			inner_counter = inner_counter + 1
			
			y_write[3].append(y_srv1_dup[inner_counter])
			inner_counter = inner_counter + 1
	elif (inner_bound==16):
		for j in range(inner_bound//4):
			x_write.append(inner_counter//2)
			x_write.append(inner_counter//2+1)
			inner_counter = inner_counter + 2
			
			y_write[3].extend((y_srv1_dup[inner_counter], y_srv1_dup[inner_counter+1]))
			inner_counter = inner_counter + 2



# ccinv

inner_counter=outer_grids[vul_num//2-1]
for i in range(88//2, 88):
	grids_ccinv.append(outer_grids[i]/2)
	inner_bound = outer_grids[i] - outer_grids[i-1]
	if (inner_bound==8):
		for j in range(inner_bound//2):
			x_ccinv.append(inner_counter/2)
			inner_counter = inner_counter + 1
			
			y_ccinv[3].append(y_srv1_dup[inner_counter])
			inner_counter = inner_counter + 1
	elif (inner_bound==16):
		for j in range(inner_bound//4):
			x_ccinv.append(inner_counter/2)
			x_ccinv.append(inner_counter/2+1)
			
			y_ccinv[3].extend((y_srv1_dup[inner_counter], y_srv1_dup[inner_counter+1]))
			inner_counter = inner_counter + 2 +2

# clflush
inner_counter=outer_grids[vul_num//2-1]
for i in range(88//2, 88):
	grids_clflush.append(outer_grids[i]/2)
	inner_bound = outer_grids[i] - outer_grids[i-1]
	if (inner_bound==8):
		for j in range(inner_bound//2):
			x_clflush.append(inner_counter/2)
			y_clflush[3].append(y_srv1_dup[inner_counter])
			inner_counter = inner_counter + 1+1
	elif (inner_bound==16):
		for j in range(inner_bound//4):
			x_clflush.append(inner_counter/2)
			x_clflush.append(inner_counter/2+1)
			inner_counter = inner_counter + 2
			y_clflush[3].extend((y_srv1_dup[inner_counter], y_srv1_dup[inner_counter+1]))
			inner_counter = inner_counter + 2


# derived for differentiating victim, attacker running on the same (hyper-threading, time-slicing)/diff core, victim running alone cases
case_arr=[4,3,4,3,4,3,4,3,0,2,0,2,0,2,0,2,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,4,3,4,3,0,2,0,2,0,2,0,2,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,0,2,0,2,4,3,4,3,0,2,0,2,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,0,2,0,2,4,3,4,3,0,2,0,2,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,0,2,0,2,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,0,2,0,2,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,0,2,0,2,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,0,2,0,2,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,0,2,0,2,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,0,2,0,2,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,0,2,0,2,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,0,2,0,2,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,0,2,0,2,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,0,2,0,2,4,3,4,3,4,3,4,3,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,0,2,0,2,4,3,4,3,4,3,4,3,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,0,2,4,3,0,2,4,3,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,4,3,4,3,0,2,4,3,0,2,4,3,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,4,3,4,3,4,3,0,2,4,3,0,2,4,3,0,2,4,3,0,2,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,0,2,4,3,0,2,4,3,0,2,4,3,0,2,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,0,2,4,3,0,2,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,0,2,4,3,4,3,4,3,0,2,4,3,4,3,4,3,4,3,0,2,4,3,4,3,4,3,0,2,4,3,0,2,4,3,4,3,4,3,0,2,4,3,4,3,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,0,2,4,3,4,3,4,3,0,2,4,3,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,0,2,4,3,4,3,0,2,4,3,4,3,4,3,4,3,4,3,0,2,0,2,4,3,4,3,4,3,4,3,0,2,4,3,4,3,4,3,4,3,0,2,4,3,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,0,2,4,3,4,3,0,2,4,3,4,3,4,3,4,3,4,3,0,2,0,2,4,3,4,3,4,3,4,3,0,2,4,3,4,3,4,3,4,3,0,2,4,3,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,0,2,4,3,4,3,0,2,4,3,4,3,4,3,4,3,4,3,0,2,0,2,4,3,4,3,4,3,4,3,0,2,4,3,4,3,4,3,4,3,0,2,4,3,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,0,2,4,3,4,3,0,2,4,3,4,3,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,4,3,0,2,4,3,4,3,0,2,4,3,4,3,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,4,3,0,2,4,3,0,2,4,3,0,2,4,3,0,2,4,3,0,2,4,3,0,2,4,3,0,2,4,3,0,2,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3]

		 
# time slicing
inner_counter_time=0
inner_counter_hyper=0
inner_counter_inner=0
inner_counter_hasatt=0
inner_bound = outer_grids[0]
for i in range(88*16):
	if(case_arr[i]==3):
		x_time.append(inner_counter_time)
		y_time[3].append(y_srv1_dup[i])
		inner_counter_time = inner_counter_time + 1
	elif(case_arr[i]==4):
		x_hyper.append(inner_counter_hyper)
		y_hyper[3].append(y_srv1_dup[i])
		inner_counter_hyper = inner_counter_hyper + 1
	elif(case_arr[i]==1):
		x_inner.append(inner_counter_inner)
		y_inner[3].append(y_srv1_dup[i])
		inner_counter_inner = inner_counter_inner + 1
	elif(case_arr[i]==2):
		x_hasatt.append(inner_counter_hasatt)
		y_hasatt[3].append(y_srv1_dup[i])
		inner_counter_hasatt = inner_counter_hasatt + 1


ia_base=[1,2,3,4,10,12,14,16,18,20,45,46,47,48,54,56,58,60,62,64]
is_base=[26,28,32,34,35,39,70,72,76,78,79,83]
isa_base=[22,24,30,33,36,40,66,68,74,77,80,84]
ea_base=[5,6,7,8,9,11,13,15,17,19,49,50,51,52,53,55,57,59,61,63,]
es_base=[25,27,31,37,41,43,69,71,75,81,85,87]
esa_base=[21,23,29,38,42,44,65,67,73,82,86,88]


for i in range(len(ia_base)):
	ia_base[i] = ia_base[i] -1
for i in range(len(isa_base)):
	is_base[i] = is_base[i] -1
for i in range(len(isa_base)):
	isa_base[i] = isa_base[i] -1
for i in range(len(ea_base)):
	ea_base[i] = ea_base[i] -1
for i in range(len(esa_base)):
	es_base[i] = es_base[i] -1
for i in range(len(isa_base)):
	esa_base[i] = esa_base[i] -1


#print len(ia_base), len(is_base), len(isa_base), len(ea_base), len(es_base), len(esa_base)


all_suc=[0,0,0,0,0,0,0,0,0,0,0]
ia_suc=[0,0,0,0,0,0,0,0,0,0,0]
is_suc=[0,0,0,0,0,0,0,0,0,0,0]
isa_suc=[0,0,0,0,0,0,0,0,0,0,0]
ea_suc=[0,0,0,0,0,0,0,0,0,0,0]
es_suc=[0,0,0,0,0,0,0,0,0,0,0]
esa_suc=[0,0,0,0,0,0,0,0,0,0,0]


for i in x_single:
	if i in x_single:
		if y_srv1_single[i]==7:
			all_suc[3]=all_suc[3]+1
	if i in ia_base:
		if y_srv1_single[i]==7:
			ia_suc[3]=ia_suc[3]+1
	if i in is_base:
		if y_srv1_single[i]==7:
			is_suc[3]=is_suc[3]+1
	if i in isa_base:
		if y_srv1_single[i]==7:
			isa_suc[3]=isa_suc[3]+1
	if i in ea_base:
		if y_srv1_single[i]==7:
			ea_suc[3]=ea_suc[3]+1
	if i in es_base:
		if y_srv1_single[i]==7:
			es_suc[3]=es_suc[3]+1
	if i in esa_base:
		if y_srv1_single[i]==7:
			esa_suc[3]=esa_suc[3]+1
print("All the vulnerability types found vulnerable for the machines in paper's order: ")
print(all_suc)
print("I-A Vulnerability types found vulnerable for the machines in paper's order: ")
print(ia_suc)
print("I-S Vulnerability types found vulnerable for the machines in paper's order: ")
print(is_suc)
print("I-SA Vulnerability types found vulnerable for the machines in paper's order: ")
print(isa_suc)
print("E-A Vulnerability types found vulnerable for the machines in paper's order: ")
print(ea_suc)
print("E-S Vulnerability types found vulnerable for the machines in paper's order: ")
print(es_suc)
print("E-SA Vulnerability types found vulnerable for the machines in paper's order: ")
print(esa_suc)

x_single_plus=[]
for i in range(len(x_single)):
	x_single_plus.append(x_single[i] + 1)


read_suc=[0,0,0,0,0,0,0,0,0,0,0]
write_suc=[0,0,0,0,0,0,0,0,0,0,0]
ccinv_suc=[0,0,0,0,0,0,0,0,0,0,0]
clflush_suc=[0,0,0,0,0,0,0,0,0,0,0]
time_suc=[0,0,0,0,0,0,0,0,0,0,0]
hyper_suc=[0,0,0,0,0,0,0,0,0,0,0]
inner_suc=[0,0,0,0,0,0,0,0,0,0,0]
hasatt_suc=[0,0,0,0,0,0,0,0,0,0,0]

#print len(x_read), len(x_write), len(x_ccinv), len(x_clflush), len(x_time), len(x_hyper), len(x_inner), len(x_hasatt)

len_xread=len(x_read)
len_xwrite=len(x_write)
len_xccinv=len(x_ccinv)
len_xclfllush=len(x_clflush)

#print grids

for i in x_read:
	if y_read[3][i]==7:
		read_suc[3]=read_suc[3]+1
	if y_read[3][i]==-2:
		len_xread = len_xread - 1
for i in x_write:
	if y_write[3][i]==7:
		write_suc[3]=write_suc[3]+1
	if y_write[3][i]==-2:
		len_xwrite = len_xwrite - 1


for i in range(len(x_ccinv)):
	if y_ccinv[3][i]==7:
		ccinv_suc[3]=ccinv_suc[3]+1
	if y_ccinv[3][i]==-2:
		len_xccinv = len_xccinv - 1
for i in range(len(x_clflush)):
	if y_clflush[3][i]==7:
		clflush_suc[3]=clflush_suc[3]+1
	if y_clflush[3][i]==-2:
		len_xclfllush = len_xclfllush - 1
for i in range(len(x_time)):
	if y_time[3][i]==7:
		time_suc[3]=time_suc[3]+1
for i in range(len(x_hyper)):
	if y_hyper[3][i]==7:
		hyper_suc[3]=hyper_suc[3]+1
for i in range(len(x_inner)):
	if y_inner[3][i]==7:
		inner_suc[3]=inner_suc[3]+1
for i in range(len(x_hasatt)):
	if y_hasatt[3][i]==7:
		hasatt_suc[3]=hasatt_suc[3]+1

#print len_xread, len_xwrite, len_xccinv, len_xclfllush

print("Vulnerability cases using local read as observation steps found vulnerable for the machines in paper's order: ")
print(read_suc)
print("Vulnerability cases using local write as observation steps found vulnerable for the machines in paper's order: ")
print(write_suc)
print("Vulnerability cases using remote write to invalidate as observation steps found vulnerable for the machines in paper's order: ")
print(ccinv_suc)
print("Vulnerability cases using flush as observation steps found vulnerable for the machines in paper's order: ")
print(clflush_suc)
print("Vulnerability cases with victim and attacker running time-slicing found vulnerable for the machines in paper's order: ")
print(time_suc)
print("Vulnerability cases with victim and attacker running hyper-threading found vulnerable for the machines in paper's order: ")
print(hyper_suc)
print("Vulnerability cases with victim and attacker running on different cores found vulnerable for the machines in paper's order: ")
print(inner_suc)
print("Vulnerability cases running with victim found vulnerable for the machines in paper's order: ")
print(hasatt_suc)



plt.rc('xtick', labelsize=13)
plt.rc('ytick', labelsize=16)


for i in range(len(x_single)):
	if y_srv1_single[i]==6:
		y_srv1_single[i]=-5


fig, ax=plt.subplots()
f1 = plt.figure(1)
f1.set_figheight(5.4)
f1.set_figwidth(28.3)
plt.plot(x_single,y_srv1_single, label='Intel Xeon E5-2690', linestyle="",color='c',marker='v', markersize=8)
plt.xlabel('vulnerabilities')
plt.ylabel('CPU Type')
ax.grid(True, which='major')
ax.set_xticks(x_single)
ax.set_ylim([-0.5,22])
ax.set_xlim([-1,88])
ax.set_xticklabels(x_single_plus)
ax.set_yticks([1,3,5,7,9,11,13,15,17,19,21])#1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])
ax.set_yticklabels(["Intel Xeon E5-1620", "Intel Xeon E5-2667 on-chip", "Intel Xeon E5-2667 inter-chip", "Intel Xeon E5-2690", "Intel Core i5-4570",  "Intel Xeon E5-2686", "Intel Xeon P-8175", "AMD FX-8150", "AMD EPYC 7571", "Found in all tested CPUs", "Found in at least one tested CPU" ])
box = ax.get_position()
ax.set_position([box.x0*1.45, box.y0 + box.height * 0.2,
				 box.width, box.height * 0.8])

plt.savefig("gen_figure/vul_by_type_"+sys.argv[1]+".pdf",bbox_inches='tight')
#f1.show()


for i in range(len(x_1)):
	if y_srv1_1[i]==6:
		y_srv1_1[i]=-5

for i in range(len(x_2)):
	if y_srv1_2[i]==6:
		y_srv1_2[i]=-5


fig, ax=plt.subplots()
f2 = plt.figure(2)
f2.set_figheight(5.4)
f2.set_figwidth(28.3)
plt.plot(x_1,y_srv1_1, label='Intel Xeon E5-2690 (srv1)', linestyle="",color='c',marker="o", markersize=2)
plt.xlabel('vulnerabilities')
plt.ylabel('CPU Type')
ax.set_xticks(grids)
ax.grid(True, which='major', axis='x',linestyle="--")
ax.set_ylim([-0.2,22])
ax.set_xlim([-1,554])
# ax.set_xticklabels(x_single_1)
ax.set_yticks([1,3,5,7,9,11,13,15,17,19,21])
ax.set_yticklabels(["Intel Xeon E5-1620", "Intel Xeon E5-2667 on-chip", "Intel Xeon E5-2667 inter-chip", "Intel Xeon E5-2690", "Intel Core i5-4570",  "Intel Xeon E5-2686", "Intel Xeon P-8175", "AMD FX-8150", "AMD EPYC 7571", "Found in all tested CPUs", "Found in at least one tested CPU" ])
box = ax.get_position()
ax.set_position([box.x0*1.5, box.y0 + box.height * 0.26,
				 box.width, box.height * 0.74])
plt.savefig("gen_figure/vul_by_case_"+sys.argv[1]+"_1.pdf",bbox_inches='tight')
#f2.show()




fig, ax=plt.subplots()
f3 = plt.figure(3)
f3.set_figheight(5.4)
f3.set_figwidth(28.3)
plt.plot(x_2,y_srv1_2, label='Intel Xeon E5-2690', linestyle="",color='c',marker="o", markersize=2)
plt.xlabel('vulnerabilities')
plt.ylabel('CPU Type')
ax.set_xticks(grids_2)
ax.grid(True, which='major', axis='x',linestyle="--")
ax.set_ylim([-0.2,22])
ax.set_xlim([-1,1094-554])
ax.set_xticklabels(x_single_2)
ax.set_yticks([1,3,5,7,9,11,13,15,17,19,21])#1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])
ax.set_yticklabels(["Intel Xeon E5-1620", "Intel Xeon E5-2667 on-chip", "Intel Xeon E5-2667 inter-chip", "Intel Xeon E5-2690", "Intel Core i5-4570",  "Intel Xeon E5-2686", "Intel Xeon P-8175", "AMD FX-8150", "AMD EPYC 7571", "Found in all tested CPUs", "Found in at least one tested CPU" ])
box = ax.get_position()
ax.set_position([box.x0*1.5, box.y0 + box.height * 0.26,
				 box.width, box.height * 0.74])

plt.savefig("gen_figure/vul_by_case_"+sys.argv[1]+"_2.pdf",bbox_inches='tight')
#f3.show()

#plt.tight_layout()
#raw_input()

print("Dot figures are export to gen_figure folder.")








