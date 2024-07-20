from projectmanagement.translation import translation

GENERIC_ERRORS = ['required', 'invalid', 'unique']


def get_generic_error(error_code) -> str:
    if error_code in GENERIC_ERRORS:
        return translation.GENERIC_ERRORS[error_code]
    return ''


def format_form_validation_errors(errors):
    error_dict = {}
    error_json_data = errors.get_json_data()
    for field in error_json_data:
        error_list = []
        for error in error_json_data[field]:
            if error['code'] in GENERIC_ERRORS:
                message = get_generic_error(error['code']) % {'field': translation.FIELDS[field]}
            else:
                message = error['message']
            # error_list.append({'message': message, 'code': error['code']})
            error_list.append(message)
        error_dict[field] = error_list[0]
    return error_dict
