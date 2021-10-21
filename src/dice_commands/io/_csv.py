import csv


def read_ints_from_csv(filename, fieldname):
    """
    Reads data from CSV file and converts {fieldname} to int.
    Returned data is sorted
    """
    with open(filename, 'r') as f:
        reader = csv.DictReader(f, delimiter=",", quotechar='"')
        data = [int(row[fieldname]) for row in reader]
        data.sort()
    return data

def write_list_data_as_dict_to_csv(data: list, output_file: str, fieldnames: list) -> None:
    with open(output_file, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)