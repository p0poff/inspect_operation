import conf
import argparse
import go_pg
import vidgets.vidget as vidget

DB_CONNECT = 'db_connect'

def getArgs():
	__parser = argparse.ArgumentParser(description='''KASSA Service API''')
	__parser.add_argument('-c', '--connect', type=str, action='store', dest='conn', choices=['prod', 'release', 'preprod'], default='release')
	__parser.add_argument('--id', type=int, action='store', dest='operation_id', required=True)
	__parser.add_argument('-v', '--verbosity', action='count', dest='verb', default=0)
	return __parser.parse_args()

def getDb(conf) -> go_pg.db_query:
    if conf is None:
        print('[ERROR] db conf is wrong, has no %s key in conf file' % (DB_CONNECT))
        exit()
    
    print('Connection to %s...' % (conf['host']), flush=True)
    try:
        db = go_pg.db_query(conf)
    except Exception as e:
        print('[ERROR] db connect %s' % (str(e)))
        exit()
    print('Connect.', flush=True)

    return db

def main():
    __args = getArgs()
    try:
        __conf = conf.getConf('./conf.yaml')
    except:
        print('[ERROR] Not found conf.yaml file')
        exit()

    __db = getDb(__conf.get(DB_CONNECT, {}).get(__args.conn))

    v = vidget.Vidget(__db, f_render = lambda : "Hello world")
    print(v.render())


if __name__ == '__main__':
    main()