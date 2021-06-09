def file_size(value): # add this to some file where you can import it from
    limit = 5242880
    if value.size > limit:
        raise ValidationError('Размер файла не должен превышать 50 мегабайт')