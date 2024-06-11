#TODO write a description for this script
#@author 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 


#TODO Add User Code Here
# This script was built based on these two resources:
#	https://github.com/NationalSecurityAgency/ghidra/issues/1994
#	https://github.com/NationalSecurityAgency/ghidra/issues/2001
instructionList = []
for instr in currentProgram.getListing().getInstructions(True):
    instructionList.append(instr)
import os, re
os.chdir('C:\\Users\\test\\Desktop\\ghidra_script')

def getSystemCallLable(instruction):
	lable = instruction.getReferencesFrom()

	if len(lable) > 1 and "DLL" in str(lable[1]):
		return str(lable[1])[2:]
	else:
		return None

def replaceAdressWithLable(instruction, lable):
	return re.sub("\[.*\]",'['+ lable +']',instruction)

with open("assembly_out.txt","w") as f:
	for i in instructionList:

		systemCallLable = getSystemCallLable(i)
		if systemCallLable:
			out_line = replaceAdressWithLable(str(i), systemCallLable)
		else:
			out_line = str(i) + "\n"

		f.write(out_line)
