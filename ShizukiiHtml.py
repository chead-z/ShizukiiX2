from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shizukii #1 para suas keys</title>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Montserrat', sans-serif;
            background: linear-gradient(to right bottom, #2c1d31, #251826);
            color: #fff;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
        header {
            background: linear-gradient(to right bottom, #1d1321, #140e18);
            color: #fff;
            padding: 20px;
            text-align: center;
            box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.5);
        }
        nav {
            text-align: center;
            margin-top: 20px;
        }
        nav a {
            color: #fff;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            background: linear-gradient(to right bottom, #1d1321, #140e18);
            margin: 0 10px;
            transition: background 0.3s ease-in-out, color 0.3s ease-in-out;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.3);
        }
        nav a:hover {
            background: linear-gradient(to right bottom, #251826, #1d1321);
        }
        section {
            padding: 20px;
            margin: 10px auto; /* Ajusta a margem verticalmente */
            max-width: 600px; /* Limita a largura da seção */
            background: linear-gradient(to right bottom, #1d1321, #140e18);
            border-radius: 10px;
            display: none;
            animation: fadeIn 1s ease-in-out;
            box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.5);
        }
        section.active {
            display: block;
        }
        footer {
            background: linear-gradient(to right bottom, #1d1321, #140e18);
            color: #fff;
            text-align: center;
            padding: 20px;
            position: fixed;
            bottom: 0;
            width: 100%;
            box-shadow: 0px -3px 10px rgba(0, 0, 0, 0.5);
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }

        /* Adiciona bordas arredondadas */
        img {
            border-radius: 10px;
            max-width: 100%; /* Altera para largura máxima de 100% */
            height: auto;
            display: block;
            margin: 0 auto;
        }

        /* Estilo para o link do Discord */
        .discord-link {
            color: #1a90db; /* Azul Discord */
            text-decoration: none;
            font-weight: bold;
        }

        /* Estilo para os contribuidores */
        .contributor {
            border: 1px solid #fff; /* Borda Branca */
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 20px;
        }
        .contributor h3 {
            color: #ffd700; /* Amarelo */
            text-align: center;
        }
    </style>
</head>
<body>
    <header>
        <h1>Shizukii #1 para suas keys</h1>
    </header>
    <nav>
        <a href="#" onclick="showTab('informacoes')">Informações</a>
        <a href="#" onclick="showTab('especial-thanks')">Especial Thanks</a>
    </nav>
    <section id="informacoes" class="active">
        <h2 style="text-align: center;">Informações</h2>
        <p>Opa! Quer chaves rápidas? Então vem para a Shizukii! Aqui nós conseguimos chaves, ajudamos em várias coisas e também temos lojinhas. Você pode subir de cargo para estagiário, staff, etc., e ter acesso a bypass para conseguir chaves facilmente. Então, o que está esperando? Junte-se a nós: <a href="https://discord.com/invite/Xh44jr6X" class="discord-link">(Shizukii Discord server)</a></p>
        <!-- Adiciona o GIF com bordas arredondadas -->
        <div style="text-align: center;">
            <img src="https://media.discordapp.net/attachments/1197643620103225391/1205015455862100019/standard_4.gif?ex=65d6d518&is=65c46018&hm=8b5452bf492577918f16ac98515b5447082a17107c5e919fd9f1b7e28485dcfd&" alt="GIF">
        </div>
    </section>
    <section id="especial-thanks">
        <h2 style="text-align: center;">Especial Thanks</h2>
        <div class="contributors">
            <div class="contributor">
                <h3>Victor</h3>
            </div>
            <div class="contributor">
                <h3>Pedro</h3>
            </div>
            <div class="contributor">
                <h3>Oneheart</h3>
            </div>
            <div class="contributor">
                <h3>Klsk</h3>
            </div>
            <div class="contributor">
                <h3>Luxy</h3>
            </div>
        </div>
    </section>
    <footer>
        &copy; Shizukii#1.
    </footer>

    <script>
        function showTab(tabId) {
            var sections = document.querySelectorAll('section');
            sections.forEach(function(section) {
                if (section.id === tabId) {
                    section.classList.add('active');
                } else {
                    section.classList.remove('active');
                }
            });
        }
    </script>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
