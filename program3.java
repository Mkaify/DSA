public class program3 {
    public static int howManySeconds(int hours) {
        // One hour has 3600 seconds (60 seconds/minute * 60 minutes/hour)
        int seconds = hours * 3600;
        return seconds;
    }

    public static void main(String[] args) {
        int hours1 = 2;
        int hours2 = 10;
        int hours3 = 24;

        System.out.println("howManySeconds(2) --> " + howManySeconds(hours1));
        System.out.println("howManySeconds(10) --> " + howManySeconds(hours2));
        System.out.println("howManySeconds(24) --> " + howManySeconds(hours3));
    }
}
