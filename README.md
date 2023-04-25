![real back](https://user-images.githubusercontent.com/103686624/234310234-05239d10-2a30-4de3-bf5e-a9d7aec59d44.jpg)
## Requerimentos
-Instale [Python](https://www.python.org/downloads/)</br>
-Instale [Microsoft Visual C++](https://visualstudio.microsoft.com/pt-br/visual-cpp-build-tools/), lembre de selecionar a opção "Desenvolvimento para desktop com C++"
</br>
![c++](https://user-images.githubusercontent.com/103686624/234313444-c1f7d5fc-53e4-4c63-84a1-25bf3b86f720.png)
</br>
-
-Usando **cmd.exe**, acesse a pasta da aplicação usadno `cd "pasta\da\aplicação"` e use o comando `pip install venv`. Agora podemos criar o virtual enviroment usando
o comando `py -m venv venv` e ativá-lo usando `"pasta\da\aplicação"\venv\Scripts\Activate.bat`. Por fim, use `pip install -r requirements.txt` para instalar as packages e
`py manage.py runserver` para iniciar a aplicação. 
</br>
![link](https://user-images.githubusercontent.com/103686624/234323414-8999ca7a-df91-4613-91c4-2684d237c18c.jpg)
</br>
Para acessar o site, use o link conforme a image acima.
## Utilizando o site
O objetivo do site é possibilitar a comunicação entre duas ou mais pessoas em tempo real, isso é feito através de salas que os usuários podem entrar para conversar. </br>
Basta criar um usuário e selecionar o nome da sala que deseja entrar, desde que os usuários estejam na mesma sala, será posível conversar.
</br>
![sala](https://user-images.githubusercontent.com/103686624/234329845-9ebfc125-74df-43a7-8eb2-317adee3c893.jpg)
</br>
Uma maneira de testar o site utilizando apenas uma máquina é abrir dois navegadores diferentes rodando o site, crair um usuário para cada e entrar em uma sala com o
mesmo nome.
</br>
## Sobre
Esse projeto foi feito para testar **Django Channels**, já que este nos permite criar sites que respondem em tempo real. Foi 
escolhido um chat, já que isso é semelhante a uma das funcionalidades de outro projeto, o **[instagram-like-blog](https://github.com/Pedroock/instagram-like-blog)**.
