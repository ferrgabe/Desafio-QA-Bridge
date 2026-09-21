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

@test("Nome com hifen", timeout=60)
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

        # Preenche o nome válido com um hifen indevidamente
        page.locator('#nomeCompleto').fill('Jean-Pierre')
        
        # Preenche o restante dos dados adequadamente para tentar submeter
        page.locator('#cpf').fill('12345678901')
        page.locator('#dataNascimento').fill('1990-01-01')
        page.locator('#principioAtivo').fill('Paracetamol')
        page.locator('#viaAdministracao').fill('Oral')
        page.locator('.periodo-input').fill('8')
        
        # Clica no salvar
        page.get_by_role("button", name="Salvar").click()
        
        # Valida se a mensagem de erro aparece na tela com a mensagem esperada
        mensagem_erro = page.locator('#span-errors')
        expect(mensagem_erro).to_be_visible()
        expect(mensagem_erro).to_have_text('Nome inválido!')

        time.sleep(2)
        
        browser.close()