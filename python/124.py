def romek(s):
    numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    n = 0
    last_value = 0
    for value in (numerals[c] for c in reversed(s.upper)):
        v = (value, -value)[value < last_value]
        print('{:6}+={:5}<==cur, prev={},{}'.format(n, v, value, last_value))  # ??
        n += (value, -value)[value < last_value]
        last_value = value
    return n


romek('MMCXVI')
