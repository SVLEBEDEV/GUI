class Group:

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return 'name: %s' % self.name

    def __eq__(self, other):
        return self.name == other.name

    def sorted_by_name(self):
        return self.name