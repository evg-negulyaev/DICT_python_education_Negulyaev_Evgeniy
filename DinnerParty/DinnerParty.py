def main():
    print("Enter the number of friends joining (including you):")
    num = int(input())
    if num <= 0:
        print('No one is joining for the party')
        return

    print("Enter the name of every friend (including you), each on a new line:")
    participants = dict()
    for _ in range(num):
        participants[input()] = 0

    print('Enter the total amount:')
    amount = int(input())
    for name in participants.keys():
        participants[name] = round(amount / num, 2)
    print(participants)


if __name__ == '__main__':
    main()
