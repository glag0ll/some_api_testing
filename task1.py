import requests
import time

class Task():
    def new_location(self, count = 5):
        url = "https://rahulshettyacademy.com"

        key = "?key=qaclick123"
        post_resource = "/maps/api/place/add/json"

        post_url = url + post_resource + key
        print(post_url)

        random_place_id = []

        print('\nсоздание новых локаций:')
        for i in range(1, count+1):
            json_for_create_new_location = {
                "location": {

                    "lat": -38.383494,

                    "lng": 33.427362

                }, "accuracy": 50,

                "name": "Frontline house",

                "phone_number": "(+91) 983 893 3937",

                "address": "29, side layout, cohen 09",

                "types": [

                    "shoe park",

                    "shop"

                ],

                "website": "http://google.com",

                "language": "French-IN"
            }
            result_post = requests.post(post_url, json=json_for_create_new_location)
            if result_post.status_code == 200:
                place_id = result_post.json().get("place_id")
                random_place_id.append(place_id)
                print(f'успешно, создана новая локация: ' + place_id)
            else:
                print('провал')


        with open('id.txt', 'w') as f:
            for pid in random_place_id:
                f.write(pid + '\n')

        with open('id.txt', 'r') as f:
            ids = [line.strip() for line in f.readlines()]

        print('\nданные локаций:')
        for pid in ids[:5]:
            get_resource = '/maps/api/place/get/json'
            get_url = f'{url.rstrip("/")}{get_resource}{key}&place_id={pid}'

            response = requests.get(get_url)
            if response.status_code == 200:
                print(f"данные локации {pid}:")
                print(response.json())
            else:
                print(f"ошибка для ID {pid}: {response.status_code}")

        delete_ids = random_place_id[1::2]

        print("\nудаление локаций:")
        for pid in delete_ids:
            # Формируем URL для DELETE запроса
            delete_resource = "/maps/api/place/delete/json"
            delete_url = f"{url}{delete_resource}{key}&place_id={pid}"
            response = requests.delete(delete_url, json={"place_id": pid})
            if response.status_code == 200:
                print(f"локация {pid} удалена")
            else:
                print(f"ошибка удаления {pid}: {response.status_code}")

        time.sleep(5)

        print("\nпроверка после удаления:")
        existing_ids = []

        for pid in ids:
            get_url = f"{url}/maps/api/place/get/json{key}&place_id={pid}"
            response = requests.get(get_url)

            if response.status_code == 200:
                existing_ids.append(pid)
                print(f"локация {pid} существует.")
            elif response.status_code == 404:
                print(f"локация {pid} удалена.")
            else:
                print(f"ошибка при проверке {pid}: {response.status_code}")

        with open('id2.txt', 'w') as f:
            for pid in existing_ids:
                f.write(f"{pid}\n")
        print(f"\nсоздан файл id2.txt с {len(existing_ids)} активными ID")




test_task = Task()
test_task.new_location()