import go_pg

def getOperation(**args):
    def f():
        q = 'SELECT * FROM system.operations WHERE id = %s' % (args['operation_id'])
        return args['db'].array_query(q)
    return f