# Salwa A. Majeed
#This programs finds to whom a sequence of all 20 DNA sequences belongs. This program goes through all 20 files to identify which file matches which individual best. 


def counts(sequence, str_list):         #counts occurences of str in dna seq
    str_counts = []
    for STR in str_list:
        str_counts.append(longest_run_count(sequence, STR))
    return str_counts

def longest_run_count(sequence, STR):  
    str_length = len(STR)
    i = 0
    max_run = 0                         #tracks max number of consectutive repeats
    running_now = 0                     #tracks current run 
    while i < len(sequence):
        if sequence[i:i + str_length] == STR:
            running_now += 1                        # If a match is found, increment the current run count
            i += str_length                         #Move to the next set of letters
        else:
            max_run = max(max_run, running_now)     # Update the maximum run if the current run is larger.
            running_now = 0                         # Reset the current run count
            i += 1                                  # Move the index forward by one position in the DNA sequence
    return max(max_run, running_now)

def is_match(nameandinfo, str_counts):
    for row in nameandinfo[1:]:            # Iterate through the rows in the nameandinfo list starting from the second row (index 1)
        list = row.split(',')
        name = list[0]                      #Get name
        dna_counts = [int(value) for value in list[1:]]
        if dna_counts == str_counts:
            return name
    return "No Match."



#filenum = int(input("Enter number (1-20): "))
for filenum in range(1, 21):                        #reads each file
    file = open(str(filenum) + '.txt')
    sequence = file.read()
    file.close()

    if 1 <= filenum <= 4:
        file = open("small.txt")
    else:
        file = open("large.txt")
    nameandinfo = file.read()
    file.close()

    nameandinfo = nameandinfo.split('\n')
    nameandinfo.pop(-1)

    str_list = (nameandinfo[0].split(','))[1:] #Take out the STR list

    counts_str = counts(sequence, str_list)

    answer = is_match(nameandinfo, counts_str)
    print(f'Dna Sequence #{filenum} matches: {answer}')
