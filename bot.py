import vk_api
import datetime as dt


def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True
    return key, remember_device


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password, auth_handler=auth_handler)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    response = vk.friends.get(fields="bdate")
    if response['items']:
        s = sorted(response['items'], key=lambda x: x['last_name'])
        for el in s:
            try:
                print(f'{el["last_name"]} {el["first_name"]} {el["bdate"]}')
            except KeyError:
                pass


if __name__ == '__main__':
    main()
