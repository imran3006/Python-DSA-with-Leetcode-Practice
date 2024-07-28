# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

class Solution:
    def defangIPaddr(address):
        return address.replace(".", "[.]")
    
    print(defangIPaddr("1.1.1.1"))
