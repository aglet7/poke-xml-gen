from pokemontcgsdk import *
import os

def write_set(f, s):
    name = s.code.upper()
    long_name = s.name
    date = s.release_date
    series = s.series

    f.write('\t\t<set>\n')
    f.write('\t\t\t<name>%s</name>\n' %name)
    f.write('\t\t\t<longname>%s</longname>\n' %long_name)
    f.write('\t\t\t<settype>%s</settype>\n' %series)
    f.write('\t\t\t<releasedate>%s</releasedate>\n' %date)
    f.write('\t\t</set>\n')

def write_card(f, c):
    name = c.name
    print(name)
    picurl = c.image_url_hi_res
    set_name = c.set_code.upper()
    f.write('\t\t<card>\n>')
    f.write('\t\t\t<name>%s-%s</name>\n' %(name, set_name))
    f.write('\t\t\t<set picurl="%s">%s</set>\n' %(picurl, set_name))
    f.write('\t\t\t<color>Water</color>\n')
    f.write('\t\t\t<manacost></manacost>\n')
    f.write('\t\t\t<cmc></cmc>\n')
    f.write('\t\t\t<type>Pokemon - Stage 1</type>\n')
    f.write('\t\t\t<tablerow>0</tablerow>\n')
    f.write('\t\t\t<text></text>\n')
    f.write('\t\t\t<font></font>\n')
    f.write('\t\t</card>\n>')

def main():
    print('Starting Script')

    sets = Set.all()
    cards = Card.all()
    print('Cards loaded.')

    fp = 'poketcg.xml'
    if os.path.exists(fp):
        os.remove(fp)
    with open(fp, 'x', encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<cockatrice_carddatabase version="3">\n')
        f.write('\t<sets>\n')
        print('Writing Sets...')
        for s in sets:
            write_set(f, s)
        f.write('\t</sets>\n')

        f.write('\t<cards>\n')
        print('Writing Cards...')
        for c in cards:
            write_card(f, c)
        f.write('\t</cards>\n')

        f.write('</cockatrice_carddatabase>\n')


if __name__ == '__main__':
    main()