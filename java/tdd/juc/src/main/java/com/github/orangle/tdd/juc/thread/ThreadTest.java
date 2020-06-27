package com.github.orangle.tdd.juc.thread;

import com.github.orangle.tdd.juc.thread.lib.ExtendsThread;
import com.github.orangle.tdd.juc.thread.lib.RunnableThread;
import lombok.extern.slf4j.Slf4j;
import org.junit.Test;

@Slf4j
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

    /**
     * 通过继承Thread实现
     */
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
        new Thread(() -> System.out.println("继承实现")).start();

        new Thread(new Runnable() {
            @Override
            public void run() {
               System.out.println("接口实现");
            }
        }).start();
    }

    @Test
    public void testThreadInterrupted() throws InterruptedException {
        Runnable runnable = () -> {
            int num = 0;
            while (!Thread.currentThread().isInterrupted() && num < 1000) {
                System.out.println(num);
                num++;
            }
        };
        Thread thread = new Thread(runnable);
        thread.start();
        Thread.sleep(1);
        thread.interrupt();
        log.info("finish");
    }

}
