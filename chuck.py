import requests

class New_joke():
    def __init__(self):
        self.categories = []
        self.jokes = {}

    def get_category(self):
        url = "https://api.chucknorris.io/jokes/categories"
        print('url')

        result = requests.get(url)
        result.encoding = 'utf-8'
        print('статус код: ' + str(result.status_code))
        if result.status_code == 200:
            print("успешно, мы получили новую категорию")
            c = self.categories = result.json()
            print(c)
        else:
            print("провал, запрос ошибочный")
            self.categories = []

    def get_single_joke(self, category):

        url = f"https://api.chucknorris.io/jokes/random?category={input(category)}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()['value']
        else:
            return f'ошибка {response.status_code}'

        joke = self.get_single_joke(category)
        self.jokes[category] = joke
        print(f"[{category.upper()}] {joke}\n")


joker = New_joke()
joker.get_category()
joker.get_single_joke()

