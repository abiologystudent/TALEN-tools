


##########
##  TALEN checker v1.0
##########

import string


def welcome():
        x = raw_input("This is talenchecker v1.0. For sequence analysis of potential TALEN array type 'S', for correct sequence of a known array of repeats type 'R', for information about a specific repeat/plasmid type 'I' - ")
        str(x)
        global answer
        answer = []
        if x == 's' or x == 'S':
            analyse_sequence()
        elif x == 'r' or x == 'R':
            give_sequence() 
        elif x == 'I' or x == 'i':
            info()
        else:
            print "That's an unhelpful input."
        return

global answer
answer = []

def info():
    x = raw_input("Type repeat, eg HD1, for info. ")
    str(x)
    x.display()
    

def give_sequence():
    y = raw_input("Paste in array repeats in the format NG, NK, HD etc - ")
   
    fasta = y + " >"
    count = 1
    repeatlist = map(str.strip, y.split(','))
    for repeat in repeatlist:
        position = string.upper(repeat) + str(count)
        count += 1
        fasta += repeat_dictionary[position]
    print fasta

  

def analyse_sequence():
        global answer
        x = raw_input("Paste in sequence data of array - ")
        there = "Repeats present - "
        nay_there = "Repeats not present - "
        sequence = ">"
        rvdlist = ['HD', 'NI', 'NN', 'NG', 'NK']
        onereplist = []
        for rep in rvdlist:
                count = 0
                while count < 10:
                        count += 1
                        label = [(str(rep)+str(count))]
                        sequence = repeat_dictionary[(str(rep)+str(count))]   #up to here just fetches bits of sequence for each repeat
                        if sequence in x:
                                onereplist = onereplist + [label]
                                a = add_another(label, sequence, x)
                                
                                
        print                        
        print answer, " - this is the longest list of repeats in your sequence."
        print
        print                      
        print "List of single repeats that are in your sequence (no particular order) - ", onereplist

def count(x, y):
        if x in y:
                return 1

def add_another(label, previoussequence, x, twoormorelist=[]):

        global answer

        rvdlist = ['NK', 'NI', 'NN', 'NG', 'HD']
        for rep in rvdlist:
                count = 0
                while count < 10:
                        count += 1
                        #if twormorelist == []:
                         #       cnt = 0
                          #      cnt += count(previoussequence, x)
                                
                                
                        combreps = previoussequence + repeat_dictionary[(str(rep)+str(count))]
                        it_there = x.find(combreps)   #searches for first X1Y2 repeat, Y2 repeat is random so if finds sequence after other possible seq, does not continue searching/passing first seq to function
                        if it_there > -1:
                            print it_there, "this is where following begins -", (str(rep)+str(count))
                        if it_there > -1:
                                add_another(label, previoussequence, x[it_there+1:], twoormorelist)
                                labelnext = [(str(rep)+str(count))]
                                twoormorelist = twoormorelist[:len(twoormorelist)-1] + label + labelnext
                                add_another(labelnext, combreps, x, twoormorelist)
                                if len(answer) < len(twoormorelist):
                                        answer = twoormorelist
                                        print answer, "- these repeats are sequentially in your sequence"       
                                return twoormorelist

        

                                
        
def get_complement(x):
        complement_fasta = "complement> "
        for char in x:
                if char == "A":
                        complement_fasta += "T"
                if char == "T":
                        complement_fasta += "A"
                if char == "C":
                        complement_fasta += "G"
                if char == "G":
                        complement_fasta += "C"
        return complement_fasta
                        
def get_reverse(x):
        count = 0
        reverse_fasta = "Reverse >"
        while count <= len(x):
                y = len(x)-count
                reverse_fasta += x[y-1:y]
                count +=1
        return reverse_fasta  

class Repeat:

    def __init__(self, name, seq, RVD, link1=0, link2=0):
        self.repeat = name
        self.sequence = seq
        self.repvardom = RVD
        self.fivelink = link1
        self.threelink = link2

    def display(self):
        print self.repeat
        print self.sequence
        print self.repvardom


HD1seq = "ctatcgccagccacgatggcggcaagcaagcgctcgaaacggtgcagcggctgttgccggtgctgtgccaggac"
HD2seq = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
HD3seq = "ggaccatggcctgactccggaccaagtggtggctatcgccagccacgatggcggcaagcaagcgctcgaaacggtgcagcggctgttgccggtgctgtg"
HD4seq = "ccaggaccatggcctgactccggaccaagtggtggctatcgccagccacgatggcggcaagcaagcgctcgaaacggtgcagcggc"
HD5seq = "tgttgccggtgctgtgccaggaccatggcctgactccggaccaagtggtggctatcgccagccacgatggcggcaagcaagcgctcgaaacgg"
HD6seq = "Tgcagcggctgttgccggtgctgtgccaggaccatggcctgactccggaccaagtggtggctatcgccagccacgatggcggcaagcaagcgctcgaaa"
HD7seq = "cggtgcagcggctgttgccggtgctgtgccaggaccatggcctgactccggaccaagtggtggctatcgccagccacgatggcggcaagcaagcgctc"
HD8seq = "gaaacggtgcagcggctgttgccggtgctgtgccaggaccatggcctgactccggaccaagtggtggctatcgccagccacgatggcggcaagcaagcgc"
HD9seq = "tcgaaacggtgcagcggctgttgccggtgctgtgccaggaccatggcctgactccggaccaagtggtggctatcgccagccacgatggcggcaagcaagc"
HD10seq = "gctcgaaacggtgcagcggctgttgccggtgctgtgccaggaccatggcctgactccggaccaagtggtggctatcgccagccacgat"

NI1seq = "ctatcgccagcaacattggcggcaagcaagcgctcgaaacggtgcagcggctgttgccggtgctgtgccaggac"
NI2seq = "catggcctgaccccggaccaagtggtggctatcgccagcaacattggcggcaagcaagcgctcgaaacggtgcagcggctgttgccggtgctgtgcca"
NI3seq = "ggaccatggcctgaccccggaccaagtggtggctatcgccagcaacattggcggcaagcaagcgctcgaaacggtgcagcggctgttgccggtgctgtg"
NI4seq = "ccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacattggcggcaagcaagcgctcgaaacggtgcagcggc"
NI5seq = "tgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacattggcggcaagcaagcgctcgaaacgg"
NI6seq = "tgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacattggcggcaagcaagcgctcgaaa"
NI7seq = "cggtgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacattggcggcaagcaagcgctc"
NI8seq = "gaaacggtgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacattggcggcaagcaagcgc"
NI9seq = "tcgaaacggtgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacattggcggcaagcaagc"
NI10seq = "gctcgaaacggtgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacatt"

NN1seq = "ctatcgccagcaacaatggcggcaagcaagcgctcgaaacggtgcagcggctgttgccggtgctgtgccaggac"
NN2seq = "catggcctgaccccggaccaagtggtggctatcgccagcaacaatggcggcaagcaagcgctcgaaacggtgcagcggctgttgccggtgctgtgcca"
NN3seq = "ggaccatggcctgaccccggaccaagtggtggctatcgccagcaacaatggcggcaagcaagcgctcgaaacggtgcagcggctgttgccggtgctgtg"  #it is likely this is wrong
NN4seq = "ccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacaatggcggcaagcaagcgctcgaaacggtgcagcggc"
NN5seq = "tgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacaatggcggcaagcaagcgctcgaaacgg"
NN6seq = "tgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacaatggcggcaagcaagcgctcgaaa"
NN7seq = "cggtgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacaatggcggcaagcaagcgctc"
NN8seq = "gaaacggtgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacaatggcggcaagcaagcgc"
NN9seq = "tcgaaacggtgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacaatggcggcaagcaagc"
NN10seq = "gctcgaaacggtgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacaat"

NK1seq = "ctatcgccagcaacaagggcggcaagcaagcgctcgaaacggtgcagcggctgttgccggtgctgtgccaggac"
NK2seq = "catggcctgaccccggaccaagtggtggctatcgccagcaacaagggcggcaagcaagcgctcgaaacggtgcagcggctgttgccggtgctgtgcca"
NK3seq = "ggaccatggcctgaccccggaccaagtggtggctatcgccagcaacaagggcggcaagcaagcgctcgaaacggtgcagcggctgttgccggtgctgtg"
NK4seq = "ccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacaagggcggcaagcaagcgctcgaaacggtgcagcggc"
NK5seq = "tgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacaagggcggcaagcaagcgctcgaaacgg"
NK6seq = "tgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacaagggcggcaagcaagcgctcgaaa"
NK7seq = "cggtgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacaagggcggcaagcaagcgctc"
NK8seq = "gaaacggtgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacaagggcggcaagcaagcgc"
NK9seq = "tcgaaacggtgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacaagggcggcaagcaagc"
NK10seq = "gctcgaaacggtgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacaag"

NG1seq = "ctatcgccagcaacggtggcggcaagcaagcgctcgaaacggtgcagcggctgttgccggtgctgtgccaggac"
NG2seq = "catggcctgaccccggaccaagtggtggctatcgccagcaacggtggcggcaagcaagcgctcgaaacggtgcagcggctgttgccggtgctgtgcca"
NG3seq = "ggaccatggcctgaccccggaccaagtggtggctatcgccagcaacggtggcggcaagcaagcgctcgaaacggtgcagcggctgttgccggtgctgtg" #as is this
NG4seq = "ccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacggtggcggcaagcaagcgctcgaaacggtgcagcggc"
NG5seq = "tgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacggtggcggcaagcaagcgctcgaaacgg"
NG6seq = "tgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacggtggcggcaagcaagcgctcgaaa"
NG7seq = "cggtgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacggtggcggcaagcaagcgctc"
NG8seq = "gaaacggtgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacggtggcggcaagcaagcgc"
NG9seq = "tcgaaacggtgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacggtggcggcaagcaagc"
NG10seq = "gctcgaaacggtgcagcggctgttgccggtgctgtgccaggaccatggcctgaccccggaccaagtggtggctatcgccagcaacggt"




#repeat_dictionary = {'HD1': HD1seq, 'HD2':, 'HD3': HD3seq, 'HD4': HD4seq, 'HD6': HD6seq, 'NI2': NI2seq}

repeat_dictionary = {'HD1':HD1seq,'HD2':HD2seq,'HD3':HD3seq,'HD4':HD4seq,'HD5':HD5seq,'HD6':HD6seq,'HD7':HD7seq,'HD8':HD8seq,'HD9':HD9seq,'HD10':HD10seq,
                     'NG1':NG1seq,'NG2':NG2seq,'NG3':NG3seq,'NG4':NG4seq,'NG5':NG5seq,'NG6':NG6seq,'NG7':NG7seq,'NG8':NG8seq,'NG9':NG9seq,'NG10':NG10seq,'NK1':NK1seq,'NK2':NK2seq,'NK3':NK3seq,'NK4':NK4seq,'NK5':NK5seq,'NK6':NK6seq,'NK7':NK7seq,'NK8':NK8seq,'NK9':NK9seq,'NK10':NK10seq,'NI1':NI1seq,'NI2':NI2seq,'NI3':NI3seq,'NI4':NI4seq,'NI5':NI5seq,'NI6':NI6seq,'NI7':NI7seq,'NI8':NI8seq,'NI9':NI9seq,'NI10':NI10seq,'NN1':NN1seq,'NN2':NN2seq,'NN3':NN3seq,'NN4':NN4seq,'NN5':NN5seq,'NN6':NN6seq,'NN7':NN7seq,'NN8':NN8seq,'NN9':NN9seq,'NN10':NN10seq}


a = Repeat("pNN2", NN2seq, "cat")
b = Repeat("pNG2", NG2seq, "tat")
HD1 = Repeat("pHD1", HD1seq, "should do this sometime")

#fix these...
welcome()
print
welcome()
print
welcome()
print
welcome()
print
welcome()
print


##for r in repeat_dictionary:
##                #goes through dictionary and finds if repeat  is in sequence data
##                if repeat_dictionary[r] in x:
##                       # print r, " is in your sequence."
##                        there += r
##                        str(r)
##                        z = r[2:3]
##                        q = int(z)+1
##                        rvdlist = ['HD', 'NI', 'NN', 'NG', 'NK']
##                        for element in rvdlist:
##                                
##                               # print repeat_dictionary[r] + repeat_dictionary[(str(element) + str(q))]
##                            a = (str(element) + str(q)) 
##                            if repeat_dictionary[r] + repeat_dictionary[a] in x:
##                                    #checks if the first element plus any of the elements in rvdlist are in sequence data
##                               # print r, (str(element) + str(q)), "is sequentially in sequence"
##                                for element2 in rvdlist:
##                                    if repeat_dictionary[r] + repeat_dictionary[a] + repeat_dictionary[(str(element2) + str(q + 1))] in x:
##                                        print r, " ", a, " ", (str(element2) + str(q + 1)), "are sequentially in sequence."
##                                        for element3 in rvdlist:
##                                            c = (str(element2) + str(q + 1))
##                                            if repeat_dictionary[r] + repeat_dictionary[a] + repeat_dictionary[c] + repeat_dictionary[(str(element3) + str(q + 2))] in x:
##                                                    print r, a, c, (str(element3) + str(q + 2)), "these things are in a row"
##                                                    maybeend = repeat_dictionary[r] + repeat_dictionary[a] + repeat_dictionary[c] + repeat_dictionary[(str(element3) + str(q + 2))]
##                                                                                                        
