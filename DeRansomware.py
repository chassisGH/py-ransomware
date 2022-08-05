#!/usr/bin/python3

try :
    import nacl, nacl.secret, pathlib, os ##req
except:
    print("Error try To run pip install requirement.txt")

"""Making class in order to decrypt"""

class Decrypt(object):                                     

    def __init__(self, Target,BoxM):     
        self.Target = Target
        self.BoxM   = BoxM

    def FileE(loc):
        DeFileN     = (loc.Target).strip(".lol")
        EnFileN     = (loc.Target)
        Date        = 0

        with open(EnFileN,"rb") as  File: Date = File.read()
        Decrypted   = loc.BoxM.decrypt(Date)
        with open(DeFileN,"wb") as  File: File.write(Decrypted)
        os.remove(EnFileN)

"""Setting Up Some Global Vars""" 

Key     = b'Your Key Hare'              ## add key here
box     = nacl.secret.SecretBox(Key)
Paths   = [r"C:\Users\\"]

"""Our ForLoop So we walkthrough Our paths """

for  AllFiles in Paths:
    if (pathlib.Path(AllFiles).exists()):
        for path, subdirs, files in os.walk(AllFiles):
            if(("\\AppData\\") in path):pass
            else:
                for file in files :
                    if(".lol" in file):
                        FilePath    = os.path.join(path, file)
                        Decrypt(FilePath,box).FileE()
