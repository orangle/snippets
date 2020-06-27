package com.github.orangle.tdd.juc.thread;

import com.github.orangle.tdd.juc.thread.lib.CallableTask;
import org.junit.Test;

import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

/**
 * 线程池的实现需要自定义，看下有没有比较优雅的代码
 */
public class ThreadPoolTest {

    @Test
    public void callableTaskTest() throws ExecutionException, InterruptedException {
        ExecutorService service = Executors.newFixedThreadPool(3);
        Future<Integer> future = service.submit(new CallableTask());
        System.out.println(future.get());
    }
}
