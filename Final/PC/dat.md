# DAT

## Summary
<img align="left" src="images\DAT_Subfiles.png" width = 200 height = 200></img> The DAT file is one of the primary [container formats](https://en.wikipedia.org/wiki/Container_format_(computing)) used by the game. Contained within the DAT files are other [subfiles](#subfiles).  The content of the [subfiles](#subfiles) can vary from *visual* assets such as models or textures, to more *abstract* functionality such as  the events that trigger in a room. The DAT file has seen a few variations between versions;  however, it is fairly ubiquitous and an important format. By modifying the [subfiles](#subfiles) inside of the DAT file we  are able to change the behaviour of the game.<br><br><br><br><br>
## Header
<img align="right" src="images\DAT_header_hex.png" width = 200 height = 200></img> The Header of the file contains all the metadata about the file. Things such as [how many](#count) subfiles are contained inside the DAT, what [type](#extensions) of files they are, and [where to find](#offsets) the data. Using this information the game navigates the dat file to load the assets needed for a room to function properly. <br><br><br><br><br>
## Subfiles
Contained inside the DAT file are other subfiles, each with their own purpose. Some of these subfiles are required for the room to function. Other subfiles are supplimentry and allow for us to use certain functionality inside the room. <br><br>
 - [AEV](aev.md) - Area Event Volumes are areas where a player can trigger an event used to progress the story in a room. <br>
 - BIN - 3D Model asset used in the room.<br>
 - BLK - Block loading, used in r002, and r100. Rooms that use this method of loading data also have supporting dat files with suffix _00x.dat<br>
 - CAM - Defines how the camera behaves in designated areas.<br>
 - CNS - Room constants<br>
 - DCT - Menu words from Mercs<br>
 - DRA - **TODO**<br>
 - DSE - Door sound effect<br>
 - EAR - **TODO**<br>
 - EAT - Bullet Collision<br>
 - EFF - Effects Package is a container used to hold the assets required for certain room effects<br>
 - EMI - **TODO**<br>
 - ESE - Environmental Sound Effects define ambient sounds such as fire, running water, etc.<br>
 - ESL - Enemy Spawn List<br>
 - ETM - Interactable Models such as movable scenery.<br>
 - ETS - **TODO**<br>
 - EVD - Assets used during cutscenes. Container format<br>
 - FCS - **TODO**<br>
 - FCV - Animation file<br>
 - FSE - Foot Sound Effect<br>
 - FNT - Font file. Defines the symbols the [MDT](mdt.md) file uses to present text to the screen.<br>
 - ITA - Positions for ITM entries<br>
 - ITM - Item definitions<br>
 - LIT - Light definitions. Works together with the CAM to light a scene.<br>
 - [MDT](mdt.md) - Message Dialog Text works together with a FNT file to create interactable dialogs on screen.<br>
 - OSD - Null file<br>
 - RTP - Route points. Path NPCs and enemies follow to navigate the room.<br>
 - SAR - **TODO**<br>
 - SAT - Room Collision<br>
 - SEQ - Sequences are a generalized series of events used for multiple purposes.<br>
 - SFD - Sofdec Video File<br>
 - SHD - Shadow Definition<br>
 - SMD - Stage Models are instanced geometry used to decorate a scene.
 - SMX - **TODO**<br>
 - SND - Room Sound Definitions<br>
 - STB - Sound Table<br>
 - TEX - **TODO**<br>
 - [TPL](tpl.md) - Texture Palette Library is a container that can hold multiple textures used by various assets in a scene. <br>
 - UWF - **TODO**<br>
 - VIB - Controller vibration definitions<br>
## Credit
Special thanks to Mariokart64n for information on these subfiles.
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
| <span id='file'>File</span> | array : Bytes [ ] |  |  | The raw data for a subfile contained in the DAT. Size is calculated using the offsets. offset[i+1] - offset[i] will equal the size of the chunk. (or offset[i] through the end of file for the last chunk) |
