
# Spektrum Discord Bot 🤖

<https://hd4niel.github.io/spektrum-bot/>

## Commands ℹ️

```
Spektrum Discord Bot 🤖

Commands:
  aslak    Lappländsk svenska
  hello    Testing testing
  inbjudan Skapa en tillfällig inbjudan
  kasta    Kasta ett specifierat antal tärningar
Greetings:
  hej      Hej på dej
Music:
  join     Joins a voice channel
  leave    Clears the queue and leaves the voice channel
  loop     Loops the currently playing song
  now      Displays the currently playing song
  pause    Pauses the currently playing song
  play     Plays a song
  queue    Shows the player's queue
  remove   Removes a song from the queue at a given index
  resume   Resumes a currently paused song
  shuffle  Shuffles the queue
  skip     Vote to skip a song, the requester can automatically skip
  stop     Stops playing song and clears the queue
  summon   Summons the bot to a voice channel
  volume   Sets the volume of the player
Svammel:
  svammel  Hmm ...
WolframAlpha:
  wolfram  Sök fakta eller lös svåra matteproblem
​No Category:
  help     Shows this message

Type !help command for more info on a command.
You can also type !help category for more info on a category.
```

## Develop 💻

```bash
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
...
$ deactivate
```

### Docker 🐋

```bash
$ docker build -t bot .
$ docker run -it bot
```

### Documentation 📖

```bash
$ cd docs
pip install -r requirements.txt
$ sphinx-quickstart
$ sphinx-apidoc -o _modules ../bot
$ make html
$ xdg-open _build/html/index.html
```

### Lint 🔍
```bash
$ autopep8 --in-place --aggressive --max-line-length 200 --recursive bot
```
