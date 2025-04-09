import requests


class New_joke:
    def __init__(self):
        self.categories = []
        self.jokes = {}

    def get_category(self):
        url = "https://api.chucknorris.io/jokes/categories"
        print(f"запрашиваем URL: {url}")

        result = requests.get(url)
        print('статус код: ' + str(result.status_code))

        if result.status_code == 200:
            print("успешно, мы получили категории")
            self.categories = result.json()
            print("доступные категории:", self.categories)
        else:
            print("провал, запрос ошибочный")

    def get_single_joke(self):
        category = input("введите категорию из списка: ").lower()
        
        url = f"https://api.chucknorris.io/jokes/random?category={category}"
        response = requests.get(url)

        if response.status_code == 200:
            joke = response.json()['value']
            print(f"\n[{category.upper()}] {joke}")
            return joke
        else:
            error = f'ошибка {response.status_code}'
            print(error)
            return error

joker = New_joke()
joker.get_category()
joker.get_single_joke()