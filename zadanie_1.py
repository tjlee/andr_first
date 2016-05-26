"""
    Function select_case(file_name, n=10)

    n:  count of random strings from file to cuting,
        n is facultative parametr, by default n = 10
        
    file_name:  name of input file with strings

"""

def select_case(file_name, n=10):
    import os.path, random            

    new_file_name = os.path.splitext(file_name)[0] + '_res.txt'
    s = []

    try:
        # Count of lines in file
        count = 0
        for line in open(file_name).xreadlines(  ):
            count += 1
            
        # Select n random line numbers
        ch = random.sample(range(count), n)

        # Write n random lines to new file
        # Use ch as list of number lines
        with open(new_file_name, 'w') as g:
            with open(file_name) as f:
                for i,line in enumerate(f):
                    if i in ch:
                        g.write(line)
                    else:
                        s.append(line)
        with open(file_name, 'w') as f:
            f.writelines(s)

        print('Complete! Look selection in:\n'+
              os.path.abspath(new_file_name)
              )

    # Except case, when user attempts cut more lines,
    # than is contained in the file.
    except ValueError:
        print('Count of lines in '+file_name+' = '+str(count)+
              "\nselect_case('all_pairs.txt', n),"+
              "here parametr n must be less than : "+
              str(count)
              )

    
