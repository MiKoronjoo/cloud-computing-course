import os
import sys
import time

import requests
import hashlib

host = sys.argv[1]
port = sys.argv[2]

SERVER_URL = f'http://{host}:{port}'
CLIENT_DIR = '/clientdata'
FILE_NAME = 'file.txt'
if not os.path.isdir(CLIENT_DIR):
    os.mkdir(CLIENT_DIR)


def get_checksum(file_path: str):
    with open(file_path, 'rb') as fp:
        file_hash = hashlib.md5()
        while chunk := fp.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()


def insert_person(name: str, family: str):
    url = SERVER_URL + '/persons'
    payload = {'name': name, 'family': family}
    response = requests.post(url, json=payload)
    return response.json()


def get_person(id):
    url = SERVER_URL + '/persons/' + str(id)
    response = requests.get(url)
    return response.json()


def delete_person(id):
    url = SERVER_URL + '/persons/' + str(id)
    response = requests.delete(url)
    return response.json()


def get_persons():
    url = SERVER_URL + '/persons'
    response = requests.get(url)
    return response.json()


def get_file():
    url = SERVER_URL + '/file'
    response = requests.get(url)
    with open(f'{CLIENT_DIR}/{FILE_NAME}', 'wb') as f:
        f.write(response.content)
    print(f'File saved to {CLIENT_DIR}/{FILE_NAME}')

    # Calculate checksum of the file and compare it with the one sent by the serve
    checksum = get_checksum(f'{CLIENT_DIR}/{FILE_NAME}')
    response_checksum = response.headers['X-Checksum']
    if checksum == response_checksum:
        print('Checksum verified successfully')
    else:
        print('Checksum verification failed')


def flush_db():
    all_persons = get_persons()
    for person in all_persons:
        delete_person(person['ID'])


def test_server():
    # flush_db()
    print('#### TESTING ####')
    person1 = insert_person('Sweeney', 'Todd')
    print('Inserted:', person1)
    person2 = insert_person('Edward', 'Scissorhands')
    print('Inserted:', person2)
    found = get_person(person2['personID'])
    print('Found:', found)
    all_persons = get_persons()
    print('All:', all_persons)
    delete_person(person1['personID'])
    delete_person(person2['personID'])
    all_persons = get_persons()
    print('All:', all_persons)
    get_file()


if __name__ == "__main__":
    test_server()

    # Keep the client running
    while True:
        time.sleep(5)
