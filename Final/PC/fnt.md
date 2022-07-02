# FNT

## Summary
 <img align='left' style='margin:10px' src='images/example.png' width=200 height=200></img> The Font file is responsible for defining the symbols that get presented to the screen for various languages. There can be multiple font files being used for different circumstances. This is useful for languages that contain thousands of characters.


The Font file works together with the [MDT](mdt.md) to create text dialogs for the player to interact with during gameplay, menus, and cutscenes. <br><br><br><br><br>

 ## Header
 The header to a font file tells the game [where to find](#sprite-sheet-offset) the [sprite sheet](#sprite-sheet) and [spacing definitions](#spacing-definitions). The [sprite sheet](#sprite-sheet) and [spacing definitions](#spacing-definitions) work together to define how the characters get presented to the screen. On the PC version of the game, for latin based languages, there also appears to be extra data in the header that has an [unknown purpose](#unknown). <sup>(suggest an edit)</sup>

 ## Font Spacing
 <img align='right' style='margin:10px; background-size: cover;' src='images/Font Spacing.png' width=200 height=200></img> The font spacing determines the margins of the font lettering. There are two bytes that determine the [distance from the start](#left-margin) of the sprite sheet's cell, and the [length](#length) in pixels till the end of the symbol. These two pieces work together to 'cut' the symbol out of the sprite sheet. Typically these values add together to the full cell size. (which can varry from sprite sheet to sprite sheet) Though, the symbol can use less than the full cell periodically.
<br><br><br><br><br> 
## Structure
### *Header*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='sprite-sheet-offset'>Sprite Sheet Offset</span> | uint32_t   |  |  | The offset that points to the start of the [TPL](tpl.md) that defines the font's sprite sheet. |
| <span id='spacing-offset'>Spacing Offset</span> | uint32_t   |  |  | The offset that points to the start of the [font spacing definitions](#spacing-definitions). |
| <span id='unknown'>Unknown</span> | uint32_t  [6] |  |  | Unknown what these bytes do; however, they only seem to be set on the pc version of the game for the latin based symbols. |
| <span id='sprite-sheet'>Sprite Sheet</span> | [TPL](tpl.md)   |  |  | The sprite sheet holding the actual font symbols that gets presented to screen. |
| <span id='spacing-defininitions'>Spacing Defininitions</span> | array : [Font Spacing](#font-spacing) [n] |  |  | The size of the array appears to be the [Spacing Offset](#spacing-offset) through the end of file. There also seems to be no bounds checking at runtime. |
### *Font Spacing*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='left-margin'>Left Margin</span> | byte   |  |  | Number of pixels between left border of the sprite and the beginning of the character. |
| <span id='length'>Length</span> | byte   |  |  | Number of pixels starting after the Left Margin going to the end of the symbol's cell. (with some variation) |
