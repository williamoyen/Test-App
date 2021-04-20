def main():
	infile = open('data.txt', 'r')
	bigList = infile.readlines()
	
	for list_item in bigList:
		print(list_item.strip())

		
	infile.close()
main()