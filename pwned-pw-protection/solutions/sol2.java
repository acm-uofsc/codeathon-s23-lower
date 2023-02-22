import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] inputLine1 = scanner.nextLine().split(" ");
        int n = Integer.parseInt(inputLine1[0]);
        int m = Integer.parseInt(inputLine1[1]);

        List<char[]> words = new ArrayList<>();
        String[] inputLine2 = scanner.nextLine().split(" ");
        for (String s : inputLine2) {
            char[] sortedChars = s.toCharArray();
            Arrays.sort(sortedChars);
            words.add(sortedChars);
        }

        for (int i = 0; i < m; i++) {
            char[] password = scanner.nextLine().toCharArray();
            Arrays.sort(password);
            boolean found = false;
            for (char[] word : words) {
                if (Arrays.equals(word, password)) {
                    System.out.println("True");
                    found = true;
                    break;
                }
            }
            if (!found) {
                System.out.println("False");
            }
        }
    }
}
