from subprocess import call

def clearScreen(): call('clear')

entryTypes = {
	'article': {
		'description': 'An article from a journal or magazine.',
		'required': [
			'author',
			'title',
			'journal',
			'year'
		],
		'optional': [
			'volume',
			'number',
			'pages',
			'month',
			'note',
			'key'
		]

	},
	'book': {
		'description': 'A book with an explicit publisher.',
		'required': [
			['author', 'editor'],
			'title',
			'publisher',
			'year'
		],
		'optional': [
			'volume',
			'series',
			'address',
			'edition',
			'month',
			'note',
			'key'
		]
	},
	'booklet': {
		'description': 'A work that is printed and bound, but without a named publisher or sponsoring institution.',
		'required': [
			'title'
		],
		'optional': [
			'author',
			'howpublished',
			'address',
			'month',
			'year',
			'note',
			'key'
		]

	},
	'conference': {
		'description': 'An article in the proceedings of a conference. This entry is identical to the \'inproceedings\' entry and is included for compatibility with another text formatting system.',
		'required': [
			'author',
			'title',
			'booktitle',
			'year'
		],
		'optional': [
			'editor',
			'pages',
			'organization',
			'publisher',
			'address',
			'month',
			'note',
			'key'
		]

	}, 
	'inbook': {
		'description': 'A part of a book, which may be a chapter and/or a range of pages.',
		'required': [
			['author', 'editor'],
			'title',
			['chapter', 'pages'],
			'publisher',
			'year'
		],
		'optional': [
			'volume',
			'series',
			'address',
			'edition',
			'month',
			'note',
			'key'
		]

	}, 
	'incollection': {
		'description': 'A part of a book with its own title.',
		'required': [
			'author',
			'title',
			'booktitle',
			'year'
		],
		'optional': [
			'editor',
			'pages',
			'organization',
			'publisher',
			'address',
			'month',
			'note',
			'key'
		]
	}, 
	'inproceedings': {
		'description': 'An article in the proceedings of a conference.',
		'required': [
			'author',
			'title',
			'booktitle',
			'year'
		],
		'optional': [
			'editor',
			'pages',
			'organization',
			'publisher',
			'address',
			'month',
			'note',
			'key'
		]
	}, 
	'manual': {
		'description': 'Technical documentation.',
		'required': [
			'title'
		],
		'optional': [
			'author',
			'organization',
			'address',
			'edition',
			'month',
			'year',
			'note',
			'key'
		]
	}, 
	'mastersthesis': {
		'description': 'A Master\'s thesis.',
		'required': [
			'author',
			'title',
			'school',
			'year'
		],
		'optional': [
			'address',
			'month',
			'note',
			'key'
		]
	}, 
	'misc': {
		'description': 'Use this type when nothing else seems appropriate.',
		'required': [
			
		],
		'optional': [
			'author',
			'title',
			'howpublished',
			'month',
			'year',
			'note',
			'key'
		]
	}, 
	'phdthesis': {
		'description': 'A PhD thesis.',
		'required': [
			'author',
			'title',
			'school',
			'year'
		],
		'optional': [
			'address',
			'month',
			'note',
			'key'
		]
	}, 
	'proceedings': {
		'description': 'The proceedings of a conference.',
		'required': [
			'title',
			'year'
		],
		'optional': [
			'editor',
			'publisher',
			'organization',
			'address',
			'month',
			'note',
			'key'
		]
	}, 
	'techreport': {
		'description': 'A report published by a school or other institution, usually numbered within a series.',
		'required': [
			'author',
			'title',
			'institution',
			'year'
		],
		'optional': [
			'type',
			'number',
			'address',
			'month',
			'note',
			'key'
		]
	}, 
	'unpublished': {
		'description': 'A document with an author and title, but not formally published.',
		'required': [
			'author',
			'title',
			'note'
		],
		'optional': [
			'month',
			'year',
			'key'
		]
	}
}

def listEntries():
	print('List of entries\n')

def listEntryTypes():
	print('Entry types:')
	i = 0
	for entryType in sorted(entryTypes):
		if i != 0 and i % 2 == 0:
			print()
		print('[{}] {}'.format(i, entryType), end=('\t\t' if len(entryType) < 12 else '\t'))
		i += 1
	print('\n')



def menu(menuType='main'):
	if menuType == 'main':
		mainMenu()
	elif menuType == 'addEntry':
		addEntryMenu()
	else:
		print(menuType)

def mainMenu():
	menuItems = ['list entries', 'add entry', 'quit']
	clearScreen()
	print('Reference-building Tool\n')
	while True:
		try:
			for i, v in enumerate(menuItems): print('[{}] {}\t'.format(i, v), end='')
			choice = int(input('\nChoice: '))
			if choice == menuItems.index('list entries'):
				listEntries()
			elif choice == menuItems.index('add entry'):
				menu('addEntry')
				clearScreen()
				print('Reference-building Tool\n')
			elif choice == menuItems.index('quit'):
				break
		except ValueError:
			clearScreen()
			print('Reference-building Tool\n')
			continue

def addEntryMenu():
	menuItems = ['list types', 'add entry', 'quit']
	clearScreen()
	print('Add an entry\n')
	while True:
		try:
			for i, v in enumerate(menuItems): print('[{}] {}\t'.format(i, v), end='')
			choice = int(input('\nChoice: '))
			if choice == menuItems.index('list types'):
				listEntryTypes()
			elif choice == menuItems.index('add entry'):
				print('Adding...\n')
			elif choice == menuItems.index('quit'):
				break
		except ValueError:
			clearScreen()
			print('Add an entry\n')
			continue

menu('main')