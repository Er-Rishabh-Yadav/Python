import CSV_Wrapper

if __name__ == "__main__":
    csv_handler = CSV_Wrapper.CSVHandler('data.csv')

    new_data = [
     ['name','age','city'],   
    ['Eve', '25', 'Boston'],
    ['Michael', '35', 'Chicago']
    ]
    csv_handler.overwrite_csv(new_data)

    csv_data = csv_handler.read_csv()
    print(csv_data)

    new_data = [
        ['Eve2', '25', 'Boston2'],
        ['Michael3', '3', 'Chicago']
    ]
    csv_handler.append_csv(new_data)

    csv_data = csv_handler.read_csv()
    print(csv_data)
    print()
    csv_data = csv_handler.read_csv_dict()
    print(csv_data)

    dict_data = [{'name': 'Eve', 'age': '25', 'city': 'Boston'}, {'name': 'Michael', 'age': '35', 'city': 'Chicago'}, {'name': 'Eve2', 'age': '25', 'city': 'Boston2'}, {'name': 'Michael3', 'age': '3', 'city': 'Chicago'}] 
    csv_handler.write_csv_dict(dict_data, ['name', 'age', 'city'])
