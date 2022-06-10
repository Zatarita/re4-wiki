# MDT File

## Summary
 The MDT File is responsible for the text presented in message dialogs throughout the game. These text dialogs are typically triggered by an [AEV event](aev.md); however, other things can trigger MDTs such as cutscenes or a [sequence](seq.md). The MDT file can contain multiple languages inside of it. Each language contains a list of encoded characters that represent the text that gets presented. These characters are determined by a [font file](fnt.md). Some of these characters aren't printed, but instead control *how* the text gets presented. Such as font color, or text justification.
## Header
 A MDT File is a list of [MDT Languages](#mdt-language). The header consists of a count, offsets pointing to each language, and then the languages themselves. Majority of the time each MDT file contains all the strings for each language in the game. This is not always the case though. There is a variation of the MDT that only contains one language. These are typically found inside folders that denote their respective language. (eg *BIO4/SS/**eng***, *BIO4/SS/**jap***, etc)<br>
 > On update 1.10 Traditional and Simplified Chinese was added to the game. This means that later versions of the game have a slight altercation to the format. The update appended the two new [MDT Languages](#mdt-language) to the end of the list **without** updating the count. You can determine if you have a new MDT by checking if the first offset instead of using the count<br>
 0x1C: pre  1.10<br>
 0x24: post 1.10<br>
 > Attempting to correct the field has resulted in the game crashing.
## MDT Language
 The MDT Language is a list of strings. When working with the standard version of the MDT we see a similar structure to the header. We have a count denoting how many strings there are, then the offsets, and the [MDT Strings](#mdt-string). The structure of the MDT Language isn't fully mapped out yet though. There is an unknown at the beginning of the language that is suspected to be vestigial from the console ports; however, [this requires confirmation](https://github.com/Zatarita/re4-wiki/issues/new?title=update-MDT-Unknown).
## MDT String
 The MDT String is a list of [16-bit numbers](https://en.wikipedia.org/wiki/16-bit_computing). These numbers either control how the text gets presented to the screen, or they *are* the characters that gets presented to screen. The highest 8-bits is the index which gets grabbed from the [FNT](fnt.md) file. The Lowest 8-bits are [special characters](#special-characters). There are only 18 of them; however, they control things such as the flow and presentation of the text.
## Special Characters
 Some characters don't actually contribute to which character is presented to screen; however, they are responsible for controlling the flow and appearance of the characters that come after it. Some of these characters utilize the next number in the sequence as a modifier. For example the color control character has another character after it that defines which color should be selected, or the left justification character has distance from the left of the page as the next character.<br>
 | Value | Has Modifier | Modifier | Description |
 | - | :-: | :-: | :- |
 | 0x00 | x |  | Start of string. |
 | 0x01 | x |  | End of string. |
 | 0x02 | ✓ | Line Number | Insert another string from the room's MDT.  |
 | 0x03 | x |  | Newline |
 | 0x04 | x |  | Newpage |
 | 0x05 | ✓ | Print Speed | Prints each character one character at a time. |
 | 0x06 | ✓ | Color Index | Changes the color of all text that comes after this point. The colors are determined by a hard coded color table. Each version has slightly different colors available. |
 | 0x07 | x |  | An option to a question. |
 | 0x08 | x |  | Wait for player input |
 | 0x09 | ✓ | Sleep Duration | Sleep for a specific duration before continuing. |
 | 0x0a | x |  | The quantity of the last item picked up. This is persistent between saves and rooms. |
 | 0x0b | ✓ | Justification Left | Distance from the left side of the screen where the message will appear |
 | 0x0c | ✓ | Justification Top | Distance from the top of the screen where the message will appear. |
 | 0x0d | ✓ | Unknown | Currently unknown what this does; however, source code indicates that it does *something* and possibly takes a modifier. |
 | 0x0e | x |  | Return from an insertion. Note! If this is called on a string that wasn't inserted it will soft lock the game. Any reference to a seperate MDT entry requires this character to return control back to the main string. |
 | 0x0f | ✓ | Line Number | Inserts a string from core_6.mdt |
 | 0x10 | x |  | The name of the last item picked up. This is persisten between saves and rooms. |
 | 0x11 | ✓ | Line Number | Inserts a string from core_17.mdt |
 | 0x12 | ✓ | Character Index | Inserts a character name. This is only used during walkie talkie cutscenes, and only works under certain circumstances. |
 
## Structure
### *Header*


| Field | <span style="display: inline-block; width:150px">Type</span> | Legal Values | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Count | uint32_t   |  | 6 | Count of how many languages are in the file. It is possible that this value does not equal 6. In that case The MDT only has one language inside of it and this will instead jump straight to the start of the [MDT Langauge](#mdt-language). |
| Offsets | array : uint32_t [Count] |  |  | Offsets pointing to the start of each language. |
| Languages | array : [MDT Language](#mdt-language-1) [Count] |  |  | The actual languages themselves. |
| Note |    |  |  | The size of the array varries depending on version. For version 1.10+ the MDT has two extra offsets for Traditional and Simplified Chinese. These are just hacked onto the end, and the count is not adjusted to reflect that; however, Fixing the value causes the game to crash. For version 1.10 Count + 2 should be used. |
### *MDT Language*


| Field | <span style="display: inline-block; width:150px">Type</span> | Legal Values | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Unknown | uint32_t   |  |  | Currently Unknown. Assumed vestigial data from console ports. |
| Count | uint32_t   |  |  | Count of how many strings are inside this particular language. |
| Offsets | array : uin32_t [Count] |  |  | Offsets pointing to the start of each string. |
| Strings | array : [MDT String](#mdt-string)[Count]  |  |  |  |
### *MDT String*


| Field | <span style="display: inline-block; width:150px">Type</span> | Legal Values | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Characters | array : short [n] | {Start: 0, End: 1, Insert: 2, Newline: 3, Newpage: 4, Speed: 5, Color: 6, Option: 7, Pause: 8, Sleep: 9, Quantity: 10, Left Justify: 11, Top Justify: 12, Unknown: 13, Return: 14, Core: 15, Last Pickup: 16, Item: 17, Character: 18, Font Character: 128, } |  | Each string starts and ends with a Start and End character respectively. Beyond that each short is either a special character, or a reference to a character defined in a [FNT](font.md) file. The lower 8 bits are reserved for special characters and the upper 8 bits (128+) are indexes into a [FNT](font.md) file. |
