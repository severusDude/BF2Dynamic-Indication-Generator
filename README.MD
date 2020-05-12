# [AGM114D Dynamic Indication](https://www.moddb.com/mods/dynamic-indication-v40-released) generator

![app-preview](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/beta1.7.3-preview.png "App Preview")

Handy tool that automatically generate required [AGM114D Dynamic Indication mod](https://www.moddb.com/mods/dynamic-indication-v40-released) 
## Features
* Automatic generate scripts on:
  * **HudElementsIndication1-6.con**
  * **HudElementsAttackerWeapon.con**
  * **weapons.py**
* Automatic generate textures both Indication and KilledIndication
* Automatic backup everytime you generate with limiter
* [Batch Processing](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/README_BATCH.md)
* Option to either only generate scripts or textures
 
## Usage
To see usage instruction, visit [INSTRUCTION.md](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/INSTRUCTION.md)

## Known issue
* Backup will be overwrite if generate multiple time on the same time without using batch option.\
  *Example: generate two times at 11:14*

## Getting started
### Clone
Clone this repository by writing
`git clone https://github.com/severusDude/BF2Dynamic-Indication-Generator.git`

### Setup
Install packages using\
`pip install pyqt5`\
`pip install qdarkstyle`\
`pip install pywin32`\
`pip install Wand`\
`pip install psd-tools`

### Built with
* [pyqt5](https://pypi.org/project/PyQt5/)
* [qdarkstyle](https://pypi.org/project/QDarkStyle/)
* [pywin32](https://pypi.org/project/pywin32)
* [wand](https://pypi.org/project/Wand)
* [psd-tools](https://pypi.org/project/psd-tools)

**NOTE**  
*This project made with python version 3.7.2*

## Dependancies
This app requires third party software such as listed below:
* [Imagemagick](https://imagemagick.org/script/download.php)\
  For Windows 32-bit: **Imagemagick-7.0.x.x-Q16-x86-dll.exe**\
  For Windows 64-bit: **Imagemagick-7.0.x.x-Q16-x64-dll.exe**
* [Photoshop](https://www.adobe.com/products/photoshop.html)\
  **NOTE**: 
  *I haven't tried using other Photoshop other than CS6, so it probably not going to work on all Photoshop version*

## Credit
* [Leeberty](https://www.moddb.com/members/leeberty) - Original author of [Dynamic indication mod](https://www.moddb.com/mods/dynamic-indication-v40-released)

## Author
* [severusDude](https://github.com/severusDude)/[Bluenix_indo(ModDB)](https://www.moddb.com/members/bluenix-indo) - Original author

## License
This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) License - see the [LICENSE](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/LICENSE) file for details

