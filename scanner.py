import os
import re

# Regular Expressions
IP_REGEX = r"\d+\.\d+\.\d+\.\d+"
URL_REGEX = r"https?://\S+"
DOMAIN_REGEX = r"[a-zA-Z0-9-]+\.[a-zA-Z]{2,}"


def extrair_iocs():
    ips = set()
    urls = set()
    dominios = set()

    try:
        for arquivo in os.listdir("logs"):

            caminho = os.path.join("logs", arquivo)

            with open(caminho, "r", encoding="utf-8") as log:

                for linha in log:

                    ips.update(re.findall(IP_REGEX, linha))
                    urls.update(re.findall(URL_REGEX, linha))
                    dominios.update(re.findall(DOMAIN_REGEX, linha))

    except FileNotFoundError:
        print("Erro: pasta 'logs' ou arquivo não encontrado.")

    return ips, urls, dominios


def imprimir_relatorio(ips, urls, dominios):

    print("\n========== IOC REPORT ==========\n")

    print("IPs encontrados:")

    if ips:
        for ip in sorted(ips):
            print(ip)
    else:
        print("Nenhum IP encontrado.")

    print("\n------------------------------\n")

    print("URLs encontradas:")

    if urls:
        for url in sorted(urls):
            print(url)
    else:
        print("Nenhuma URL encontrada.")

    print("\n------------------------------\n")

    print("Domínios encontrados:")

    if dominios:
        for dominio in sorted(dominios):
            print(dominio)
    else:
        print("Nenhum domínio encontrado.")


def main():

    ips, urls, dominios = extrair_iocs()

    imprimir_relatorio(
        ips,
        urls,
        dominios
    )


if __name__ == "__main__":
    main()