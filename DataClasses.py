class Actor:

    def __init__(self, name):
        self.name = name

    def __lt__(self, other):
        return self.name < other

    def __gt__(self, other):
        return self.name > other

    def __eq__(self, other):
        return self.name == other

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Actor({:s})'.format(self.name)


class Movie:

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def get_weight(self):
        return 1 + (2015 - self.year)

    def __lt__(self, other):
        if self.title < other.title:
            return True
        elif self.title == other.title and self.year < other.year:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.title > other.title:
            return True
        elif self.title == other.title and self.year > other.year:
            return True
        else:
            return False

    def __eq__(self, other):
        return self.title == other.title and self.year == other.year

    def __hash__(self):
        return hash((self.title, self.year))

    def __str__(self):
        return '{:s}#@{:s}'.format(self.title, str(self.year))

    def __repr__(self):
        return 'Movie({:s}, {:s})'.format(self.title, repr(self.year))
