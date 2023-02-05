# Navier Stokes Präsentation

## Navier Stokes Gleichungen
- Drei Gleichungen
  - Konti
  - Impuls
  - Energie
- F^C : konvektiver Anteil
- F^D : diffusiver Anteil

- Gradient von u (Nabla U) muss konsisten approximiert werden. Die Gleichungen dürfen nicht entkoppelt werden --> Schachbrett Muster

## Satz von Green / empirische Methode

- Die Raumableitung wird für die viskosen Flüsse benötigt. Daher muss bei den Tesbeispielen mit einer Raumapproximation = 2 gerechnet werden.

## Konvergenztest SineWaxe

Hat die um eine Ordnung geringere Bestimmung der Gradiententerme einen Einfluss auf die Konvergenzordnung des Verfahrens?
- Nein. Konvergenzordnung stets unabhängig von der Viskosität

Wie verhält sich die Ordnung mit zu ohne Viskosität
- Unabhängig. Auch hier wieder nährungsweise gleich. Lediglich Unterschied bei SImulationsdauer (DFL - Bedingung)
  

## Zylinderumströmung
- Reynoldszahl von 1000: Andere Größen müssen wieder entdimensionalisiert werden
- Man kann das Problem jetzt natürlich nicht stationär lösen --> Karmansche Wirbelstraße die sich ausbildet.

#### Welcher Unterschied ist auffallend?
- Der Widerstandsbeiwer des reibungsbehafteten Falls ist wesentlich größer
- Instationärer Fall mit Reibung

#### Welchen zusätzlichen Widerstandsanteil 