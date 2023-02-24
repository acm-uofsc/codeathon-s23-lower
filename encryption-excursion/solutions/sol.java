import java.util.*;
import java.lang.*;
import java.io.*;

public class Solution {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int offset = sc.nextInt();
        String pw = sc.next();
        for(int i=0; i < pw.length(); i++) {
            char c = pw.charAt(i);
            System.out.print((char)(c + offset));
        }
        System.out.println();
    }
}