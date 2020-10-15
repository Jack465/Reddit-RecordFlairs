import praw
import os

reddit = praw.Reddit(client_id='###',
                client_secret='####',
                user_agent='FDXgeekplan056 r_RequestABot Request',
                username='####',
                password='####')

waiting_list = []

if os.path.isfile('processed_users.txt'):
	with open('processed_users.txt', 'r') as file:
		processed_users = [line.rstrip('\n') for line in file]


for flair in reddit.subreddit('musicbottesting').flair(limit=None):
	user = flair['user'].name
	flair_text = flair['flair_text']
	print("{} has flair {}".format(user, flair_text))
	if user not in processed_users:
		if flair_text == "TestingFlair":
			page = reddit.subreddit('musicbottesting').wiki['TestingFlairUsers']
			modify_content = page.content_md + "\n\n" + user
			page.edit(content=modify_content)
			print("Added {} to Wiki Page".format(user))
		elif flair_text == "ExampleFlair":
			page = reddit.subreddit('musicbottesting').wiki['ExampleFlairUsers']
			modify_content = page.content_md + "\n\n" + user
			page.edit(content=modify_content)
			print("Added {} to Wiki Page".format(user))
		else:
			print("Couldn't process {} for user {}".format(flair_text,user))

		waiting_list.append(user)

with open('processed_users.txt','a') as file:
	for item in waiting_list:
		file.write('{}\n'.format(item))
