def string_ext(string, column):
    # Takes a string and adds empty space until last letter is in des. column
    out = list(string)
    for x in out:
        if len(out) < column:
            out.insert(0, ' ')
        else:
            output = ''
            return output.join(out)
