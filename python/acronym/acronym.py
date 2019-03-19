def abbreviate(words):
    str=''
    res1 = words.replace('-', ' ').replace('_', ' ')
    res = res1.split()
    for n in res:

            cap = n[:1].upper()
            str = str+cap

    return str


