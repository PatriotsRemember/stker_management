# stker_management

## Purpose

Want to print things quickly and efficiently?

Do you have a linux operating system?

Then you've come to the right place :)

... In this repository you will find a simple script that takes advantage of the native linux 'lp' printing command, allowing you to print pictures very quickly, in whatever quantity you want.

I say stickers, I use jpgs as examples - but you could use this script to print whatever you want!

## Requirements

Setup your printer, however you have to do that...

Python3 - this will probably work on python 2.7 but I have not tested.  This script uses the standard python library, you should not have to install any packages.

Linux Operating System (I don't think distribution should matter) - Why? Because this script will call the 'lp' command in order to talk to your default printer, and this command is strictly linux I believe (if for some reason you don't have the 'lp' command already, please conduct an online search on how to install)

## Architecture - What is everything doing?

The python script is simple, it is housed in the file 'sticker_printer.py'

The python script will look for two things: 1) campaign_files (each campaign file is a file listing numbers) and 2) stickers - these are files prefixed with numbers.

The WHOLE idea of this script revolves around number assignment for pictures. Numbers are easier to type than names, if you write the number on the back of a picture it is really easy to reference - then when you want to the print the picture, you just look for the file beginning with that number! 

## Usage

Note: If you do not wish to use the example files, replace the files in the stickers directory with whatever files you want - so long as they are prefixed with numbers, this script will work.

The same can be said of campaigns: if you have many-related files you want to print in unison, you can create your own campaign files and replace the existing ones.  All a campaign file is is a list of numbers, these numbers correlate to filesnames from the stickers directory.

### General

First, copy down this repository - either clone or in the 'code' menu, click 'download zip'

Second, in console/terminal, make sure you are in the same folder/directory as the script.

#### Print 1 copy of several stickers

To print 1 copy of 1 or more stickers, you will use the following command.

For 1 sticker:

```
python3 sticker_printer.py from_ids 21
``` 

For several stickers:
```
python3 sticker_printer.py from_ids 21 34 101
```

#### Print multiple copies of a range of stickers

Want to print your whole sticker set in multiple copies, or maybe just a subset?

This command will allow you to do just that:
```
python3 sticker_printer.py from_range 50 100 2
``` 

^^ In the above command: 50 is the start number for finding files, 100 is the end number, and 2 is the number of copies you would like

#### Print multiple copies of campaigns

As previously described, all a campaign 'is' is a file listing numbers, these numbers are associated with files in the stickers directory.

To print campaigns, use the following command - this example assumes the campaign file is named 'children':
```
python3 sticker_printer.py from_campaign children 
```

If you forget what campaigns exist, use the following command:
```
python3 sticker_printer.py list_campaigns
```



## DISCLAIMER

Is this good code? absolutely not.... We are passing raw arguments to the command line, it would be much better if these were named arguments (i.e. pass a '--num_copies' option for the number of copies, instead of just just numbers running rampant on the command line).


Does it work? Hell yeah.  

Your contributions to make this better are more than welcome
