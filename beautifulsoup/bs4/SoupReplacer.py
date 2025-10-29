class SoupReplacer:


    def __init__(self, og_tag, alt_tag):
        self.og_tag = str(og_tag)
        self.alt_tag = str(alt_tag)

    def replace_tag_name(self, name):
        if name == self.og_tag:
            return self.alt_tag
        return name
