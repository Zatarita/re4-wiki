# python script used to compile md source into final md

# The things that need to happen here are
#   All {TODO:x} references pooled into todo.md

import os
import re
import shutil

outputPath  = "Final/"
todoOutPath = "Todo/"

def main():
    files = getFilenames()
    for file in files:
        fileText                         = open(file, "r").read()
        bracketExpressions, strippedText = isolateBracketExpressions(fileText)
        todo, additionalInfo             = processBracketExpressions(bracketExpressions)
        writeFinalText(file, strippedText, todo, additionalInfo)
    createTodoMain(files)
    copyBinary("PC/archive")
    copyBinary("PC/images")
    
def getFilenames():
    files = []
    for(dir, _, filenames) in os.walk(os.curdir):
        if dir[2:].startswith((outputPath[:-1], todoOutPath[:-1], ".git")):
            continue

        for filename in filenames:
            if filename == "readme.md":
                continue
            
            if filename.endswith(".md"):
                files.append(dir[2:] + "/" + filename)
    return files

bracketRegEx = r'\{(.*?)\}'
def isolateBracketExpressions(string : str):
    bracketExpressions = re.findall(bracketRegEx, string)
    return (bracketExpressions, re.sub(bracketRegEx, "", string))

def processBracketExpressions(strings : list):
    todo = []
    additional = []
    for string in strings:
        if string.startswith("TODO:"):
            todo.append(string[5:])
        else:
            additional.append(string)
    return (todo, additional)

def writeFinalText(path : str, body : str, todo : list, additionalInfo : list):
    createFilePath(f"{outputPath}{path}")
    open(f"{outputPath}{path}", "w").write(body)

    createFilePath(f"{todoOutPath}{path}")

    with open(f"{todoOutPath}{path}", "w") as todoOut:
        todoOut.write(os.path.basename(path)[0:-3] + " Todo:<br>\n")
        for line in todo:
            todoOut.write(f"* {line}\n")

        if len(additionalInfo) > 0:
            todoOut.write(f"\n{os.path.basename(path)[0:-3]} Additional Info:<br>\n")
            for line in additionalInfo:
                todoOut.write(f"* {line}<br>\n")

        todoOut.write("## [Todo Main](../main.md)<br>\n")

def createFilePath(path : str):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

def copyBinary(path : str):
    if os.path.exists(f"{outputPath}{path}"):
        shutil.rmtree(f"{outputPath}{path}")
    createFilePath(f"{outputPath}{path}")

    shutil.copytree(os.path.abspath(path), f"{outputPath}{path}")

def createTodoMain(files : list):
    todoMain = "Todo\main.md"
    createFilePath(todoMain)
    with open(todoMain, "w") as fileout:
        fileout.write("# Todo Mainpage\n")
        for file in files:
            fileout.write(f"* [{os.path.basename(file)[:-3]}]({file})\n")
        fileout.write("## [Main](../readme.md)<br>\n")

main()