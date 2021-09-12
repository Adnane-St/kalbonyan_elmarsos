using System;

class Program{
    static void Main(){
        int[][] jagged = new int[3][] // Here we have set the two dimesion array with Three row and undifined colmns

        // row 0
        jagged[0] = new int[2]
        jagged[0][0] = 4
        jagged[0][1] = 8

        // row 1
        jagged[1] = new int[9];

        // row 2
        jagged[2] = new int[4] {3,4,2,5}

        Console.WriteLine(jagged)
    }
}