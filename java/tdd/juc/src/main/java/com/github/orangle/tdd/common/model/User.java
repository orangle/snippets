package com.github.orangle.tdd.common.model;


import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class User {
    private String name;
    private Integer age;
}
