# Modelo de Automação de Testes - Desafio Técnico QA Bridge

Este repositório contém um modelo de testes automatizados desenvolvid para o Desafio Prático de QA da Bridge. O projeto utiliza **Python** e **Playwright** para simular o comportamento do usuário e validar cenários críticos de falhas.

## Estrutura do Projeto

O framework foi **adaptado** de outro projeto pessoal, desenvolvido de forma modular para facilitar a manutenção e a escalabilidade dos testes:

* **`framework/`**: O "motor" da automação. Contém os decoradores, gerenciamento de execução, controle de tempo (*timeout*) e os geradores de relatórios consolidados.
* **`tests/`**: Diretório principal dos arquivos de validação. O orquestrador reconhece automaticamente qualquer arquivo com o prefixo `test_` e adiciona ele na fila de execução.
* **`config/`**: Responsável pelo carregamento seguro de variáveis de ambiente. Manterei desativado neste desafio.
* **`main.py`**: O script orquestrador. Ele varre a pasta de testes, executa as funções em sequência e exibe o resultado no console, além de salvar os relatórios.
* **`reports/`**: Armazena automaticamente os relatórios de cada execução em formato `.json`.

## Cenários de Teste Automatizados

Os testes do desafio foram focados em buscar brechas de validação:

1. **Falso Positivo em Nomes Válidos (`test_nome_hifen.py`)**
   * **Objetivo:** Provar que a *Regex* do sistema bloqueia nomes reais e válidos (como "Roza-Garcia").
2. **Submissão com Campos Vazios (`test_campos_vazios.py`)**
   * **Objetivo:** Verificar se o sistema é capaz de enviar de formulários em branco.
3. **Interação com Autocomplete Customizado (`test_autocomplete.py`)**
   * **Objetivo:** Testa esperas dinâmicas. É digitado um fragmento de texto no campo "Princípio Ativo", depois aguarda a a renderização e clica no `.dropdown` no elemento dinâmico.
4. **Risco Clínico no Período da Dose (`test_periodo_fracionado.py`)**
   * **Objetivo:** Insere valores fracionados (ex: `5.459`) no campo de texto livre de posologia para provar a ausência de validação de números inteiros.

---

## Passo a Passo para Execução

Como este repositório ignora arquivos de configuração sensíveis e ambientes virtuais, É necessário configurá-los manualmente na primeira execução.

### Pré-requisitos
* **Python 3.x** instalado.
* **Git** instalado.

### 1. Clonar o Repositório
```bash
git clone https://github.com/ferrgabe/Desafio-QA-Bridge.git
cd Desafio_QA_Bridge
```

### 2. Criar e Ativar o Ambiente Virtual
**No Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```
**No Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as Dependências
Instale os pacotes do Python necessários para rodar o framework:
```bash
pip install -r requirements.txt
```
Instale os navegadores embutidos do Playwright:
```bash
playwright install
```

### 4. Configurar as Credenciais
1. Na raiz do projeto, faça uma cópia do arquivo `.env.example` e renomeie a cópia para `.env`.
2. Abra o arquivo `.env` recém-criado.
3. Preencha as variáveis `USER` e `PASSWORD` com as suas credenciais de acesso ao sistema do desafio.

### 5. Executar os Testes
Para rodar o sistema de testes de uma vez e gerar o relatório final, execute o orquestrador na raiz do projeto:
```bash
python main.py
```
*Por padrão, configurei o parâmetro `headless=False` para visualizar os testes acontecendo no navegador.*