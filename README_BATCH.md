# Getting started
## Write a batch set
### Create batch set file
1. Create a new .txt file.
2. Open it.
3. Add activate on the first line.
4. Save the file.

**NOTE**\
*After you write activate on the first line, the file is now considered a valid batch set.*
### Decide item for batch set
1. Start by find the weapons you wanted to add to your batch set.
2. To do this, simply navigate through your weapons folder.
3. The .tweak file name is what you are looking for, example.\
   ```bf4_ak47.tweak```
4. Try to remember it, or just write it on a note
5. Decide your name pick for the indication, for example.\
   ```AK-47```
### Write picked item to batch set
1. Start by adding brackets, example\
   ```[] ()```
2. Note that the there is two brackets and it separated by whitespace, the square bracket contain the ***Indicator***, while round brackets contain the ***The name of the weapon***
3. By following the principle, your weapon item should look like this\
   ```[AK-47] (bf4_ak47)```
4. If you still unsure, check the see [batch set example](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/batch/batch-test.txt)
5. That should be the end of the tutorial.

## Generate created batch set
1. Go to batch page, which is a button with **BATCH** text on it
2. Open batch set file using **OPEN FILE** button
3. Select your batch set file
4. If the text next to the button say\
   ```Batch file is active```\
   you can then continue
5. If it say otherwise, please check [batch set file requirment](https://github.com/severusDude/BF2Dynamic-Indication-Generator/blob/master/README_BATCH.md#create-batch-set-file)
6. Before generating, you need to fill **STARTING INDEX** input
7. The input will be a starting point for the index
8. Please see the [rules](https://github.com/severusDude/BF2Dynamic-Indication-Generator#weapon-index-fill) to fill the input
9. Hit the **START BATCH** button
10. A compressed backup file will be generated at *Backups* folder