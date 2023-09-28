from src.service.service_user import ServiceUser

class TestServiceUser:

    def test_add_user_com_sucesso(self):
        #Setup
        service = ServiceUser()
        resposta_esperada = "Usuário adicionado"

        #Chamada
        resposta = service.add_user("Talita", "QA")

        #Avaliação
        assert resposta_esperada == resposta

    def test_add_user_com_falha_name_none(self):
        # Setup
        service = ServiceUser()
        resposta_esperada = "Usuário inválido"

        #Chamada
        resposta = service.add_user(None, "QA")

        #Avaliação
        assert resposta_esperada == resposta

    def test_add_user_com_falha_name_existente(self):
        # Setup
        service = ServiceUser()
        service.add_user("Talita", "QA")
        resposta_esperada = "Usuário já existe!"

        #Chamada
        resposta = service.add_user("Talita", "QA")

        #Avaliação
        assert resposta_esperada == resposta

    def test_remove_user_com_sucesso(self):
        # Setup
        service = ServiceUser()
        service.add_user("Talita", "QA")
        resposta_esperada = "Usuário removido!"

        #Chamada
        resposta = service.remove_user("Talita", "QA")

        #Avaliação
        assert resposta_esperada == resposta

    def test_remove_user_com_falha_user_inexistente(self):
        # Setup
        service = ServiceUser()
        service.add_user("Talita", "QA")
        resposta_esperada = "Usuário não existe!"

        # Chamada
        resposta = service.remove_user("Palita", "QA")

        # Avaliação
        assert resposta_esperada == resposta

    def test_remove_user_com_falha_user_job_none(self):
        # Setup
        service = ServiceUser()
        service.add_user(None, None)
        resposta_esperada = "Usuário inválido"

        # Chamada
        resposta = service.remove_user(None, None)

        # Avaliação
        assert resposta_esperada == resposta

    def test_udate_user_name_com_sucesso(self):
        # Setup
        service = ServiceUser()
        service.add_user("Talita para Atualizar", "QA")
        resposta_esperada = "Usuário atualizado: Talita de Oliveira"

        #Chamada
        resposta = service.update_user_name("Talita para Atualizar", "QA", "Talita de Oliveira")

        #Avaliação
        assert resposta_esperada == resposta

    def test_udate_user_name_com_falha_user_job_none(self):
        # Setup
        service = ServiceUser()
        service.add_user(None, None)
        resposta_esperada = "Usuário inválido"

        #Chamada
        resposta = service.update_user_name(None, "QA", None)

        #Avaliação
        assert resposta_esperada == resposta

    def test_get_user_by_name_com_sucesso(self):
        # Setup
        service = ServiceUser()
        service.add_user("Talita de Oliveira", "QA")
        resposta_esperada = "Talita de Oliveira"

        #Chamada
        resposta = service.get_user_by_name("Talita de Oliveira", "QA")

        #Avaliação
        assert resposta_esperada == resposta

    def test_get_user_by_name_com_falha_name_none(self):
        # Setup
        service = ServiceUser()
        service.add_user(None, None)
        resposta_esperada = "Usuário inválido"

        #Chamada
        resposta = service.get_user_by_name(None, None)

        #Avaliação
        assert resposta_esperada == resposta