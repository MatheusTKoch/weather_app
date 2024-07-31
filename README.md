# Weather App

Weather App é uma aplicação web que permite aos usuários buscar informações meteorológicas atuais de uma cidade específica. A aplicação utiliza Vue.js para o frontend e Flask para o backend, realizando requisições para a OpenWeatherAPI.

## Índice

- [Instalação](#instalação)
- [Uso](#uso)
- [Arquitetura do Projeto](#arquitetura-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Instalação

### Pré-requisitos

- Node.js e npm
- Python 3.x
- pip
- Flask
- OpenWeatherAPI Key

### Passos para instalar

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seuusuario/weather-app.git
    cd weather-app
    ```

2. **Instale as dependências do frontend:**

    ```bash
    cd client
    npm install
    ```

3. **Instale as dependências do backend:**

    ```bash
    cd ../server
    pip install -r requirements.txt
    ```

4. **Configure as variáveis de ambiente:**

    Crie um arquivo `.env` na pasta `server` com o seguinte conteúdo:

    ```plaintext
    OPEN_WEATHER_KEY=seu_api_key
    ```

## Uso

### Executar o Frontend

1. **Inicie o servidor de desenvolvimento Vue:**

    ```bash
    cd client
    npm run dev
    ```

### Executar o Backend

1. **Inicie o servidor Flask:**

    ```bash
    cd server
    python app.py
    ```

### Acessar a Aplicação

Abra seu navegador e acesse `http://localhost:5173`.

## Arquitetura do Projeto

weather-app/
├── client/ # Código fonte do frontend (Vue.js)
│ ├── public/
│ ├── src/
│ │ ├── assets/
│ │ ├── components/
│ │ │ ├── Pesquisa.vue
│ │ │ ├── Resultados.vue
│ │ ├── views/
│ │ │ ├── PesquisaView.vue
│ │ ├── App.vue
│ │ ├── main.js
│ ├── package.json
│ ├── vite.config.js
├── server/ # Código fonte do backend (Flask)
│ ├── app.py
│ ├── requirements.txt
│ ├── .env
├── README.md

## Tecnologias Utilizadas

### Frontend

- [Vue.js](https://vuejs.org/)
- [Axios](https://axios-http.com/)

### Backend

- [Flask](https://flask.palletsprojects.com/)
- [Requests](https://requests.readthedocs.io/)

### APIs

- [OpenWeatherAPI](https://openweathermap.org/api)

## Contribuição

Se você deseja contribuir com este projeto, siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Faça um push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.