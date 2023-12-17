//import java.util.concurrent.ExecutorService;
//import java.util.concurrent.Executors;

import java.util.concurrent.locks. *;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Multithreading {
    private static Account account = new Account();
    public static void main(String[] args) throws Exception {
        /*ExecutorService executor = Executors.newFixedThreadPool(3);

        executor.execute(new PrintChar('a', 100));
        executor.execute(new PrintChar('b', 100));
        executor.execute(new PrintNum(100));

        executor.shutdown();*/

        ExecutorService executor = Executors.newCachedThreadPool();

        for (int i = 0; i < 100; i++){
            executor.execute(new AddPennyTask());
        }

        executor.shutdown();

        while (!executor.isTerminated()){}

        System.out.println("What is balance? " + account.getBalance());
    }


/*class PrintChar implements Runnable {
    private char charToPrint;
    private int times;

    public PrintChar(char c, int t){
        charToPrint = c;
        times = t;

    }

    public void run(){
        for (int i = 0; i < times; i++){
            System.out.print(charToPrint);
        }
    }
}

class PrintNum implements Runnable {
    private int lastNum;

    public PrintNum(int n){
        lastNum = n;
    }

    public void run(){
        for(int i = 1; i <= lastNum; i++){
            System.out.print(" " + i);
        }
    }
}
*/

private static class AddPennyTask implements Runnable{
    public void run(){
        account.deposit(1);
    }
}

private static class Account {
    private static Lock lock = new ReentrantLock();
    private int balance = 0;

    public int getBalance(){
        return balance;
    }

    public synchronized void deposit(int amount){
        lock.lock();
    

    try{
        int newBalance = balance + amount;

        Thread.sleep(5);

        balance = newBalance;
    }
    catch (InterruptedException ex){
    }
    finally{
        lock.unlock();
    }
}
}
}