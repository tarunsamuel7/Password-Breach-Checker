import requests
import hashlib
import sys


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {res.status_code}; please check the API and try again"
        )

    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count

    return 0


def pwned_api_check(password):
    hashed_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    pwd_initial_5char, pwd_tail = hashed_password[:5], hashed_password[5:]
    response = request_api_data(pwd_initial_5char)
    return get_password_leaks_count(response, pwd_tail)


def main(path_to_passwords_file):
    passwords = open(path_to_passwords_file, "r").read().splitlines()

    for password in passwords:
        count = pwned_api_check(password)
        if count:
            print(
                f"{password} was found {count} times... you should change your password!"
            )
        else:
            print(f"{password} was NOT found. Carry on!")

    return "done!"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
