import java.util.Scanner;
import java.util.HashSet;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.nextLine();
        String[] passwords = sc.nextLine().split(" ");
        assert passwords.length == n;
        boolean result;
        for (int i = 0; i < m; i++) {
            String user = sc.nextLine();
            result = check(passwords, user);
            if (result) {
                System.out.println("True");
            } else {
                System.out.println("False");
            }
        }
    }
        
    public static boolean check(String[] passwords, String user) {
        for (String password : passwords) {
            if (user.length() != password.length()) {
                continue;
            }
            HashSet<Integer> passwordUsed = new HashSet<Integer>();
            for (int j = 0; j < user.length(); j++) {
                boolean found = false;
                for (int i = 0; i < password.length(); i++) {
                    if (user.charAt(j) == password.charAt(i) && !passwordUsed.contains(i)) {
                        passwordUsed.add(i);
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    break;
                }
            }
            if (passwordUsed.size() == password.length()) {
                return true;
            }
        }
        return false;
    }

}
