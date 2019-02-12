<div align="center">

<img src="./media/icons/512x512/fastmind.png" width="20%" />
<br><br>

Solve mazes and measure your time to complete them as fast as you can.

<i>
No habrá nunca una puerta. Estás adentro<br>
y el alcázar abarca el universo<br>
y no tiene ni anverso ni reverso<br>
ni externo muro ni secreto centro.<br><br>
</i>
Fragment of the poem <i>Laberinto</i> of <i>Jorge Luis Borges</i>.
<br><br>

<img src="./media/caps/together1.jpg" width="90%" />

</div>

## Requirements

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![pygame 1.8.0](https://img.shields.io/badge/pygame-%3E1.8.0-blue.svg)](https://www.pygame.org/wiki/GettingStarted)

The program uses the __pygame__ library for its full operation, so it is mandatory to install it on your computer before running the program.

> For more questions, go to the official pygame website: https://www.pygame.org/wiki/GettingStarted

### Generic Unix pygame installation

```
python3 -m pip install -U pygame --user
```

> If you do not have pip installed for python3 in Debian/Ubuntu/Mint: `sudo apt-get install python3-pip`

#### Another option for Debian/Ubuntu/Mint

```
sudo apt-get install python3-pygame
```

#### Another option for Fedora/Red Hat

```
sudo yum install python3-pygame
```

### Windows

Make sure you [__install python3.x__](https://www.python.org/downloads/windows/) with the _"Add python 3.x to PATH"_ option selected. This means that python, and pip will work for you from the command line.

```
python -m pip install -U pygame --user
```

## Get and run the program :rocket:

Currently the project is at a very early stage of its development (_alpha_), you can install it on your PC, but future versions may delete previous configurations in the program.

> At the moment this program has not been tested in __Mac OS__, so I still can not specify whether it works or how to install it correctly.

### Assuming you have git installed

```
git clone https://github.com/boot1110001/fastmind
cd fastmind
```

#### GNU/Linux

```
chmod u+x linux-run.sh
./linux-run.sh
```

#### Windows

```
win-run.bat
```

### Getting a .zip or a .tar.gz file from GitHub

- Extract the `fastmind-x.zip/.tar.gz` in the current folder.
- Open a terminal and navigate to the folder where the content of the `fastmind-x.zip/.tar.gz` has been extracted (using the `cd` command).
- Execute the following command: `bash linux-run.sh` for __GNU/Linux__ and `win-run.bat` for __Windows__.

### Run options

```
 -h			--help			Show this help.
 -v			--verbose		Enables verbose mode.
 -l <lang_name>		--lang=<lang_name>	Change the language.
 -p <level_name>	--play=<level_name>	Play the level directly.
 -s			--show			Show the available levels.
```

#### Languages avaliable

- __en.EN__ English (UK).
- __es.ES__ Spanish (Spain).
- __es.GL__ Galician.

## Things that I would like to add in the future

- Add more levels.
- Add a configuration section to the main menu.
- Improve the gameplay.
- Rethink the graphics (but keeping the retro style).
- Save the results locally.
- Show results table after each level and be able to compare with others.
- Add teleports.
- Add original music.
- Put the most efficient and understandable code.

## Credits

Created, programmed and maintained by [boot1110001](https://github.com/boot1110001).

## Licenses

- Project under the __[GNU General Public License version 3](https://www.gnu.org/licenses/gpl.txt)__.
- The icons sets are under the __[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)__ (CC BY 4.0) license .

## Donations

- __Bitcoin:__ 37Cx8i8Q4VjJJpMX6oRYVh2FUpXR1yMf54
- __Litecoin:__ MMUTvmaiZhPHjK68Jy1Z9roVFo7siGCcf8
- __Dogecoin:__ DSaqBstRo4h6dpzs9n7UDv39cg9wqErZvo
