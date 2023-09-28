from src.service.service_user import ServiceUser

service = ServiceUser()
resposta = service.add_user("Talita", "QA")
print("add_user_test: " + resposta)

resposta = service.add_user("Talita para Atualizar", "QA")
print("add_user_test: " + resposta)

resposta = service.add_user(None, "QA")
print("add_user_test_none: " + resposta)

resposta = service.add_user(None, "QA")
print("add_user_test_exists: " + resposta)

resposta = service.remove_user("Talita", "QA")
print("remove_user_test: " + resposta)

resposta = service.update_user_name("Talita para Atualizar", "QA", "Talita de Oliveira")
print("update_user_name_test: " + resposta)

resposta = service.get_user_by_name("Talita de Oliveira", "QA")
print("get_user_name_test: ", resposta)