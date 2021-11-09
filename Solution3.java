public class Solution3 {
    public static int solution(int start, int length) {
    
        int checksum = 0;

        for(int i = length; i > 0; i--) { // loop from the length down to 0
            int offset = length * (length - i); // Calculate the offset for the current iteration
            for(int a = start + offset; a < start + offset + i; a++) { // add the offset to the start and loop from there i times
                checksum ^= a; // xor checksum
            }
        }
        return checksum;
    }
}