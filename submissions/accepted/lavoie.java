/**
* Author: Sean Lavoie
* filename: DoomsdayRule.java
* date: 02.02.2018
*/
import java.io.File;
import java.util.Date;
import java.util.Scanner;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.text.SimpleDateFormat;
import java.text.ParseException;

public class lavoie {
    
    static String[] dayOfWeek = {"Wut", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

    public static void main(String[] args) throws ParseException {
        Scanner scn = new Scanner(System.in);
        int numDates = scn.nextInt();
        scn.nextLine();

        for(int i = 0; i < numDates; i++) {
            int day = scn.nextInt();
            String month = scn.next();
            int year = scn.nextInt();
            GregorianCalendar cal = new GregorianCalendar();
            cal.clear();
            cal.setGregorianChange(new Date(Long.MIN_VALUE));
            cal.set(Calendar.DAY_OF_MONTH, day);
            cal.set(Calendar.MONTH, new SimpleDateFormat("MMMM").parse(month).getMonth());
            cal.set(Calendar.YEAR, year);
            System.out.println(dayOfWeek[cal.get(Calendar.DAY_OF_WEEK)]);
        }
    }
}
