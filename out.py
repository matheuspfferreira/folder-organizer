import os

# Obtenção do diretório da pasta raiz e suas subpastas
folder_dir = os.path.join(os.getcwd(), 'archives')
subfolders_names = os.listdir(folder_dir)

# Envio dos arquivos para a pasta raiz
for subfolder in subfolders_names:
    for archive in os.listdir(os.path.join(folder_dir, subfolder)):
        actual_dir = os.path.join(folder_dir, subfolder, archive)
        move_dir = os.path.join(folder_dir, archive)

        os.rename(actual_dir, move_dir)

    remove_dir = os.path.join(folder_dir, subfolder)
    if os.access(remove_dir, os.R_OK):
        os.rmdir(remove_dir)
    else:
        print('Não é possível excluir o arquivo devido às permissões') 

print('Processo de desorganização concluído')