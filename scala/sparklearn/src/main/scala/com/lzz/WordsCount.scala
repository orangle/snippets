package com.lzz

import com.alibaba.fastjson.JSON
import redis.clients.jedis.Jedis
import org.apache.spark.{SparkConf, SparkContext}


object WordsCount {
  //判断类型
  def printType[T](x:T) :Unit = {
    println(x.getClass.toString())
  }

  def wordsCount() = {
    println("job start....")
    val logFile = "/etc/hosts" // Should be some file on your system
    //val conf = new SparkConf().setAppName("Simple Application").setMaster("local[2]")
    val conf = new SparkConf().setAppName("Simple Application")
    //conf.set("spark.driver.allowMultipleContexts", "true")
    val sc = new SparkContext(conf)
    sc.setLogLevel("ERROR")

    val logData = sc.textFile(logFile, 2).cache()
    val numAs = logData.filter(line => line.contains("a")).count()
    val numBs = logData.filter(line => line.contains("b")).count()
    println("Lines with a: %s, Lines with b: %s".format(numAs, numBs))

    val jsonString1 = "{\"name\":\"张三\",\"age\":50}"
    val jsonObject = JSON.parseObject(jsonString1)
    //println(jsonObject.keySet())

    sc.stop()
    println("job stop....")
  }

  def main(args: Array[String]) {
    val jedis = new Jedis("localhost")

    while(true) {
      var keys = jedis.brpop(5, "list_test")
      //printType(keys)
      val times = System.currentTimeMillis()
      println(times)

      if (!keys.isEmpty()) {
        println(keys.get(1))
        wordsCount()
      } else {
        println("没有获取到值")
      }
    }
  }
}
