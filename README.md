  <h1>🤖 Hands Controll</h1>

  <p>
    Projeto desenvolvido para controlar ações no sistema local do usuário por meio de gestos capturados pela webcam, utilizando Python, OpenCV e MediaPipe.
  </p>

  <h2>🎯 Funcionalidades</h2>
  <ul>
    <li>📷 Captura de gestos em tempo real via webcam</li>
    <li>🖐️ Reconhecimento de gestos com uma ou duas mãos</li>
    <li>🌐 Ações automatizadas como abrir navegador, capturar tela e acessar LinkedIn</li>
    <li>🔊 Controle de volume baseado na distância entre polegar e indicador</li>
  </ul>

  <h2>🛠️ Tecnologias Utilizadas</h2>
  <ul>
    <li>Python 3</li>
    <li>OpenCV</li>
    <li>MediaPipe</li>
    <li>PyAutoGUI</li>
    <li>PyCaw (para controle de volume no Windows)</li>
  </ul>

  <h2>🚀 Como Executar</h2>
  <ol>
    <li>Clone o repositório:
      <pre><code>git clone https://github.com/livio1212/hands_controll.git</code></pre>
    </li>
    <li>Instale as dependências:
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Execute o aplicativo:
      <pre><code>python app.py</code></pre>
    </li>
  </ol>

  <h2>🖱️ Gestos Reconhecidos</h2>
  <table border="1" cellpadding="5">
    <tr>
      <th>Gesto</th>
      <th>Ação</th>
    </tr>
    <tr>
      <td>Mão fechada</td>
      <td>Abrir navegador</td>
    </tr>
    <tr>
      <td>Dois dedos levantados</td>
      <td>Capturar print da tela</td>
    </tr>
    <tr>
      <td>Duas mãos detectadas</td>
      <td>Abrir LinkedIn</td>
    </tr>
    <tr>
      <td>Polegar e indicador próximos</td>
      <td>Controle de volume</td>
    </tr>
  </table>

  <h2>📄 Estrutura do Projeto</h2>
  <ul>
    <li><strong>app.py</strong>: Arquivo principal que inicia a detecção de gestos</li>
    <li><strong>gestures.py</strong>: Contém as funções de reconhecimento de gestos e ações correspondentes</li>
    <li><strong>requirements.txt</strong>: Lista de dependências necessárias</li>
  </ul>

  <h2>📬 Contato</h2>
  <p>
    Desenvolvido por <a href="https://www.linkedin.com/in/livio-costa/">Lívio Costa</a> - <a href="https://devlivio.site/">Portfólio</a>
  </p>
