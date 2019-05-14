import sys 
import re

if len(sys.argv) < 2:
    Exception("No input file given")

filepath = sys.argv[1]

table_list = []

with open(filepath, 'r') as inputfile:
    content = inputfile.read()
    content = content.replace('\n', ' ')
    # print(content)

    match = re.search("CREATE TABLE .* ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;", content)

    match_str = match.string[match.span()[0]:match.span()[1]]

    table_name_list = match_str.split('`')

    table_name_str = table_name_list[1]

    print(match_str)
    print(table_name_str)

    # for line in inputfile:
    #     match = re.search('CREATE TABLE `.*`', line)
    #     if match:
    #         match_str = match.string[match.span()[0]:match.span()[1]]
    #         match_str_list = match_str.split('`')
    #         table_name = match_str_list[1]

    #         table_list.append(table_name)

print(table_list)