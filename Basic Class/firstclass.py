class First:
    language = 'Python'

    def learn():  # static method
        print(f'I am learning to write {First.language} programing language')

    def teach(self):
        First.learn()
        print(f'I can teach to write {self.language} programing language')


if __name__ == '__main__':
    print(f'This is {First.language} language')
    First.learn()

    first = First()
    first.teach()
