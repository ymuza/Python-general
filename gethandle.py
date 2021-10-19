def get_handle():
    handle = input("enter a twitter username: ")
    return handle


if __name__ == '__main__':
    h = get_handle()
    length = len(h)
    print(f"your username has {length} characters.")

