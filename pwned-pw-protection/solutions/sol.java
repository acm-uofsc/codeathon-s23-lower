import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] inputLine1 = scanner.nextLine().split(" ");
        int n = Integer.parseInt(inputLine1[0]);
        int m = Integer.parseInt(inputLine1[1]);

        List<Map<Character, Integer>> database = new ArrayList<>();
        String[] inputLine2 = scanner.nextLine().split(" ");
        for (String s : inputLine2) {
            Map<Character, Integer> counter = new HashMap<>();
            for (char c : s.toCharArray()) {
                counter.put(c, counter.getOrDefault(c, 0) + 1);
            }
            database.add(counter);
        }

        for (int i = 0; i < m; i++) {
            Map<Character, Integer> password = new HashMap<>();
            String passwordString = scanner.nextLine();
            for (char c : passwordString.toCharArray()) {
                password.put(c, password.getOrDefault(c, 0) + 1);
            }
            boolean found = false;
            for (Map<Character, Integer> entry : database) {
                if (entry.equals(password)) {
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
