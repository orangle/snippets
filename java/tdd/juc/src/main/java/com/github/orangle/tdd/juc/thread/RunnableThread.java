package com.github.orangle.tdd.juc.thread;

/**
 * @author liuzhizhi
 */
public class RunnableThread implements Runnable {
    private String name;
    private Thread t;

    RunnableThread (String name) {
        this.name = name;
    }

    @Override
    public void run() {
        System.out.println("Runnable thread " + name);
    }

    public void start() {
        System.out.println("String " + name);
        if (t == null) {
            t = new Thread(this, name);
            t.start();
        }
    }

}
