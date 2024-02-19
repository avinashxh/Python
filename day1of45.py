#keywords
def sample():
    name = "Abinash,"

    def sample2():
        nonlocal name
        print(name)
        name = "tested it in a lame way :) "
        print(name)

    sample2()
    print(name)

sample()