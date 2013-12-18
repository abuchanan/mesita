__version__ = '1.0.1'

class Formatter(object):
    def __init__(self, delimiter='\t', row_heading_name=''):
        self.delimiter = delimiter
        self.row_heading_name = row_heading_name

    def __call__(self, table):
        # TODO just use csv.writer
        header = self.delimiter.join([self.row_heading_name] + table.columns)
        rows = [header]

        for row in table.rows:
            x = [row]

            for col in table.columns:
                x.append(table[row, col])

            s = self.delimiter.join(str(col) for col in x)
            rows.append(s)

        return '\n'.join(rows)


class Table(object):
    Formatter = Formatter

    def __init__(self, default_factory=None):
        self.default_factory = default_factory
        self._data = {}
        self._columns = set()
        self._rows = set()

        self.formatter = self.Formatter()

    def __getitem__(self, key):
        try:
            return self._data[key]
        except KeyError:
            if self.default_factory:
                val = self.default_factory()
                self.__setitem__(key, val)
                return val
            else:
                raise

    def __setitem__(self, key, value):
        row, column = key
        self._rows.add(row)
        self._columns.add(column)
        self._data[key] = value

    def __str__(self):
        return self.formatter(self)

    @property
    def columns(self):
        return list(self._columns)

    @property
    def rows(self):
        return list(self._rows)

    def cells(self):
        for row in self.rows:
            for col in self.columns:
                key = row, col
                yield key, self.__getitem__(key)
