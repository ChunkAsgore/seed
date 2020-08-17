import re

display = {
    'seed': '种子： [\u00A7a{}]'
}

def on_info(server, info):
    if info.is_player == 1:
        if info.content.startswith('!!seed'):
            server.say(display['seed'].format(re.findall(re.compile('level-seed=.*'), open('./server/server.properties').read())[0][11:]))

def on_load(server, old):
	server.add_help_message('!!seed', '查询服务器地图种子')