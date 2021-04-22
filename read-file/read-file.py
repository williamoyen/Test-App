def main():
	infile = open('data.txt', 'r')
	list = infile.readlines()
	
	for list_item in list:
		print(list_item.strip())

		
	infile.close()
main()
