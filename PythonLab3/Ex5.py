def function5(s, d):
    for d_key in d:
        for tuplu in s:
            if d_key in tuplu:
                if tuplu[1] != "":
                    if d[d_key].startswith(tuplu[1]) == False:
                        return False
                if tuplu[2] != "":
                    if d[d_key].find(tuplu[2]) == -1:
                        return False
                    if d[d_key].startswith(tuplu[2]) and tuplu[1] != "":
                        return False
                    if d[d_key].endswith(tuplu[2]) and tuplu[3] != "":
                        return False
                if tuplu[3] != "":
                    if d[d_key].endswith(tuplu[3]) == False:
                        return False
            else:
                return False
    return True



s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"}

print(function5(s,d))

