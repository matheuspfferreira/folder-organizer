import os

# Obtenção do diretório da pasta e seus arquivos
folder_dir = os.path.join(os.getcwd(), 'archives')
archives_names = os.listdir(folder_dir)

# Obtenção das extensões dos arquivos
extensions= [archive.split('.')[1] for archive in archives_names]
uniques_extensions = list(set(extensions))

# Envio dos arquivos para suas pastas
os.chdir(folder_dir)
for extension in uniques_extensions:
    os.mkdir(extension)

    archives_send = [archive for archive in archives_names if archive.split('.')[1] == extension]

    for archive in archives_send:
        os.rename(archive, os.path.join(extension, archive))
    
os.chdir(os.path.dirname(os.getcwd()))    
print('Processo de organização concluído')