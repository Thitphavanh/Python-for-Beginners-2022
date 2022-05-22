from firstclass import First

class Second:
	pass


if __name__ == '__main__':
    print(f'This is {First.language} language')
    First.learn()

    first = First()
    first.teach()
