# Bulk leaked email checker

Essa ferramenta tem como objetivo utilizar a API do "https://haveibeenpwned.com/" para consultar quais emails de uma lista de emails esteve em algum vazamento de dados.

# Tutorial de uso:

1) Crie um arquivo chamado "emails.txt" que contenha uma lista de emails no seguite formato:

teste1@gmail.com

teste2@gmail.com

2) Em seguida execute o comando no terminal: `python bulk-leaked-email-checker.py`

3) O resultado das consultas será salvo no arquivo "logs.csv".
