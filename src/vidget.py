import go_pg

class Vidget:
    def __init__(self, **args):
        self.fGetData = args.get('f_get_data')
        self.fRender = args.get('f_render')

    def render(self):
        return self.fRender(self.fGetData())