What is UASparser for Python
============================

UASparser for Python is a UserAgent string analyzer
[UASParser](http://user-agent-string.info/download/UASparser) in
Python version。

Features
========

 * Auto fetch the latest version of [uas.ini](http://user-agent-string.info/rpc/get_data.php?key=free&format=ini&download=y|uas.ini) from the remote server and cache it.
 * Faster than online version and PHP version

Usage
=====

    #!/usr/bin/python
    from uasparser import UASparser

    #set a custom writable cache folder or use the folder where the script locate 
    uas_parser = UASparser('/path/to/your/cache/folder')

    #useragent: The UserAgent String
    #entire_url: Optional,please set to the key label which need to return entire url.Excepted 'ua_icon' or 'os_icon' or both,split by comma.
    result = uas_parser.parse('YOUR_USERAGENT_STRING',entire_url='ua_icon,os_icon')

Return
======

    return = {
               'typ':'unknown',                  #Type
               'ua_family':'unknown',            #UserAgent's family
               'ua_name':'unknown',              #UserAgent's name,version included
               'ua_url':'unknown',               #UserAgent's offical website
               'ua_company':'unknown',           #UserAgent's company
               'ua_company_url':'unknown',       #UserAgent's company offical website
               'ua_icon':'unknown.png',          #UserAgent's icon,if 'ua_icon' in entire_url，then return entire url
               'ua_info_url':'unknown',          #UserAgent's info url（http://user-agent-string.info）。
               'os_family':'unknown',            #OS's family
               'os_name':'unknown',              #OS's name,version included
               'os_url':'unknown',               #OS's offical website
               'os_company':'unknown',           #OS's company
               'os_company_url':'unknown',       #OS's company offical website
               'os_icon':'unknown.png',          #OS's icon，if 'os_icon' in entire_url，then return entire url
               }

Example
=======

    #!/usr/bin/python
    from uasparser import UASparser
    uas = UASparser()
    test = ['SonyEricssonK750i/R1L Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-GB; rv:1.8.1.18) Gecko/20081029 Firefox/2.0.0.18',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; en-us) AppleWebKit/525.26.2 (KHTML, like Gecko) Version/3.2 Safari/525.26.12',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows XP 5.1) Lobo/0.98.4',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; )',
        'Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.2.15 Version/10.00',
        'boxee (alpha/Darwin 8.7.1 i386 - 0.9.11.5591)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; CSM-NEWUSER; GTB6; byond_4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 1.1.4322; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; InfoPath.1)',
        'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)',
        ]

    for item in test:
        res = uas.parse(item)
        print "---%s: %s @ %s" % (res['typ'],res['ua_name'],res['os_name'])

Return

    hermes@localhost ~/Desktop $ python sample.py
    ---Mobile Browser: SEMC Browser 4.2 @ JVM (Java)
    ---Browser: Firefox 2.0.0.18 @ Windows 2003 Server
    ---Browser: Safari 3.2 @ Mac OS X
    ---Browser: IE 6.0 @ Windows XP
    ---Browser: IE 7.0 @ Windows XP
    ---Browser: Opera 9.80 @ Windows XP
    ---Multimedia Player: Boxxe 0.9.11.5591 @ unknown
    ---Browser: IE 8.0 @ Windows XP
    ---Robot: Yahoo! Slurp @ unknown
