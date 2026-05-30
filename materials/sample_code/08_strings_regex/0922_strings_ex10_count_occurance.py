def count(sub_str, the_str):
    counts = 0
    len_sub = len(sub_str)
    len_str = len(the_str)

    for i in range(len_str):
        if the_str[i: (i + len_sub)] == sub_str:
            counts = counts + 1

    return counts


def main():
    the_str = '\'Faith\' is a fine invention. When Gentlemen can see –. ' \
              'But Microscopes are prudent. In an Emergency.'
    sub_str = 'en'
    result = count(sub_str, the_str)
    print(result)


if __name__ == '__main__':
    main()
