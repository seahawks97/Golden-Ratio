
import matplotlib.pyplot as plt

# reference: https://nrich.maths.org/2737


def get_number(initial=0):
    while True:
        selection = input('Enter a number: ')
        try:
            selection = int(selection)
            if selection < 1:
                print('Please type a positive number.')
            elif selection < initial:
                print('Please type a larger number than the first.')
            else:
                return selection
        except TypeError:
            print('Please enter a number.')


def get_iter():
    while True:
        selection = input('Enter a number of iterations to complete (< 50): ')
        try:
            selection = int(selection)
            if selection < 1:
                print('Please type a positive number.')
            else:
                return selection
        except TypeError:
            print('Please enter a number.')


def main():
    golden_ratio = (1 + (5 ** 0.5))/2
    n1 = get_number()
    n2 = get_number(n1)
    iterations = get_iter()

    sums, quotients, differences = [], [], []
    golden_list = [golden_ratio for i in range(iterations)]

    for i in range(iterations):
        sum = n2 + n1
        quotient = sum / n2

        sums.append(sum)
        quotients.append(quotient)

        difference = quotient - golden_ratio
        differences.append(difference)

        print('n1:', n1, 'n2:', n2, 'Sum:', sum, 'Ratio:', quotient, 'Difference:', difference)

        n1 = n2
        n2 = sum

    plt.plot([i for i in range(iterations)], differences)
    plt.plot([i for i in range(iterations)], golden_list)
    plt.legend(['Calculated', 'Actual'])
    plt.show()


if __name__ == '__main__':
    main()
