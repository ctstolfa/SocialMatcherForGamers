from .models import Account, Friend


def connections(user):
	friend = Friend.objects.get(current_user=user)
	already_friends = friend.users.all()
	exclude = list(already_friends)
	exclude.append(user)
	possible_friends_query = Account.objects.all().exclude(user__in=exclude).exclude(role=1)
	possible_friends = []
	for friend in possible_friends_query:
		weight = 1
		if user.account.gameStyle != friend.gameStyle or user.account.time != friend.time:
			weight = 0
		weight *= (len(set(friend.genres) & set(user.account.genres))*0.1)
		weight *= (len(set(friend.schedule) & set(user.account.schedule))*(1/7))
		possible_friends.append((weight, friend))
	merge_sort(possible_friends)
	return possible_friends


def merge_sort(lst):
	if len(lst) > 1:
		mid = len(lst) // 2
		L = lst[:mid]
		R = lst[mid:]
		merge_sort(L)
		merge_sort(R)
		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i][0] > R[j][0]:
				lst[k] = L[i]
				i += 1
			else:
				lst[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			lst[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			lst[k] = R[j]
			j += 1
			k += 1
