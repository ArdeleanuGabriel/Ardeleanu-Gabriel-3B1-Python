def function4(tag, content, **dictionar):
    string = "<" + tag
    for cheie in dictionar:
        string = string + cheie + "=\"" + dictionar[cheie] + "\""
    string = string + ">" + content + "</" + tag + ">"
    return string

print( function4 ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))

#string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"