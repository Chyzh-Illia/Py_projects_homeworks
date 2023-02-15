def digits_remover():
    with open('input.txt', 'r') as f1, open('output.txt', 'w') as f2:
        f2.write("".join([c for c in f1.read() if not c.isdigit()]))


digits_remover()

if __name__ == '__main__':
