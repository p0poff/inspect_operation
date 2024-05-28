import conf
import argparse

def getArgs():
	__parser = argparse.ArgumentParser(description='''KASSA Service API''')
	__parser.add_argument('-c', '--connect', type=str, action='store', dest='conn', choices=['prod', 'release', 'preprod'], default='release')
	__parser.add_argument('--id', type=int, action='store', dest='operation_id', required=True)
	__parser.add_argument('-v', '--verbosity', action='count', dest='verb', default=0)
	return __parser.parse_args()


def main():
    __args = getArgs()
    try:
        __conf = conf.getConf('./conf.yaml')
    except:
        print('Not found conf.yaml file')
        exit()

    print(__conf['db_connect'].keys())
    print(__args)


if __name__ == '__main__':
    main()