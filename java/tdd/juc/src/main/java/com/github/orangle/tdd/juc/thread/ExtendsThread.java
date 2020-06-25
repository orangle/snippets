package com.github.orangle.tdd.juc.thread;

public class ExtendsThread extends Thread{

    @Override
    public void run() {
        System.out.println("Extend thread");
    }
}
