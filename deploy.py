# python script used to compile md source into final md

# The things that need to happen here are
#   All {TODO:x} references pooled into todo.md

from yaml import load, Loader
import os
import re
import shutil

outputPath  = "Final/"
todoOutPath = "Todo/"
structureTableFormat = '\n| Field | <span style="display: inline-block; width:200px">Type</span> | Legal Values | <span style="display: inline-block; width:100px">Default Value</span> | Comment |\n| :- | :- | :-: | :- | :- |'


def createFilePath(path : str):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))

def copyBinary(path : str, outpath : str):
    if os.path.exists(os.path.abspath(outpath)):
        os.remove(os.path.abspath(outpath))
    createFilePath(os.path.abspath(outpath))

    shutil.copy(os.path.abspath(path), os.path.abspath(outpath))

def main():
    print(getFilenames())
    for file in getFilenames():
        print(file)
        if meta := loadMeta(file):
            parseMeta(meta)
        else:
            print(f"Unable to parse meta file: {file}")
    
def getFilenames():
    files = []
    for(dir, _, filenames) in os.walk(os.curdir):
        for filename in filenames:
            if filename == "meta.yml":
                files.append(dir[2:] + "/" + filename)
    return files

def loadMeta(path: str):
    if not os.path.exists(path):
        return None
    text = open(path, "r").read()
    return load(text, Loader)

def replaceReferences(text: str, references: dict):
    ret = text
    for key, value in references.items():
        ret = re.sub(key, f"[{key}]({value})", ret)
    return ret

def writeBody(stream, body : dict):
    title = body.get("title", None)
    children = body.get("children", None)
    if not children:
        print("Unable to process body. \n\tReason: No children were defined")
    if not title:
        print("Unable to process body. \n\tReason: No title was defined")

    stream.write(f"# {title}\n\n")
    for name, meta in children.items():
        if text := meta.get("text", None):
            references = meta.get("references", {})
            stream.write(f"## {name}\n{replaceReferences(text, references)}")

def parseStruct(stream, path : str ):
    if not os.path.exists(os.path.abspath(path)):
        return

    stream.write("\n## Structure\n")
    structureData = load(open(path, "r"), Loader)
    structures = structureData.get("structure", None)
    if not structures: return

    for structure, fields in structures.items():
        stream.write(f"### *{structure}*\n\n{structureTableFormat}\n")
        for field, meta in fields.items():
            type = meta.get("type", None)
            subtype = meta.get("subtype", None)
            options = meta.get("options", None)
            comments = meta.get("comments", None)
            default = meta.get("default", None)
            size = meta.get("size", None)
            references = meta.get("references", {})
            hexView = meta.get("hex", False)

            if not type: print("Unable to parse field:", field)
            
            if not subtype: subtype = ""
            else:           subtype = ": " + subtype
            if not comments: comments = ""
            if not default: default = ""
            if not size:    size = ""
            else:          
                if isinstance(size, int): 
                    if hexView:
                        size = f"[{hex(size)}]"
                    else:
                        size = f"[{size}]"
                else:
                    size = f"[{size}]"

            if options:
                if isinstance(options, dict):
                    ret = "{"
                    for key, value in options.items():
                        ret += f"{key}: {value}, "
                    options = ret + "}"
                if isinstance(options, list):
                    if len(options) > 0:
                        if isinstance(options[0], int):
                            if hexView:
                                options = '[0x{}]'.format(', 0x'.join(hex(x)[2:].upper() for x in options))
            else: options = ""

            formattedString = f"| {field} | {type} {subtype} {size} | {options} | {default} | {comments} |\n"
            stream.write(replaceReferences(formattedString, references))

def parseDependencies(dependencies : dict):
    for dependency, outPath in dependencies.items():
        copyBinary(dependency, outputPath + outPath)

def parsePage(page):
    body = page.get("body", None)
    out = page.get("out", None)
    name = page.get("name", None)
    dependencies = page.get("dependencies", None)
    if not body or not out:
        print(f"Body or output directory invalid: \n\tBody: {body} \n\tOutput Directory: {out}")
        return
    if not name:
        print("No name was assigned.")

    if dependencies:
        parseDependencies(dependencies)

    if out == ".":      # check if we're storing into root
        out = ""

    outpath = f"{ outputPath }{ out }{ name }.md"
    createFilePath(outpath)
    fileout = open(outpath, "w")

    for item in body:
        file = open(item, "r").read()
        data = load(file, Loader)
        writeBody(fileout, data)

    return fileout

def parseFiletype(file: dict):
    structPath = file.get("structure", None)
    if not structPath:
        print(f"No 'structure' field defined in { file['name'] } meta.yml")

    stream = parsePage(file)
    parseStruct(stream, structPath)
    stream.close()

PageTypes = {
    "Page"     : parsePage,
    "Filetype" : parseFiletype 
}

def parseMeta(meta : dict):
    if type := meta.get("type", None):
        if func := PageTypes.get(type, None):
            func(meta)
            return
    raise RuntimeError("Unknown filetype: ", meta)
    return



main()