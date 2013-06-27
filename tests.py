import mesita


if __name__ == '__main__':
    t = mesita.Table()
    t[1, 'a'] = 'foo'
    t[1, 'b'] = 'bar'
    t[2, 'a'] = 'baz'
    t[2, 'b'] = 'bat'

    print t
