# Udas

## Summary
The udas is one of the [container formats](https://en.wikipedia.org/wiki/Container_format_(computing)) used by the [UHD Version](../Versions.md#Ultimate-HD(UHD)) of the game. It not only holds the assets required for a [room](../Room.md) to work, but it also contains files that define *how* the [room](../Room.md) works.  Using various [tools](../Tools.md) the udas can be modified. This allows modders to be able to adjust the behavior of a [room](../Room.md) or the game as a whole. This is the primary approach used for modding the game.<br> The udas works by bundling together a [DAT](dat.md) file with a [SND](snd.md) file. The [DAT](dat.md) file is *the* primary container format used by the game. The [DAT](dat.md) conatined within the udas is the file that actually contains majority of the game assets used by a particular [room](../Room.md). The [SND](snd.md) file (at least in this version of the game) helps link the [room](../Room.md)'s [soundbanks](snd.md#Pc-Soundbanks) found inside the *BIO4/snd* folder to their respective [room](../Room.md). These two files work together to do majority of the heavy lifting.

## Structure
### *Header*


| Field | <span style="display: inline-block; width:200px">Type</span> | Legal Values | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Magic | array : int32_t [0x8] | [0xCAB6BE20, 0x20BEB6CA] |  |  |
| SubFileMetadata | array : [HeaderEntry](#HeaderEntry)  |  |  | Dynamically sized array. Read until an entry with Segment Type -1 is reached. |
| Padding | array : byte [0x400] |  |  | Header typically has anywhere from 0x3B0-0x400 bytes of padding after the last segment. |
### *HeaderEntry*


| Field | <span style="display: inline-block; width:200px">Type</span> | Legal Values | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| SegmentType | enum : int32_t  | {END: -1, [DAT](dat.md): 0, [SND](snd.md): 4, } |  |  |
| Size | uint32_t   |  |  |  |
| Unknown | uint32_t   |  |  |  |
| Offset | uint32_t   |  |  |  |
| Unused | array : uint32_t [4] |  | [0, 0, 0, 0] |  |
