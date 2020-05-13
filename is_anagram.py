#takes two strings as arguments and returns if they are anagrams of one another

def is_anag(st1, st2):
 if(sorted(st1)== sorted(st2)):
     print("The strings are anagrams.")
 else:
     print("The strings aren't anagrams.")

is_anag("oopa", "opoa")
