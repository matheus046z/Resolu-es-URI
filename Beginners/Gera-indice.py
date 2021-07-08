import glob

files = glob.glob('/home/Matheus/Documentos/VS_Clone/URI_Problems-Solved/Beginners/Python/*.py')

i = 0
cortastr = []
numera = []

for i in range(len(files)):
    cortastr.append(files[i][-28:])

for i in range(len(cortastr)):
    numera.append(cortastr[i][17:25])

for i in range(len(files)):
    print("["+numera[i]+"]("+cortastr[i]+")\n")
