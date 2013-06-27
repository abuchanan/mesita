
class Formatter(object):
    def __call__(self, table):
        header = '\t'.join([''] + table.columns)
        rows = [header]

        for row in table.rows:
            x = [row]

            for col in table.columns:
                x.append(table[row, col])

            s = '\t'.join(str(col) for col in x)
            rows.append(s)

        return '\n'.join(rows)


class Table(object):
    def __init__(self, default=None):
        self.default = default
        self._data = {}
        self._columns = set()
        self._rows = set()

    def __getitem__(self, key):
        try:
            return self._data[key]
        except KeyError:
            return self.default

    def __setitem__(self, key, value):
        row, column = key
        self._rows.add(row)
        self._columns.add(column)
        self._data[key] = value

    @property
    def columns(self):
        return list(self._columns)

    @property
    def rows(self):
        return list(self._rows)

    def __str__(self):
        f = Formatter()
        return f(self)
