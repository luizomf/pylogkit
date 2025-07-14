# Python Logging Course

Criei um artigo sobre esse curso para te ajudar a acompanhar os vídeos. Acesse no link abaixo:

- [`logging` no Python: Pare de usar `print` no lugar errado](https://www.otaviomiranda.com.br/2025/logging-no-python-pare-de-usar-print-no-lugar-errado/)

Também temos a playlist completa desse curso no link abaixo:

- [Logging no Python: Curso completo](https://www.youtube.com/playlist?list=PLbIBj8vQhvm28qR-yvWP3JELGelWxsxaI)

Espero que goste.

## CLI

Você pode usar `pylogkit` para adicionar as variáveis de ambiente e criar o arquivo de configuração JSON automaticamente para você. Por exemplo:

```sh
# Instalação
uv add 'git+https://github.com/luizomf/pylogkit'

# Criando .env e json
# Se o .env existir, vamos adicionar variáveis de ambiente ele toda vez
# que você executar este comando. Se o JSON existir, vamos sobrescrever.
uv run pylogkit --dotenv .env --json logging.conf.json
```

Isso gera um `.env` e `logging.conf.json`. Vamos testar:

```python
from pylogkit import get_logger

logger = get_logger("mylogger", level="DEBUG")
logger.debug("Your log works")
```
