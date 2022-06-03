# Dat
The DAT File is the primary container format used to hold scene assets. Contained inside the DAT are sub-files responsible for defining behaviour seen in a room. These subfiles have many different uses ranging from models, to events. Utilizing some [tools](tools.md) we are able to access the content of these files and modify them. This is the primary workflow used for modding the game.

# Structure
The file consists of a header and a body. The header acts a glossary that contains the metadata for all the data. Like a glossary in a book that has chapters and pages; the header contains the offsets and size of the data. This helps us navigate the body of the file. The header also contains the format of the sub-file. This lets us know how to interpret the data. Such as if the file is animation, model, or level geometry.

![DAT File Header](images/DAT_header_hex.png)

# Subfiles
[AEV]()<BR>
[BIN]()<BR>
[BLK]()<BR>
[CAM]()<BR>
[CNS]()<BR>
[DCT]()<BR>
[DRA]()<BR>
[DSE]()<BR>
[EAR]()<BR>
[EAT]()<BR>
[EFF]()<BR>
[EMI]()<BR>
[ESE]()<BR>
[ESL]()<BR>
[ETM]()<BR>
[ETS]()<BR>
[EVD]()<BR>
[FCS]()<BR>
[FCV]()<BR>
[FNT]()<BR>
[ITA]()<BR>
[ITM]()<BR>
[LIT]()<BR>
[MDT]()<BR>
[OSD]()<BR>
[RTP]()<BR>
[SAR]()<BR>
[SAT]()<BR>
[SEQ]()<BR>
[SFD]()<BR>
[SHD]()<BR>
[SMD]()<BR>
[SMX]()<BR>
[SND]()<BR>
[STB]()<BR>
[TEX]()<BR>
[TPL]()<BR>
[UWF]()<BR>
[VIB]()<BR>
[MHT]()<BR>

{TODO:Verify udas sub-file list & fill out entries}