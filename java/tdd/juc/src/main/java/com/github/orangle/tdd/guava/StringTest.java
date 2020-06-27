package com.github.orangle.tdd.guava;

import com.google.common.base.Joiner;
import com.google.common.base.Splitter;
import joptsimple.internal.Strings;
import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class StringTest {
   @Test
   public void joinTest() {
      // join合并list
      String res = Joiner.on("|").join(Arrays.asList(1, 29, 13));
      System.out.println(res);

      //
      String ret = Joiner.on(",").join("好人", "美剧");
      System.out.println(ret);

      // skip null
      List<String> l2 = Arrays.asList("baidu", null, "tencent");
      System.out.println(Joiner.on("&").skipNulls().join(l2));

      // 替换 NULL
      List<String> l3 = Arrays.asList("baidu", null, "tencent");
      System.out.println(Joiner.on("&").useForNull("^^").join(l2));
   }

   @Test
   public void checkNullTest(){
      String name = null;
      String label = "lzz";
      String empty = "";
      Assert.assertEquals(true, Strings.isNullOrEmpty(name));
      Assert.assertEquals(true, Strings.isNullOrEmpty(empty));
      Assert.assertEquals(false, Strings.isNullOrEmpty(label));
   }

   @Test
   public void splitTest() { 
      //切分一串字符
      String s2 = "a, c, d,, 6, 8";
      System.out.println(Splitter.on(",").splitToList(s2));
      //忽略空白
      System.out.println(Splitter.on(",").omitEmptyStrings().splitToList(s2));
      //除去空白和两边的空
      System.out.println(Splitter.on(",").omitEmptyStrings().trimResults().splitToList(s2));
   }


   @Test
   public void stringsTest() {
      System.out.println(1);
   }

}
