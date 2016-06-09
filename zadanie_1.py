"""
    Function select_case(file_name, n=10)

    n:  count of random strings from file to cuting,
        n is facultative parametr, by default n = 10
        
    file_name:  name of input file with strings

"""

def select_case(file_name, n=10):
    import os.path, random, sys
    
    # Check input file
    if not os.path.isfile(file_name):
        sys.exit()
    # Check n
    if type(n) is not int or n < 0:
        sys.exit()

    new_file_name = os.path.splitext(file_name)[0] + '_res.txt'
    
    if n == 0:
        open(new_file_name, 'w').close()
        print (os.path.abspath(new_file_name))
        sys.exit()
        
    count = 0    # count of lines in input file
    for line in open(file_name).xreadlines():
        count += 1

    if n > count:
        sys.exit()

    after_cut = []          

    # Select n random line numbers
    ch = random.sample(range(count), n)

    # Write n random lines to output file
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
              
"""

    Test cases:

    1)  Count of lines (count) in input file = 12,
        select_case(file_name, n=10) --> cut 10 random lines to output file

    2)  Count = 100, n = 100
        Function cut all lines from input to output file

    3)  (n < 0) or (n > count) or (n not integer)
        Function stops working before opening input file to cuting, output file is not created

    4)  file_name at select_case(file_name, n=10) incorrect, or does not exist
        Function stops working before opening input file to cuting, output file is not created

    5)  n = 0
        Function creates an empty output file and stops before opening input file to cuting

"""
