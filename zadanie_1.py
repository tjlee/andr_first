"""
    Function select_case(file_name, n=10)

    n:  count of random strings from file to cuting,
        n is facultative parametr, by default n = 10
        
    file_name:  name of input file with strings

"""

def select_case(file_name, n=10):
    import os.path, random, sys

    if not os.path.isfile(file_name):
        print('Incorrect name of input file, or file does not exist')
        sys.exit()
    # Incorrect n
    if type(n) is not int or n <= 0:
        print('Incorrect n, type must be integer and n > 0')
        sys.exit()
        
    count = 0
    for line in open(file_name).readlines(  ):
        count += 1

    if n > count:
        print('Incorrect n, in select_case(file_name, n) 0 < n <', count)
        sys.exit()
    if n == count:
        if input('Do you want cut all lines from input file?\
                 \nprint yes to cuting or another to exit : ')!= 'yes':
            sys.exit()

    after_cut = []        
    new_file_name = os.path.splitext(file_name)[0] + '_res.txt'    

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
              
"""

    Test cases:

    1)  Count of lines (count) in input file = 12,
        select_case(file_name, n=10) --> cut 10 random lines to output file

    2)  Count = 100, n = 100
        Function request to cut all lines from input to output file

    3)  (n <= 0) or (n > count) or (n not integer)
        Function repot about incorrect value of parametr n

    4)  file_name at select_case(file_name, n=10) incorrect, or does not exist
        Function repot abut incorrect value of parametr

"""
