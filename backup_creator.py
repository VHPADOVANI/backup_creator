import shutil
import os
import csv
import datetime

origem = input("Digite o caminho do arquivo de origem: ")
destino = input('Digite o caminho do arquivo de destino: ')

if not os.path.exists(os.path.join(destino, 'backup')):
      os.mkdir(os.path.join(destino, 'backup'))   # Cria a pasta de destino se não existir

total_copiados = 0


for file in os.listdir(origem):
    if not os.path.isfile(os.path.join(origem, file)):
        continue  # Verifica se é um arquivo regular
    shutil.copy(os.path.join(origem, file), os.path.join(destino, 'backup', file))  # Copia o arquivo para o destino
    total_copiados += 1

    with open(os.path.join(destino, 'backup', 'backup_log.csv'), mode='a', newline='', encoding='utf-8')as log_file:
        log_writer = csv.writer(log_file)
        log_writer.writerow([file, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])  # Registra o arquivo copiado e a data/hora no log

print(f'Copiado : {total_copiados} arquivo(s)')