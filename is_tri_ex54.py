#This program checks to see if three lenghts can be combined to create a triangle

#aquire in

def get_input():
    len1 = input("First length?: ")
    len2 = input("Second length?: ")
    len3 = input("Third length?: ")
    length_list = []
    length_list.append(len1)
    length_list.append(len2)
    length_list.append(len3)
    print length_list
    return length_list

#begin def
def check_input(list):
    float_list = []
    for x in list:
        if type(x) == int or type(x) == float:
            new_x = float(x)
            float_list.append(new_x)
        else:
            if type(x) == str:
                print "Gimmie Numbers!"
                Check_input(get_input())
            else:
                print "idk what you put in there..."
    return float_list

def is_triangle():
    try:
        input = get_input()
    except:
        print "Gimmie Numbers!"
        input = get_inputs()
    #comment for separation
    fl_list = check_input(input)
    if fl_list[0] >= (fl_list[1] + fl_list[2]):
        print "No bueno, can't triangle"
    elif fl_list[1] >= (fl_list[2] + fl_list[0]):
        print "No bueno, can't triangle"
    elif fl_list[2] >= (fl_list[1] + fl_list[0]):
        print "No bueno, can't triangle"
    else:
        print "I guess...you can triangle?"


#Execution stage
is_triangle()
