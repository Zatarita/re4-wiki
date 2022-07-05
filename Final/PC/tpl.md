# TPL File

## Summary
 The TPL File is a filetype that see's a lot of variation between versions. This page is related to the UHD release of the game.<sup>(disambiguation)</sup> 
## Structure
### *Header*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='identifier'>Identifier</span> | enum : uint32_t  | {Nintendo: 0x0020AF30, PS2: 0x00001000, PC : 0x12345678, PC: 0x78563412} |  | Magic used to identify file type. |
| <span id='texture-count'>Texture Count</span> | uint32_t   |  |  | Denotes how many images are contained within the tpl. |
| <span id='image-offset-table'>Image Offset Table</span> | array : [Texture Offsets](#texture-offsets) [Texture Count] |  |  | Table holding the metadata for each texture in the TPL. |
### *Texture Offsets*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='texture-header-offset'>[Texture Header](#texture-header) Offset</span> | uint32_t   |  |  | Offset pointing to this texture's metadata. |
| <span id='palette-header-offset'>[Palette Header](#palette-header) Offset</span> | uint32_t   |  |  | Offset pointing to this texture's palette header. Can be null. |
### *Texture Header*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='height'>Height</span> | uint32_t   |  |  | Height of the texture in pixels. |
| <span id='width'>Width</span> | uint32_t   |  |  | Width of the texture in pixels. |
| <span id='format'>Format</span> | enum : uint32_t  | {I4: 0, I8: 1, I4A4: 2, I8A8: 3, R5G6B5: 4, R4G5B4A3: 5, R8G8B8A8: 6, P4: 8, P8: 9, P16: 10, CMPR: 14} |  | The format of the pixel data. |
| <span id='texture-data-address'>Texture Data Address</span> | uint32_t   |  |  | On PC this points to an [ImagePack Reference](#imagepack-reference) that tells the game which [Texture Index](#imagepack-index) to use from a specified [ImagePack ID](#imagepack-id). On console this address points to the raw pixel data. |
| <span id='wraps'>WrapS</span> | uint32_t   |  |  |  |
| <span id='wrapt'>WrapT</span> | uint32_t   |  |  |  |
| <span id='min-filter'>Min Filter</span> | uint32_t   |  |  |  |
| <span id='mag-filter'>Mag Filter</span> | uint32_t   |  |  |  |
| <span id='lod-bias'>LOD Bias</span> | Float   |  |  |  |
| <span id='edge-lod-enable'>Edge LOD Enable</span> | byte   |  |  |  |
| <span id='min-lod'>Min LOD</span> | byte   |  |  |  |
| <span id='max-lod'>Max LOD</span> | byte   |  |  |  |
| <span id='unpacked'>Unpacked</span> | byte   |  |  |  |
### *Palette Header*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='entry-count'>Entry Count</span> | uint16_t   |  |  |  |
| <span id='unpacked'>Unpacked</span> | bool : uint16_t   |  |  |  |
| <span id='palette-format'>Palette Format</span> | enum : uint32_t  | {I8A8: 0, R5G6B5: 1, R4G5B4A3: 2} |  |  |
| <span id='palette-data-address'>Palette Data Address</span> | uint32_t   |  |  |  |
### *ImagePack Reference*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='imagepack-id'>ImagePack ID</span> | uint32_t   |  |  | A reference to the ImagePack used in the PC version of the game that holds a collection of textures. The ImagePack ID in hex **is** the name of the file found in "ImagePackHD/0x_______" |
| <span id='imagepack-index'>ImagePack Index</span> | uint32_t   |  |  | Since the ImagePack can contain multiple textures, this specifiies which texture to use from the ImagePack. |
### *Thanks!*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='mariokart64n'>MarioKart64n</span> |     |  |  | Special thanks to MarioKart64n for sharing their knowledge on the PC version and how it connects to the console versions. |
| <span id='custom-mario-kart-wiiki'>Custom Mario Kart Wiiki</span> |     |  |  | Special thanks to the [MarioKart](https://wiki.tockdom.com/wiki/TPL_(File_Format)) community sharing their knowledge on the console formats. |
