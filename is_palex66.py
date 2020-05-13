#takes a string and returns True if the string is a Palindrom and False if otherwise

#Requests Input
string = str(raw_input("Palin-whosits-whatsits? (Word Please): "))

#define func
def is_pal(string):
    length = len(string)
    if length % 2 == 0: #check to see if it has an even number of letters
        half_len = (length/2)
        print "-logistical stuff-"
        print string[:half_len]
        second_half = string[-half_len:]
        rev_half = second_half[::-1]
        print rev_half
        print "--end logics--"
        if string[:half_len] == rev_half:
            print "You got yourself a palindrome, broh!"
        elif string[:half_len] != rev_half:
            print "No cigar buddy, not palindrome"
        else:
            print "OOOOoofda, big error somewhere"
    elif length % 2 != 0:
        middle_letter = (length - 1) / 2
        other_letters = middle_letter
        print "-logistical stuff-"
        print string[:other_letters]
        print "Middle letter: ", string[middle_letter]
        second_part = string[-other_letters:]
        rev_secpart = second_part[::-1]
        print rev_secpart
        print "--end logics--"
        if string[:other_letters] == rev_secpart:
            print "You got yourself a palindrome, broh!"
        elif string[:other_letters] != rev_secpart:
            print "No cigar buddy, not palindrome"
        else:
            print "OOOOoofda, big error somewhere"
    else:
        print "something is wrong with conditions"


#execution
is_pal(string)
