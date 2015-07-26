# BUILD ACRONYM DICTIONARY FOR EUCLID APP

import os

LIST_FILE_NAME = 'acronym_list.txt'
DELIMITER = ' = '
FILE_SUFFIX = '_info.txt'

##
# Generate Acronym Dictionary
#
class GenDict():

    ##
    # Initialise GenDict class.
    #
    def __init__(self):
    
        self.check_file(LIST_FILE_NAME)
        
        l_vals = self.read_list_file(LIST_FILE_NAME)
        l_vals.append(self.info_file_search(l_vals[0]))

        self.values = dict(zip(*[l_vals[0], zip(*[l_vals[1], l_vals[2]])]))

    ##
    # Raise exception if file not found.
    # param[in] file_name: Input file name.
    #
    def check_file(self, file_name):

        if not os.path.isfile(file_name):
            raise ValueError('Acronym file [' + file_name + '] not found.')

    ##
    # Read file and return list of lines.
    # param[in] file_name: Input file name.
    #
    def read_list_file(self, file_name):

        return zip(*[line.split(DELIMITER) for line in open(file_name, 'r')])

    ##
    # Look for info files and return list
    # of contents.
    # param[in] a_list: List of acronyms.
    #
    def info_file_search(self, a_list):

        res = []
        
        for value in a_list:
            new_file = value + FILE_SUFFIX
            if os.path.isfile(new_file):
                res.append(self.read_info_file(new_file))
            else:
                res.append('')

        return res
    
    ##
    # Read file and return a single string.
    # param[in] file_name: Input file name.
    #
    def read_info_file(self, file_name):

        return open(file_name, 'r').read()
