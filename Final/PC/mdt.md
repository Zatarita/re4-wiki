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

## Structure
### *Header*


| Field | <span style="display: inline-block; width:150px">Type</span> | Legal Values | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Count | uint32_t   |  | 6 | Count of how many languages are in the file. It is possible that this value does not equal 6. In that case The MDT only has one language inside of it and this will instead jump straight to the start of the [MDT Langauge](#mdt-language). |
| Offsets | array : uint32_t [Count] |  |  | Offsets pointing to the start of each language. |
| Languages | array : [MDT Language](#mdt-language) [Count] |  |  | The actual languages themselves. |
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
