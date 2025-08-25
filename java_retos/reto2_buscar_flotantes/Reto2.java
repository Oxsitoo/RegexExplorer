// Reto 2: Buscar números flotantes en un texto usando regex en Java
// Paso a paso:
// 1. Leer el texto de entrada.
// 2. Definir una expresión regular para encontrar números flotantes.
// 3. Buscar todos los flotantes en el texto.
// 4. Imprimir los resultados.

import java.util.regex.*;

public class Reto2 {
    public static void main(String[] args) {
        String texto = "El precio es 12.50 dólares, pero antes era 10.0, pero por ser humanoo el descuento es del 67.80 %";
        // Expresión regular para flotantes (números con punto decimal)
        String patron = "-?\\b\\d+\\.\\d+\\b";
        Pattern pattern = Pattern.compile(patron);
        Matcher matcher = pattern.matcher(texto);
        System.out.print("Flotantes encontrados: ");
        while (matcher.find()) {
            System.out.print(matcher.group() + " ");
        }
        System.out.println();
        // Paso a paso:
        // 1. Cambia el texto de prueba.
        // 2. Modifica la expresión regular si es necesario.
        // 3. Ejecuta el programa y observa los resultados.
    }
}
