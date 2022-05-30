# stores the key value pairs of the predefined variables in hack
symTab = {"R0": '0', "R1": '1', "R2": '2', "R3": '3', "R4": '4', "R5": '5', "R6": '6', "R7": '7', "R8": '8', "R9": '9',
          "R10": '10', "R11": '11', "R12": '12', "R13": '13', "R14": '14', "R15": '15',
          "SCREEN": '16384',
          "KBD": '24576',
          "SP": '0',
          "LCL": '1',
          "ARG": '2',
          "THIS": '3',
          "THAT": '4',
          "LOOP": '4',
          "STOP": '18',
          "i": '16',
          "sum": '17'
          }


# codes for destination part of the instruction
dest = {'null': '000', 'M': '001', 'D': '010', 'MD': '011', 'A': '100', 'AM': '101', 'AD': '110', 'AMD': '111'}

# codes for computation part of the instruction
comp = {'0': '0101010', '1': '0111111', '-1': '0111010', 'D': '0001100', 'A': '0110000',
        'M': '1110000', '!D': '0001101', '!A': '0110001', '!M': '1110001', '-D': '0001111',
        '-A': '0110011', '-M': '1110011', 'D+1': '0011111', 'A+1': '0110111', 'M+1': '1110111',
        'D-1': '0001110', 'A-1': '0110010', 'M-1': '1110010', 'D+A': '0000010', 'D+M': '1000010',
        'D-A': '0010011', 'D-M': '1010011', 'A-D': '0000111', 'M-D': '1000111', 'D&A': '0000000',
        'D&M': '1000000', 'D|A': '0010101', 'D|M': '1010101'}

# codes for jump part of the instruction
jump = {'null': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011', 'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'}

my_file = open("max/Max.asm", "r")
content = my_file.read()
content_list = content.splitlines()
my_file.close()
new = []
print(content_list)
print(len(content_list))
# comments are filtered out and while spaces are removed
for i in range(len(content_list)):
    print(i)
    if (content_list[i] != ''):
        x=content_list[i].replace(' ', '')
        idx=x.find('//')
        if (idx==-1):
            new.append(x)
        elif (idx!=-1 and x[:idx]!=''):
            new.append(x[:idx])

content_list=new
#print(content_list)

lab = {}
without_lab = []
count = 0

for i in range(len(content_list)):
    if(content_list[i][0] == '('):
        x = content_list[i].find(')')
        s = content_list[i][1:x]
        lab[s] = str(i - count)
        count += 1
    else:
        without_lab.append(content_list[i])

content_list = without_lab
    
final = []



count=16
for i in range(0,len(content_list)):
    if(content_list[i][0]=='@'):
        x1 = content_list[i][1:]
        s = ""
        if(x1 in symTab and x1 in lab):
            s = s + lab[x1]
        elif(x1 in symTab):
            s = s + symTab[x1]
        elif(x1 in lab):
            s = s + lab[x1]
        else:
            symTab[x1] = count
            s = s + str(count)
            count += 1
        s='0' + '{0:015b}'.format(int(s))
        final.append(s)
                  
    elif('=' in content_list[i]):
        a='111'
        y=content_list[i].split("=")
        # if(y[1] in comp):
        a=a+comp[y[1]]
        # if(y[0] in dest):
        a=a+dest[y[0]]
        a = a + "000"
        final.append(a)
        
    elif(';' in content_list[i]):
        y=content_list[i].split(";")    
        # if(y[0] in comp):
        a = "111"
        a=a+comp[y[0]]
        a = a + "000"
        # if(y[1] in jump):
        a=a+jump[y[1]]
        final.append(a)
            
    else:
        print("error")
        break

print(final)

with open("test.hack", "w") as f:
    for i in final:
        f.write(i)
        f.write("\n")
        
    
        
