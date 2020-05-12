# Getting Started
![app-preview](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/beta1.7.3-preview.png "App Preview")
## Dependancies
This app requires third party software such as listed below:
* [Imagemagick](https://imagemagick.org/script/download.php)
  For Windows 32-bit: **Imagemagick-7.0.x.x-Q16-x86-dll.exe**
  For Windows 64-bit: **Imagemagick-7.0.x.x-Q16-x64-dll.exe**
* [Photoshop](https://www.adobe.com/products/photoshop.html)\
  **NOTE**: 
  *I haven't tried using other Photoshop other than CS6, so it probably not going to work on all Photoshop version*
## Instruction
If you wanted to generate textures, please follow this [instruction](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/INSTRUCTION.md#generate-textures) first.
### Usage
1. Go to [release page](https://github.com/severusDude/BF2Dynamic-Indication-Generator/releases) and download the latest version.
2. Place the app inside [directory structure similar to this](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/INSTRUCTION.md#structure).
2. Fill text field with the weapon you want to register.
3. Scripts will be generated by default but can be disable by user.
4. Texture generating is optional and disabled by default.
5. When generating, a compressed files containing unmodified files will be generated.
6. After a succesfull generate, a notification window will be appear.
7. Re-examine files before you applied them to your mod.

### Batch processing
To use batch processing, please refer to [**Batch processing guide**](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/README_BATCH.md).

**CAUTION**
* *Generating texture will be memory consuming, make sure you close apps you don't need.*
* *If both options is checked, there will two different succesfull generate notification window, don't close app before the second one appear.*

### Options
1. If generate scripts option is checked(*by default*), files named as below will be opened and modified
   * CustomizeIndication1-6Weapon.con
   * HudElementsAttackerWeapon.con
   * scoring_wpn.py
2. If generate textures option is checked, photoshop will be run and files named as below will be opened, modified and exported as .dds file
   * Indicationweapon.psd
   * KilledIndicationWeapon.psd

### Structure
* [your directory/]()
  * [Crypter.exe]()
  * [HUD/]()
    * [HudSetup/]()
      * [KillText/]()
        * [CustomizeIndication1Weapon.con]()
        * [CustomizeIndication2Weapon.con]()
        * [CustomizeIndication3Weapon.con]()
        * [CustomizeIndication4Weapon.con]()
        * [CustomizeIndication5Weapon.con]()
        * [CustomizeIndication6Weapon.con]()
        * [HudElementsAttackerWeapon.con]()
  * [game/]()
    * [scoring_wpn.py]()
  * [psd/]()
    * [Indicationweapon.psd]()
    * [KilledIndicationWeapon.psd]()

### Generate Textures
Before you generate textures, please follow this instruction.
1. Open Indicationweapon.psd file from [Dynamic Indication mod](https://www.moddb.com/mods/dynamic-indication-v40-released) with Photoshop, I will use Photoshop CS6.\
   ![step-1](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial1.png "Step 1")
2. Double click the most top layer and change it name into ***Shade***.\
   ![step-2](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial2.png "Step 2")
3. Select text and change it alignment to right.\
   ![step-3](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common.images/psd-tutorial/psd-tutorial3.png "Step 3")
4. Double click the second to top layer and change it name into ***Main***.\
   ![step-4](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial4.png "Step 4")
5. Select text and change it alignment to right.\
   ![step-5](https://gihub.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial5.png "Step 5")
6. Select 3 layers.\
   ![step-6](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial6.png "Step 6")
7. Align them to right edges.\
   ![step-7](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial7.png "Step 7")
8. Hide the black colored box layer.\
   ![step-8](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial8.png "Step 8")
9.  Save and close the psd file.\
   ![step-9](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial9.png "Step 9")
10. Open KilledIndicationWeapon.psd file from [Dynamic Indication mod](https://www.moddb.com/mods/dynamic-indication-v40-released).\
   ![step-10](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial10.png "Step 10")
11. Double click the most top layer and change it name into ***Shade***.\
   ![step-11](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial11.png "Step 11")
12. Select text and change it allignment to left.\
   ![step-12](https://gtihub.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial12.png "Step 12")
13. Double click second most top layer and change it name into ***Main***.\
   ![step-13](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial10.png "Step 13")
14. Select text and change it allignment to left.\
   ![step-14](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial14.png "Step 14")
15. Select the 3 layers.\
   ![step-15](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial15.png "Step 15")
16. Align them to the left edges.\
   ![step-16](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial16.png "Step 16")
17. Hide the black colored box layer.\
   ![step-17](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial17.png "Step 17")
18. Save and close the psd file.\
   ![step-18](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/common/images/psd-tutorial/psd-tutorial18.png "Step 18")