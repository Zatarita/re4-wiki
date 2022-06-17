# AEV

## Summary
<img align="right" src="images/AEV Generic.png" width = 200 height = 200> The AEV file is used to define actions a player can take in a room. Each action is given a designed trigger area. When an entity is standing in the trigger area they are able to interact with the event. Some events happen automatically, while others require the player to press the  action button to enable it. Some of the events are linked to internal functionality and thusly aren't easily modable. Any event falling in this category is left out until more information  can be found out about them. <br><br><br><br><br><br><br>


---
## Door Event
<img align="left" style="margin:10px" src="images/Events/Door Event.png" width = 200 height = 200></img> The Door event is used to transition between rooms. When activating a door event the game checks the [parameters](#door-event-1) supplied and will play a designated "Open Sound" from the room's sound table and attempt to load the Next Room in the Next Stage. It will then place the player in the desired Position and Facing (or Room Part) supplied in the event [parameters](#door-event-1). Some doors might be locked. In this case the event must have a lock flag assigned that signifies the current locked state of the door. This is stored internally by the game. There are a maximum of 0x3f flags reserved for this purpose. They are stored along with other player information during save. (Validation needed) Doors locked in this manor have a sister door that toggles the locked flag by unlocking it. typically the "other side" of the door. In the event the door is unlocked. The game checks the [parameters](#door-event-1) of the event to pull a sound from the room sound table for unlocking the door. <br><br><br>

---
## Structure
### *Header*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Signature | string   | AEV | AEV | Signature denoting the begining of the file. Used to validate the data. Null terminated |
| Unknown | byte   |  | 4 | Unknown what this does. Set to 4 most times. |
| Unknown 2 | byte   |  | 1 | unknown what this does. Set to 1 most times. |
| Count | byte   |  |  | How many events are in the AEV. Max 127 |
| Padding | array : byte [13] |  |  |  |
| Event Entries | array : Event [Count] |  |  | The array of events contained inside the room. |
### *Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Unknown | byte   |  |  | This is used by the game at runtime. |
| Area Hit Type | enum : byte  | {Square: 0, Circle: 1, Eye Trigger: 2} | 1 | Determines if the collision area is rectangular, or a cylindrical. Note "Eye Trigger" has been disabled; however, appears to still have some functionality. |
| Unused | array : byte [3] |  |  |  |
| Y Position | float   |  |  | Starting Y position of the trigger volume |
| Height | float   |  |  | Height of the trigger volume |
| Position 1 | array : float [2] |  |  | Position (x,z) of the first point in the square. Note if Area Hit Type set to Circle this value is (x,z) for the center of the circle. |
| Position 2 | array : float [2] |  |  | Position (x,z) of the second point in the square. Note if Area Hit Type set to Circle this value is unused. |
| Position 3 | array : float [2] |  |  | Position (x,z) of the third point in the square. Note if Area Hit Type set to Circle this value is unused. |
| Position 4 | array : float [2] |  |  | Position (x,z) of the fourth point in the square. Note if Area Hit Type set to Circle this value is unused. |
| Active | byte   | {Inactive: 2, Active: 3} | 3 | This is used to enable or disable the event. This is used internally to disable an event being interacted with to prevent multiple activations. |
| Type | enum : byte  | {Normal: 0, Door: 1, Exec: 2, Unused: 3, Flag: 4, Message: 5, Planter: 6, Jump: 7, Save: 8, SHD Display: 9, Damage: 10, SCR_AT: 11, View Control: 12, Field Info: 13, Crouch (Stoop): 14, Small Key: 15, Ladder: 16, Use: 17, Hide: 18, Position Jump: 19, Item Parent: 20} |  | Determines the event type. Each event type has different parameters inside the "buffer" area |
| Hit Type | enum : byte  | {under: 0, front: 1, under+angle: 2, front+angle: 3} |  | todo when I can think |
| Trigger Type | enum : byte  | {auto: 1, manual: 2, semiauto: 4, action button: 8, onetime: 128} |  | Determines how the event gets triggered. |
| Target Type | enum : byte  | {player: 1, enemy: 2, object: 4, ashlee: 8} |  | Determines which entities can trigger the event. |
| Priority | byte   |  | 3 | Max 15 |
| Hit Angle | byte   |  |  | Determines the angle upon which the target should be facing to allow triggering of the event. Only set if Hit Type is one of the +angle variants. |
| Open Angle | byte   |  |  | Determines "spread" of the view cone when Hit Type is set to a +angle variant |
| Action Type | byte   |  |  | Determines the activation text that gets displayed to screen if Trigger Type is set to manual, semiauto, or action button |
| Padding | array : byte [8] |  |  |  |
| Parameter Buffer Area | array : byte [64] |  |  | This area is multipurpose. Depending on the value of "Type" different parameters will be in here. See the different types below for the structure of each type in this buffer area. |
| unknown pointer | uint32_t   |  |  | This is used by the game at runtime. Assumed it is a function pointer. |
### *Normal Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Note |     |  |  | There are no parameters for the Normal Event type. |
### *Door Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Position | array : float [3] |  |  | (x,y,z) Position in the room being transitioned into. |
| Facing | float   |  |  | Desired facing (in degrees) in the room being transitioned into. |
| Next Stage | byte   |  |  | Stage number for the desired room. |
| Next Room | byte   |  |  | Desired room number for the above Stage. |
| Key ID | enum : byte  | {default: 0, In Lock Close: 1, In Lock Open: 2} |  | Fill this out |
| Flag Number | byte   |  |  | Determines which lock flag gets checked to see if the door is locked. Max 0x3f |
| Unused | array : byte [4] |  |  |  |
| Next Part Number | byte   |  |  | Determines which part number in a room to jump to. |
| Key Sound Effect | byte   |  |  | Determines which sound plays from the room's sound table during unlock. |
| Open Sound Effect | byte   |  |  | Determines which sound plays from the room's sound table during opening. |
| Fade Effect | enum : byte  | {Normal: 1, Fade: 2, Black: 3} |  | Determines the effect used after interacting with the door. Normal is the zoom effect. |
### *Execute Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Note |     |  |  | There are no parameters for the Execute Event type. |
### *Flag*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Flag ID | enum : byte  | {Room Flag: 0, Room Save Flag: 1, Scenario Flags: 2} |  | Determines where the flag that is being toggled is located. |
| Flag Action | enum : byte  | {Turn On: 0, Turn Off: 1} |  | Determines if the flag is being set, or unset. |
| Flag Number | uint16_t   |  |  | Determines which flag is being toggled. Max 0xFF |
### *Message Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Message Type | enum : uint16_t  | {Room Message: 0, Common Message: 1} |  | todo |
| Message Number | uint16_t   |  |  | Determines which line is grabbed from the MDT file |
| Camera Number | byte   |  |  | Determines which index from the CAM to use when interacting with the message. |
| Sound Effect Type | enum : byte  | {Room: 0, Player: 1} |  | Determines if the sound is pulled from the room, or the player sound table. |
| Sound Effect Number | byte   |  |  | Determines which sound to be pulled from the sound table. |
### *Jump Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Position | array : float [3] |  |  | Position to jump to (x,y,z) |
### *Save Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Terminal Number | uint32_t   |  |  | unknown what this does. Max 10 |
### *SHD Display Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| SHD Number | uint16_t   |  |  | Determines which SHD index to toggle. |
| Display Flag | enum : byte  | {False: 0, True: 1} |  | Determines if the SHD is being toggled on, or toggled off. |
### *Damage Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Damage Timer | uint32_t   |  |  |  |
| Damage Type | enum : byte  | {No Hit: 0, Fire: 1, Electricity: 2, Env Light: 3, Env Fire: 4, Grenade Blast: 5, Push: 6} |  | Determines what type of damage is being applied. |
| Flags | enum : byte  | {Damage Die Flag: 1, Damage Angle Set: 2} |  | Todo |
| Unused | array : byte [2] |  |  |  |
| Damage | uint32_t   |  |  | Determines how much damage is applied |
| Damage Angle | uint32_t   |  |  | Determines the knock back angle when "Damage Angle Set" flag is active |
### *SCR_AT Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Note |     |  |  | Todo |
### *View Control Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Position | array : float [3] |  |  | TODO |
| Angle Y | float   |  |  | TODO |
| Unknown | byte   |  |  | unknown |
| Type | array : byte  | {Unknown_0: 0, Unknown_1: 1} |  |  |
| Radius | float   |  |  | TODO |
| Out Range | float   |  |  | TODO |
### *Field Info*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Field ID | uint32_t   |  |  |  |
### *Ladder Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Position | array : float [3] |  |  | Position of the ladder (x, y, z) |
| Angle | float   |  |  | Angle of approach for the ladder. |
| Height | uint32_t   |  |  | height of the ladder |
| Cam Indexes | array : byte [3] |  |  | Indexes of the CAM to be used when accending ladder. |
### *Use Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Use ID | uint32_t   |  |  | Item ID to be used. |
### *Hide Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| Type | byte   | 3 | 3 | 3 is the only value that can be used here. |
| Hide Position Set | byte   | 1 | 1 | Flag is set so long as there is a hide position assigned |
| Hide Area Set | byte   | 1 | 1 | Flag is set so long as there is a Hide Area assigned |
| Active | byte   |  |  | Use internally by the game to determine if ashlee is currently hiding in the area. If she is hiding the value is 2 |
| Hiding Position | array : float [8] |  |  | 4 points that make up the Hiding Position area |
| Hiding Position Y | float   |  |  |  |
| Height | float   |  |  |  |
| Hiding Area | array : float [3] |  |  | Position (x, y, z) of the hiding area |
