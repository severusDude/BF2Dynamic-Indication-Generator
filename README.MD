# [AGM114D Dynamic Indication](https://www.moddb.com/mods/dynamic-indication-v40-released) script generator

![app preview](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/v1.1.2-beta/common/images/beta1.0.0%20preview.png "App Preview")

Handy tool that automatically generate required [AGM114D Dynamic Indication mod](https://www.moddb.com/mods/dynamic-indication-v40-released) script, such as:
* **HudElementsIndication1-6.con**
* **HudElementsAttackerWeapon.con**
* **weapons.py**

## Features
* Automatic generate scripts on:
  * **HudElementsIndication1-6.con**
  * **HudElementsAttackerWeapon.con**
  * **weapons.py**\
  *it mean, you don't need to worry about write the required scripts anymore*
* Automatic backup everytime you generate with limiter
* [Batch Processing](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/README_BATCH.md)
 
## Usage
### Batch Processing
For more detail about batch processing, visti [README_BATCH.md](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/README_BATCH.md)
### Instruction
1. Go to [release page](https://github.com/severusDude/BF2Dynamic-Indication-Generator/releases)
2. Download the lastest release(**Crypter.exe**)
3. Place it on a directory alongside with [**Structure**](https://github.com/severusDude/BF2Dynamic-Indication-Generator#structure)
4. Run the file
5. Fill all the input correspond to your wanted with inputting weapon index follow the rule [**Weapon index fill**](https://github.com/severusDude/BF2Dynamic-Indication-Generator#weapon-index-fill)
6. Press the generate button
7. It should pop up a notification window after generating was succesfull
   
### Example
**Your input should look like this**\
![fill_inputfield](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/v1.1.2-beta/common/images/beta1.0.0%20fill%20input.png "Input examples")

**After succesfull generating**\
![succes_generate](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/v1.1.2-beta/common/images/beta1.0.0%20succes%20generate.png "Succesfull generate")



**CAUTION**\
*My code is trash, so better to check the files after generating. but atleast it work afaik*\
*but if it isn't working the way it should, there should a compress file inside backups, pick the most recent one*
### Weapon index fill
To fill weapon index there is certain guide
1. see your weapons.py and go to the most bottom.
2. if you have standard weapons.py *(not changed)* the most bottom should be\
   `"tnk_type98"         : 160,		 # ZTZ98 MBT`
3. as you can tell, tnk_type98 have number of 160, this number should be the highest since it placed on the most bottom.
4. but i advise to search the highest number possible
5. after you have found it, the weapon index you should be input is 1 value larger.
   
**Note**\
The program will really appreciate you if everytime the index you generate is in order, not with random number

### Structure
Place the **Crypter.exe** inside directory with structure like shown below

* [yourdirectory]()
  * [Crypter.exe]()
  * [game/]()
    * [weapons.py]()
  * [HUD/]()
    * [HudSetup/]()
      * [KillText/]()
        * [HudElementsAttackerWeapon.con]()
        * [HudElementsIndication1.con]()
        * [HudElementsIndication2.con]()
        * [HudElementsIndication3.con]()
        * [HudElementsIndication4.con]()
        * [HudElementsIndication5.con]()
        * [HudElementsIndication6.con]()

### Known issue
* Program break if weapon index inputed does not stack, this is due to the way generating dictionary item\
  *Example: from index 160 to 234*
* backup will be overwrite if generate multiple time on the same time without using batch option
  *Example: generate two times at 11:14*



## Getting started

### Clone
Clone this repository by writing
`https://github.com/severusDude/BF2Dynamic-Indication-Generator.git`

### Setup
Install the pyqt5 framework from pip by using\
`pip install pyqt5`\
and install the qdarkstyle stylesheet by using\
`pip install qdarkstyle`

## Built with
* [pyqt5](https://pypi.org/project/PyQt5/) - The app framework used
* [qdarkstyle](https://pypi.org/project/QDarkStyle/) - The app stylesheet used

**NOTE**  
*This project made with python version 3.7.2*

## Credit
* [Leeberty](https://www.moddb.com/members/leeberty) - Original author of [Dynamic indication mod](https://www.moddb.com/mods/dynamic-indication-v40-released)

## Author
* [severusDude](https://github.com/severusDude)/[Bluenix_indo(ModDB)](https://www.moddb.com/members/bluenix-indo) - Original author

## License
This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) License - see the [LICENSE.md](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/LICENSE) file for details

