def return_string():
    with open('string_source', "r") as myfile:
        data = myfile.read()

    return data