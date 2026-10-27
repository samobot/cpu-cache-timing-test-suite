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

# any files input here will be included on the graph, it may need to be made bigger to accomodate more data
files = ["wkst10_gen_v16_recon_fix.output.res.tran",
"srv2_onchip_gen_v17_recon_fix.output.res.tran",
"srv2_interchip_gen_v17_recon_fix.output.res.tran",
"srv1_gen_v16_recon_fix.output.res.tran", 
"wkst5_gen_v16_recon_fix.output.res.tran", 
"broadwell_gen_v16_recon_fix.output.res.tran", 
"skylake_gen_v16_recon_fix.output.res.tran",
"amd_local_gen_v16_recon_fix.output.res.tran",
"amd_amazon_gen_v16_recon_fix.output.res.tran"]

# values for marker type and color, if there are less colors/markers than files they will loop
colors = ["b", "g", "m", "c", "#A1887F", "#99004C", "#FF9933", "#FF80AB", "k"]
markers = ["<", "X", "*", "v", "o", "P", ">", "p", "H"]

# generate the plots
plt.rc('xtick', labelsize=13)
plt.rc('ytick', labelsize=16)
fig1, ax1=plt.subplots()
f1 = plt.figure(1)
f1.set_figheight(5.4)
f1.set_figwidth(28.3)

fig2, ax2=plt.subplots()
f2 = plt.figure(2)
f2.set_figheight(5.4)
f2.set_figwidth(28.3)

fig3, ax3=plt.subplots()
f3 = plt.figure(3)
f3.set_figheight(5.4)
f3.set_figwidth(28.3)

step=0
for index in range(len(files)):
	x = []
	y = []
	y_1 = []
	y_2 = []
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
	x_single = []
	y_single = []
	with open('benchmark_output/'+files[index],'r') as csvfile:
		plots = csv.reader(csvfile, delimiter=' ')
		for row in plots:
			if row==[]:
				grids.append(counter)
				outer_grids.append(outer_counter)
			else:
				if(row==['222']):
					continue
				elif(int(row[0], 2)==2):
					y.append(1+step)
					x.append(counter)
					counter = counter + 1
				else:
					y.append(0+step)
					x.append(counter)
					counter = counter + 1
				outer_x.append(outer_counter)
				outer_counter = outer_counter + 1
	

	for i in range(554):
		y_1.append(y[i])
		x_1.append(x[i])

	for i in range(554, 1094):
		y_2.append(y[i])
		x_2.append(x[i]-554)

	for i in range(vul_num//2):
		x_single_1.append(i+1)
		x_single_2.append(i+vul_num/2+1)
		grids_2.append(grids[i+vul_num//2]-554)

	inner_counter=0
	inner_bound = grids[0]
	for i in range(vul_num):
		x_single.append(i)
		y_single.append(y[inner_counter]-step)
		inner_counter = inner_counter + 1
		if i!=0:
			inner_bound = grids[i] - grids[i-1]
		for j in range(inner_bound-1):
			y_single[i] = y_single[i] or (y[inner_counter]-step)
			inner_counter = inner_counter + 1
		y_single[i] = y_single[i] + step

	x_single_plus=[]
	for i in range(len(x_single)):
		x_single_plus.append(x_single[i] + 1)

	for i in range(len(x_single)):
		if y_single[i]==step:
			y_single[i]=-5

	for i in range(len(x_1)):
		if y_1[i]==step:
			y_1[i]=-5

	for i in range(len(x_2)):
		if y_2[i]==step:
			y_2[i]=-5

	step = step +2

	markerColor = colors[index % len(colors)]
	markerType = markers[index % len(markers)]
	ax1.plot(x_single,y_single, label=files[index], linestyle="",color=markerColor,marker=markerType, markersize=8)
	ax2.plot(x_1,y_1, label=files[index], linestyle="",color=markerColor,marker="o", markersize=2)
	ax3.plot(x_2,y_2, label=files[index], linestyle="",color=markerColor,marker="o", markersize=2)

ax1.set_xlabel('vulnerabilities')
ax1.set_ylabel('CPU Type')
ax1.grid(True, which='major')
ax1.set_xticks(x_single)
ax1.set_ylim([-0.5,22])
ax1.set_xlim([-1,88])
ax1.set_xticklabels(x_single_plus)
ax1.set_yticks([1,3,5,7,9,11,13,15,17,19,21])#1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])
ax1.set_yticklabels(["Intel Xeon E5-1620", "Intel Xeon E5-2667 on-chip", "Intel Xeon E5-2667 inter-chip", "Intel Xeon E5-2690", "Intel Core i5-4570",  "Intel Xeon E5-2686", "Intel Xeon P-8175", "AMD FX-8150", "AMD EPYC 7571", "Found in all tested CPUs", "Found in at least one tested CPU" ])
box = ax1.get_position()
ax1.set_position([box.x0*1.45, box.y0 + box.height * 0.2,
				 box.width, box.height * 0.8])

fig1.savefig("gen_figure/vul_by_type_"+sys.argv[1]+".pdf",bbox_inches='tight')

ax2.set_xlabel('vulnerabilities')
ax2.set_ylabel('CPU Type')
ax2.set_xticks(grids)
ax2.grid(True, which='major', axis='x',linestyle="--")
ax2.set_ylim([-0.2,22])
ax2.set_xlim([-1,554])
# ax.set_xticklabels(x_single_1)
ax2.set_yticks([1,3,5,7,9,11,13,15,17,19,21])
ax2.set_yticklabels(["Intel Xeon E5-1620", "Intel Xeon E5-2667 on-chip", "Intel Xeon E5-2667 inter-chip", "Intel Xeon E5-2690", "Intel Core i5-4570",  "Intel Xeon E5-2686", "Intel Xeon P-8175", "AMD FX-8150", "AMD EPYC 7571", "Found in all tested CPUs", "Found in at least one tested CPU" ])
box = ax2.get_position()
ax2.set_position([box.x0*1.5, box.y0 + box.height * 0.26,
				 box.width, box.height * 0.74])
fig2.savefig("gen_figure/vul_by_case_"+sys.argv[1]+"_1.pdf",bbox_inches='tight')

ax3.set_xlabel('vulnerabilities')
ax3.set_ylabel('CPU Type')
ax3.set_xticks(grids_2)
ax3.grid(True, which='major', axis='x',linestyle="--")
ax3.set_ylim([-0.2,22])
ax3.set_xlim([-1,1094-554])
ax3.set_xticklabels(x_single_2)
ax3.set_yticks([1,3,5,7,9,11,13,15,17,19,21])#1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])
ax3.set_yticklabels(["Intel Xeon E5-1620", "Intel Xeon E5-2667 on-chip", "Intel Xeon E5-2667 inter-chip", "Intel Xeon E5-2690", "Intel Core i5-4570",  "Intel Xeon E5-2686", "Intel Xeon P-8175", "AMD FX-8150", "AMD EPYC 7571", "Found in all tested CPUs", "Found in at least one tested CPU" ])
box = ax3.get_position()
ax3.set_position([box.x0*1.5, box.y0 + box.height * 0.26,
				 box.width, box.height * 0.74])

fig3.savefig("gen_figure/vul_by_case_"+sys.argv[1]+"_2.pdf",bbox_inches='tight')

print("Dot figures are export to gen_figure folder.")
