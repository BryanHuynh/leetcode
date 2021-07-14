from typing import List


def numUniqueEmails(emails: List[str]) -> int:
    ret = []
    for i in range(len(emails)):
        atindex = emails[i].index("@")
        domain = emails[i][atindex:]
        local = emails[i][:atindex]
        local = local.replace(".", '')

        plusIndex = local.find("+")
        if(plusIndex != -1):
            #print('found at:', plusIndex)
            local = local[:plusIndex]
            
        #print("local: {} \ndomain: {}".format(local, domain))
        ret.append(local+domain)

    ret = set(ret)
    return len(ret)
        
if __name__ == '__main__':
    print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))