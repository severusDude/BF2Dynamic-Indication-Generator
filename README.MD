# AGM114D Dynamic Indication script generator

Handy tool that automatically generate required AGM114D Dynamic Indication mod script, such as:
* **HudElementsIndication1-6.con**
* **HudElementsAttackerWeapon.con**
* **weapons.py**
 
## Usage
### Instruction
1. Go to release page
2. Download the lastest release(**Crypter.exe**)
3. Place it on a directory alongside with see ***Structure***
4. Run the file
5. Fill all the input correspond to your wanted\
   **warning**\
   see ***Weapon Index fill***
6. Press the generate button
7. Pray it work

### Weapon index fill
To fill weapon index there is certain guide
1. see your weapons.py and go to the most bottom.
2. if you have standard weapons.py *(not changed)* the most bottom should be\
   "tnk_type98"         : 160,		 # ZTZ98 MBT.
3. as you can tell, tnk_type98 have number of 160, the number should be the highest since it placed on the most bottom.
4. but i advise to search the highest number possible
5. after you have found it, the weapon index you should be input is 1 value larger.

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


**CAUTION**\
*My code is trash, so better to check the files after generating. but atleast it work afaik.*

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

## Author
* [severusDude](https://github.com/severusDude) - Bluenix_Indo(ModDB)

## License
This project is licensed under the GNU General Public License v3.0 License - see the LICENSE.md file for details

