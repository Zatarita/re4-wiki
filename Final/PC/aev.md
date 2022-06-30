# AEV

## Summary
<img align="right" src="images/AEV Generic.png" width = 200 height = 200> The AEV file is used to define actions a player can take in a room. Each action is given a designed trigger area. When an entity is standing in the trigger area they are able to interact with the event. Some events happen automatically, while others require the player to press the  action button to enable it. Some of the events are linked to hard coded internal functionality and thusly aren't easily modifiable. Any event falling in this category is left out until more information  can be found out about them. <br><br><br><br><br><br><br>


---
## Trigger Volumes
<img align="left" style="margin:10px" src="images\Volumes\Square Trigger Volume - Points.png" width=100 height=100></img> <img align="left" src="images\Volumes\Circular Trigger Volume.png" width=100 height=100></img> A trigger volume is a defined area where an [entity](#target-type) can initiate an AEV event. Each event has it's own dedicated trigger volume. These volumes have extra [metadata](#event) used to define it's [shape ](#area-[hit-type](#hit-type)) and [functionality](#active). There are two primary shapes the trigger area can be, rectangular (default) and circular. When the trigger volume is rectangular the game reads  all [four points of the rectangle](#position-1) (x, z), the starting [Y position](#y-position) for all the points, and the [height ](#height)of the trigger area; however, when the trigger volume is circular the game treats the [first of the four points](#position-1) as the center of the circle (x, z); <img align="left" style="margin:10px" src="images\Volumes\Volume Generic - PY.png" width=100 height=100></img> <img align="left" src="images\Volumes\Volume Generic - Height.png" width=100 height=100></img> the other 3 points are unused. Instead the [radius](#radius) will be used. This determines the size and position of the trigger area. Beyond that the [Y position](#y-position) and [height ](#height)are still applied the same way as the rectangular trigger area. <br><br> <img align="right" style="margin:10px" src="images\Volumes\Collision Detection - Front.png" width=100 height=100></img> <img align="right" src="images\Volumes\Collision Detection - Under.png" width=100 height=100></img> Beyond position there are parameters that determine *how* a volume gets triggered. The game needs to know which entities the volume targets (eg the player, enemies, ashlee). When that [entity](#target-type) enters the area it checks the [hit-type](#hit-type) to determine *when* the [entity](#target-type) triggers the volume. The most simple case is when the [hit-type](#hit-type) is in *front of*, or directly *under* the [entity](#target-type); however, the game can also be set to ensure the [entity](#target-type) is *facing a specific angle* as well. The [hit angle](#hit-angle) and [open angle](#open-angle) determine the facing upon which an [entity](#target-type) can trigger the volume.  <img align="right" style="margin:10px" src="images\Volumes\Volume Generic - Hit Angle.png" width=100 height=100></img> <img align="right" src="images\Volumes\Volume Generic - Open Angle.png" width=100 height=100></img> This can be represented with a "fan". The [hit angle](#hit-angle) deteremines the direction the fan faces, and the [open angle](#open-angle) determines the spread of the "fan". When the [entity](#target-type)'s viewing angle is  within the boundaries of the fan, the event will be triggerable. <br><br> Finally, once the event has been triggered, the trigger volume will check the[ type](#type) associated with the event. Each[ type](#type) has extra information to know how to do it's job. These bits of extra information are called parameters, and they're stored at the end in the [parameter buffer area](#parameter-buffer-area) of the event. These parameters tell the game how to handle each event. Things such as where to place the player when transitioning rooms, or what item number is needed to progress. Some events don't have any modifiable parameters and rely on [hard coded functions](#function-pointer) instead. <br><br>

---
## Door Event
<img align="left" src="images/Events/Door Event.png" width = 220 height = 220></img> <img align="left" src="images\Events\Door Event - Locked.png" width = 100 height = 100></img> The Door event is used to transition between rooms. When activating a door event the game checks the [parameters](#door-event-1) supplied. It will play a designated "Open Sound" from the room's sound table and attempt to load the Next Room in the Next Stage. It will then place the player in the desired Position and Facing supplied in the event [parameters](#door-event-1). Some doors might be locked. In this case the event must have a lock flag assigned that signifies the current locked <img align="left" src="images\Events\Door Event - Unlock Door.png" width = 100 height = 100></img> state of the door. This is stored internally by the game. There are a maximum of 0x3f flags reserved for this purpose. They are stored along with other player information during save. (Validation needed) Doors locked in this manor have a sister door that toggles the locked flag by unlocking it. typically the "other side" of the door. In the event the door is unlocked. The game checks the [parameters](#door-event-1) of the event to pull a sound from the room sound table for unlocking the door. Then it will toggle the locked flag. <br><br><br>

---<br><br>## Flag Event
The Flag event is used to modify a flag stored in memory. The event is able to [toggle on or off](#flag-action) a specific [flag number](#flag-number) from one of the [Room flags, Room-Save Flags, and Scenario flags](#flag-id). <br><br><br> <br><br><br>
---
## Structure
### *Header*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='signature'>Signature</span> | string   | AEV | AEV | Signature denoting the begining of the file. Used to validate the data. Null terminated |
| <span id='unknown'>Unknown</span> | byte   |  | 4 | Unknown what this does. Set to 4 most times. |
| <span id='unknown-'>Unknown </span> | byte   |  | 1 | unknown what this does. Set to 1 most times. |
| <span id='count'>Count</span> | byte   |  |  | How many events are in the AEV. Max 127 |
| <span id='padding'>Padding</span> | array : byte [9] |  |  |  |
| <span id='event-entries'>Event Entries</span> | array : Event [Count] |  |  | The array of events contained inside the room. |
### *Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='pointer-to-next'>Pointer To Next</span> | uint32_t   |  |  | This value is populated at run time with the offset to the next entry. |
| <span id='unknown'>Unknown</span> | byte   |  | 1 | Currently unknown |
| <span id='area-hit-type'>Area Hit Type</span> | enum : byte  | {Circle: 0, Square: 1, Eye Trigger: 2} | 1 | Determines if the collision area is rectangular, or a cylindrical. Note "Eye Trigger" has been disabled; however, appears to still have some functionality. |
| <span id='pad'>Pad</span> | array : byte [2] |  |  | 2 bytes padding |
| <span id='y-position'>Y Position</span> | float   |  |  | Starting Y position of the trigger volume |
| <span id='height'>Height</span> | float   |  |  | Height of the trigger volume |
| <span id='position-1'>Position 1</span> | array : float [2] |  |  | Position (x,z) of the first point in the square. Note if Area Hit Type set to Circle this value is (x,z) for the center of the circle. |
| <span id='position-2'>Position 2</span> | array : float [2] |  |  | Position (x,z) of the second point in the square. Note if Area Hit Type set to Circle this value is unused. |
| <span id='position-3'>Position 3</span> | array : float [2] |  |  | Position (x,z) of the third point in the square. Note if Area Hit Type set to Circle this value is unused. |
| <span id='position-4'>Position 4</span> | array : float [2] |  |  | Position (x,z) of the fourth point in the square. Note if Area Hit Type set to Circle this value is unused. |
| <span id='active'>Active</span> | byte   | {Inactive: 2, Active: 3} | 3 | This is used to enable or disable the event. This is used internally to disable an event being interacted with to prevent multiple activations. |
| <span id='type'>Type</span> | enum : byte  | {Normal: 0, Door: 1, Exec: 2, Unused: 3, Flag: 4, Message: 5, Planter: 6, Jump: 7, Save: 8, SHD Display: 9, Damage: 10, SCR_AT: 11, View Control: 12, Field Info: 13, Crouch (Stoop): 14, Small Key: 15, Ladder: 16, Use: 17, Hide: 18, Position Jump: 19, Item Parent: 20} |  | Determines the event type. Each event type has different parameters inside the "buffer" area |
| <span id='index'>Index</span> | byte   |  |  | Index for the current entry in the AEV. |
| <span id='hit-type'>Hit Type</span> | enum : byte  | {under: 0, front: 1, under+angle: 2, front+angle: 3} |  | todo when I can think |
| <span id='trigger-type'>Trigger Type</span> | enum : byte  | {auto: 1, manual: 2, semiauto: 4, action button: 8, onetime: 128} |  | Determines how the event gets triggered. |
| <span id='target-type'>Target Type</span> | enum : byte  | {player: 1, enemy: 2, object: 4, ashlee: 8} |  | Determines which entities can trigger the event. |
| <span id='unknown-'>Unknown </span> | byte   |  |  | Unknown, populated at runtime |
| <span id='unknown--'>Unknown  </span> | array : byte [5] |  |  |  |
| <span id='function-pointer'>Function Pointer</span> | uint32_t   |  |  | Pointer to a hard coded function (assumed to be inside the scenario) associated with the event. |
| <span id='priority'>Priority</span> | byte   |  | 3 | Max 15 |
| <span id='unused-'>Unused </span> | array : byte [3] |  |  |  |
| <span id='hit-angle'>Hit Angle</span> | byte   |  |  | Determines the angle upon which the target should be facing to allow triggering of the event. Only set if Hit Type is one of the +angle variants. |
| <span id='open-angle'>Open Angle</span> | byte   |  |  | Determines "spread" of the view cone when Hit Type is set to a +angle variant |
| <span id='action-type'>Action Type</span> | byte   |  |  | Determines the activation text that gets displayed to screen if Trigger Type is set to manual, semiauto, or action button |
| <span id='padding'>Padding</span> | array : byte [8] |  |  |  |
| <span id='unknown---'>Unknown   </span> | byte   |  |  | This is used by the game at runtime. |
| <span id='padding-'>Padding </span> | array : byte [8] |  |  |  |
| <span id='parameter-buffer-area'>Parameter Buffer Area</span> | array : byte [64] |  |  | This area is multipurpose. Depending on the value of "Type" different parameters will be in here. See the different types below for the structure of each type in this buffer area. |
### *Normal Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='note'>Note</span> |     |  |  | There are no parameters for the Normal Event type. |
### *Door Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='position'>Position</span> | array : float [3] |  |  | (x,y,z) Position in the room being transitioned into. |
| <span id='facing'>Facing</span> | float   |  |  | Desired facing (in degrees) in the room being transitioned into. |
| <span id='next-stage'>Next Stage</span> | byte   |  |  | Stage number for the desired room. |
| <span id='next-room'>Next Room</span> | byte   |  |  | Desired room number for the above Stage. |
| <span id='key-id'>Key ID</span> | enum : byte  | {default: 0, In Lock Close: 1, In Lock Open: 2} |  | Fill this out |
| <span id='flag-number'>Flag Number</span> | byte   |  |  | Determines which lock flag gets checked to see if the door is locked. Max 0x3f |
| <span id='unused'>Unused</span> | array : byte [4] |  |  |  |
| <span id='next-part-number'>Next Part Number</span> | byte   |  |  | Determines which part number in a room to jump to. |
| <span id='key-sound-effect'>Key Sound Effect</span> | byte   |  |  | Determines which sound plays from the room's sound table during unlock. |
| <span id='open-sound-effect'>Open Sound Effect</span> | byte   |  |  | Determines which sound plays from the room's sound table during opening. |
| <span id='fade-effect'>Fade Effect</span> | enum : byte  | {Normal: 1, Fade: 2, Black: 3} |  | Determines the effect used after interacting with the door. Normal is the zoom effect. |
### *Execute Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='note'>Note</span> |     |  |  | There are no parameters for the Execute Event type. |
### *Flag*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='flag-id'>Flag ID</span> | enum : byte  | {Room Flag: 0, Room Save Flag: 1, Scenario Flags: 2} |  | Determines where the flag that is being toggled is located. |
| <span id='flag-action'>Flag Action</span> | enum : byte  | {Turn On: 0, Turn Off: 1} |  | Determines if the flag is being set, or unset. |
| <span id='flag-number'>Flag Number</span> | uint16_t   |  |  | Determines which flag is being toggled. Max 0xFF |
### *Message Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='message-type'>Message Type</span> | enum : uint16_t  | {Room Message: 0, Common Message: 1} |  | todo |
| <span id='message-number'>Message Number</span> | uint16_t   |  |  | Determines which line is grabbed from the MDT file |
| <span id='camera-number'>Camera Number</span> | byte   |  |  | Determines which index from the CAM to use when interacting with the message. |
| <span id='sound-effect-type'>Sound Effect Type</span> | enum : byte  | {Room: 0, Player: 1} |  | Determines if the sound is pulled from the room, or the player sound table. |
| <span id='sound-effect-number'>Sound Effect Number</span> | byte   |  |  | Determines which sound to be pulled from the sound table. |
### *Jump Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='note'>Note</span> |     |  |  | This event doesn't work. The parameters are known; however, in game the event doesn't trigger. |
| <span id='position'>Position</span> | array : float [3] |  |  | Position to jump to (x,y,z) |
### *Save Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='terminal-number'>Terminal Number</span> | uint32_t   |  |  | unknown what this does. Max 10 |
### *SHD Display Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='shd-number'>SHD Number</span> | uint16_t   |  |  | Determines which SHD index to toggle. |
| <span id='display-flag'>Display Flag</span> | enum : byte  | {False: 0, True: 1} |  | Determines if the SHD is being toggled on, or toggled off. |
### *Damage Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='damage-timer'>Damage Timer</span> | uint32_t   |  |  | Determines the durations between stacking damage. |
| <span id='damage-type'>Damage Type</span> | enum : byte  | {No Hit: 0, Fire: 1, Electricity: 2, Env Light: 3, Env Fire: 4, Grenade Blast: 5, Push: 6} |  | Determines what type of damage is being applied. |
| <span id='flags'>Flags</span> | enum : byte  | {Damage Die Flag: 1, Damage Angle Set: 2} |  | Todo |
| <span id='unused'>Unused</span> | array : byte [2] |  |  |  |
| <span id='damage'>Damage</span> | uint32_t   |  |  | Determines how much damage is applied |
| <span id='damage-angle'>Damage Angle</span> | uint32_t   |  |  | Determines the knock back angle when "Damage Angle Set" flag is active |
### *SCR_AT Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='note'>Note</span> |     |  |  | Todo |
### *View Control Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='note'>Note</span> |     |  |  | While the parameters are known, it doesn't appear as though this type is functional |
| <span id='position'>Position</span> | array : float [3] |  |  | TODO |
| <span id='angle-y'>Angle Y</span> | float   |  |  | TODO |
| <span id='unknown'>Unknown</span> | byte   |  |  | unknown |
| <span id='type'>Type</span> | array : byte  | {Unknown_0: 0, Unknown_1: 1} |  |  |
| <span id='radius'>Radius</span> | float   |  |  | TODO |
| <span id='out-range'>Out Range</span> | float   |  |  | TODO |
### *Field Info*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='field-id'>Field ID</span> | uint32_t   |  |  | Max 3 |
### *Ladder Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='position'>Position</span> | array : float [3] |  |  | Position of the ladder (x, y, z) |
| <span id='angle'>Angle</span> | float   |  |  | Angle of approach for the ladder. |
| <span id='height'>Height</span> | uint32_t   |  |  | height of the ladder |
| <span id='cam-indexes'>Cam Indexes</span> | array : byte [3] |  |  | Indexes of the CAM to be used when accending ladder. |
### *Use Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='use-id'>Use ID</span> | uint32_t   |  |  | Item ID to be used. |
### *Hide Event*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='type'>Type</span> | byte   | 3 | 3 | 3 is the only value that can be used here. |
| <span id='hide-position-set'>Hide Position Set</span> | byte   | 1 | 1 | Flag is set so long as there is a hide position assigned |
| <span id='hide-area-set'>Hide Area Set</span> | byte   | 1 | 1 | Flag is set so long as there is a Hide Area assigned |
| <span id='active'>Active</span> | byte   |  |  | Use internally by the game to determine if ashlee is currently hiding in the area. If she is hiding the value is 2 |
| <span id='hiding-position'>Hiding Position</span> | array : float [8] |  |  | 4 points that make up the Hiding Position area |
| <span id='hiding-position-y'>Hiding Position Y</span> | float   |  |  | Y coordinate of the Hiding Position |
| <span id='height'>Height</span> | float   |  |  | Height of the Hiding Position |
| <span id='hiding-area'>Hiding Area</span> | array : float [3] |  |  | Position (x, y, z) of the hiding area |
