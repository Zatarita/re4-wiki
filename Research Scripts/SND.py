import os
import sys
import struct

HELP_TEXT = "Invalid syntax - Example: 'python SND.py filename.snd'";
SIZEOF_HEADER_ENTRY = CHUNK_ALIGNMENT = 0x20

FORMAT_SWITCH = {
    -12 : ".unknown_12",
    -13 : ".unknown_13",
    -14 : ".vag",
}

def main(filepath : str):
    with open(filepath, "rb") as file:
        file.read(SIZEOF_HEADER_ENTRY)
        entries  = readHeaderEntries(file)
        segments = getSegmentData(file, entries)
        saveSegmentData(f"SND/{os.path.basename(filepath)[:-4]}/", entries, segments)
    return

def readHeaderEntries(stream):
    entries = []
    while(True):
        unkwn, size, fmt, offset, unkwn2, unkwn3, _, _ = struct.unpack("<iIiIIIII", stream.read(SIZEOF_HEADER_ENTRY))
        if unkwn == -1:
            return entries
        entries.append( (unkwn, size, fmt, offset, unkwn2, unkwn3) )

def getSegmentData(stream, entries : list):
    data = []
    for entry in entries:
        _, size, _, offset, _, _ = entry
        stream.seek(offset)
        data.append(stream.read(size))
    return data

def saveSegmentData(path : str, entries : list, segments : list):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    
    for index, entry in enumerate(entries):
        _, _, fmt, _, _, _ = entry
        data = segments[index]
        ext  = FORMAT_SWITCH.get(fmt - 65536, ".UNKNOWN_EXTENSION")
        with open(f"{path}{index}{ext}", "wb") as file:
            file.write(data)

def getFilename():
    if len(sys.argv) < 2:
        return None
    return sys.argv[1]

if file := getFilename():
    main(file)
else:
    print(HELP_TEXT)