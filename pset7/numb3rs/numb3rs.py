def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip_address):
    segments = ip_address.split(".")
    if len(segments) != 4:
        return False
    for segment in segments:
        if not segment.isdigit():
            return False
        num = int(segment)
        if num < 0 or num > 255:
            return False
    return True


if __name__ == "__main__":
    main()
