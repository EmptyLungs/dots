import dbus

output = "{artist} - {song}"

session_bus = dbus.SessionBus()
try:
    spotify_bus = session_bus.get_object(
            'org.mpris.MediaPlayer2.spotify',
            '/org/mpris/MediaPlayer2'
            )

    spotify_properties = dbus.Interface(
            spotify_bus,
            'org.freedesktop.DBus.Properties'
            )

    metadata = spotify_properties.Get('org.mpris.MediaPlayer2.Player', 'Metadata')

    artist = metadata['xesam:artist'][0]
    song = metadata['xesam:title']

    print(output.format(artist=artist, song=song))
except Exception as e:
    if isinstance(e, dbus.exceptions.DBusException):
        print('')
    else:
        print(e)
