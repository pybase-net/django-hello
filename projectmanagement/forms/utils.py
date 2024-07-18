def format_form_validation_errors(errors):
    error_dict = {}
    error_json_data = errors.get_json_data()
    for field in error_json_data:
        error_list = []
        for error in error_json_data[field]:
            error_list.append({'message': error['message'], 'code': error['code']})
        error_dict[field] = error_list
    return error_dict
