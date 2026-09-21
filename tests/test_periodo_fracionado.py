from playwright.sync_api import sync_playwright
from framework.decorators import test
from playwright.sync_api import expect
import os
from dotenv import load_dotenv
import time
import sys

load_dotenv()
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

if not USER or not PASSWORD:
    print("❌ ERRO: Credenciais não encontradas!")
    print("Por favor, crie um arquivo .env baseado no .env.example e preencha USER e PASSWORD.")
    sys.exit(1)

@test("Período da dose fracionado", timeout=60)
def validar_nova_pagina():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # True pra não ver o navegador

        # Acessa a página do desafio, faz o login e inicia o desafio
        page = browser.new_page()
        page.goto("https://desafio-ps-qa.bridge.ufsc.tech/")
        page.locator('#usuario').fill(USER)
        page.locator('#password').fill(PASSWORD)
        page.locator('#termos-de-uso').check()
        page.locator('.btn-acessar').click()
        page.wait_for_load_state('networkidle')
        time.sleep(2)
        page.get_by_text('Iniciar desafio').click()

        # Insere um valor fracionado que viola a regra da ANVISA
        campo_periodo = page.locator('.periodo-input')
        campo_periodo.fill('5.459')
        
        # Clique fora para atualizar o valor oculto
        page.locator('body').click() 
        
        # Captura o valor que foi formatado no input oculto #periodoDose
        valor_oculto = page.locator('#periodoDose').input_value()
        
        # Valida se o sistema aceitou o número e concatenou na string conforme o receituário
        assert valor_oculto == 'a cada 5.459h', f"Comportamento inesperado. O sistema capturou: {valor_oculto}"

        time.sleep(2)
        
        browser.close()