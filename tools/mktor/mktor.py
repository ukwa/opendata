from makeTorrent import makeTorrent

mk = makeTorrent(
    announce='http://example.com/announce',
    comment='Test Torrent',
    httpseeds=['http://example.com/file.iso'],
    announcelist=[['http://announce1.example.com'],['http://announce2.example.com']]
)

mk.multi_file('test')

with open('my.torrent', 'wb') as tf:
    tf.write(mk.getBencoded())
