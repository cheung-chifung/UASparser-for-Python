#!/usr/bin/python
from pprint import pprint
from uasparser import UASparser


def main():
    uas_parser = UASparser('.')
    ua = 'SonyEricssonK750i/R1L Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1'
    print('User Agent: {0}'.format(ua))
    # only 'ua_icon' or 'os_icon' or both are allowed in entire_url
    result = uas_parser.parse(ua, entire_url='ua_icon,os_icon')
    pprint(result)

if __name__ == '__main__':
    main()
