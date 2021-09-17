Нужно закинуть эти два файла по пути

venv/Lib/site-packages/enchant/data/mingw64/share/enchant/hunspell
(если вы пользуетесь виртуальным окружением)

Если вы пользуетесь глобальным окружением, закиньте эти два файла в (windows)

C:\Users\<YOUR_USER_NAME>\AppData\Local\Programs\Python\Python<YOUR_VERSION>\Lib\site-packages\enchant\data\mingw64\share\enchant\hunspell

Также, если вы используете Linux Ubuntu, закиньте эти файлы в

/usr/share/hunspell
через

sudo mv ru_RU.aff /usr/share/hunspell
sudo mv ru_RU.dic /usr/share/hunspell

Если вдруг убунту не видит импорт и не запускает бота, удалите библиотеку pyenchant  установите через
pip3 uninstall pyenchant
sudo apt-get install libenchant1c2a
pip3 install pyenchant

<YOUR_USER_NAME> заменить на имя пользователя
<YOUR_VERSION> заменить на версию питона(рекомендуется использовать Python38)

Если папки нет, вы не установили pyenchant. Рекомендуется использовать venv
