



def mask_data(data = {}) -> dict:

    """
    ODPCC requires that personally identifiable information MUST be masked.

    """

    result = {}

    for k, v in data.items():
        result[k] = v[:2] + "".join(['*' for c in v[2:] ])
        

    return result


if __name__ == '__main__':
    
    data = dict({
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "2017-01-25",
        "mobile": "0738492832"
    })

    print(f"Masked Data: {mask_data(data)}")