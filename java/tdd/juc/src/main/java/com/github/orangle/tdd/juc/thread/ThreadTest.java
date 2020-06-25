package com.github.orangle.tdd.juc.thread;

import org.junit.Test;


public class ThreadTest {
    /**
     * 接口实现线程
     */
    @Test
    public void testNewThreadInterace() {
        RunnableThread runnableThread = new RunnableThread("t1");
        Thread t1 = new Thread(runnableThread);
        t1.start();

        RunnableThread t2 = new RunnableThread("t2");
        t2.start();
    }

    @Test
    public void testNewThreadExtend() {
        ExtendsThread extendsThread = new ExtendsThread();
        extendsThread.start();
    }

    /**
     * 匿名线程创建
     */
    @Test
    public void testLambdaThread() {
        System.out.println(2);
    }
}
