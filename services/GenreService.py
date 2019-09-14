from Exceptions.GenreExceptions import InvalidGenreDescription, InvalidId


class GenreService:
    def __init__(self, repository):
        self.repository = repository

    def insert(self, genre):
        try:
            self.validate(genre)
            self.repository.insert(genre)
            return 'Genero Inserida com sucesso'
        except InvalidGenreDescription as e:
            return e

    def delete(self, id):
        try:
            if id is None:
                raise InvalidId
            if not isinstance(id, int):
                raise InvalidId
            self.repository.delete(id)
            return 'Genero deletado com sucesso'
        except InvalidId as e:
            return e

    def validate(self, publisher):
        if publisher.description is None:
            raise InvalidGenreDescription
        if publisher.description.strip() == '':
            raise InvalidGenreDescription
        if len(publisher.description) <= 3:
            raise InvalidGenreDescription
