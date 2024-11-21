import argparse
import os


def GetFile():
    parser = argparse.ArgumentParser(description="这是 systems OS app code的解释器")
    parser.add_argument("-f","--FilePath")
    parser.add_argument("-o","--OutPath")
    parser.add_argument("-t","--Type")
    args=parser.parse_args()

    file_path=args.FilePath
    file_name = os.path.basename(file_path)

    # 分离文件名和扩展名
    _ , extension = os.path.splitext(file_name)

    if (not extension == ".sui" and (args.Type == "w" or args.Type == "W")) or (not extension == ".Output" and (args.Type == "r" or args.Type == "R")):
        return f"无法运行{file_path}，文件扩展名应为“.sui” "
    try:
        with open(args.FilePath,"r",encoding="utf-8") as file:
            code=file.read()
    except Exception:
        with open(args.FilePath,"r",encoding="gbk") as file:
            code=file.read()
    
    try:
        OutPath=args.OutPath
    except:
        OutPath=None
    return args.Type,OutPath,code