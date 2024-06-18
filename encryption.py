import random
#generate a random srting of 3 characters
def rand_str_gen():
    rand_str="".join(random.choice("abcdefghijklmnopqrstuvwxyz") for i in range(3))
    return(rand_str)


mg = input("Enter the message to be encryped:")
words= mg.split(" ")
coding= input("Enter 1 for coding and 0 for decoding:")
coding = True if (coding=="1") else False

if(coding):
    nwords=[]
    for word in words:
        if(len(word)>2):
            stnew= rand_str_gen() + word[1:] + word[0] + rand_str_gen()
            nwords.append(stnew)
        else:
             nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords=[]
    for word in words:
        if(len(word)>2):
            stnew= word[3:-3]
            stnew=  stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
             nwords.append(word[::-1])
    print(" ".join(nwords))




               

      

