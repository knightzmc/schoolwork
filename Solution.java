import java.util.*;
public class Solution {
    static class Vector {
        double x, y;
        Vector(double x, double y){
            this.x = x;
            this.y = y;
        }
        Vector add(Vector v) {
            return new Vector(x + v.x, y + v.y);
        }
        @Override
        public String toString() {
            return "(" + x + ", " + y + ")";
        }
        public double angle() {
            return Math.atan2(y, x);
        }
        public double magSquared() {
            return x*x + y * y;
        }
        public double mag() {
            return Math.sqrt(magSquared());
        }
    }
    // takes a direction vector v, a position vector start, and the dimensions of the room and calculates the next point that v would collide with
    // Returns a new vector pointing in the resulting direction
    private static Vector trace(Vector v, Vector start, int[] dimensions) {
        double m = v.y / v.x;
        // y = mx + c
        double c = start.y - m * start.x;
    
        Vector a = new Vector(dimensions[0], m * dimensions[0] + c);
        Vector a2 = new Vector(0, c);
        Vector b = new Vector(dimensions[1] / m - c, dimensions[1]);
        Vector b2 = new Vector(-c, 0);
        return Arrays.asList(a, a2, b, b2).stream()
        .min(Comparator.comparingDouble(Vector::magSquared))
        .get();
    }

    private static Vector resultant(Vector ans) {
        double angleOfIncidence = Math.PI / 2 - ans.angle();

        double mag = ans.mag();
        return new Vector(Math.cos(angleOfIncidence) * mag, -Math.sin(angleOfIncidence) * mag);
    }
    public static int solution(int[] dimensions, int[] your_position, int[] trainer_position, int distance) {
        List<Vector> vecs = new ArrayList<>();
    
        return -1;
    }

    public static void main(String[] args) {
        Vector yourPoint = new Vector(1, 1);
        Vector v = new Vector(3, 2);
        int[] dim = {3, 2};
        Vector a = trace(v, yourPoint, dim);
        System.out.println("a = " + a);
        System.out.println("angle(a) = " + a.angle());
        System.out.println("res(a) = " + trace(resultant(a), a, dim));
        Vector b = trace(a, yourPoint.add(a), dim);
        System.out.println("b = " + b);
        System.out.println("angle(b) = " + b.angle());
        System.out.println("res(b) = " + trace(resultant(b), b, dim));
        System.out.println(trace(b, yourPoint.add(b.add(b)), dim));
    }
}