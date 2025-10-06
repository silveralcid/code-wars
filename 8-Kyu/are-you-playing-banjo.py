def are_you_playing_banjo(name):
    chars = list(name)
    if chars[0] == 'r' or chars[0] == 'R':
        return (name + " plays banjo")
    else:
        return (name + " does not play banjo")