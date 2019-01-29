def zip_generator(first_zip, second_zip):
    
    def create_int(string_variable):
        return int(string_variable.replace('-', ''))


    first_zip = create_int(first_zip)
    second_zip = create_int(second_zip)
    current_zip = first_zip
    generated_zips = []
    while (current_zip < second_zip-1):
        current_zip += 1
        current_zip_as_string = str(current_zip)
        current_zip_as_string = current_zip_as_string[:2] + '-' + current_zip_as_string[2:]
        generated_zips.append(current_zip_as_string)

    return generated_zips


# start = "79-900"
# stop = "80-155"
# print(zip_generator(start, stop))
