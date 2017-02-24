# creates a list of requests with (start, end) from the data
def get_requests_from_file(request_file):
	file_requests = request_file.readlines()

	requests = []

	for request in file_requests:
		start, end = request.split(',')
		requests.append((int(start), int(end.strip())))

	return requests

def compatible(this, that):
	return not (this[1] > that[0] or this[0] > that[1])

# uses a greedy algorithm to find the request
# for which has the smallest finishing time and
# remove requests that are imcomptabile
def choose_best_requests(sorted_requests):
	result = []

	while len(sorted_requests) > 0:
		chosen_request = sorted_requests.pop(0)
		result.append(chosen_request)

		# find all the incomptabile start times
		to_remove = []
		for request in sorted_requests:
			if not compatible(chosen_request, request):
				to_remove.append(request)

		for request in to_remove:
			sorted_requests.remove(request)

	return result

def main():
	with open('requests.txt') as request_file:
		requests = get_requests_from_file(request_file)

	sorted_requests = sorted(requests, key=lambda tup: tup[1])

	print choose_best_requests(sorted_requests)

if __name__ == "__main__":
	main()