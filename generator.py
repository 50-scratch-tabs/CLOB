# This was borrowed from an AI project I'm working on, that's why it talks about the "system prompt"

import os
def gensysprompt(data,level=0):
    if os.path.isdir(data):
        for line in open(os.path.join(data,"index")):
            line=line.strip()
            if line.startswith("!"):
                yield line
            elif line.startswith("#"):
                pass
            else:
                for i in gensysprompt(os.path.join(data,line.split(" ")[0]),level+1):
                    yield i
    else:
        d= open(data).read()
        if not d[-1]=="\n":
            d+="\n"
        yield d

def getprompt(name):
    out="".join(list(gensysprompt(name)))
    return out

systemprompt=getprompt(os.path.join(os.path.dirname(__file__),"static"))
if __name__=="__main__":
    print(systemprompt)
