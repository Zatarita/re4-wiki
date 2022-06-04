# Dat
The DAT File is the primary container format used to hold scene assets. Contained inside the DAT are sub-files responsible for defining behaviour seen in a room. These subfiles have many different uses ranging from models, to events. Utilizing some [tools](tools.md) we are able to access the content of these files and modify them. This is the primary workflow used for modding the game.

DAT Files are used for many purposes from general purpose containers to containing all the data for a [room](). 

# Structure
The file consists of a header and a body. The header acts a glossary that contains the metadata for all the data. Like a glossary in a book that has chapters and pages; the header contains the offsets pointing to the data. This helps us navigate the body of the file. The header also contains the extension of the sub-file. This lets us know how to interpret the data. Such as if the file is animation, model, or level geometry.

The Structure of the file is as follows:
![DAT File Header](images/DAT_header_hex.png)

```c
struct Header
{
    int  count;                 // Blue
    int  padding[3];
    int  offset[count];         // Green
    char extension[4][count];   // Orange
}
```

> All offsets in the file are aligned to the nearest 0x20 offset boundary. It is unknown if this is a requirement or optimization. <sup>[testing needed](https://github.com/Zatarita/re4-wiki/issues/new?title=update-DAT_Alignment_Requirement)</sup>

# Subfiles
Contained inside the DAT are other subfiles with their own functionality. Each of these files work together to create the functionality we see in game.

[AEV]() - Room events <BR>
[BIN]() - Models <BR>
[BLK]() - <BR>
[CAM]() - Cameras <BR>
[CNS]() - <BR>
[DCT]() - <BR>
[DRA]() - <BR>
[DSE]() - <BR>
[EAR]() - <BR>
[EAT]() - <BR>
[EFF]() - <BR>
[EMI]() - <BR>
[ESE]() - <BR>
[ESL]() - <BR>
[ETM]() - <BR>
[ETS]() - <BR>
[EVD]() - <BR>
[FCS]() - <BR>
[FCV]() - <BR>
[FNT]() - Font <BR>
[ITA]() - <BR>
[ITM]() - <BR>
[LIT]() - Room Lights <BR>
[MDT]() - Message Text <BR>
[OSD]() - <BR>
[RTP]() - <BR>
[SAR]() - <BR>
[SAT]() - Level Collision Geometry <BR>
[SEQ]() - Sequence <BR>
[SFD]() - <BR>
[SHD]() - <BR>
[SMD]() - <BR>
[SMX]() - <BR>
[SND]() - <BR>
[STB]() - <BR>
[TEX]() - <BR>
[TPL]() - Texture <BR>
[UWF]() - <BR>
[VIB]() - <BR>
[MHT]() - <BR>

