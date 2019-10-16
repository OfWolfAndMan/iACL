

class iACL(object):
    def __init__(self, device_acl, match_check):
        self.acl_strip = []
        self.result_list = []
        self.no_match_list = []
        self.number_of_acls = 0
        self.match_check = match_check
        self.device_acl = device_acl
    
    # Add ACLs in device_acl to a list
    def create_acl_list(self):
        for line in self.device_acl:
            self.acl_strip.append(line.lstrip(' '))
        return self.acl_strip

    # Returns the number of lines in a ACL_file
    def count_acl_lines(self):
        return len(self.create_acl_list())
    
    # Compares device_acl.txt and match_check_acl.txt
    # Returns valid matches as list
    def compare_acl(self):
        for line in self.match_check:
            if line in self.create_acl_list():
                self.result_list.append(line)
        if len(self.result_list) > 0:
            result = list(set(self.result_list))
        else:
            result = "No ACL conflicts found!"
        return result

    # Returns a list of ACLs with HitCounts
    def acl_hitcnt(self):
        for line in self.create_acl_list():
            if "matches" in line:
                self.result_list.append(line)
            elif "hitcnt=" in line:
                if "hitcnt=0" in line:
                    pass
                else:
                    self.result_list.append(line)
        return self.result_list

    # Displays the total number acl lines, number of hits, and lines without hits
    def number_of_acl_matches(self):
        number_of_matches = 0
        if len(self.acl_hitcnt()) > 0:
            for line in self.acl_hitcnt():
                number_of_matches += 1
        else:
            pass
        acl_difference = self.count_acl_lines() - number_of_matches
        return f"There were {self.count_acl_lines()} total acls \
                \n- {number_of_matches} Total HITS\n - {acl_difference} \
                without hits."

    # Returns a list of ACLs lines that have no hits
    def no_hits_ACL(self):
        for line in self.create_acl_list():
            if line not in self.acl_hitcnt():
                self.no_hits_ACL.append(line)
        return self.no_hits_ACL
