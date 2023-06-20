def main():
    answer = input('File name: ')
    answer = answer.lower().strip()
    extension = answer.split('.')[-1]

    match extension:
        case 'gif' | 'png':
            print('image/' + extension)
        case 'jpg' | 'jpeg':
            print('image/jpeg')
        case 'pdf' | 'zip':
            print('application/' + extension)
        case 'txt':
            print('text/plain')
        case _:
            print('application/octet-stream')


main()
