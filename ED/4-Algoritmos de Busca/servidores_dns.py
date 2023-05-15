import csv
from typing import List

class ServidorDNS:
    def __init__(self, ip: str, nome: str):
        self.ip = ip
        self.nome = nome
    def __str__(self) -> str:
        return f'{self.ip} - {self.nome}'

servidores_dns = []
with open('dns_br.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=';')
  next(csv_reader, None)  # pula os cabeçalhos
  for row in csv_reader:
    servidor_dns = ServidorDNS(row[0], row[1])
    servidores_dns.append(servidor_dns)

servidores_dns.sort(key=lambda servidor: servidor.ip)