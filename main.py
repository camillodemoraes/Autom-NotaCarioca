import subprocess
import time

print('=' * 20, 'Automação da Nota Carioca', '=' * 20, '\n')
time.sleep(2)

encerra_processo = 'prowin32.exe'
am_shortcut = r'C:\PML\Icones Pml Grafico\Nota Carioca\Nota Carioca Ambario.lnk'
gs_shortcut = r'C:\PML\Icones Pml Grafico\Nota Carioca\Nota Carioca Gmais01.lnk'
eb_shortcut = r'C:\PML\Icones Pml Grafico\Nota Carioca\Nota Carioca Euroame.lnk'
sq_shortcut = r'C:\PML\Icones Pml Grafico\Nota Carioca\Nota Carioca Eurojpa.lnk'
ib_shortcut = r'C:\PML\Icones Pml Grafico\Nota Carioca\Nota Carioca Eurorec.lnk'
br_shortcut = r'C:\PML\Icones Pml Grafico\Nota Carioca\Nota Carioca Eurosub.lnk'
im_shortcut = r'C:\PML\Icones Pml Grafico\Nota Carioca\Nota Carioca Usarec.lnk'
us_shortcut = r'C:\PML\Icones Pml Grafico\Nota Carioca\Nota Carioca Usastar.lnk'
eupsame_shortcut = r'C:\PML\Icones Pml Grafico\Nota Carioca\Nota Carioca eupsaame.lnk'
xml_shortcut = r'C:\Users\cpd\Desktop\XML FIAT.lnk'


# CODIGO PARA ENCERRAR AS APLICAÇÕES
def terminate_application(encerra_processo):
    try:
        subprocess.run(['taskkill', '/f', '/im', encerra_processo], check=True)
        print(f"Processo {encerra_processo} finalizado com Sucesso.\n")
    except subprocess.CalledProcessError:
        print(f"Não foi possivel encerrar o processo {encerra_processo}.\n")


# CODIGO PARA INICIAR AS APLICAÇÕES
def launch_application(shortcut_path):
    try:
        subprocess.Popen([shortcut_path], shell=True)
        print(f"Processo iniciado com Sucesso.\n")
    except Exception as e:
        print(f"Falha na execução do Processo. Error: {e}\n")


if __name__ == "__main__":
    print('-' * 15, 'Finalizando Processos', '-' * 15)
    time.sleep(2)

    # Encerramento dos processos
    terminate_application(encerra_processo)
    time.sleep(1)

    print('-' * 15, 'Iniciando Processos', '-' * 15)
    time.sleep(2)

    # Abertura do processos Americas
    launch_application(am_shortcut)
    time.sleep(1)

    # Abertura do processos Gmais
    launch_application(gs_shortcut)
    time.sleep(1)

    # Abertura do processos Squadra
    launch_application(sq_shortcut)
    time.sleep(1)

    # Abertura do processos Euro Barra
    launch_application(eb_shortcut)
    time.sleep(1)

    # Abertura do processos italia Barra
    launch_application(ib_shortcut)
    time.sleep(1)

    # Abertura do processos Brilhauto
    launch_application(br_shortcut)
    time.sleep(1)

    # Abertura do processos Usa Star
    launch_application(us_shortcut)
    time.sleep(1)

    # Abertura do processos italia Master
    launch_application(im_shortcut)
    time.sleep(1)

    # Abertura do processos Euro PSA
    launch_application(eupsame_shortcut)
    time.sleep(1)

    # Abertura do processos XML Fiat
    launch_application(xml_shortcut)
    time.sleep(5)