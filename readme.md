# Simulador de Personas
Este repositório contém o código do simulador de personas. Através dele é possível simular o comportamento de diferentes clientes do banco, cada um com suas características e particularidades.

## Antes de usar: configurações do ambiente
Antes de usar você deve configurar uma variavel de ambiente para armazenar sua chave de acesso à API da OpenAI.

Para isso, caso você use windows, você deve: 

1. Pressionar as teclas `Win` `R` e digitar:

```
rundll32.exe sysdm.cpl,EditEnvironmentVariables
```

2. Na seção superior, **Variáveis do usuário para \[seu nome\]**, clique em **Novo**. Em seguida preencha os seguintes campos:

   - **Nome da variável**: OPENAI_API_KEY
   - **Valor da variável**: cole aqui a chave API que você copiou anteriormente.
  
3. Clique em OK para confirmar.

## Como usar
Para usar o simulador, primeiro o usuário deve instalar as dependências do projeto. Para isso, basta executar o comando:

```bash
pip install -r requirements.txt
```

Após isso, o usuário pode executar o simulador através do comando:

```bash
python launch_simulador.py
```

### Prompts
No arquivo `exemplos_prompts.xlsx`, o usuário pode encontrar exemplos de prompts que podem ser utilizados no simulador.
