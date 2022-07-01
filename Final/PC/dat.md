# DAT

## Summary
 The DAT file is one of the primary [container formats](https://en.wikipedia.org/wiki/Container_format_(computing)) used by the game. Contained within the DAT files are other [subfiles](#subfiles). The content of the [subfiles](#subfiles) can vary from *visual* assets such as models or textures, to more *abstract* functionality such as the events that trigger in a room. The DAT file has seen a few variations between versions; however, it is fairly ubiquitous and an important format. By modifying the [subfiles](#subfiles) inside of the DAT file we are able to change the behaviour of the game.
## Subfiles
Contained inside the DAT file are other sub files, each with their own purpose. Some of these subfiles are required for the room to function. Other subfiles are supplimentry and allow for us to use certain functionality inside the room. <br><br> * AEV - This subfile holds room events * BIN - 3D Model asset used in the room. * BLK - Block loading, used in r002, and r100. Rooms that use this method of loading data also have supporting dat files with suffix _00x.dat * CAM - Defines how the camera behaves in designated areas. * CNS - Room constants * DCT - Menu words from Mercs * DRA - ~~TODO~~ * DSE - Door sound effect * EAR - ~~TODO~~ * EAT - Bullet Collision * EFF - Effects Package is a container used to hold the assets required for certain room effects * EMI - ~~TODO~~ * ESE - Environmental Sound Effects define ambient sounds such as fire, running water, etc. * ESL - Enemy Spawn List * ETM - Interactable Models such as movable scenery. * ETS - ~~TODO~~ * EVD - Assets used during cutscenes. Container format * FCS - ~~TODO~~ * FCV - Animation file * FSE - Foot Sound Effect * FNT - Font file. Defines the symbols the MDT file uses to present text to the screen. * ITA - Positions for ITM entries * ITM - Item definitions * LIT - Light definitions. Works together with the CAM to light a scene. * MDT - Message Dialog Text works together with a FNT file to create interactable dialogs on screen. * OSD - Null file * RTP - Route points. Path NPCs and enemies follow to navigate the room. * SAR - ~~TODO~~ * SAT - Room Collision * SEQ - Sequences are a generalized series of events used for multiple purposes such as progressing an MDT during a cutscene, or stepping through animations. * SFD - Sofdec Video File * SHD - Shadow Definition * SMD - Stage Models are instanced geometry used to decorate a scene. Depending on the room there can be an accompanying BLK file used to stream SMDs from other DATs life. * SMX - ~~TODO~~ * SND - Room Sound Definitions * STB - Sound Table * TEX - ~~TODO~~ * TPL - Texture Palette Library is a container that can hold multiple textures used by various assets in a scene.  * UWF - ~~TODO~~ * VIB - Controller vibration definitions
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
