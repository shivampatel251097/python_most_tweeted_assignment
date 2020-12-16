# !/usr/bin/python3
from collections import Counter

no_test_cases = int(input("Enter the number of Test Cases: "))
testcase_count = 0
tweet_names_withid = []
checkpoint=[0]
sum=0
while testcase_count < no_test_cases:
	number_of_tweets = int(input("Enter the number of tweets for each Test Case:"))
	sum=sum+number_of_tweets
	checkpoint.append(sum)
# 	print(checkpoint)
	current_count = 0
	while current_count < number_of_tweets:
		name = str(input("Enter the name with Twitter ID (then press Enter): "))
		tweet_names_withid.append(name)
		current_count += 1
	testcase_count += 1

tweet_names = [namelist.split()[0] for namelist in tweet_names_withid]
# print(tweet_names)

for k in range(0,len(checkpoint)-1):
    current_case_names=tweet_names[checkpoint[k]:checkpoint[k+1]]
    current_case_times = Counter(current_case_names)
    countedList=current_case_times.most_common(len(current_case_names))
    for i in range(0,len(countedList)):
        max=countedList[0][1]
        if(countedList[i][1]>=max):
            print(countedList[i][0],' ',countedList[i][1])