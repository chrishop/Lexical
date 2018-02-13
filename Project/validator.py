#Validator.py

# functions to manage validation

def NameValidation(name):
    """takes in a name checks for digit
    if there are no digits in the string
    it returns the name with the first letter capitalised"""
    number = False
    for i in name:
        if i.isdigit() is True:
            number = True
    if number is True:
        return False
    else:
        return name[0].upper() + name[1:len(name)].lower()


def Password(string):
    """checks there are no capital letters and numbers
    returns true if they are all present
    returns false if any of them aren't present"""
    alpha = False
    number = False
    capital = False

    if len(string) > 7 and len(string) < 17:
        for i in string:
            if i.isalpha() is True:
                alpha = True

            if i.isdigit() is True:
                number = True

            if i.isupper() is True:
                capital = True

        if alpha and number and capital is True:
            return True

        else:
            return False
    return False


def check_settings(setting_pack):
    """checks that the setting entry has an index of at least 8
    that each position in the array hold a number
    and that the number is less than 255
    uf all of these are true the function returns true"""
    passed = True
    try:
        setting_pack = setting_pack.split(",")
        test = setting_pack[8]
    except IndexError:
        passed = False

    for i in setting_pack:
        if i.isdigit() == False:
            passed = False
        elif int(i) > 255:
            passed = False
    return passed


def centre(x0pos,y0pos,xlen,ylen):
    """changes the point of reference from the top left hand corner to the center"""
    xpos = (1920/2) - (xlen/2) + x0pos
    ypos = (1010 / 2) - (ylen/ 2) + y0pos
    return xpos,ypos,xlen,ylen
