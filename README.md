![O Shanti é um aplicativo inovador que utiliza inteligência artificial para proporcionar uma abordagem holística à saúde, oferecendo orientação personalizada em exercícios físicos, concentração e t (1)](https://github.com/amandaarruda/Shanti/assets/66084295/f8625bf8-4c68-4ece-ad92-55730da6a1bd)


# Como testar o MVP da visão computacional do Shanti
Obs: As instruções abaixo são direcionadas para computadores com um sistema operacional Linux

### Pré-requisitos
- Python >= 3.7.0
- Uma IDE de sua preferência
- Ultralytics package

Você pode instalá-la através do terminal com o seguinte comando:
```bash
pip install ultralytics
```

### Para rodar
1. Instale o arquivo best.pt que está disponiblizado no [Drive](https://drive.google.com/file/d/1m5aCaufS1EqIC-he3QHYh73GkvFIYkBG/view?usp=sharing)
2. Baixe também o [MVP.py](https://github.com/amandaarruda/Shanti/blob/main/MVP.py) para rodar a inferência
3. Baixe o vídeo de teste, o [flow](https://github.com/amandaarruda/Shanti/blob/main/flow.mp4), ou teste com a webcam, como mostrado no código
4. Junte tudo na mesma pasta e rode o MVP.py na sua IDE preferida ou através do terminal

### Exemplo do funcionamento

https://github.com/amandaarruda/Shanti/assets/66084295/9e7515b4-f896-4cfb-92d4-d694636ad291

A leitura de uma pose pode ser verificada através das junções dos labels. 

Por exemplo,a pose Adho Mukha Vrksasana é identificada da seguinte maneira:

![Output no terminal](https://github.com/amandaarruda/Shanti/assets/66084295/d10bd85f-e908-4e57-902e-c558e66ad951)

### Você também pode treinar o dataset com as instruções disponíveis no [jupiter notebook](https://drive.google.com/file/d/1mI7jneSFV8xU2HAkgrr6YAzcYnlyM8WJ/view?usp=sharing)
