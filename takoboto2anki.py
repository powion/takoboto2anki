# encoding: utf-8
from csv import reader
import os
import glob
import string

deck_lists = {
        'takoboto0': [u'東京0', u'東京1', u'SHOULD PRACTICE'],
        'takobotoFav': [u'Favorites'],
        'takoboto3': [u'東京2', u'東京3']
        }

def make_list2deck():
    list2deck = {}
    for deck in deck_lists:
        for tlist in deck_lists[deck]:
          list2deck[tlist] = deck
        if os.path.exists(deck + '.txt'):
            os.remove(deck + '.txt')
    return list2deck


def process_csv(filename, list2deck):
    with open(filename) as tcsv:
        for line in reader(tcsv):
            list_name = unicode(line[0], 'utf-8')
            if list_name in list2deck:
                with open(list2deck[list_name] + '.txt', 'a') as txt:
                   txt.write(create_ankiline(line))

def create_ankiline(line):
    jap = line[3].split(', , ')[0]
    trans = line[4]
    trans = string.replace(trans, ', , ', '<br><br>')
    return jap + ';' + trans + '\n'


def find_takofile():
    takofiles = glob.glob("Takoboto.*.csv")
    takofiles.sort()
    return takofiles[-1]

def main():
    process_csv(find_takofile(), make_list2deck())
    print('Done!')

main()
