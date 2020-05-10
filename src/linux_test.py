import modelsim
import pathlib
import subprocess

p = pathlib.Path("/home/ff/intelFPGA_lite/18.1/modelsim_ase/linuxaloem/")

	# a = subprocess.Popen([p  / 'vlib', "work"],
	# 			universal_newlines=True,
	# 			stdout=subprocess.PIPE)

	# data_a = " "
	# while not (not( data_a )):
	# 	data_a = a.stdout.readline()
	# 	print(data_a)

	# b = subprocess.Popen([p  / 'vmap', "work", "work"],
	# 			universal_newlines=True,
	# 			stdout=subprocess.PIPE)

	# data_b = " "
	# while not (not( data_b )):
	# 	data_b = b.stdout.readline()
	# 	print(data_b)


	# c = subprocess.Popen([p  / 'vlog', '*.v'],
	# 			universal_newlines=True,
	# 			stdout=subprocess.PIPE)

	# data_c = " "
	# while not (not( data_c )):
	# 	data_c = c.stdout.readline()
	# 	print(data_c,end='')



print("HERE 1")
d = subprocess.Popen([p  / 'vsim','work.MyProject'],
			universal_newlines=True,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			stdin=subprocess.PIPE,
			shell=False)
print("HERE 2")

d.stdin.flush()

dat = " "
while 1:
	dat = d.stdout.readline()
	print(dat)

print("HERE 3")
d.stdin.write("transcript file \"\"\r\n")
d.stdin.flush()
print("HERE 4")
data_d = " "



print("HERE 5")


# print("HERE 4")

# d.stdin.write("transcript file \"\"\n")
# d.stdin.flush()


# data_d = " "
# while not ((data_d == '') | (data_d == '>')):
# 	data_d = d.stdout.read(1)
# 	print(data_d,end="")
