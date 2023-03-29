def to_camel_case(s):
    if len(s)==0:
        return ""
    a = s[0]
    if "_" in s and "-" in s:
        s = s.replace("-", " ")
        s = s.replace("_", " ")
        s = s.title().replace(" ", "")
        if a.isupper():
            return s[0].upper()+s[1:]
        if a.islower():
            return s[0].lower()+s[1:]
    if "_" in s and "-" not in s:
        s = s.replace("_", " ")
        s = s.title().replace(" ", "")
        if a.isupper():
            return s[0].upper()+s[1:]
        if a.islower():
            return s[0].lower()+s[1:]

    if "_" not in s and "-" in s:
        s = s.replace("-", " ")
        s = s.title().replace(" ", "")
        if a.isupper():
            return s[0].upper()+s[1:]
        if a.islower():
            return s[0].lower()+s[1:]
