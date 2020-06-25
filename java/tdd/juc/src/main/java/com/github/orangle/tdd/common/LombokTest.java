package com.github.orangle.tdd.common;

import com.github.orangle.tdd.common.model.User;
import org.junit.Test;

public class LombokTest {

    @Test
    public void modelTest(){
        User user = User.builder().name("lzz").age(89).build();
        System.out.println(user);
    }
}
