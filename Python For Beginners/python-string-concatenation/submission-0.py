def concatenate(s1: str, s2: str) -> str:
    added = s1 + s2
    if len(added) > 10:
        return "Too long!"
    else: return added
    




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
