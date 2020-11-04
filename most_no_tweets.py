def most_no_of_tweets(num_of_testcases):
	final_counts_list = []
	for num_test in range(num_of_testcases):
		tweets_list = []
		no_of_tweets = int(input("enter no of tweets:"))
		for num_tweet in range(no_of_tweets):
			data = input("enter your tweet:")
			tweets_list.append(data.split()[0])
		user_names = list(set(tweets_list))
		data_dict = {}
		for uname in user_names:
			data_dict[uname]=tweets_list.count(uname)
		max_value = max(data_dict.values())
		final_dict = {}
		for key,value in data_dict.items():
			if data_dict[key] == max_value:
				final_dict[key] = value
		final_counts_list.append(final_dict)
	for each_test in final_counts_list:
		print("In Test case:", final_counts_list.index(each_test)+1)
		for each_key,each_value in each_test.items():
			print(each_key,each_value)
		print("*"*20)


num_of_testcases = int(input("enter no of test cases:"))
most_no_of_tweets(num_of_testcases)
