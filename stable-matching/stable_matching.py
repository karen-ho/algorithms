# splits the preference files based on given format
# university:students in order of preference
def get_preference(file_preferences):
	preferences = {}

	for preference in file_preferences:
		key, value = preference.split(":")
		order_preferences = value.strip().split(",")
		preferences[key.strip()] = order_preferences

	return preferences

# creates a empty set of matches for each of the students
def init_matches(students):
	matches = {}

	for student in students:
		matches[student] = None

	return matches

# performs the stable matching algorithm
def gale_and_shapley(universities_preference, students_preference):
	universities = universities_preference.keys()
	students = students_preference.keys()

	set_unmatched_universities = set(universities)
	matches = init_matches(students)

	# while there is a university that is free and hasn't selected a student
	while len(set_unmatched_universities) > 0:
		#pick a university
		university = set_unmatched_universities.pop()

		university_preference = universities_preference[university]

		for student in university_preference:
			# if the student has not been selected then form a match
			if matches[student] == None:
				matches[student] = university
				break
			else:
				other_university = matches[student]
				student_preference = students_preference[student]
				# if the student prefers this university over the other university
				# reform match and make the other university back to the set of
				# unmatched ones
				if student_preference.index(university) < student_preference.index(other_university):
					matches[student] = university
					set_unmatched_universities.update({other_university})
					break

	return matches

def main():
	with open('universities.txt') as university_file:
		university_preference_file = university_file.readlines()

		universities_preference = get_preference(university_preference_file)

	with open('students.txt') as students_file:
		students_preference_file = students_file.readlines()

		students_preference = get_preference(students_preference_file)

	results = gale_and_shapley(universities_preference, students_preference)

	print results
	
if __name__ == "__main__":
	main()