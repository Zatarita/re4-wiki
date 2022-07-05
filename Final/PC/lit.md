# AEV


## Structure
### *Header*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='count'>Count</span> | uint16_t   |  |  | Number of Light Groups contained in the LIT |
| <span id='unknown'>Unknown</span> | array : Byte [2] |  |  |  |
| <span id='light-group-offsets'>Light Group Offsets</span> | array : uint32_t [Count] |  |  | The offsets pointing to the start of each Light Group |
### *Light Group*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='parent'>Parent</span> | Light Group Properties   |  |  | Global settings for the current LIT. Also holds Fog, Wind, and Blur settings |
| <span id='light-entry'>Light Entry</span> | array : Light Group Entry [n] |  |  | The definition for each light in the light group. |
### *Light Group Properties*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='scroll-lighting'>Scroll Lighting</span> | Color R8G8B8A8   |  |  | Ambient light color for "Scroll" objects. |
| <span id='unknown'>Unknown</span> | array : Byte [4] |  |  |  |
| <span id='fog-type'>Fog Type</span> | enum : Byte  | {None: 0, Linear: 2, Exponential: 4, Exponential 2: 5, Reverese Exponential: 6, Reverse Exponential 2: 7} |  | Method used to calculate the fog density. |
| <span id='fog-start'>Fog Start</span> | Float   |  |  | Near plane for fog to start at. |
| <span id='fog-end'>Fog End</span> | Float   |  |  | Beyond the end point fog no longer becomes more dense. |
| <span id='fog-color'>Fog Color</span> | Color R8G8B8A8   |  |  | Controls the fog color. |
| <span id='padding'>Padding</span> | array : Byte [3] |  |  |  |
| <span id='mirror-fog-type'>Mirror Fog Type</span> | enum : Byte  | {None: 0, Linear: 2, Exponential: 4, Exponential 2: 5, Reverese Exponential: 6, Reverse Exponential 2: 7} |  |  |
| <span id='mirror-fog-start'>Mirror Fog Start</span> | Float   |  |  | Near plane; Where fog to starts. |
| <span id='mirror-fog-end'>Mirror Fog End</span> | Float   |  |  | Beyond the end point fog no longer becomes more dense. |
| <span id='mirror-fog-color'>Mirror Fog Color</span> | Color R8G8B8A8   |  |  | Controls the mirror fog color. (Research needed) |
| <span id='focus-distance'>Focus Distance</span> | uint32_t   |  |  | Sets the blur focal distance. |
| <span id='focus-level'>Focus Level</span> | uint16_t   |  |  | Sets the blur iterations. |
| <span id='focus-mode'>Focus Mode</span> | enum : Byte  | {Near: 0, Far: 1, Follow Player Near: 2, Follow Player Far: 3} |  |  |
| <span id='blur-rate'>Blur Rate</span> | Byte   |  |  |  |
| <span id='lit-tuning-target'>LIT Tuning Target</span> | Byte   |  |  | Determines if the game uses the Core or the Room lit for ambient tuning. |
| <span id='room-light-tuning-color'>Room Light Tuning Color</span> | Color R8G8B8A8   |  |  | Adjusts the light colors for each child light group in the room. |
| <span id='room-ambient-tuning-color'>Room Ambient Tuning Color</span> | Color R8G8B8A8   |  |  | Adjusts the light colors for each child light group in the room. |
| <span id='room-effect-tuning-color'>Room Effect Tuning Color</span> | Color R8G8B8A8   |  |  | Adjusts the light colors for each child light group in the room. |
| <span id='model-tev-scale-multiplier'>Model Tev Scale Multiplier</span> | enum : Byte  | {1x: 0, 2x: 1, 4x: 2} |  | Model lighting multiplier. |
| <span id='player-tev-scale-multiplier'>Player Tev Scale Multiplier</span> | enum : Byte  | {1x: 0, 2x: 1, 4x: 2} |  |  |
| <span id='padding-'>Padding </span> | array : Byte [2] |  |  |  |
| <span id='far-play'>Far Play</span> | Float   |  |  | Adjusts how the game culls distant objects. |
| <span id='hokan'>Hokan</span> | Byte   |  |  |  |
| <span id='unknown-'>Unknown </span> | array : Byte [164] |  |  |  |
| <span id='wind-direction'>Wind Direction</span> | Byte   |  |  | Wind direction. (0x80 = π = 180°; 0xFF = 2π = 360°) |
| <span id='wind-power'>Wind Power</span> | Byte   |  |  | Wind Power (1 = 0.20 units) |
| <span id='wind-frequency'>Wind Frequency</span> | Byte   |  |  | Frequency of "gusts" of wind. (1 = 0.01 units) |
| <span id='padding--'>Padding  </span> | Byte   |  |  |  |
| <span id='blur-type'>Blur Type</span> | enum : Byte  | {Normal: 0, Spread: 1, Add: 2} |  | Blur type used by the game filter. |
| <span id='blur-power'>Blur Power</span> | Byte   |  |  | Strength of the blur. |
| <span id='mipmap-min-lod'>Mipmap Min LOD</span> | Byte   | Must be less than the Mipmap Max LOD level |  | Sets the minimum LOD state of objects in the LIT |
| <span id='mipmap-max-lod'>Mipmap Max LOD</span> | Byte   | Must be greater than the Mipmap Max LOD level |  | Sets the maximum LOD state of objects in the LIT |
| <span id='anisotropic-filter-format'>Anisotropic Filter Format</span> | enum : Byte  | {GX_ANISO_1: 0, GX_ANISO_2: 1, GX_ANISO_4: 2} |  | Sets the Anisotropic Filtering format. |
| <span id='contrast-level'>Contrast Level</span> | Byte   |  |  | Sets the contrast settings for the current Light Group. |
| <span id='contrast-power'>Contrast Power</span> | Byte   |  |  | Sets the contrast power for the current Light Group. ** TODO ** Update this with something substantial |
| <span id='contrast-bias'>Contrast Bias</span> | Byte   |  |  | Adjusts the bias for the current Light Group settings. ** TODO ** Update this with something substantial |
| <span id='lod-bias'>LOD Bias</span> | Byte   |  |  | biases the LOD settings one way or the other. |
| <span id='ambient-enemies-and-objects-color'>Ambient Enemies And Objects Color</span> | Color R8G8B8A8   |  |  | Tunes the lighting towards enemies and objects for the light group. |
| <span id='ambient-effects-color'>Ambient Effects Color</span> | Color R8G8B8A8   |  |  | Tunes the lighting towards effects for the light group. |
### *Light Group Entry*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='activated'>Activated</span> | Byte   |  |  | Activated? |
| <span id='light-type'>Light Type</span> | enum : Byte  | {Constants: 0, Linear: 1, Quadratic: 2, Spotlight: 3, Custom: 4, Parallel: 5, Spot Quad: 6, Local Ambient: 7} |  |  |
| <span id='light-attributes'>Light Attributes</span> | enum : Byte  | {Normal: 0, Flicker: 1, Wave: 2, Spot Rotate: 3, Shadow: 4, Path: 5, Fade: 6, Shine: 7} |  | Controls attributes related to the light. |
| <span id='light-mask'>Light Mask</span> | flag : Byte  | {Player: 1, Enemy: 2, Object: 4, Effect: 8, Ambient: 16, Item: 32, Sub Character: 64, Thermo: 128} |  | Controls what objects are effected by the light entry. |
| <span id='position'>Position</span> | array : Float [3] |  |  | (X, Y, Z) location for the light. |
| <span id='radius'>Radius</span> | Float   |  |  | The extents of the lights reach. |
| <span id='light-color'>Light Color</span> | R8G8B8A   |  |  | Emitted color from the light. |
| <span id='intensity'>Intensity</span> | Float   |  |  | Intensity of the light emitted from the entry. |
| <span id='parent'>Parent</span> | enum : Byte  | {World: 0, Enemy: 1, Scroll: 2, ETC Model: 3, Object: 4} |  | Links the light's position to an entity's position in the scene. |
| <span id='subgroup'>Subgroup</span> | Byte   |  |  | Add's the light to a "layer" that can be toggled somehow **TODO** |
| <span id='attributes'>Attributes</span> | enum : Byte  | {None: 0, Ignore Tuning: 1, Electric Light: 2, Flashlight: 4} |  | Set's special attributes to influence how the light behaves. |
| <span id='priority'>Priority</span> | Byte   |  |  | Priority determines which lights get calculated when more than 6 lights are effecting an object. |
| <span id='part/bone-number'>Part/Bone Number</span> | Byte   |  |  | When a parent is set this controls bone gets used for parenting |
| <span id='parent-id'>Parent ID</span> | Byte   |  |  | When a parent is set this controls which index is selected from the requested entity. |
| <span id='light-type-parameter-area'>Light Type Parameter Area</span> | array : Bytes [20] |  |  | This area has different parameters in it depending on the Light Type assigned. See below for each structure definition. |
| <span id='unused'>Unused</span> | array : bytes [44] |  |  |  |
| <span id='light-attribute-parameter-area'>Light Attribute Parameter Area</span> | array : Bytes [16] |  |  | This area has different parameters in it depending on the Light Attribute set. See below for each structure definition. |
| <span id='unused-'>Unused </span> | array : Byte [176] |  |  |  |
### *Light Type Constant*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='note'>Note</span> |     |  |  | There are no parameters for the constant light type. |
### *Light Type Linear*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='note'>Note</span> |     |  |  | There are no parameters for the Linear light type. |
### *Light type Quadratic*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='smooth-edge'>Smooth Edge</span> | Float   |  |  |  |
### *Light Spot Light*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='position'>Position</span> | array : Float [3] |  |  | (x, y, z) Position for the spot light |
| <span id='range'>Range</span> | Float   | > 1.0 |  | How far the spotlight can reach. Must be greater than 1 |
| <span id='smooth-edges'>Smooth Edges</span> | Float   |  |  |  |
### *Light Local Ambient*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='smooth-edges'>Smooth Edges</span> | Float   |  |  |  |
### *Attribute Type Flicker*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='color'>Color</span> | R8G8B8A   |  |  | Color that is shifted between with the main color to create the flicker effect. |
| <span id='range'>Range</span> | Float   |  |  | Intensity of the "flickering" effect |
### *Attribute Type Wave*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='center'>Center</span> | Float   |  |  | Adjusts the midpoint of the wave function. |
| <span id='range'>Range</span> | Float   |  |  | Adjusts the spread of the wave function. Increates intensity. |
| <span id='speed'>Speed</span> | Float   |  |  | Adjusts the period of the wave function. |
| <span id='position'>Position</span> | Float   |  |  | Current position of the wave function. Used by the game at runtime. |
### *Attribute Type Rotate*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='rotation'>Rotation</span> | array : Float [3] |  |  | Adjusts the X, Y Rotation of the light over time. Z parameter doesn't effect the final product. |
### *Attribute Type Shadow*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='flags'>Flags</span> | enum : Byte  | {No TEX: 0, Use TEX: 1, Invert TEX: 2} |  | If Shadow Type is anything but Normal, or Foot "Use TEX" must be true. |
| <span id='shadow-type'>Shadow Type</span> | enum : Byte  | {Normal: 0, Cast: 1, Cast Add: 2, Cast 2: 3, Cast Add 2: 4, Foot: 5} |  |  |
### *Attribute Type Path*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='start'>Start</span> | uint32_t   |  |  |  |
| <span id='position'>Position</span> | uint32_t   |  |  |  |
| <span id='flags'>Flags</span> | enum : Byte  | {None: 0, Loop: 1, Inverse: 2} |  | Flags that augment how the path is processed. |
| <span id='path-index'>Path Index</span> | byte   |  |  | When there are multiple sub paths in the current path being used. This specifies the index for the desired path. |
### *Attribute Type Fade*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='start'>Start</span> | Float   |  |  | Starting point for the fade effect |
| <span id='speed'>Speed</span> | Float   |  |  | Speed upon which the light fades. |
### *Attribute Type Shine*


| <span style="display: inline-block; width:100px">Field</span> | <span style="display: inline-block; width:200px">Type</span> | <span style="display: inline-block; width:100px">Legal Values</span> | <span style="display: inline-block; width:100px">Default Value</span> | Comment |
| :- | :- | :-: | :- | :- |
| <span id='current-position'>Current Position</span> | array : Float [3] |  |  | Used internally by the game to keep track of how far through the shine animation the current LIT entry is. |
| <span id='speed'>Speed</span> | array : Float [3] |  |  | Determines how quickly the the shinning happens on each axis (except for the z axis) |
