import java.util.*;
import java.lang.*;
import java.io.*;

public class Solution {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int[] denominations = new int[x];
        for(int i=0; i<x; i++) {
            denominations[i] = sc.nextInt();
        }
        for(int i=0; i<y; i++) {
            int coins = 0;
            int change = sc.nextInt();
            int[] output = new int[x];
            for(int j=0; j<x; j++) {
                int num_coin = change / denominations[j];
                coins += num_coin;
                change = change % denominations[j];
                output[j] = num_coin;
            }
            for(int j=0; j<x; j++) {
                System.out.print(output[j] + " ");
            }
            System.out.println();
        }
    }
}