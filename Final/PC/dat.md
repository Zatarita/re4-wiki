# DAT

## Summary
 The DAT file is one of the primary [container formats](https://en.wikipedia.org/wiki/Container_format_(computing)) used by the game. Contained within the DAT files are other [subfiles](#subfiles). The content of the [subfiles](#subfiles) can vary from *visual* assets such as models or textures, to more *abstract* such as defining the functionality of the objects in the room. The DAT file has seen a few variations between versions; however, it is fairly ubiquitous and an important format. By modifying the [subfiles](#subfiles) inside of the DAT file we are able to change the behaviour of the game.
## Subfiles
There should be another section
## Differences In Versions
and another?
## Structure
### *Header*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='count'>Count</span> | uint32_t   |  |  | The amount of subfiles contained within the DAT. |
| <span id='padding'>Padding</span> | array : byte [12] |  |  |  |
| <span id='offsets'>Offsets</span> | array : uint32_t [Count] |  |  | List of offsets pointing to the start of each chunk of data. |
| <span id='extensions'>Extensions</span> | array : string [Count] | ['AEV', 'BIN', 'BLK', 'CAM', 'CNS', 'DCT', 'DRA', 'DSE', 'EAR', 'EAT', 'EFF', 'EMI', 'ESE', 'ESL', 'ETM', 'ETS', 'EVD', 'FCS', 'FCV', 'FNT', 'ITA', 'ITM', 'LIT', 'MDT', 'MHT', 'OSD', 'RTP', 'SAR', 'SAT', 'SEQ', 'SFD', 'SHD', 'SMD', 'SMX', 'SND', 'STB', 'TEX', 'TPL', 'UWF', 'VIB'] |  | List of extension for the files. |
| <span id='files'>Files</span> | array : File Data [Count] |  |  | List of raw data for the contained files. |
### *File Data*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='file'>File</span> | array : Bytes [ ] |  |  | The raw data for a subfile contained in the DAT. Size is calculated using the offsets. offset[i+1] - offset[i] will equal the size of the chunk. (or offset[i] through the end of file) |
