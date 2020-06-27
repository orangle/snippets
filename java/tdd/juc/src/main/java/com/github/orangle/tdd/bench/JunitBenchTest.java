package com.github.orangle.tdd.bench;

import org.junit.Test;
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import org.openjdk.jmh.runner.Runner;
import org.openjdk.jmh.runner.options.Options;
import org.openjdk.jmh.runner.options.OptionsBuilder;
import org.openjdk.jmh.runner.options.TimeValue;

import java.util.concurrent.TimeUnit;

import static org.junit.Assert.assertTrue;

/**
 * https://nickolasfisher.com/blog/posts-by-categories
 */
public class JunitBenchTest {
    @Test
    public void runBenchmarks() throws Exception {
        Options options = new OptionsBuilder()
                .include(this.getClass().getName() + ".*")
                .mode(Mode.AverageTime)
                .warmupTime(TimeValue.seconds(1))
                .warmupIterations(6)
                .threads(1)
                .measurementIterations(6)
                .forks(1)
                .shouldFailOnError(true)
                .shouldDoGC(true)
                .build();

        new Runner(options).run();
    }

    private static String hello = "not another hello world";

    @Benchmark
    @OutputTimeUnit(TimeUnit.MILLISECONDS)
    public void stringsWithoutStringBuilder() throws Exception {
        String hellos = "";
        for (int i = 0; i < 1000; i++) {
            hellos += hello;
            if (i != 999) {
                hellos += "\n";
            }
        }
        assertTrue(hellos.startsWith((hello + "\n")));
    }

    @Benchmark
    @OutputTimeUnit(TimeUnit.MILLISECONDS)
    public void stringsWithStringBuilder() throws Exception {
        StringBuilder hellosBuilder = new StringBuilder();
        for (int i = 0; i < 1000; i++) {
            hellosBuilder.append(hello);
            if (i != 999) {
                hellosBuilder.append("\n");
            }
        }
        assertTrue(hellosBuilder.toString().startsWith((hello + "\n")));
    }
}
