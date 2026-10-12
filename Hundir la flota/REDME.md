# Hundir la flota

Juego de **Hundir la flota** donde jugas vos contra la CPU.
Cada uno tiene 6 barcos: tres de 2 casillas, dos de 3 y uno de 4. Los barcos se colocan al azar, en horizontal o vertical, y pueden quedar pegados.

## Cómo se ejecuta

1. Clona el repositorio y entra a la carpeta del juego:

    git clone https://github.com/Patricio-M-Artaza/ONLINE_DS_THEBRIDGE_PMA.git
    cd ONLINE_DS_THEBRIDGE_PMA/"Hundir la flota"

2. Instala las dependencias:

    python3 -m pip install -r requirements.txt

3. Arranca el juego:

    python3 main.py

## Cómo se juega

- En cada turno te pide la fila y la columna con números del 0 al 9.
- Si acertas, volves a disparar. Si fallas, le toca a la CPU que dispara a una casilla al azar.
- Si disparas a una casilla que ya habias probado, te avisa y elegis otra.
- Simbolos del tablero: `O` barco, `X` tocado, `A` agua y `_` casilla sin descubrir.
- Ves dos tableros: el tuyo, con tus barcos, y el del enemigo donde solo aparecen tus disparos.
- Gana quien hunde primero todos los barcos del otro.

