""" iACL """
__author__ = "Du'An Lightfoot"
__email__ = "duanl@labeveryday.com"

from acl_tool.iacl import iACL


# Main function to call iACL
def main(options, iacl):
    if options == 1:
        print(f"There are {iacl.count_acl_lines()} ACL lines")
    if options == 2:
        print(f"ACL Comparision Results:\n{iacl.count_acl_lines()} ACL lines")
    if options == 3:
        print()

# Execute script
if __name__ == "__main__":
    device_acl = open("device_acl.txt", "r").readlines()
    match_check = open("match_check_acl.txt", "r").readlines()
    options = int(input("""
    --------Welcome to the ACL Comparision Script--------
    1. Count ACL Lines
    2. Compare ACL Files
    3. Both
    Enter a selection: """))
    iacl = iACL(device_acl, match_check)
    main(options, iacl)
