# Text-To-Speech

## Requirements

* Ubuntu
  * Ubuntu Bionic Beaver 18.04.*

## Installation

Download this TTS package.

```
mkdir TOW
cd ~/TOW
git clone https://github.com/NguyenCanhThanh/Text-To-Speech.git
```

Install library

```
sudo chmod +x requirement.sh
./requirement.sh
```

## QuickStart

After the installation, run the following commands.

```
python3 Main.py -i <input text> -o <output mp3 file>
```

where: 
* input text: string text you want to read
* output mp3 file: name of file mp3, where the output file is saved

Ex:
```
python3 Main.py -i "test text to speech" -o "bot.mp3"
```
