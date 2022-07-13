import vk_api
import datetime
import time
ts = time.time()

vk_token = 'TOKEN'

vk = vk_api.VkApi(token=vk_token)

MAX_COUNT_OF_POSTS = 40
EACH_NUM_POST = 10 
OUR_ID = '718243705'

with open('post_text.txt', mode = 'r', encoding ='utf-8') as f_t, open('post_att.txt', 'r') as f_a,open('groups.txt', 'r') as f_g:
	post_text = f_t.read()
	post_att = f_a.read().replace('\n', ',')
	groups = f_g.read().strip().split('\n')
while True:
	for group in groups:
		rs = vk.method('wall.get', {'count': EACH_NUM_POST, 'owner_id':group})
		flag = False
		for item in rs['items']:
			if str(item['from_id']) == OUR_ID:
				flag = True
				continue
		if not flag:
			dt = datetime.datetime.now()
			st = dt.strftime(dt.strftime("Day: %d/%m/%Y  time: %H:%M:%S"))
			print(f'In group {group} created post at {st}', vk.method('wall.post', {'message': post_text, 'owner_id':group, 'attachment': post_att}))
	time.sleep (300)
