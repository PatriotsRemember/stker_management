 
import os
from os import listdir
from os.path import isfile, join
import sys

STICKER_DIRECTORY = './data_sources/stickers'
CAMPAIGN_DIRECTORY = './data_sources/stickers'

class StickerPrinter:

    def __init__(self, campaign_dir=CAMPAIGN_DIRECTORY):
        self.campaign_dir = campaign_dir

    def list_campaigns(self):
        print(listdir(self.campaign_dir))

    def print_campaign(self, campaign_name='test', print_num=1):
        onlyfiles = [f for f in listdir(self.campaign_dir) if isfile(join(self.campaign_dir, f))]
        for f in listdir(self.campaign_dir):
            if isfile(join(self.campaign_dir, f)) and campaign_name in f:
                num_ids = []
                with open(join(self.campaign_dir, f)) as f:
                    num_ids = f.readlines()
                clean_num_ids = []
                for element in num_ids:
                    clean_num_ids.append(element.strip())
                clean_num_ids = list(filter(None, num_ids))
                self.print_stickers(clean_num_ids, print_num)

    def print_stickers_by_id(self, num_ids, print_num=1):
        sticker_files = []
        for nid in num_ids:
            sticker_files.append(f'{STICKER_DIRECTORY}/{nid}*')
        sticker_files = " ".join(sticker_files)
        string = f'lp -n {print_num} {sticker_files}'
        os.system(string)


# Here, we are checking if the script was called directly (as opposed to being imported)
# i.e. when you call 'python3 sticker_printer.py' , name will be main
if __name__ == '__main__':
    actions = ['list_campaigns','from_campaign','from_ids','from_range']
    args = sys.argv
    sp = StickerPrinter()
    if args[1] == 'list_campaigns':
        sp.list_campaigns()
    elif args[1] == 'from_campaign':
        name = args[2]
        num_to_print = 1
        if len(args) == 4:
            num_to_print = args[3]
        sp.print_campaign(name, num_to_print)
    elif args[1] == 'from_ids':
        sticker_numbers = args[2:]
        sp.print_stickers_by_id(sticker_numbers)
        num_to_print = 1
        sp.print_stickers_by_id(sticker_numbers, num_to_print)
    elif args[1] == 'from_range':
        beginning_rng = args[2]
        ending_rng = args[3]
        num_to_print = 1
        if len(args) == 5:
            num_to_print = int(args[4])
        sticker_numbers = range(int(beginning_rng), int(ending_rng))
        sp.print_stickers_by_id(sticker_numbers, num_to_print)
    else:
        print("BAD ARGUMENT SUPPLIED: Must choose an action from this list")
        print(actions)
