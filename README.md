# Comparación de la sensibilidad de los sensores de temperatura LM35 y DS18B20
## Resumen

Se realizó una comparación de los sensores de temperatura LM35 y DS18B20, la principal diferencia entre ambos sensores es que el LM35 es de señal analógica y el DS18B20 digital.

Se conectaron los sensores mediante Arduino UNO y guardando los datos en un emulador serial, el experimentó consistió en medir la temperatura con los 2 sensores al mismo tiempo, primero al aire, seguidamente en agua fría y luego en agua caliente, estos cambios repentinos de la temperatura hacen que los sensores demuestren su rendimiento en cuestión de sensibilidad, resultando que el sensor digital DS18B20 tiene una mayor sensibilidad y precisión.

Aunque el sensor DS18B20 presente mejores características técnicas, hay unos factores a tener en cuenta, como el código, conexión y precio; concluyendo que para aplicaciones que no exijan una lectura con cambios repentinos y no tan precisos, un sensor analógico LM35 es suficiente, pero si existen cambios repentinos de temperatura y es necesaria una lectura precisa, es necesario por lo menos un sensor digital DS18B20.

## Objetivos

Comparar la sensibilidad y precisión que tienen los sensores de temperatura LM35 y DS18B20.

## Hipótesis

La sensibilidad y precisión de cada sensor es diferente y, por lo tanto, uno de los 2 sensores ofrece resultados más confiables.

## Introducción

En la adquisición de datos por medio de sensores, existen distintas maneras en las que un mismo dato puede ser presentado, entre estas se encuentran las analógicas y digitales.

El sensor LM35 funciona mediante una señal analógica y el DS18B20 funciona con una señal digital.

Entre las señales analógicas y digitales hay importantes diferencias a tomar en cuenta como:

| Analógica | Digital  |
| --------- | -------- |
| Continua  | Discreta |
| Ondas senoidales | Ondas cuadradas |
| Puede distorsionarse teniendo ruido en el ciclo de lectura o escritura | Es inmune a presentar ruido en el ciclo de lectura o escritura |
| El ruido afecta en la precisión | Ciclos más precisos |
| Bajo costo | Costo elevado |

La señal analógica es una señal continua que varía con el tiempo generando una onda que representa el voltaje que varía, en caso de Arduino, la señal analógica varía en un rango entre 0 y 1023, es decir que ocupa un espacio de 10 bits.

En caso de la señal digital, su principal característica es que es una señal discreta, la cual permite que haya saltos abruptos de bits entre lecturas o escrituras, puede representar distintos datos, como números, letras, sonidos, imágenes, hasta puede representar señales continuas si se requiere. (Diffen, 2011)

El sensor LM35 es un circuito integrado de precisión de temperatura con una salida de voltaje linealmente proporcional a temperatura en grados Centígrados, no requiere de calibración previa, por lo general tiene una precisión entre ±0.25°C y ±0.75°C, dependiendo de las condiciones ambientales, con un rango de temperatura entre -55°C y 150°C, lo llamativo de este sensor es la facilidad que tiene en su conexión ya que solo es necesario alimentarlo con una fuente directa de voltaje entre 4V y 30V y conectar el pin de lectura analógica. (Texas Instruments)

El termómetro digital DS18B20 provee lecturas de temperatura en Celsius entre 9 y 12 bits, se comunica con un solo puerto digital logrando la comunicación con el microprocesador principal, se alimenta con una fuente de voltaje de entre 0.5V y 6.0V dando lecturas de temperatura con un rango entre -55°C y 125°C, comercialmente suele venir encapsulado para poder hacer mediciones en el agua sin filtraciones. (Maxim Integrated)

## Materiales

* LM35
* DS18B20
* Arduino UNO
* Protoboard
* Resistencia de 4.7k Ohm
* Cables Dupont
* Alambre para protoboard
* Terminal
* Cautín
* Estaño para soldar
* Pasta para soldar
* Cronómetro
* Bolsa de plástico
* Vasos de unicel

## Procedimiento

1. Con ayuda del cautín y del estaño, soldar y sellar alambres de aproximadamente 30 cm a cada uno de los pines del sensor LM35.
2. Realizar las conexiones de acuerdo con el siguiente esquema, cubriendo al sensor LM35 con la bolsa de plástico para no tener filtraciones de agua en el circuito.
3. Cargar el código anexado a la placa Arduino.
4. Configurar el emulador de terminal para guardar los datos del puerto serial en un archivo de texto.
5. Preparar en agua caliente y colocarlo en un vaso de unicel, en el otro vaso de unicel colocar agua fría con hielo.
6. Empezar a grabar los datos.
7. Medir la temperatura durante 2 minutos sosteniendo los 2 sensores en el aire.
8. Sumergir los 2 sensores en el vaso con agua fría durante 2 minutos, con cuidado de que el agua no se filtre por la bolsa de plástico.
9. Sumergir los 2 sensores en el vaso con agua caliente durante 2 minutos, con cuidado de que no se filtre agua por la bolsa de plástico.
10. Terminar de grabar los datos en el emulador serial.

## Resultados y discusión

Se graficaron cada uno de los datos de cada sensor obteniendo:

Considerando que la lectura de datos consistió en 2 minutos a temperatura ambiente, 2 minutos en agua fría y 2 minutos en agua caliente, se puede observar en cada gráfica una baja en la temperatura seguida de una subida, ambas con comportamiento asintótico hasta cierta temperatura de equilibrio.

Observando mejor las gráficas se puede notar que tanto en la bajada como en la subida de temperatura, el sensor DS18B20 tiene una pendiente mucho más pronunciada que la del sensor LM35, la pendiente indica que el cambio de la temperatura con respecto al tiempo es mayor en el sensor DS18B20, al momento de sumergirlos en al agua caliente, los datos indican que el sensor DS18B20 alcanzó la temperatura de estabilización casi inmediatamente, en cambio, el sensor LM35 requiere más tiempo para lograr estabilizar la lectura de temperatura.

En cuestión de precisión, los únicos indicadores que existen son los 2 sensores utilizados, así que no se puede hacer una comparación global con datos externos para comprobar si dichas lecturas eran precisas en los distintos medios, aunque según pronósticos meteorológicos, el sensor DS18B20 indicaba una temperatura más cercana a la temperatura ambiental al instante de medir temperatura ambiente.

## Aplicaciones ingenieriles

### Control termostático
Mediante lecturas de temperatura se puede mandar señales a otros dispositivos para realizar diversas acciones de acuerdo con la temperatura del medio sobre el que se esté midiendo, como los aires acondicionados.

### Sistemas industriales
La industria puede utilizar estos sensores para supervisar la calidad de sus productos seleccionando los productos de temperatura ideal, o realizar ciertos procesos al alcanzar temperaturas específicas.

### Termómetros
Un termómetro es la aplicación más clara que pueden tener estos sensores debido a que se está dando la lectura directa de un dato que se está buscando.

## Conclusión

Al comparar las características y comportamientos de los sensores de temperatura LM35 y DS18B20, se puede concluir, apegándose a la hipótesis principal, que el sensor DS18B20 tiene una mayor precisión y sensibilidad ante la temperatura en distintos medios, en cambio el sensor LM35 puede presentar datos menos precisos y con un mayor tiempo para lograr la estabilización ante cambios repentinos de la temperatura.

Algunas ventajas de la utilización del sensor LM35 es que tiene un precio mucho menor que el DS18B20, y la conexión es fácil y rápida, en el sensor DS18B20 es necesario hacer un pequeño circuito con una resistencia y descargar una librería, en cuestión de código, para que pueda funcionar.

Para aplicaciones rápidas y donde no haya cambios repentinos de la temperatura, un sensor LM35 es un buen indicador cumpliendo con lo que se requiera sin tanto rigor.

Si se está pensando en una aplicación que involucre cambios repentinos de la temperatura y se están tratando productos o maquinaria que exija una lectura de temperatura precisa, el sensor DS18B20 es ideal, aparte con su encapsulado incorporado, puede utilizarse hasta dentro de líquidos sin riesgo a un cortocircuito.

## Referencias
Diffen. (21 de Septiembre de 2011). Obtenido de Analog vs Digital: https://www.diffen.com/difference/Analog_vs_Digital

Maxim Integrated. (s.f.). DS18B20. Obtenido de https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf

Texas Instruments. (s.f.). LM35 Precision Centigrade Temperature Sensors. Obtenido de http://www.ti.com/lit/ds/symlink/lm35.pdf
