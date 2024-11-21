import argparse
import os
from includes.InputFile import GetFile as InputFile
from includes.CompileCode import Compile as CompileCode
from includes.WiriteFile import WriteFile as WiriteFile


def main():
    Type,outpath,code=InputFile()
    if Type=="w" or Type=="W":
        ReturnCodes=CompileCode(code)
        WiriteFile(outpath+".Output",ReturnCodes)
    elif Type=="r" or Type=="R":
        exec(code)
if __name__ == "__main__":
    main()
    
    