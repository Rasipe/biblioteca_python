class InvalidDateDevolution(Exception):
    def __init__(self):
        Exception.__init__(self, 'Data e devolução invalida')


class InvalidUser(Exception):
    def __init__(self):
        Exception.__init__(self, 'Usuário inválido')


class InvalidBook(Exception):
    def __init__(self):
        Exception.__init__(self, 'Livro ivalido')


class IvalidDateLoan(Exception):
    def __init__(self):
        Exception.__init__(self, 'Data do emprestimo invalida')


class IvalidDateDevolution(Exception):
    def __init__(self):
        Exception.__init__(self, 'Data do devolução invalida')


class InsertException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel ralizar o empréstimo')


class UpdateException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel finalizar o empréstimo')


class NotFoundLoanException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Empréstimo não encontrado')
