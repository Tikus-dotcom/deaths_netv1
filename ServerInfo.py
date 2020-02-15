class Info:
    def __init__(self, get):
        self.get = get
    def get_info(self):
        if self.get.lower() == 'uid':
            return '0x00000000'
        if self.get.lower() == 'heap':
            return '0x8000-0x1000000'
        if self.get.lower() == 'name':
            return 'deaths_NET'
        if self.get.lower() == 'ver':
            return 'v2'
