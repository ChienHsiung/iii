
# coding: utf-8

# ## Comment

# In[5]:


# I am a comment
"""
this can also be used as a comment
multi line comment
"""


# ## Print

# In[1]:


print("hello world") # print "hello world"


# In[2]:


print(123)


# ## String

# In[3]:


"hello" # string


# In[6]:


'hello again' # string


# In[4]:


"""hello
again
and
agian""" # multi line string


# In[7]:


type("hello")


# ## Integer

# In[8]:


123 # int


# In[10]:


456 # int


# In[11]:


-1 # int


# In[12]:


type(100)


# ## Float

# In[13]:


3.14 # float


# In[14]:


type(3.14)


# ## Boolean

# In[15]:


True


# In[16]:


False


# ##### Truthy

# In[17]:


123


# In[21]:


"hello"


# #### Falsy

# In[18]:


0


# In[19]:


""


# ## Algebra

# In[22]:


1 + 1


# In[23]:


2 - 1


# In[24]:


2 * 2


# In[25]:


3 / 2


# In[28]:


2**3


# In[30]:


10 % 3 # mod


# ### Boolean operations

# In[7]:


True and False


# In[8]:


True or False


# In[31]:


True == True


# In[32]:


True == False


# In[33]:


3 > 1


# In[9]:


1 >= 3


# In[35]:


True != False


# In[36]:


True is False


# In[37]:


True is True


# In[38]:


not True is False # Python only feature!


# In[39]:


"a" is "A"


# In[41]:


"a" is "a"


# In[50]:


# negative number is also truthy
if -1:
    print("OK")


# ## Variables

# In[46]:


a123 = '1'


# In[48]:


1aa = 1


# In[51]:


x = 'my name'


# In[52]:


x


# ## Conditional

# In[54]:


if 1:
    print("hi")


# In[56]:


if 3 > 1:
    pass


# In[57]:


x = 1
if x > 3:
    print("grater than 3")
else:
    print("small int")


# In[59]:


x = 3
if x > 3:
    print("grater than 3")
elif x > 2:
    print("grater than 2")
else:
    print("small int")


# ## Collections

# In[10]:


"hello"


# In[11]:


"Hello"[1]


# In[12]:


"Hello"[-1]


# In[13]:


"Hello"[1:3]


# In[18]:


"Hello"[1:6:3] # [start:end:step]


# In[19]:


len("hello")


# In[21]:


"hello" + " " + "world" # concatenation


# In[25]:


"3d printer is " + 199 + " dollars" # String can only concatenate with strings


# In[ ]:


"3d printer is " + "199" + " dollars"


# In[26]:


"3d printer is {} dollars".format(199)


# In[32]:


# Code can be broken into multiple lines with \
"{item} is {price} dollars in {country},{country} is the most expensive".format(item="Tesla",
        country="Taiwan",
        price=500000000)


# In[27]:


"3d printer is %s dollars"%199


# In[33]:


# use case
# blah blah code
my_buggy_var = 123
print("[DEBUG] my_buggy_var is %s"%my_buggy_var)
# my code continues....


# ## List

# In[35]:


li = []


# In[36]:


li


# In[38]:


# insert in to list
li.append("3d printer")


# In[39]:


li


# In[40]:


li.append("cnc machine")


# In[41]:


li


# In[42]:


li.pop()


# In[43]:


li


# In[44]:


li[0]


# In[45]:


li.append("python")


# In[47]:


li.append("ruby")


# In[48]:


li


# In[50]:


li[1:]


# In[52]:


li[:2]


# In[53]:


li[::2]


# In[54]:


li[::-1]


# In[55]:


del li[1]


# In[56]:


li


# In[57]:


li.insert(1, "python")


# In[58]:


li


# In[59]:


["3d printer"] + ["cnc machine"]


# In[60]:


li


# In[63]:


"3d printer" in li


# In[64]:


if "3d printer" in li:
    print("I have a 3d printer")


# ## Dictionary

# In[78]:


mydict = {}


# In[79]:


type(mydict)


# In[80]:


mydict


# In[81]:


mydict['name'] = "Ian"


# In[82]:


mydict


# In[112]:


printer = {
    "name": "Prusa i3 mk2",
    "print speed": 100,
    "country": "USA",
    "features": ["laser cutting", "3d printing", "cnc milling"],
    "price": 300
}


# In[84]:


printer


# In[85]:


# lookup
printer['name']


# In[86]:


# lookup
printer['country']


# In[88]:


# create
printer['dimensions'] = [220, 220, 240]


# In[89]:


printer


# In[90]:


# update
printer['country'] = "Taiwan"


# In[91]:


printer


# In[92]:


# delete
del printer['price']


# In[93]:


printer


# In[94]:


# look up keys in dict
"name" in printer


# In[96]:


# cannot lookup values
'Prusa i3 mk2' in printer


# In[98]:


# Dealing with missing keys
printer['country']


# In[113]:


printer2 = {'dimensions': [220, 220, 240],
 'features': ['laser cutting', '3d printing', 'cnc milling'],
 'name': 'Prusa i3 mk2',
 'print speed': 100}


# In[114]:


printer2


# In[116]:


del printer2['features']


# In[117]:


printer2


# In[118]:


printer2['features']


# In[119]:


# Graceful dictionary indexing
printer.get("features")


# In[121]:


printer2.get("features") # returns None


# In[123]:


printer2.get("features", "N/A") # returns default value


# ## Tuple

# In[161]:


first_last = ('Ian', 'Chen')
first_last


# In[162]:


first_last[0]


# In[163]:


first_last[1]


# In[164]:


first_last[1] = "Lin"


# ## Set

# In[124]:


myset = set()


# In[125]:


myset.add(5)


# In[126]:


myset


# In[127]:


myset.add(1)


# In[128]:


myset


# In[129]:


myset.add(5)


# In[130]:


myset


# In[131]:


{1,2,3,4} - {3,4,5} # difference


# In[132]:


{1,2,3,4} ^ {3,4,5} # symmetric diff


# In[133]:


{1,2,3,4} & {3,4,5} # intersection


# In[134]:


{1,2,3,4} | {3,4,5} # union


# ## For loops

# In[136]:


for feature in ["3d printing", "cnc milling", "laser cutting"]:
    print("It is feature %s"%feature)


# In[137]:


for i in range(4):
    print(i)


# In[138]:


for i in range(0,4):
    print(i)


# In[139]:


for i in range(1,4):
    print(i)


# In[144]:


range(4)


# In[142]:


type(range(4))


# In[146]:


x = 0
while x < 4:
    print(x)
    x += 1 # x = x + 1


# In[147]:


x = 0
while True:
    if x > 3:
        break
    print(x)
    x += 1


# In[152]:


# Simple retry mechanism
retry = 0
while retry < 4:
    print("crawling website")
    is_success = 1 # Successfully get a web page
    if is_success:
        break
    else:
        retry += 1


# In[166]:


mydict = {("Ian", "Chen"): 1,
          ('David', 'Chiu'): '2'}


# In[167]:


mydict[('Ian', "Chen")]


# In[168]:


mydict[('David','Chiu')]


# ## String...advnaced

# In[169]:


"my name is Ian"


# In[170]:


"my name is Ian".split()


# In[172]:


"my name is Ian".split()[2]


# In[173]:


for word in "my name is Ian".split():
    print(word)


# In[171]:


"123,Ian Chen".split(",")


# In[174]:


[123,"David Chiu", "LargitData"]


# In[178]:


",".join(["123","David Chiu", "LargitData"])


# In[179]:


"Harry Potter".lower()


# In[180]:


"nice".upper()


# In[181]:


"harry potter".title()


# In[186]:


"""


this is my awesome multiline string


"""


# In[190]:


"""


this is my awesome multiline string


""".strip()


# In[191]:


"Japan is good".replace("Japan", "USA")


# In[194]:


"※ 發信站: 批踢踢實業坊(ptt.cc), 來自: 223.139.18.149".split("來自: ")


# In[195]:


"※ 發信站: 批踢踢實業坊(ptt.cc), 來自: 223.139.18.149".split("來自: ")[1]


# In[196]:


"※ 發信站: 批踢踢實業坊(ptt.cc), 來自: 223.139.18.149".split("發信站: ")


# In[197]:


"※ 發信站: 批踢踢實業坊(ptt.cc), 來自: 223.139.18.149".split("發信站: ")[1]


# In[199]:


"※ 發信站: 批踢踢實業坊(ptt.cc), 來自: 223.139.18.149".split("發信站: ")[1].split(", 來自")[0]


# In[210]:


f = open('./donald_trump.txt', 'w')


# In[211]:


type(f)


# In[212]:


f.write("Make America great again")


# In[213]:


f.close()


# In[214]:


# ! for shell command
get_ipython().system('ls')


# In[215]:


get_ipython().system('pwd')


# In[225]:


f2 = open('./donald_trump.txt')


# In[226]:


type(f2)


# In[227]:


quote = f2.read()
quote


# In[228]:


# Read again, hmmm returns nothing
quote2 = f2.read()
quote2


# In[229]:


# Seeks the cursor back to start
f2.seek(0)


# In[230]:


quote2 = f2.read()
quote2


# In[231]:


f2.close()


# In[232]:


speech = open('./speech.txt')


# In[233]:


speech.read()


# In[243]:


speech.seek(0)


# In[244]:


speech.readlines()


# In[240]:


for line in speech:
    print(line.strip())
    print("-" * 50)


# In[245]:


speech.close()


# ## Error handling (Try Except)

# In[247]:


raise IndexError("hi")


# In[248]:


try:
    raise IndexError("hi")
except IndexError as e:
    print(e)


# In[249]:


ll = []
ll[1]


# In[250]:


ll = []
try:
    ll[1]
except IndexError as e:
    print("Error is %s"%e)


# In[251]:


ll = []
try:
    ll[1]
except (IndexError, TypeError) as e:
    print("Error is %s"%e)


# In[254]:


ll = []
try:
    ll[1]
except:
    print("Error is %s")


# In[255]:


ll = []
try:
    ll[1]
except IndexError as e:
    print("Error is %s"%e)
finally:
    print("execute finally")


# In[256]:


ll = [1,2]
try:
    ll[1]
except IndexError as e:
    print("Error is %s"%e)
finally:
    print("execute finally")


# In[257]:


ll = [1,2]
try:
    ll[1]
except IndexError as e:
    print("Error is %s"%e)
else:
    print("executed successfully, no error")
finally:
    print("execute finally")


# In[259]:


ll = [1]
try:
    ll[1]
except IndexError as e:
    # Execute to handle error
    print("Error is %s"%e)
else:
    # Only execute when no error
    print("executed successfully, no error")
finally:
    # Always execute
    print("execute finally")


# In[261]:


# Example
f = open("./donald_trump.txt")
f.read()
raise IndexError("Error reading file")
# do something
f.close()


# In[262]:


f.readable()


# In[263]:


f.close()


# In[264]:


f.readable()


# In[265]:


try:
    f = open("./donald_trump.txt")
    f.read()
    raise IndexError("Error reading file")
except IndexError as e:
    # Execute to handle error
    print("Error is %s"%e)
else:
    # Only execute when no error
    print("executed successfully, no error")
finally:
    # Always execute
    print("Cleaning up files....")
    f.close()


# In[266]:


f.readable()


# In[271]:


# Context Manager
with open('./donald_trump.txt') as f:
    print(f.read())
    f.seek(0)
    print("read second time")
    print(f.read())


# In[270]:


f.readable()


# ### Exercise:
# 
# Donald Trump speech word count

# In[273]:


# with open('./donald_trump.txt') as f:
# Output:
# [('America', 99), ('great', 80), .....]


# In[288]:


mydict = {
    "chief": 1,
    'justice': 2,
    'roberts': 1,
}


# In[289]:


for x in mydict:
    print(x)


# In[290]:


for x in mydict:
    print(mydict[x])


# In[297]:


mydict.keys()


# In[298]:


mydict.values()


# In[299]:


mydict.items()


# In[309]:


with open('./donald_trump.txt') as f:
    speech = f.read().replace(',', "").replace(".", "")
    cnt = {}
    for word in speech.split():
        word = word.lower()
        if word in cnt:
            cnt[word] += 1
        else:
            cnt[word] = 1
            
def custom_sort(entry):
    return entry[1]
    
print(sorted(cnt.items(), key=lambda x: x[1], reverse=True)[:10])
#print(sorted(cnt.items(), key=custom_sort, reverse=True))
    


# In[308]:


from collections import Counter

with open('./donald_trump.txt') as f:
    speech = f.read().replace(',', "").replace(".", "")
    cnt = Counter()
    for word in speech.split():
        word = word.lower()
        if word in cnt:
            cnt[word] += 1
        else:
            cnt[word] = 1
            
cnt.most_common(10)


# ## package import

# In[311]:


import collections


# In[312]:


collections.Counter()


# In[313]:


from collections import Counter


# In[314]:


Counter()


# In[321]:


import collections as cl


# In[316]:


cl.Counter()


# In[317]:


from collections import Counter as cntr


# In[318]:


cntr()


# In[322]:


get_ipython().system('pip install jieba')


# In[323]:


import jieba


# In[324]:


jieba.cut("很多獨立樂迷自以為獨立音樂就是高尚瞧不起流行音樂")


# In[325]:


for word in jieba.cut("很多獨立樂迷自以為獨立音樂就是高尚瞧不起流行音樂"):
    print(word)


# In[ ]:




