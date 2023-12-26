import requests
from setting import HOST, PORT

url = f"http://{HOST}:{PORT}"

def check_login(login: str, password: str) -> int | str | None:
    data = f'{{ "login": "{login}", "password": "{password}" }}'
    r = requests.get(url='http://127.0.0.1:8000/users/login', data=data)
    answer = r.json()
    code = answer["code"]
    message = answer["message"]
    if code != 200:
        return f"Server error: {message}"
    if type(answer["position_id"][0]) == int:
        return answer["position_id"][0]
    elif type(answer["position_id"]) is None:
        return None


def data_for_table_masters() -> list[tuple]:
    data = []
    row = []
    answer = requests.get(url=f"{url}/master/get_all").json()
    for dict in answer:
        for key, value in dict.items():
            row.append(value)
        data.append(tuple(row))
        row.clear()

    return data


def new_master(name: str, id: int) -> dict:
    data = f'{{ "name_master": "{name}", "service_id": "{id}" }}'
    answer = requests.post(url=f"{url}/master/create", data=data).json()
    print(answer)
    code = answer["code"]
    msg = answer["message"]
    if code != 200:
        return {"Error": msg, "code": code}
    return {"message": msg, "code": code, "master": answer["master"]}


def upd_master(id: int, name: str, type_id: int) -> dict:
    data = f'{{ "name_master": "{name}", "service_id": "{type_id}" }}'
    answer = requests.put(url=f"{url}/master/update/{id}/", data=data).json()
    code = answer["code"]
    msg = answer["message"]
    if code != 200:
        return {"error": msg, "code": code}
    return {"message": msg, "code": code}


def del_master(id: int) -> dict:
    answer = requests.delete(url=f"{url}/master/delete/{id}/").json()
    code = answer["code"]
    msg = answer["message"]
    if code != 200:
        return {"Error": msg, "code": code}
    return {"message": msg, "code": code}