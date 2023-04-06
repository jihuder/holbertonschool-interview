## Minimum Operations 

![Minimum Operations](/images/Minimum%20Operations.png)


El problema se trata que tengo que igualar el carácter  "H" según el número de veces que me llega como parámetro, es decir, si por el parámetro me llega  "n= 15" tengo que hacer "15 H", ya que "H == 15", por lo cual, me toca hacer un marco calcula de H copiando y pegando para hacer el cálculo de cuantas veces la puedo copiar  si excederme haciendo el mínimo de copias.

Entonces, ¿Cómo podemos calcular la cantidad óptima de operaciones para llegar a n caracteres "H"?
Para hacer este tipo de cálculos podemos hacerlo de dos formas, una sería un algoritmo de fuerza bruta  que prueba todas las posibles combinaciones de operaciones para encontrar la solución óptima y la otra opción alternativa para resolver este problema es utilizar la factorización.

Este enfoque es más eficiente que la fuerza bruta, ya que no se necesita probar todas las posibles combinaciones de operaciones. En su lugar, se puede utilizar la estructura de la cadena final para determinar la solución óptima de manera más eficiente. Sin embargo, es importante tener en cuenta que este enfoque solo funciona para cadenas con estructuras específicas y podría no funcionar para todos los valores de n.

Comenzamos por el tema de Factorización debido a que es el algoritmo más óptimo, ya que no tenemos que ver todas las opciones para saber cuantas veces tenemos que utilizar las operaciones de pegar y copiar.

### FACTORIZAR
Factorizar es el proceso que le aplica a un número cuyo producto es una multiplicación para hallar ese número por medio de sus factores que son primos. La lógica de los primos es que no pueden dividirse a un más como si los harían los compuestos para hallar el número.  En sí, la factorización implica descomponer un número en factores más pequeños. En particular, la factorización de enteros se refiere a descomponer un número entero en sus factores primos.

Un número primo es un número entero mayor que 1 que solo es divisible por 1 y por sí mismo. Por ejemplo, 2, 3, 5, 7, 11 y 13 son números primos. Los números que no son primos se llaman números compuestos.

La factorización de enteros se puede utilizar para simplificar expresiones, resolver ecuaciones y encontrar la solución a problemas relacionados con la teoría de números. Además, la factorización también es importante en la criptografía y la seguridad informática.