import 
html = urllib.requset.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')
#Retrive all tags
tags = soup('a')
counts = {}
total = 0
for tag in tags:
    text = tag.text.strip()
    #printing all tag infos
    print("TAG:", tag)
    print("URL:", tag.get('href',None))
    print("Contents:", tag.text)
    print("Attrs:", tag.attrs)
    #geting numbers from text
    nums = re.findall(r'[0-9]+', text)
    for num in nums:
        n = int(num)
        counts[n] = counts.get(n, 0) + 1
        total += n
        for k,v in counts.items():
            print(k,"-->", v)
            
print("Sum:", total)
    
    
    