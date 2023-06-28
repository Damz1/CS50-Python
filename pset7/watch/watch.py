import re


def main():
    html = input("HTML: ")
    print(parse(html))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        url_pattern = re.search(
            r"https?:\/\/(www\.)?youtube\.com\/embed\/(\w+)", s)
        if url_pattern:
            split_url = url_pattern.group(2)
            return "https://youtu.be/" + split_url


if __name__ == "__main__":
    main()
