__author__ = 'meganlee'

import re
file = 'apps.html'
infile = open(file, 'r')
infile.seek(0)

link_list = []
while True:
    text = infile.readline()
    if text == '':
        break   # End of file
    else:
        anchor_tag_pattern = ur'<a\b[^<>]*>' # \b means words boundary
        anchor_tag_list = re.findall(anchor_tag_pattern, text)
        for anchor_tag in anchor_tag_list:
            link_pattern = ur'\bhref\s*=\s*"[^"]*"' # consider white spaces such as 'href  =  "http://..."'
            link = re.findall(link_pattern, anchor_tag)[0]
            link = re.sub(ur'\s' ,'', link) # remove all the white spaces
            link = link[6:-1] # remove the 'href="' and the '"'in the end
            if link[:7]=="http://":
                link_list.append(link)

infile.close()
link_list.sort()

i = 0
for e in link_list:
    i = i+1
    print i, e

j = 0
sum = 0
link_set = sorted(set(link_list))
for e in link_set:
    j = j+1
    count = link_list.count(e)
    sum = sum + count
    print j, count, e

print sum, i
