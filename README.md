# Verificador de Números da Loteria

Programa para verificar acertos em concursos de loteria usando a API: [Loterias Api](https://github.com/guto-alves/loterias-api).

## Como Utilizar o Programa

### Para Windows:
1. Acesse a página de [Releases](https://github.com/Filipi565/Numeros-Loteria/releases)
2. Baixe o arquivo `.zip` mais recente
3. Extraia o arquivo
4. Abra a pasta e execute o arquivo baixado

### Para Linux/macOS:
```bash
git clone https://github.com/Filipi565/Numeros-Loteria.git
cd Numeros-Loteria
python3 main.py
```

## Requisitos

### Windows:

* Nenhum requisito adicional (versão compilada disponível)

### Linux/macOS:
* Python 3.9 ou mais atual instalado
* Tkinter

## Funcionalidades

* Seleção de modalidades de loteria (Mega-Sena, Quina, etc)
* Consulta de resultados por concurso
* Verificação automática de acertos
* Interface simples e intuitiva

## Passo a Passo de Uso
1. Selecione a modalidade no menu suspenso
2. Digite o número do concurso
3. Insira seus números apostados (separados por vírgula, ex: 01, 02, 15, 20, 30)
4. Clique em "Calcular Acertos"
5. Veja o resultado na parte inferior da tela

## API Utilizada
* Dados obtidos através da API pública mantida por Guto Alves:
https://github.com/guto-alves/loterias-api