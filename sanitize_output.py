lines_to_sanitize = []
input_filename = "i7_1195G7"

f1 = open("benchmark_output/broadwell_gen_v16_recon_fix.output.res.tran")
f2 = open("benchmark_output/"+input_filename+".output.res")
f2_lines = f2.readlines()
for i, line in enumerate(f1):
    if(line == "222\n"):
        f2_lines[i] = "222\n"
f1.close()
f2.close()
output_file = open("benchmark_output/"+input_filename+".output.res.tran", "w")
output_file.writelines(f2_lines)
output_file.close()