# Takoboto to Anki

This is a small script that converts a Takoboto .csv to .txt files that Anki will accept. It will make cards like this:

```
        Front               Back
 _________________    _________________
| Kanji, hiragana |  | Kanji, hiragana |
|                 |  | --------------- |
|                 |  |     meaning     |
|                 |  | more meaning    |
|_________________|  |_________________|

```

I'll probably add an option to have kanji only on the front and hiragana on the back. If you find this and want that, open an issue and I'll get on it asap.

### Usage

#### The Takoboto csv

You can get a .csv file from Takoboto by going into your lists, hitting the menu button and selecting "Export to file...". It ends up in Download/Takoboto/Takoboto.[date-time].csv. Which I think isn't even the Downloads folder but some sad non-pluralised lonely thing. This makes it trickier to move the file, but just use some file explorer and put it in your Dropbox or something.

#### The script

First you need to edit the script to define which lists you want to put in which deck. Here's an example of my setup:

```
deck_lists = {
        'takoboto0': [u'東京0', u'東京1', u'SHOULD PRACTICE'],
        'takobotoFav': [u'Favorites'],
        'takoboto3': [u'東京2', u'東京3']
        }
```

For example, "takoboto3" is the name of my deck, and I want the lists "東京2" and "東京3" in that deck. This accepts Japanese characters, as long as you keep the `u` before the quotes. Avoid looking at the rest of the code if you like PEP8.

Then, just place the script in the same folder as your Takoboto file, and run it. It will create one text file for each deck, named for example "takoboto3.txt". The script always picks out the latest Takoboto file so you can keep as many as you want in the folder. I keep it all in a Dropbox folder.

#### The Anki import

Open up the Anki desktop app, select "Import file", pick one of your .txt files, make sure you have the right deck selected and check the "Allow HTML in fields" box. Hit Import. Do this for all your decks. Sync it up and sync it down to your phone, and you're done!

### Stuff 

I kinda wanted to automate more parts of this but after consulting [this chart](https://xkcd.com/1205/) I decided not to. You can go through this as often as you like, Anki is very kind about filtering out cards you already have so you won't get duplicates.

頑張って！

 
