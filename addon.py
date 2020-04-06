from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://www.listennotes.com/c/r/658b13f1769449f89b937754c17feee4" #HARDCOREHIST
url2 = "https://www.listennotes.com/c/r/74f6f88d4bdc4e5cb2982c50d17295b1" #HARDCOREHIST-ADDENDUM
url3 = "https://www.listennotes.com/c/r/ffb64d537bb14563a648de7772d47334" #COMMONSENSE
url4 = "https://s3-us-west-2.amazonaws.com/stuff-ts/dchh-ep43-47.rss" #WRATHOFKHANS
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://www.dancarlin.com/graphics/DC_HH_iTunes.jpg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/6/b/f/e/6bfe939ed4336498/HHA-1400px_b.jpg"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "http://www.dancarlin.com/graphics/CS_DC_iTunes.jpg"},
        {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://s3-us-west-2.amazonaws.com/hhpodcastcovers/HardcoreHistory-Khans-Series-Dan-Carlin.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(url4)
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items

if __name__ == '__main__':
    plugin.run()
