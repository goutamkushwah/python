def foo():
    print("foo")  # print it


a = [1, 2, 3, 4]

b = {
    "first": 10,
    "second": 50,
    "third": 25,
    "fourth": 15,
    "fifth": 10,
    "sixth": 5,
    "seventh": 5,
    "eighth": 2,
}


def my_cool_function(
    input_size,
    output_size,
    num_classes=2,
    num_features=5,
    print_output=True,
    include_log=True,
):
    if print_output:
        print(
            input_size,
            output_size,
            num_classes,
            num_features,
        )
