def remove(sub_str, the_str):
    len_sub = len(sub_str)
    len_str = len(the_str)
    new_str = ''
    i = 0
    while i < len_str:
        if the_str[i: (i + len_sub)] != sub_str:
            new_str = new_str + the_str[i]
            i = i + 1
        else:
            # new_str = new_str
            i = i + len_sub
    return new_str


def main():
    the_str = "Faith is a fine invention. When Gentlemen can see –. But Microscopes are prudent. In an Emergency."
    sub_str = 'ion'
    result = remove(sub_str, the_str)
    print(result)
    sub_str = "en"
    result = remove(sub_str, the_str)
    print(result)


if __name__ == '__main__':
    main()
