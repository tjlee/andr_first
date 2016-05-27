"""
    Function select_case(file_name, n=10)

    n:  count of random strings from file to cuting,
        n is facultative parametr, by default n = 10
        
    file_name:  name of input file with strings

"""

def select_case(file_name, n=10):
    import os.path, random            

    new_file_name = os.path.splitext(file_name)[0] + '_res.txt'
    after_cut = []

    try:
        # Count of lines in file
        count = 0
        for line in open(file_name).xreadlines(  ):
            count += 1
            
        # Select n random line numbers
        ch = random.sample(range(count), n)

        # Write n random lines to new file
        # Use ch as list of number lines
        with open(new_file_name, 'w') as cut:
            with open(file_name) as until_cut:
                for i,line in enumerate(until_cut):
                    if i in ch:
                        cut.write(line)
                    else:
                        after_cut.append(line)
        with open(file_name, 'w') as f:
            f.writelines(after_cut)

        print (os.path.abspath(new_file_name))
              
    # Except case, when user attempts cut more lines,
    # than is contained in the file.
    except ValueError:
        print('Count of lines in '+file_name+' = '+str(count)+
              "\nselect_case('all_pairs.txt', n),"+
              "here parametr n must be less than : "+
              str(count)
              )
"""

Test at all_pairs.txt consist of:

    case One Book Low Book Rating Product Date pairings
    5 Hd | STB/Other LT | ST POL Rating L|C|C LM 5
    9 Hd LT GTD Rati	ng L|C|C LM 1
    7 All All GTD Rating L|C|C | Index LM 3
    10 Hd | STB/Other | TTd LT | ST POL Rating L|C|C Expected 1
    4 Hd | TTd LT POL Rating L|C|C Expected 5
    2 Hd | STB/Other LT | ST POL Rating L|C|C LM 5
    3 Hd LT GTD Ra	ting L|C|C LM 1
    1 All All GTD Rating L|C|C | Index LM 3
    8 Hd | STB/Other | TT	d LT | ST POL Rating L|C|C Expected 1
    11 Hd | TTd LT POL Rating L|C|C Expected 5
    case One Book Low Book Rating Product Date pairings
    5 Hd | STB/Other LT | ST POL Rating L|C|C LM 5
    9 Hd LT 	GTD Rating L|C|C LM 1
    7 All All GTD Rating L|C|C | Index LM 3
    10 Hd | STB/Other | TTd LT | ST POL Rating L|C|C Expected 1
    4 Hd | TTd LT POL Rating L|C|C Expected 5
    2 Hd | STB/Other LT | ST POL Rating L|C|C LM 5
    3 Hd LT GTD Rat	ing L|C|C LM 1	
    1 All All GTD Rating L|C|C | Index LM 3
    8 Hd | STB/Other | TTd LT | ST POL Rating L|C|C Expected 1
    11 Hd | TTd LT POL Rating L|C|C Expected 5

    >>> select_case('all_pairs.txt')
    C:\Users\ProninA\andr_first\all_pairs_res.txt

Result at all_pairs_res.txt

    5 Hd | STB/Other LT | ST POL Rating L|C|C LM 5
    7 All All GTD Rating L|C|C | Index LM 3
    3 Hd LT GTD Ra	ting L|C|C LM 1
    11 Hd | TTd LT POL Rating L|C|C Expected 5
    case One Book Low Book Rating Product Date pairings
    9 Hd LT 	GTD Rating L|C|C LM 1
    7 All All GTD Rating L|C|C | Index LM 3
    2 Hd | STB/Other LT | ST POL Rating L|C|C LM 5
    1 All All GTD Rating L|C|C | Index LM 3
    8 Hd | STB/Other | TTd LT | ST POL Rating L|C|C Expected 1



"""
    
