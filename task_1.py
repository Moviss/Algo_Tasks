def zip_generator(first_zip, second_zip):
    first_zip = int(first_zip.replace('-', ''))
    second_zip = int(second_zip.replace('-', ''))
    current_zip = first_zip
    generated_zips = []
    while current_zip < second_zip-1:
        current_zip += 1
        current_zip_str = str(current_zip)
        current_zip_str = current_zip_str[:2] + '-' + current_zip_str[2:]
        generated_zips.append(current_zip_str)

    return generated_zips


# start = "79-900"
# stop = "80-155"
# print(zip_generator(start, stop))
