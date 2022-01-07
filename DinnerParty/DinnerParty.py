from random import randint


def main():
    print("Enter the number of friends joining (including you):")
    num = int(input())
    if num <= 0:
        print('No one is joining for the party')
        return

    print("\nEnter the name of every friend (including you), each on a new line:")
    participants = dict()
    for _ in range(num):
        participants[input()] = 0

    print('\nEnter the total amount:')
    amount = int(input())

    for name in participants.keys():
        participants[name] = round(amount / num, 2)

    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    if input() != 'Yes':
        print('No one is going to be lucky')
    else:
        names = list(participants.keys())
        lucky = names[randint(0, len(names) - 1)]
        print(f'{lucky} is the lucky one!')
        for name in participants.keys():
            if name != lucky:
                participants[name] = round(amount / (num - 1), 2)
            else:
                participants[name] = 0

    print()
    print(participants)


if __name__ == '__main__':
    main()
